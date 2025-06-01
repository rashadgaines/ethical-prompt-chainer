import unittest
from unittest.mock import Mock, patch
import pandas as pd
from ..benchmark import ModelBenchmarker, BenchmarkMetrics

class TestModelBenchmarker(unittest.TestCase):
    def setUp(self):
        self.benchmarker = ModelBenchmarker(models=['test-model'])
        self.test_dilemma = "Should the government implement universal basic income?"
    
    def test_constitutional_coverage(self):
        # Test with response containing some principles
        response = "This policy should consider general welfare and equal protection."
        coverage = self.benchmarker._calculate_constitutional_coverage(response)
        self.assertGreater(coverage, 0)
        self.assertLessEqual(coverage, 1)
    
    def test_recommendation_clarity(self):
        # Test with response containing clear recommendations
        response = "We should implement this policy because it is necessary."
        clarity = self.benchmarker._calculate_recommendation_clarity(response)
        self.assertGreater(clarity, 0)
        self.assertLessEqual(clarity, 1)
    
    def test_ethical_consistency(self):
        # Test with response containing ethical reasoning
        response = "This is an ethical issue that requires careful consideration of moral principles."
        consistency = self.benchmarker._calculate_ethical_consistency(response)
        self.assertGreater(consistency, 0)
        self.assertLessEqual(consistency, 1)
    
    def test_cost_efficiency(self):
        # Test cost efficiency calculation
        token_count = 1000
        cost_per_token = 0.002
        efficiency = self.benchmarker._calculate_cost_efficiency(token_count, cost_per_token)
        self.assertGreater(efficiency, 0)
        self.assertLessEqual(efficiency, 1)
    
    @patch('ethical_prompt_chainer.models.ModelFactory')
    def test_benchmark_model(self, mock_factory):
        # Mock the model factory and response
        mock_model = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Test response"))]
        mock_response.usage = Mock(total_tokens=100)
        mock_model.chat.completions.create.return_value = mock_response
        mock_factory.create_model.return_value = mock_model
        mock_factory.get_cost_per_token.return_value = 0.002
        
        # Run benchmark
        metrics = self.benchmarker.benchmark_model('test-model', self.test_dilemma)
        
        # Verify metrics
        self.assertIsInstance(metrics, BenchmarkMetrics)
        self.assertEqual(metrics.model_name, 'test-model')
        self.assertGreater(metrics.response_time, 0)
        self.assertEqual(metrics.token_count, 100)
        self.assertGreater(metrics.constitutional_coverage, 0)
        self.assertGreater(metrics.recommendation_clarity, 0)
        self.assertGreater(metrics.ethical_consistency, 0)
        self.assertEqual(metrics.cost_per_token, 0.002)
        self.assertEqual(metrics.total_cost, 0.2)
    
    def test_run_benchmark(self):
        # Test running benchmark on multiple dilemmas
        dilemmas = [
            "Should the government implement universal basic income?",
            "Is it ethical to use AI in healthcare decision-making?"
        ]
        
        # Mock the benchmark_model method
        self.benchmarker.benchmark_model = Mock(return_value=BenchmarkMetrics(
            model_name='test-model',
            response_time=1.0,
            token_count=100,
            constitutional_coverage=0.5,
            recommendation_clarity=0.7,
            ethical_consistency=0.6,
            cost_per_token=0.002,
            total_cost=0.2
        ))
        
        # Run benchmark
        results = self.benchmarker.run_benchmark(dilemmas)
        
        # Verify results
        self.assertIsInstance(results, pd.DataFrame)
        self.assertEqual(len(results), 2)  # One result per dilemma
        self.assertIn('model', results.columns)
        self.assertIn('dilemma', results.columns)
        self.assertIn('overall_score', results.columns)
    
    def test_format_benchmark_results(self):
        # Create sample results
        results = pd.DataFrame([
            {
                'model': 'test-model',
                'response_time': 1.0,
                'constitutional_coverage': 0.5,
                'recommendation_clarity': 0.7,
                'ethical_consistency': 0.6,
                'total_cost': 0.2,
                'overall_score': 0.65
            }
        ])
        
        # Format results
        report = self.benchmarker.format_benchmark_results(results)
        
        # Verify report format
        self.assertIsInstance(report, str)
        self.assertIn('Model Benchmark Results', report)
        self.assertIn('test-model', report)
        self.assertIn('Average Response Time', report)
        self.assertIn('Constitutional Coverage', report)
        self.assertIn('Recommendation Clarity', report)
        self.assertIn('Ethical Consistency', report)
        self.assertIn('Average Cost', report)
        self.assertIn('Overall Score', report)

if __name__ == '__main__':
    unittest.main() 