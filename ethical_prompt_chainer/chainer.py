from typing import Dict, Any, Optional, Tuple, List, Set
from dataclasses import dataclass
import json
import logging
from pathlib import Path
from datetime import datetime
from .models import ModelFactory, ModelType
from .prompts import EthicalPromptTemplates
from .data_validator import DilemmaValidator
from .cost_benefit import CostBenefitAnalyzer, CostBenefitMetrics
from .benchmark import ModelBenchmarker, BenchmarkMetrics
from .ethical_frameworks import EthicalFrameworkManager, EthicalPrinciple
from .stakeholder_analysis import StakeholderAnalyzer, StakeholderImpact
from .long_term_impact import LongTermImpactAnalyzer, LongTermImpact
from .explainable_ai import ExplainableAI, AIExplanation, ExplanationType, ExplanationLevel
import pandas as pd

logger = logging.getLogger(__name__)

@dataclass
class EthicalAnalysis:
    """Container for complete ethical analysis results."""
    dilemma: str
    context: List[str]
    ethical_principles: List[str]
    analysis: str
    recommendations: List[str]
    confidence_score: float
    model_used: str
    timestamp: datetime
    benchmark_results: Optional[BenchmarkMetrics] = None
    ethical_alignment: Optional[Dict[str, float]] = None
    stakeholder_impacts: Optional[List[StakeholderImpact]] = None
    long_term_impact: Optional[LongTermImpact] = None
    ai_explanation: Optional[AIExplanation] = None

