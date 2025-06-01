import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

@dataclass
class CostBenefitMetrics:
    """Container for cost-benefit analysis metrics."""
    total_cost: float
    total_benefit: float
    net_benefit: float
    benefit_cost_ratio: float
    payback_period: float
    roi: float
    metrics_by_year: Dict[int, Dict[str, float]]
    stakeholder_impacts: Dict[str, Dict[str, float]]

class CostBenefitAnalyzer:
    """Analyzes costs and benefits of policy options."""
    
    # Economic indicators and their weights for different contexts
    ECONOMIC_INDICATORS = {
        'economic': {
            'gdp_impact': 0.3,
            'employment_impact': 0.3,
            'tax_revenue': 0.2,
            'market_stability': 0.2
        },
        'social': {
            'poverty_reduction': 0.3,
            'health_outcomes': 0.3,
            'education_access': 0.2,
            'social_mobility': 0.2
        },
        'environmental': {
            'emissions_reduction': 0.4,
            'resource_conservation': 0.3,
            'biodiversity': 0.2,
            'resilience': 0.1
        }
    }
    
    def __init__(self, analysis_period: int = 10, discount_rate: float = 0.03):
        """
        Initialize the cost-benefit analyzer.
        
        Args:
            analysis_period: Number of years to analyze
            discount_rate: Annual discount rate for future costs/benefits
        """
        self.analysis_period = analysis_period
        self.discount_rate = discount_rate
    
    def calculate_present_value(self, future_value: float, year: int) -> float:
        """Calculate present value of a future cost or benefit."""
        return future_value / ((1 + self.discount_rate) ** year)
    
    def estimate_implementation_costs(self, policy_type: str, scale: str) -> Dict[int, float]:
        """Estimate implementation costs over time."""
        # Base costs by policy type and scale
        base_costs = {
            'ubi': {'small': 100e9, 'medium': 500e9, 'large': 1e12},
            'healthcare': {'small': 50e9, 'medium': 200e9, 'large': 500e9},
            'environmental': {'small': 20e9, 'medium': 100e9, 'large': 300e9}
        }
        
        # Get base cost for the policy type and scale
        base_cost = base_costs.get(policy_type, {}).get(scale, 100e9)
        
        # Distribute costs over time with front-loading
        costs = {}
        for year in range(self.analysis_period):
            if year == 0:
                costs[year] = base_cost * 0.4  # 40% in first year
            elif year == 1:
                costs[year] = base_cost * 0.3  # 30% in second year
            else:
                costs[year] = base_cost * 0.3 / (self.analysis_period - 2)  # Remaining 30% spread over remaining years
        
        return costs
    
    def estimate_benefits(self, policy_type: str, context: str, 
                         scale: str) -> Dict[int, Dict[str, float]]:
        """Estimate benefits over time by category."""
        # Base benefits by policy type and context
        base_benefits = {
            'ubi': {
                'economic': {'gdp_impact': 0.02, 'employment_impact': 0.03},
                'social': {'poverty_reduction': 0.15, 'health_outcomes': 0.1}
            },
            'healthcare': {
                'economic': {'gdp_impact': 0.01, 'employment_impact': 0.02},
                'social': {'health_outcomes': 0.2, 'education_access': 0.1}
            },
            'environmental': {
                'environmental': {'emissions_reduction': 0.2, 'resource_conservation': 0.15}
            }
        }
        
        # Scale factors
        scale_factors = {'small': 0.5, 'medium': 1.0, 'large': 2.0}
        scale_factor = scale_factors.get(scale, 1.0)
        
        # Calculate benefits over time
        benefits = {}
        base_benefit = base_benefits.get(policy_type, {}).get(context, {})
        
        for year in range(self.analysis_period):
            year_benefits = {}
            for metric, impact in base_benefit.items():
                # Benefits typically increase over time
                year_benefits[metric] = impact * scale_factor * (1 + 0.05 * year)
            benefits[year] = year_benefits
        
        return benefits
    
    def calculate_stakeholder_impacts(self, costs: Dict[int, float],
                                    benefits: Dict[int, Dict[str, float]],
                                    context: str) -> Dict[str, Dict[str, float]]:
        """Calculate impacts on different stakeholder groups."""
        stakeholders = {
            'economic': ['taxpayers', 'businesses', 'workers', 'consumers'],
            'social': ['low_income', 'middle_class', 'high_income', 'vulnerable_groups'],
            'environmental': ['local_communities', 'future_generations', 'ecosystems']
        }
        
        impacts = {}
        for stakeholder in stakeholders.get(context, []):
            # Distribute costs and benefits among stakeholders
            # This is a simplified model - in practice, would use more sophisticated distribution
            impacts[stakeholder] = {
                'cost_share': np.mean(list(costs.values())) / len(stakeholders[context]),
                'benefit_share': np.mean([sum(b.values()) for b in benefits.values()]) / len(stakeholders[context])
            }
        
        return impacts
    
    def analyze_policy(self, policy_type: str, context: str, 
                      scale: str = 'medium') -> CostBenefitMetrics:
        """
        Perform a complete cost-benefit analysis for a policy.
        
        Args:
            policy_type: Type of policy (e.g., 'ubi', 'healthcare', 'environmental')
            context: Context of the policy (e.g., 'economic', 'social', 'environmental')
            scale: Scale of implementation ('small', 'medium', 'large')
            
        Returns:
            CostBenefitMetrics object containing the analysis results
        """
        # Estimate costs and benefits
        costs = self.estimate_implementation_costs(policy_type, scale)
        benefits = self.estimate_benefits(policy_type, context, scale)
        
        # Calculate present values
        present_value_costs = sum(self.calculate_present_value(cost, year) 
                                for year, cost in costs.items())
        present_value_benefits = sum(
            self.calculate_present_value(sum(benefits[year].values()), year)
            for year in range(self.analysis_period)
        )
        
        # Calculate key metrics
        net_benefit = present_value_benefits - present_value_costs
        benefit_cost_ratio = present_value_benefits / present_value_costs if present_value_costs > 0 else float('inf')
        
        # Calculate payback period
        cumulative_benefits = 0
        payback_period = float('inf')
        for year in range(self.analysis_period):
            year_benefit = sum(benefits[year].values())
            cumulative_benefits += self.calculate_present_value(year_benefit, year)
            if cumulative_benefits >= present_value_costs:
                payback_period = year + 1
                break
        
        # Calculate ROI
        roi = (net_benefit / present_value_costs) * 100 if present_value_costs > 0 else float('inf')
        
        # Calculate stakeholder impacts
        stakeholder_impacts = self.calculate_stakeholder_impacts(costs, benefits, context)
        
        return CostBenefitMetrics(
            total_cost=present_value_costs,
            total_benefit=present_value_benefits,
            net_benefit=net_benefit,
            benefit_cost_ratio=benefit_cost_ratio,
            payback_period=payback_period,
            roi=roi,
            metrics_by_year={
                year: {
                    'cost': costs.get(year, 0),
                    'benefit': sum(benefits[year].values())
                }
                for year in range(self.analysis_period)
            },
            stakeholder_impacts=stakeholder_impacts
        )
    
    def format_analysis(self, metrics: CostBenefitMetrics) -> str:
        """Format the cost-benefit analysis results in a readable way."""
        return f"""Cost-Benefit Analysis Report

Financial Metrics:
-----------------
Total Cost: ${metrics.total_cost:,.2f}
Total Benefit: ${metrics.total_benefit:,.2f}
Net Benefit: ${metrics.net_benefit:,.2f}
Benefit-Cost Ratio: {metrics.benefit_cost_ratio:.2f}
Payback Period: {metrics.payback_period:.1f} years
ROI: {metrics.roi:.1f}%

Annual Metrics:
--------------
{self._format_annual_metrics(metrics.metrics_by_year)}

Stakeholder Impacts:
------------------
{self._format_stakeholder_impacts(metrics.stakeholder_impacts)}"""
    
    def _format_annual_metrics(self, metrics_by_year: Dict[int, Dict[str, float]]) -> str:
        """Format annual metrics in a table-like structure."""
        lines = []
        for year, metrics in metrics_by_year.items():
            lines.append(f"Year {year + 1}:")
            lines.append(f"  Cost: ${metrics['cost']:,.2f}")
            lines.append(f"  Benefit: ${metrics['benefit']:,.2f}")
            lines.append(f"  Net: ${metrics['benefit'] - metrics['cost']:,.2f}")
        return "\n".join(lines)
    
    def _format_stakeholder_impacts(self, impacts: Dict[str, Dict[str, float]]) -> str:
        """Format stakeholder impacts in a readable way."""
        lines = []
        for stakeholder, metrics in impacts.items():
            lines.append(f"{stakeholder.replace('_', ' ').title()}:")
            lines.append(f"  Cost Share: ${metrics['cost_share']:,.2f}")
            lines.append(f"  Benefit Share: ${metrics['benefit_share']:,.2f}")
            lines.append(f"  Net Impact: ${metrics['benefit_share'] - metrics['cost_share']:,.2f}")
        return "\n".join(lines) 