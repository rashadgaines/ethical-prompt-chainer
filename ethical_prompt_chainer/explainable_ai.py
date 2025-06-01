from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass
import json
import logging
from pathlib import Path
from enum import Enum
import numpy as np
from datetime import datetime

logger = logging.getLogger(__name__)

class ExplanationType(Enum):
    """Types of explanations for AI decisions."""
    FEATURE_IMPORTANCE = "feature_importance"
    DECISION_PATH = "decision_path"
    COUNTERFACTUAL = "counterfactual"
    SIMILAR_CASES = "similar_cases"
    CONFIDENCE_BREAKDOWN = "confidence_breakdown"
    ETHICAL_REASONING = "ethical_reasoning"

class ExplanationLevel(Enum):
    """Levels of explanation detail."""
    BASIC = "basic"  # Simple explanation
    DETAILED = "detailed"  # Comprehensive explanation
    TECHNICAL = "technical"  # Technical details included

@dataclass
class FeatureImportance:
    """Container for feature importance analysis."""
    feature: str
    importance_score: float  # 0-1 score
    contribution: str
    confidence: float  # 0-1 score

@dataclass
class DecisionPath:
    """Container for decision path analysis."""
    steps: List[str]
    reasoning: List[str]
    alternatives: List[str]
    confidence_scores: List[float]

@dataclass
class CounterfactualAnalysis:
    """Container for counterfactual analysis."""
    scenario: str
    outcome: str
    changed_factors: List[str]
    confidence: float  # 0-1 score

@dataclass
class SimilarCase:
    """Container for similar case analysis."""
    case_id: str
    similarity_score: float  # 0-1 score
    key_similarities: List[str]
    key_differences: List[str]
    outcome: str

@dataclass
class ConfidenceBreakdown:
    """Container for confidence score breakdown."""
    factors: Dict[str, float]  # Factor name to confidence score
    reasoning: Dict[str, str]  # Factor name to explanation
    overall_confidence: float  # 0-1 score

@dataclass
class EthicalReasoning:
    """Container for ethical reasoning explanation."""
    principles_applied: List[str]
    reasoning_steps: List[str]
    tradeoffs: List[str]
    justification: str

@dataclass
class AIExplanation:
    """Container for complete AI explanation."""
    feature_importance: List[FeatureImportance]
    decision_path: DecisionPath
    counterfactuals: List[CounterfactualAnalysis]
    similar_cases: List[SimilarCase]
    confidence_breakdown: ConfidenceBreakdown
    ethical_reasoning: EthicalReasoning
    timestamp: datetime

