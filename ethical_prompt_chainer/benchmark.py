import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
import logging
import json
from pathlib import Path
import time
from datetime import datetime
from .models import ModelFactory

logger = logging.getLogger(__name__)

@dataclass
class BenchmarkMetrics:
    """Container for model benchmarking metrics."""
    model_name: str
    response_time: float
    token_count: int
    constitutional_coverage: float
    recommendation_clarity: float
    ethical_consistency: float
    cost_per_token: float
    total_cost: float

class ModelBenchmarker:
    """Benchmarks different language models on ethical dilemmas."""
    
    # Metrics weights for overall score calculation
    METRIC_WEIGHTS = {
        'response_time': 0.1,
        'constitutional_coverage': 0.3,
        'recommendation_clarity': 0.3,
        'ethical_consistency': 0.2,
        'cost_efficiency': 0.1
    }
    
    # Constitutional principles to check for coverage
    CONSTITUTIONAL_PRINCIPLES = [
        'general welfare',
        'equal protection',
        'due process',
        'individual liberty',
        'property rights',
        'federalism',
        'separation of powers'
    ]
    
    def __init__(self, models: List[str] = None):
        """
        Initialize the model benchmarker.
        
        Args:
            models: List of model names to benchmark
        """
        self.models = models or ['gpt-4', 'gpt-3.5-turbo', 'claude-3-opus']
        self.model_factory = ModelFactory()
        self.results = []
    
    def _calculate_constitutional_coverage(self, response: str) -> float:
        """Calculate the coverage of constitutional principles in the response."""
        principles_found = sum(1 for principle in self.CONSTITUTIONAL_PRINCIPLES 
                             if principle.lower() in response.lower())
        return principles_found / len(self.CONSTITUTIONAL_PRINCIPLES)
    
    def _calculate_recommendation_clarity(self, response: str) -> float:
        """Calculate the clarity of recommendations in the response."""
        # Check for clear recommendation indicators
        clarity_indicators = [
            'recommend',
            'propose',
            'suggest',
            'conclude',
            'therefore',
            'should',
            'must',
            'need to'
        ]
        
        # Count indicators and normalize
        indicators_found = sum(1 for indicator in clarity_indicators 
                             if indicator.lower() in response.lower())
        return min(indicators_found / len(clarity_indicators), 1.0)
    
    def _calculate_ethical_consistency(self, response: str) -> float:
        """Calculate the consistency of ethical reasoning in the response."""
        # Check for ethical reasoning indicators
        consistency_indicators = [
            'ethical',
            'moral',
            'principle',
            'value',
            'right',
            'wrong',
            'just',
            'fair',
            'equitable',
            'balanced'
        ]
        
        # Count indicators and normalize
        indicators_found = sum(1 for indicator in consistency_indicators 
                             if indicator.lower() in response.lower())
        return min(indicators_found / len(consistency_indicators), 1.0)
    
    def _calculate_cost_efficiency(self, token_count: int, cost_per_token: float) -> float:
        """Calculate the cost efficiency of the response."""
        # Normalize cost efficiency (lower is better)
        max_expected_tokens = 2000  # Maximum expected tokens for a response
        max_expected_cost = max_expected_tokens * cost_per_token
        
        actual_cost = token_count * cost_per_token
        return 1 - (actual_cost / max_expected_cost)
    
    def _calculate_overall_score(self, metrics: BenchmarkMetrics) -> float:
        """Calculate the overall benchmark score."""
        scores = {
            'response_time': 1 - (metrics.response_time / 30),  # Normalize to 30 seconds
            'constitutional_coverage': metrics.constitutional_coverage,
            'recommendation_clarity': metrics.recommendation_clarity,
            'ethical_consistency': metrics.ethical_consistency,
            'cost_efficiency': self._calculate_cost_efficiency(
                metrics.token_count, metrics.cost_per_token
            )
        }
        
        return sum(score * self.METRIC_WEIGHTS[metric] 
                  for metric, score in scores.items())
    
    def benchmark_model(self, model_name: str, dilemma: str) -> BenchmarkMetrics:
        """
        Benchmark a single model on a dilemma.
        
        Args:
            model_name: Name of the model to benchmark
            dilemma: The dilemma to analyze
            
        Returns:
            BenchmarkMetrics object containing the benchmark results
        """
        try:
            # Initialize model
            model = self.model_factory.create_model(model_name)
            
            # Measure response time
            start_time = time.time()
            response = model.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": dilemma}],
                temperature=0.7,
                max_tokens=2048
            )
            end_time = time.time()
            
            # Extract response and metrics
            response_text = response.choices[0].message.content
            token_count = response.usage.total_tokens
            response_time = end_time - start_time
            
            # Calculate metrics
            constitutional_coverage = self._calculate_constitutional_coverage(response_text)
            recommendation_clarity = self._calculate_recommendation_clarity(response_text)
            ethical_consistency = self._calculate_ethical_consistency(response_text)
            
            # Get cost information
            cost_per_token = self.model_factory.get_cost_per_token(model_name)
            total_cost = token_count * cost_per_token
            
            return BenchmarkMetrics(
                model_name=model_name,
                response_time=response_time,
                token_count=token_count,
                constitutional_coverage=constitutional_coverage,
                recommendation_clarity=recommendation_clarity,
                ethical_consistency=ethical_consistency,
                cost_per_token=cost_per_token,
                total_cost=total_cost
            )
            
        except Exception as e:
            logger.error(f"Error benchmarking model {model_name}: {str(e)}")
            raise
    
    def run_benchmark(self, dilemmas: List[str], output_file: str = None) -> pd.DataFrame:
        """
        Run benchmarks for all models on a list of dilemmas.
        
        Args:
            dilemmas: List of dilemmas to benchmark
            output_file: Optional file to save results to
            
        Returns:
            DataFrame containing benchmark results
        """
        results = []
        
        for model_name in self.models:
            for dilemma in dilemmas:
                try:
                    metrics = self.benchmark_model(model_name, dilemma)
                    overall_score = self._calculate_overall_score(metrics)
                    
                    result = {
                        'model': model_name,
                        'dilemma': dilemma,
                        'response_time': metrics.response_time,
                        'token_count': metrics.token_count,
                        'constitutional_coverage': metrics.constitutional_coverage,
                        'recommendation_clarity': metrics.recommendation_clarity,
                        'ethical_consistency': metrics.ethical_consistency,
                        'cost_per_token': metrics.cost_per_token,
                        'total_cost': metrics.total_cost,
                        'overall_score': overall_score,
                        'timestamp': datetime.now().isoformat()
                    }
                    results.append(result)
                    
                except Exception as e:
                    logger.error(f"Error in benchmark for {model_name} on dilemma: {str(e)}")
                    continue
        
        # Convert to DataFrame
        df = pd.DataFrame(results)
        
        # Save results if output file specified
        if output_file:
            df.to_csv(output_file, index=False)
            logger.info(f"Benchmark results saved to {output_file}")
        
        return df
    
    def format_benchmark_results(self, results: pd.DataFrame) -> str:
        """Format benchmark results in a readable way."""
        # Calculate average metrics by model
        avg_metrics = results.groupby('model').agg({
            'response_time': 'mean',
            'constitutional_coverage': 'mean',
            'recommendation_clarity': 'mean',
            'ethical_consistency': 'mean',
            'total_cost': 'mean',
            'overall_score': 'mean'
        }).round(3)
        
        # Format the report
        report = "Model Benchmark Results\n"
        report += "=" * 50 + "\n\n"
        
        for model in avg_metrics.index:
            metrics = avg_metrics.loc[model]
            report += f"Model: {model}\n"
            report += "-" * 30 + "\n"
            report += f"Average Response Time: {metrics['response_time']:.2f} seconds\n"
            report += f"Constitutional Coverage: {metrics['constitutional_coverage']:.2%}\n"
            report += f"Recommendation Clarity: {metrics['recommendation_clarity']:.2%}\n"
            report += f"Ethical Consistency: {metrics['ethical_consistency']:.2%}\n"
            report += f"Average Cost: ${metrics['total_cost']:.2f}\n"
            report += f"Overall Score: {metrics['overall_score']:.2%}\n\n"
        
        return report 