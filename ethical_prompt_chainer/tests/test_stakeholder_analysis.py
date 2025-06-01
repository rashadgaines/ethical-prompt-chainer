import unittest
from unittest.mock import Mock, patch
from ..stakeholder_analysis import (
    StakeholderAnalyzer,
    StakeholderGroup,
    StakeholderImpact,
    ImpactType,
    ImpactSeverity
)

class TestStakeholderAnalyzer(unittest.TestCase):
    """Test cases for the StakeholderAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = StakeholderAnalyzer()
        self.sample_decision = (
            "Implement a new carbon tax policy to reduce emissions and "
            "fund renewable energy initiatives, while providing subsidies "
            "for low-income households to offset increased energy costs."
        )
    
    def test_get_stakeholder_group(self):
        """Test retrieving stakeholder groups."""
        # Test valid group
        group = self.analyzer.get_stakeholder_group('individuals')
        self.assertIsInstance(group, StakeholderGroup)
        self.assertEqual(group.name, "Individual Citizens")
        
        # Test invalid group
        group = self.analyzer.get_stakeholder_group('invalid')
        self.assertIsNone(group)
    
    def test_identify_stakeholders(self):
        """Test stakeholder identification."""
        # Test environmental context
        context = "environmental policy climate change"
        groups = self.analyzer.identify_stakeholders(context)
        self.assertTrue(any(g.name == "Environmental Stakeholders" for g in groups))
        
        # Test business context
        context = "market competition regulatory compliance"
        groups = self.analyzer.identify_stakeholders(context)
        self.assertTrue(any(g.name == "Businesses and Corporations" for g in groups))
    
    def test_analyze_impact(self):
        """Test impact analysis."""
        group = self.analyzer.get_stakeholder_group('individuals')
        impact = self.analyzer.analyze_impact(self.sample_decision, group)
        
        self.assertIsInstance(impact, StakeholderImpact)
        self.assertEqual(impact.stakeholder, group.name)
        self.assertIsInstance(impact.impact_type, ImpactType)
        self.assertIsInstance(impact.severity, ImpactSeverity)
        self.assertIsInstance(impact.description, str)
        self.assertIsInstance(impact.affected_aspects, list)
        self.assertIsInstance(impact.mitigation_suggestions, list)
        self.assertIsInstance(impact.confidence_score, float)
        self.assertTrue(0 <= impact.confidence_score <= 1)
    
    def test_determine_impact_type(self):
        """Test impact type determination."""
        # Test positive impact
        decision = "This policy will benefit all citizens and improve quality of life"
        group = self.analyzer.get_stakeholder_group('individuals')
        impact_type = self.analyzer._determine_impact_type(decision, group)
        self.assertEqual(impact_type, ImpactType.POSITIVE)
        
        # Test negative impact
        decision = "This policy will harm businesses and increase costs"
        group = self.analyzer.get_stakeholder_group('businesses')
        impact_type = self.analyzer._determine_impact_type(decision, group)
        self.assertEqual(impact_type, ImpactType.NEGATIVE)
        
        # Test mixed impact
        decision = "This policy will benefit some but harm others"
        group = self.analyzer.get_stakeholder_group('individuals')
        impact_type = self.analyzer._determine_impact_type(decision, group)
        self.assertEqual(impact_type, ImpactType.MIXED)
    
    def test_determine_impact_severity(self):
        """Test impact severity determination."""
        group = self.analyzer.get_stakeholder_group('vulnerable')
        
        # Test critical severity
        decision = "This policy will have critical and irreversible impacts"
        severity = self.analyzer._determine_impact_severity(decision, group)
        self.assertEqual(severity, ImpactSeverity.CRITICAL)
        
        # Test low severity
        decision = "This policy will have minor and negligible impacts"
        severity = self.analyzer._determine_impact_severity(decision, group)
        self.assertEqual(severity, ImpactSeverity.LOW)
    
    def test_identify_affected_aspects(self):
        """Test affected aspects identification."""
        group = self.analyzer.get_stakeholder_group('businesses')
        aspects = self.analyzer._identify_affected_aspects(self.sample_decision, group)
        
        self.assertIsInstance(aspects, list)
        self.assertTrue(all(isinstance(aspect, str) for aspect in aspects))
        self.assertTrue(len(aspects) > 0)
    
    def test_generate_mitigation_suggestions(self):
        """Test mitigation suggestions generation."""
        group = self.analyzer.get_stakeholder_group('vulnerable')
        impact_type = ImpactType.NEGATIVE
        severity = ImpactSeverity.HIGH
        
        suggestions = self.analyzer._generate_mitigation_suggestions(
            self.sample_decision, group, impact_type, severity
        )
        
        self.assertIsInstance(suggestions, list)
        self.assertTrue(all(isinstance(suggestion, str) for suggestion in suggestions))
        self.assertTrue(len(suggestions) > 0)
    
    def test_calculate_confidence_score(self):
        """Test confidence score calculation."""
        group = self.analyzer.get_stakeholder_group('individuals')
        impact_type = ImpactType.POSITIVE
        severity = ImpactSeverity.MEDIUM
        
        score = self.analyzer._calculate_confidence_score(
            self.sample_decision, group, impact_type, severity
        )
        
        self.assertIsInstance(score, float)
        self.assertTrue(0 <= score <= 1)
    
    def test_format_impact_analysis(self):
        """Test impact analysis formatting."""
        group = self.analyzer.get_stakeholder_group('individuals')
        impact = self.analyzer.analyze_impact(self.sample_decision, group)
        formatted = self.analyzer.format_impact_analysis(impact)
        
        self.assertIsInstance(formatted, str)
        self.assertIn(impact.stakeholder, formatted)
        self.assertIn(impact.impact_type.value, formatted)
        self.assertIn(impact.severity.value, formatted)
        self.assertIn(str(impact.confidence_score), formatted)
        self.assertIn(impact.description, formatted)
        
        for aspect in impact.affected_aspects:
            self.assertIn(aspect, formatted)
        
        for suggestion in impact.mitigation_suggestions:
            self.assertIn(suggestion, formatted)

if __name__ == '__main__':
    unittest.main() 