class ExplainableAI:
    """Provides explanations for AI-driven ethical analysis."""
    
    def __init__(self):
        """Initialize the explainable AI system."""
        self.explanation_templates = self._initialize_templates()
        self.feature_weights = self._initialize_feature_weights()
    
    def _initialize_templates(self) -> Dict[str, str]:
        """Initialize explanation templates."""
        return {
            "feature_importance": "The {feature} was important because {contribution}",
            "decision_step": "Step {step}: {reasoning}",
            "counterfactual": "If {scenario}, then {outcome}",
            "similar_case": "Case {case_id} is similar because {similarities}",
            "confidence_factor": "{factor} contributes {score} to confidence because {reasoning}",
            "ethical_principle": "Applied {principle} because {reasoning}"
        }
    
    def _initialize_feature_weights(self) -> Dict[str, float]:
        """Initialize weights for different features."""
        return {
            "ethical_principles": 0.3,
            "stakeholder_impacts": 0.2,
            "long_term_effects": 0.2,
            "context_relevance": 0.15,
            "historical_precedents": 0.15
        }
    
    def explain_analysis(
        self,
        analysis: Any,
        explanation_type: ExplanationType,
        level: ExplanationLevel = ExplanationLevel.DETAILED
    ) -> AIExplanation:
        """
        Generate explanations for the ethical analysis.
        
        Args:
            analysis: The ethical analysis to explain
            explanation_type: Type of explanation to generate
            level: Level of detail for the explanation
            
        Returns:
            AIExplanation object containing the explanations
        """
        # Generate feature importance analysis
        feature_importance = self._analyze_feature_importance(analysis)
        
        # Generate decision path analysis
        decision_path = self._analyze_decision_path(analysis)
        
        # Generate counterfactual analysis
        counterfactuals = self._generate_counterfactuals(analysis)
        
        # Find similar cases
        similar_cases = self._find_similar_cases(analysis)
        
        # Break down confidence scores
        confidence_breakdown = self._break_down_confidence(analysis)
        
        # Explain ethical reasoning
        ethical_reasoning = self._explain_ethical_reasoning(analysis)
        
        return AIExplanation(
            feature_importance=feature_importance,
            decision_path=decision_path,
            counterfactuals=counterfactuals,
            similar_cases=similar_cases,
            confidence_breakdown=confidence_breakdown,
            ethical_reasoning=ethical_reasoning,
            timestamp=datetime.now()
        )
    
    def _analyze_feature_importance(self, analysis: Any) -> List[FeatureImportance]:
        """Analyze importance of different features in the analysis."""
        features = []
        
        # Analyze ethical principles
        if hasattr(analysis, 'ethical_principles'):
            for principle in analysis.ethical_principles:
                features.append(FeatureImportance(
                    feature=f"Ethical Principle: {principle}",
                    importance_score=self.feature_weights["ethical_principles"],
                    contribution=f"This principle guided the analysis by {self._explain_principle_contribution(principle)}",
                    confidence=0.8
                ))
        
        # Analyze stakeholder impacts
        if hasattr(analysis, 'stakeholder_impacts'):
            for impact in analysis.stakeholder_impacts:
                features.append(FeatureImportance(
                    feature=f"Stakeholder Impact: {impact.stakeholder}",
                    importance_score=self.feature_weights["stakeholder_impacts"],
                    contribution=f"This impact was considered because {self._explain_impact_contribution(impact)}",
                    confidence=impact.confidence_score
                ))
        
        # Analyze long-term impacts
        if hasattr(analysis, 'long_term_impact'):
            features.append(FeatureImportance(
                feature="Long-term Impact Analysis",
                importance_score=self.feature_weights["long_term_effects"],
                contribution=f"This analysis provided insights into {self._explain_long_term_contribution(analysis.long_term_impact)}",
                confidence=analysis.long_term_impact.confidence_score
            ))
        
        return features
    
    def _analyze_decision_path(self, analysis: Any) -> DecisionPath:
        """Analyze the decision-making path in the analysis."""
        steps = []
        reasoning = []
        alternatives = []
        confidence_scores = []
        
        # Add steps based on analysis components
        if hasattr(analysis, 'ethical_principles'):
            steps.append("Identify ethical principles")
            reasoning.append("Analyzed the dilemma to identify relevant ethical principles")
            alternatives.append("Consider alternative ethical frameworks")
            confidence_scores.append(0.9)
        
        if hasattr(analysis, 'stakeholder_impacts'):
            steps.append("Analyze stakeholder impacts")
            reasoning.append("Evaluated effects on different stakeholder groups")
            alternatives.append("Consider different stakeholder perspectives")
            confidence_scores.append(0.85)
        
        if hasattr(analysis, 'long_term_impact'):
            steps.append("Assess long-term impacts")
            reasoning.append("Analyzed potential future consequences")
            alternatives.append("Consider different future scenarios")
            confidence_scores.append(0.8)
        
        return DecisionPath(
            steps=steps,
            reasoning=reasoning,
            alternatives=alternatives,
            confidence_scores=confidence_scores
        )
    
    def _generate_counterfactuals(self, analysis: Any) -> List[CounterfactualAnalysis]:
        """Generate counterfactual scenarios for the analysis."""
        counterfactuals = []
        
        # Generate counterfactuals for different aspects
        if hasattr(analysis, 'ethical_principles'):
            counterfactuals.append(CounterfactualAnalysis(
                scenario="Different ethical principles were applied",
                outcome="The analysis would have focused on different aspects",
                changed_factors=["Ethical framework", "Principle weights"],
                confidence=0.7
            ))
        
        if hasattr(analysis, 'stakeholder_impacts'):
            counterfactuals.append(CounterfactualAnalysis(
                scenario="Different stakeholder groups were considered",
                outcome="The impact assessment would have different priorities",
                changed_factors=["Stakeholder selection", "Impact weights"],
                confidence=0.75
            ))
        
        return counterfactuals
    
    def _find_similar_cases(self, analysis: Any) -> List[SimilarCase]:
        """Find similar cases to the current analysis."""
        # This would typically involve a case database
        # For now, return a placeholder
        return [
            SimilarCase(
                case_id="CASE001",
                similarity_score=0.85,
                key_similarities=["Similar ethical principles", "Similar stakeholder impacts"],
                key_differences=["Different context", "Different time horizon"],
                outcome="Similar recommendations were made"
            )
        ]
    
    def _break_down_confidence(self, analysis: Any) -> ConfidenceBreakdown:
        """Break down the confidence score into contributing factors."""
        factors = {}
        reasoning = {}
        
        # Add factors based on analysis components
        if hasattr(analysis, 'confidence_score'):
            factors["Overall Analysis"] = analysis.confidence_score
            reasoning["Overall Analysis"] = "Based on the complete analysis"
        
        if hasattr(analysis, 'ethical_principles'):
            factors["Ethical Principles"] = 0.9
            reasoning["Ethical Principles"] = "Clear application of ethical principles"
        
        if hasattr(analysis, 'stakeholder_impacts'):
            factors["Stakeholder Analysis"] = 0.85
            reasoning["Stakeholder Analysis"] = "Comprehensive stakeholder impact assessment"
        
        if hasattr(analysis, 'long_term_impact'):
            factors["Long-term Impact"] = 0.8
            reasoning["Long-term Impact"] = "Thorough future scenario analysis"
        
        return ConfidenceBreakdown(
            factors=factors,
            reasoning=reasoning,
            overall_confidence=analysis.confidence_score if hasattr(analysis, 'confidence_score') else 0.8
        )
    
    def _explain_ethical_reasoning(self, analysis: Any) -> EthicalReasoning:
        """Explain the ethical reasoning process."""
        principles = []
        steps = []
        tradeoffs = []
        
        # Add principles and reasoning
        if hasattr(analysis, 'ethical_principles'):
            principles.extend(analysis.ethical_principles)
            steps.append("Identified relevant ethical principles")
            steps.append("Applied principles to the dilemma")
            tradeoffs.append("Balanced different ethical considerations")
        
        if hasattr(analysis, 'stakeholder_impacts'):
            steps.append("Evaluated stakeholder impacts")
            tradeoffs.append("Balanced different stakeholder interests")
        
        if hasattr(analysis, 'long_term_impact'):
            steps.append("Considered long-term consequences")
            tradeoffs.append("Balanced short-term and long-term effects")
        
        return EthicalReasoning(
            principles_applied=principles,
            reasoning_steps=steps,
            tradeoffs=tradeoffs,
            justification="The analysis followed a systematic approach to ethical reasoning"
        )
    
    def _explain_principle_contribution(self, principle: str) -> str:
        """Explain how an ethical principle contributed to the analysis."""
        return f"providing a framework for evaluating the ethical implications of the decision"
    
    def _explain_impact_contribution(self, impact: Any) -> str:
        """Explain how a stakeholder impact contributed to the analysis."""
        return f"highlighting the effects on {impact.stakeholder} and their interests"
    
    def _explain_long_term_contribution(self, impact: Any) -> str:
        """Explain how long-term impact analysis contributed to the analysis."""
        return "future consequences and sustainability considerations"
    
    def format_explanation(self, explanation: AIExplanation) -> str:
        """Format the AI explanation into a readable report."""
        report = "AI Explanation Report\n"
        report += "=" * 50 + "\n\n"
        
        # Feature Importance
        report += "Feature Importance Analysis:\n"
        report += "-" * 30 + "\n"
        for feature in explanation.feature_importance:
            report += f"• {feature.feature} (Score: {feature.importance_score:.1%})\n"
            report += f"  Contribution: {feature.contribution}\n"
            report += f"  Confidence: {feature.confidence:.1%}\n\n"
        
        # Decision Path
        report += "Decision Path Analysis:\n"
        report += "-" * 30 + "\n"
        for i, (step, reason) in enumerate(zip(explanation.decision_path.steps,
                                             explanation.decision_path.reasoning)):
            report += f"Step {i+1}: {step}\n"
            report += f"Reasoning: {reason}\n"
            report += f"Alternative: {explanation.decision_path.alternatives[i]}\n"
            report += f"Confidence: {explanation.decision_path.confidence_scores[i]:.1%}\n\n"
        
        # Counterfactuals
        report += "Counterfactual Analysis:\n"
        report += "-" * 30 + "\n"
        for counter in explanation.counterfactuals:
            report += f"Scenario: {counter.scenario}\n"
            report += f"Outcome: {counter.outcome}\n"
            report += "Changed Factors:\n"
            for factor in counter.changed_factors:
                report += f"• {factor}\n"
            report += f"Confidence: {counter.confidence:.1%}\n\n"
        
        # Similar Cases
        report += "Similar Cases:\n"
        report += "-" * 30 + "\n"
        for case in explanation.similar_cases:
            report += f"Case ID: {case.case_id}\n"
            report += f"Similarity Score: {case.similarity_score:.1%}\n"
            report += "Key Similarities:\n"
            for sim in case.key_similarities:
                report += f"• {sim}\n"
            report += "Key Differences:\n"
            for diff in case.key_differences:
                report += f"• {diff}\n"
            report += f"Outcome: {case.outcome}\n\n"
        
        # Confidence Breakdown
        report += "Confidence Score Breakdown:\n"
        report += "-" * 30 + "\n"
        for factor, score in explanation.confidence_breakdown.factors.items():
            report += f"• {factor}: {score:.1%}\n"
            report += f"  Reasoning: {explanation.confidence_breakdown.reasoning[factor]}\n"
        report += f"\nOverall Confidence: {explanation.confidence_breakdown.overall_confidence:.1%}\n\n"
        
        # Ethical Reasoning
        report += "Ethical Reasoning:\n"
        report += "-" * 30 + "\n"
        report += "Applied Principles:\n"
        for principle in explanation.ethical_reasoning.principles_applied:
            report += f"• {principle}\n"
        report += "\nReasoning Steps:\n"
        for step in explanation.ethical_reasoning.reasoning_steps:
            report += f"• {step}\n"
        report += "\nTradeoffs Considered:\n"
        for tradeoff in explanation.ethical_reasoning.tradeoffs:
            report += f"• {tradeoff}\n"
        report += f"\nJustification: {explanation.ethical_reasoning.justification}\n"
        
        return report 