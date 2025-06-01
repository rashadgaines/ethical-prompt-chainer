import unittest
from ..cost_benefit import CostBenefitAnalyzer, CostBenefitMetrics

class TestCostBenefitAnalysis(unittest.TestCase):
    def setUp(self):
        self.analyzer = CostBenefitAnalyzer(analysis_period=5, discount_rate=0.03)
    
    def test_present_value_calculation(self):
        # Test present value calculation
        future_value = 1000
        year = 2
        present_value = self.analyzer.calculate_present_value(future_value, year)
        expected_value = 1000 / ((1 + 0.03) ** 2)
        self.assertAlmostEqual(present_value, expected_value, places=2)
    
    def test_implementation_costs(self):
        # Test cost estimation for different policy types and scales
        costs = self.analyzer.estimate_implementation_costs('ubi', 'medium')
        
        # Check that costs are distributed over the analysis period
        self.assertEqual(len(costs), 5)
        
        # Check that first year has highest cost (40%)
        total_cost = sum(costs.values())
        self.assertAlmostEqual(costs[0] / total_cost, 0.4, places=2)
        
        # Check that second year has 30%
        self.assertAlmostEqual(costs[1] / total_cost, 0.3, places=2)
    
    def test_benefit_estimation(self):
        # Test benefit estimation for different contexts
        benefits = self.analyzer.estimate_benefits('ubi', 'economic', 'medium')
        
        # Check that benefits are calculated for each year
        self.assertEqual(len(benefits), 5)
        
        # Check that benefits increase over time
        first_year_benefit = sum(benefits[0].values())
        last_year_benefit = sum(benefits[4].values())
        self.assertGreater(last_year_benefit, first_year_benefit)
    
    def test_stakeholder_impacts(self):
        # Test stakeholder impact calculation
        costs = {0: 100, 1: 100, 2: 100}
        benefits = {
            0: {'gdp_impact': 50, 'employment_impact': 50},
            1: {'gdp_impact': 60, 'employment_impact': 60},
            2: {'gdp_impact': 70, 'employment_impact': 70}
        }
        
        impacts = self.analyzer.calculate_stakeholder_impacts(costs, benefits, 'economic')
        
        # Check that impacts are calculated for each stakeholder
        self.assertIn('taxpayers', impacts)
        self.assertIn('businesses', impacts)
        self.assertIn('workers', impacts)
        self.assertIn('consumers', impacts)
        
        # Check that cost and benefit shares are calculated
        for stakeholder in impacts.values():
            self.assertIn('cost_share', stakeholder)
            self.assertIn('benefit_share', stakeholder)
    
    def test_complete_analysis(self):
        # Test complete policy analysis
        metrics = self.analyzer.analyze_policy('ubi', 'economic', 'medium')
        
        # Check that all required metrics are present
        self.assertIsInstance(metrics, CostBenefitMetrics)
        self.assertIsInstance(metrics.total_cost, float)
        self.assertIsInstance(metrics.total_benefit, float)
        self.assertIsInstance(metrics.net_benefit, float)
        self.assertIsInstance(metrics.benefit_cost_ratio, float)
        self.assertIsInstance(metrics.payback_period, float)
        self.assertIsInstance(metrics.roi, float)
        
        # Check that metrics by year are calculated
        self.assertEqual(len(metrics.metrics_by_year), 5)
        
        # Check that stakeholder impacts are calculated
        self.assertGreater(len(metrics.stakeholder_impacts), 0)
    
    def test_analysis_formatting(self):
        # Test analysis report formatting
        metrics = self.analyzer.analyze_policy('ubi', 'economic', 'medium')
        report = self.analyzer.format_analysis(metrics)
        
        # Check that report contains all required sections
        self.assertIn('Financial Metrics:', report)
        self.assertIn('Annual Metrics:', report)
        self.assertIn('Stakeholder Impacts:', report)
        
        # Check that financial metrics are formatted correctly
        self.assertIn('Total Cost:', report)
        self.assertIn('Total Benefit:', report)
        self.assertIn('Net Benefit:', report)
        self.assertIn('Benefit-Cost Ratio:', report)
        self.assertIn('Payback Period:', report)
        self.assertIn('ROI:', report)

if __name__ == '__main__':
    unittest.main() 