class EthicalPromptChainer:
    """Main class for chaining ethical analysis prompts."""
    
    def __init__(
        self,
        model_type: ModelType = ModelType.GPT4,
        benchmark_models: Optional[List[ModelType]] = None,
        include_benchmark: bool = False,
        include_explanation: bool = True
    ):
        """
        Initialize the ethical prompt chainer.
        
        Args:
            model_type: The type of model to use for analysis
            benchmark_models: Optional list of models to benchmark against
            include_benchmark: Whether to include benchmarking in analysis
            include_explanation: Whether to include AI explanations
        """
        self.model_factory = ModelFactory()
        self.model = self.model_factory.get_model(model_type)
        self.benchmarker = ModelBenchmarker() if include_benchmark else None
        self.benchmark_models = benchmark_models if include_benchmark else None
        self.framework_manager = EthicalFrameworkManager()
        self.stakeholder_analyzer = StakeholderAnalyzer()
        self.long_term_analyzer = LongTermImpactAnalyzer()
        self.explainer = ExplainableAI() if include_explanation else None
    
    def analyze_dilemma(
        self,
        dilemma: str,
        context: Optional[List[str]] = None,
        include_benchmark: bool = False,
        explanation_level: ExplanationLevel = ExplanationLevel.DETAILED
    ) -> EthicalAnalysis:
        """
        Perform a complete ethical analysis of a dilemma.
        
        Args:
            dilemma: The ethical dilemma to analyze
            context: Optional list of relevant contexts
            include_benchmark: Whether to include benchmarking in analysis
            explanation_level: Level of detail for AI explanations
            
        Returns:
            EthicalAnalysis object containing the complete analysis
        """
        logger.info(f"Starting ethical analysis of dilemma: {dilemma[:100]}...")
        
        # Step 1: Identify ethical principles
        principles = self._identify_ethical_principles(dilemma)
        logger.info(f"Identified {len(principles)} ethical principles")
        
        # Step 2: Analyze the dilemma
        analysis = self._analyze_dilemma(dilemma, principles)
        logger.info("Completed initial analysis")
        
        # Step 3: Generate recommendations
        recommendations = self._generate_recommendations(analysis)
        logger.info(f"Generated {len(recommendations)} recommendations")
        
        # Step 4: Calculate confidence score
        confidence_score = self._calculate_confidence_score(
            dilemma, analysis, recommendations
        )
        logger.info(f"Calculated confidence score: {confidence_score:.2f}")
        
        # Step 5: Run model benchmarking if requested
        benchmark_results = None
        if include_benchmark and self.benchmarker and self.benchmark_models:
            try:
                benchmark_results = self.benchmarker.benchmark_model(
                    self.model,
                    dilemma,
                    self.benchmark_models
                )
                logger.info("Completed model benchmarking")
            except Exception as e:
                logger.error(f"Error during benchmarking: {str(e)}")
        
        # Step 6: Analyze ethical alignment
        try:
            ethical_alignment = self._analyze_ethical_alignment(analysis)
            logger.info("Completed ethical alignment analysis")
        except Exception as e:
            logger.error(f"Error during ethical alignment analysis: {str(e)}")
            ethical_alignment = None
        
        # Step 7: Analyze stakeholder impacts
        try:
            stakeholder_impacts = self._analyze_stakeholder_impacts(dilemma, context)
            logger.info("Completed stakeholder impact analysis")
        except Exception as e:
            logger.error(f"Error during stakeholder impact analysis: {str(e)}")
            stakeholder_impacts = None
        
        # Step 8: Analyze long-term impacts
        try:
            long_term_impact = self._analyze_long_term_impacts(dilemma, context)
            logger.info("Completed long-term impact analysis")
        except Exception as e:
            logger.error(f"Error during long-term impact analysis: {str(e)}")
            long_term_impact = None
        
        # Step 9: Generate AI explanations
        ai_explanation = None
        if self.explainer:
            try:
                ai_explanation = self._generate_ai_explanation(
                    dilemma, analysis, explanation_level
                )
                logger.info("Completed AI explanation generation")
            except Exception as e:
                logger.error(f"Error during AI explanation generation: {str(e)}")
        
        return EthicalAnalysis(
            dilemma=dilemma,
            context=context or [],
            ethical_principles=principles,
            analysis=analysis,
            recommendations=recommendations,
            confidence_score=confidence_score,
            model_used=self.model.model_type.value,
            timestamp=datetime.now(),
            benchmark_results=benchmark_results,
            ethical_alignment=ethical_alignment,
            stakeholder_impacts=stakeholder_impacts,
            long_term_impact=long_term_impact,
            ai_explanation=ai_explanation
        )
    
    def _analyze_long_term_impacts(
        self,
        dilemma: str,
        context: Optional[List[str]]
    ) -> LongTermImpact:
        """
        Analyze long-term impacts of the dilemma.
        
        Args:
            dilemma: The ethical dilemma to analyze
            context: Optional list of relevant contexts
            
        Returns:
            LongTermImpact object containing the analysis
        """
        return self.long_term_analyzer.analyze_long_term_impact(
            dilemma,
            context or []
        )
    
    def _generate_ai_explanation(
        self,
        dilemma: str,
        analysis: str,
        level: ExplanationLevel
    ) -> AIExplanation:
        """
        Generate AI explanations for the analysis.
        
        Args:
            dilemma: The ethical dilemma
            analysis: The analysis to explain
            level: Level of detail for the explanation
            
        Returns:
            AIExplanation object containing the explanations
        """
        return self.explainer.explain_analysis(
            analysis,
            ExplanationType.FEATURE_IMPORTANCE,
            level
        )
    
    def format_analysis(self, analysis: EthicalAnalysis) -> str:
        """
        Format the complete ethical analysis into a readable report.
        
        Args:
            analysis: The EthicalAnalysis object to format
            
        Returns:
            Formatted analysis report as a string
        """
        report = "Ethical Analysis Report\n"
        report += "=" * 50 + "\n\n"
        
        # Basic information
        report += f"Dilemma: {analysis.dilemma}\n"
        report += f"Context: {', '.join(analysis.context)}\n"
        report += f"Model Used: {analysis.model_used}\n"
        report += f"Timestamp: {analysis.timestamp}\n\n"
        
        # Ethical principles
        report += "Ethical Principles:\n"
        report += "-" * 30 + "\n"
        for principle in analysis.ethical_principles:
            report += f"• {principle}\n"
        report += "\n"
        
        # Analysis
        report += "Analysis:\n"
        report += "-" * 30 + "\n"
        report += analysis.analysis + "\n\n"
        
        # Recommendations
        report += "Recommendations:\n"
        report += "-" * 30 + "\n"
        for recommendation in analysis.recommendations:
            report += f"• {recommendation}\n"
        report += "\n"
        
        # Confidence score
        report += f"Confidence Score: {analysis.confidence_score:.1%}\n\n"
        
        # Benchmark results
        if analysis.benchmark_results:
            report += "Model Benchmark Results:\n"
            report += "-" * 30 + "\n"
            report += self.benchmarker.format_benchmark_results(
                analysis.benchmark_results
            ) + "\n\n"
        
        # Ethical alignment
        if analysis.ethical_alignment:
            report += "Ethical Alignment Analysis:\n"
            report += "-" * 30 + "\n"
            for principle, score in analysis.ethical_alignment.items():
                report += f"• {principle}: {score:.1%}\n"
            report += "\n"
        
        # Stakeholder impacts
        if analysis.stakeholder_impacts:
            report += "Stakeholder Impact Analysis:\n"
            report += "-" * 30 + "\n"
            for impact in analysis.stakeholder_impacts:
                report += f"\nStakeholder: {impact.stakeholder}\n"
                report += f"Impact Type: {impact.impact_type.value}\n"
                report += f"Severity: {impact.severity.value}\n"
                report += f"Description: {impact.description}\n"
                report += "Affected Aspects:\n"
                for aspect in impact.affected_aspects:
                    report += f"  • {aspect}\n"
                report += "Mitigation Suggestions:\n"
                for suggestion in impact.mitigation_suggestions:
                    report += f"  • {suggestion}\n"
                report += f"Confidence Score: {impact.confidence_score:.1%}\n"
            report += "\n"
        
        # Long-term impacts
        if analysis.long_term_impact:
            report += self.long_term_analyzer.format_impact_analysis(
                analysis.long_term_impact
            )
        
        # AI Explanation
        if analysis.ai_explanation:
            report += "\n" + self.explainer.format_explanation(
                analysis.ai_explanation
            )
        
        return report