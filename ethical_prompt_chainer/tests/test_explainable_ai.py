import unittest
from unittest.mock import Mock, patch
from datetime import datetime
from ..explainable_ai import (
    ExplainableAI,
    ExplanationType,
    ExplanationLevel,
    FeatureImportance,
    DecisionPath,
    CounterfactualAnalysis,
    SimilarCase,
    ConfidenceBreakdown,
    EthicalReasoning,
    AIExplanation
)

class TestExplainableAI(unittest.TestCase):
    """Test cases for the ExplainableAI class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.explainer = ExplainableAI()
        
        # Create a mock analysis object
        self.mock_analysis = Mock()
        self.mock_analysis.ethical_principles = ["Autonomy", "Beneficence"]
        self.mock_analysis.stakeholder_impacts = [
            Mock(stakeholder="Community", confidence_score=0.85),
            Mock(stakeholder="Environment", confidence_score=0.9)
        ]
        self.mock_analysis.long_term_impact = Mock(confidence_score=0.8)
        self.mock_analysis.confidence_score = 0.85
    
    def test_explain_analysis(self):
        """Test the main explanation generation method."""
        explanation = self.explainer.explain_analysis(
            self.mock_analysis,
            ExplanationType.FEATURE_IMPORTANCE,
            ExplanationLevel.DETAILED
        )
        
        # Verify the structure of the explanation
        self.assertIsInstance(explanation, AIExplanation)
        self.assertIsInstance(explanation.feature_importance, list)
        self.assertIsInstance(explanation.decision_path, DecisionPath)
        self.assertIsInstance(explanation.counterfactuals, list)
        self.assertIsInstance(explanation.similar_cases, list)
        self.assertIsInstance(explanation.confidence_breakdown, ConfidenceBreakdown)
        self.assertIsInstance(explanation.ethical_reasoning, EthicalReasoning)
        self.assertIsInstance(explanation.timestamp, datetime)
    
    def test_analyze_feature_importance(self):
        """Test feature importance analysis."""
        features = self.explainer._analyze_feature_importance(self.mock_analysis)
        
        # Verify features
        self.assertIsInstance(features, list)
        self.assertTrue(len(features) > 0)
        
        for feature in features:
            self.assertIsInstance(feature, FeatureImportance)
            self.assertTrue(0 <= feature.importance_score <= 1)
            self.assertTrue(0 <= feature.confidence <= 1)
            self.assertTrue(len(feature.contribution) > 0)
    
    def test_analyze_decision_path(self):
        """Test decision path analysis."""
        path = self.explainer._analyze_decision_path(self.mock_analysis)
        
        # Verify decision path
        self.assertIsInstance(path, DecisionPath)
        self.assertTrue(len(path.steps) > 0)
        self.assertTrue(len(path.reasoning) > 0)
        self.assertTrue(len(path.alternatives) > 0)
        self.assertTrue(len(path.confidence_scores) > 0)
        
        # Verify all lists have same length
        self.assertEqual(len(path.steps), len(path.reasoning))
        self.assertEqual(len(path.steps), len(path.alternatives))
        self.assertEqual(len(path.steps), len(path.confidence_scores))
    
    def test_generate_counterfactuals(self):
        """Test counterfactual generation."""
        counterfactuals = self.explainer._generate_counterfactuals(self.mock_analysis)
        
        # Verify counterfactuals
        self.assertIsInstance(counterfactuals, list)
        self.assertTrue(len(counterfactuals) > 0)
        
        for counter in counterfactuals:
            self.assertIsInstance(counter, CounterfactualAnalysis)
            self.assertTrue(len(counter.scenario) > 0)
            self.assertTrue(len(counter.outcome) > 0)
            self.assertTrue(len(counter.changed_factors) > 0)
            self.assertTrue(0 <= counter.confidence <= 1)
    
    def test_find_similar_cases(self):
        """Test similar case finding."""
        cases = self.explainer._find_similar_cases(self.mock_analysis)
        
        # Verify cases
        self.assertIsInstance(cases, list)
        self.assertTrue(len(cases) > 0)
        
        for case in cases:
            self.assertIsInstance(case, SimilarCase)
            self.assertTrue(len(case.case_id) > 0)
            self.assertTrue(0 <= case.similarity_score <= 1)
            self.assertTrue(len(case.key_similarities) > 0)
            self.assertTrue(len(case.key_differences) > 0)
            self.assertTrue(len(case.outcome) > 0)
    
    def test_break_down_confidence(self):
        """Test confidence score breakdown."""
        breakdown = self.explainer._break_down_confidence(self.mock_analysis)
        
        # Verify breakdown
        self.assertIsInstance(breakdown, ConfidenceBreakdown)
        self.assertTrue(len(breakdown.factors) > 0)
        self.assertTrue(len(breakdown.reasoning) > 0)
        self.assertTrue(0 <= breakdown.overall_confidence <= 1)
        
        # Verify factors and reasoning have same keys
        self.assertEqual(set(breakdown.factors.keys()),
                        set(breakdown.reasoning.keys()))
    
    def test_explain_ethical_reasoning(self):
        """Test ethical reasoning explanation."""
        reasoning = self.explainer._explain_ethical_reasoning(self.mock_analysis)
        
        # Verify reasoning
        self.assertIsInstance(reasoning, EthicalReasoning)
        self.assertTrue(len(reasoning.principles_applied) > 0)
        self.assertTrue(len(reasoning.reasoning_steps) > 0)
        self.assertTrue(len(reasoning.tradeoffs) > 0)
        self.assertTrue(len(reasoning.justification) > 0)
    
    def test_format_explanation(self):
        """Test explanation formatting."""
        # Create a sample explanation
        explanation = AIExplanation(
            feature_importance=[
                FeatureImportance(
                    feature="Test Feature",
                    importance_score=0.8,
                    contribution="Test contribution",
                    confidence=0.9
                )
            ],
            decision_path=DecisionPath(
                steps=["Test Step"],
                reasoning=["Test Reasoning"],
                alternatives=["Test Alternative"],
                confidence_scores=[0.85]
            ),
            counterfactuals=[
                CounterfactualAnalysis(
                    scenario="Test Scenario",
                    outcome="Test Outcome",
                    changed_factors=["Test Factor"],
                    confidence=0.75
                )
            ],
            similar_cases=[
                SimilarCase(
                    case_id="TEST001",
                    similarity_score=0.85,
                    key_similarities=["Test Similarity"],
                    key_differences=["Test Difference"],
                    outcome="Test Outcome"
                )
            ],
            confidence_breakdown=ConfidenceBreakdown(
                factors={"Test Factor": 0.8},
                reasoning={"Test Factor": "Test Reasoning"},
                overall_confidence=0.85
            ),
            ethical_reasoning=EthicalReasoning(
                principles_applied=["Test Principle"],
                reasoning_steps=["Test Step"],
                tradeoffs=["Test Tradeoff"],
                justification="Test Justification"
            ),
            timestamp=datetime.now()
        )
        
        report = self.explainer.format_explanation(explanation)
        
        # Verify report format
        self.assertIsInstance(report, str)
        self.assertTrue(len(report) > 0)
        self.assertIn("AI Explanation Report", report)
        self.assertIn("Test Feature", report)
        self.assertIn("Test Step", report)
        self.assertIn("Test Scenario", report)
        self.assertIn("TEST001", report)
        self.assertIn("Test Factor", report)
        self.assertIn("Test Principle", report)
    
    def test_explanation_templates(self):
        """Test explanation template initialization."""
        templates = self.explainer._initialize_templates()
        
        # Verify templates
        self.assertIsInstance(templates, dict)
        self.assertTrue(len(templates) > 0)
        
        required_templates = [
            "feature_importance",
            "decision_step",
            "counterfactual",
            "similar_case",
            "confidence_factor",
            "ethical_principle"
        ]
        
        for template in required_templates:
            self.assertIn(template, templates)
            self.assertTrue(len(templates[template]) > 0)
    
    def test_feature_weights(self):
        """Test feature weight initialization."""
        weights = self.explainer._initialize_feature_weights()
        
        # Verify weights
        self.assertIsInstance(weights, dict)
        self.assertTrue(len(weights) > 0)
        
        required_weights = [
            "ethical_principles",
            "stakeholder_impacts",
            "long_term_effects",
            "context_relevance",
            "historical_precedents"
        ]
        
        for weight in required_weights:
            self.assertIn(weight, weights)
            self.assertTrue(0 <= weights[weight] <= 1)
        
        # Verify weights sum to 1
        self.assertAlmostEqual(sum(weights.values()), 1.0)

if __name__ == '__main__':
    unittest.main() 