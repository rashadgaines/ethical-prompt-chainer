from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
import json
import logging
from pathlib import Path
from enum import Enum
import numpy as np
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class TimeHorizon(Enum):
    """Time horizons for impact assessment."""
    SHORT_TERM = "short_term"  # 1-2 years
    MEDIUM_TERM = "medium_term"  # 3-5 years
    LONG_TERM = "long_term"  # 5-10 years
    FUTURE_GENERATIONS = "future_generations"  # 10+ years

class ImpactCategory(Enum):
    """Categories of long-term impacts."""
    ENVIRONMENTAL = "environmental"
    SOCIAL = "social"
    ECONOMIC = "economic"
    TECHNOLOGICAL = "technological"
    POLITICAL = "political"
    CULTURAL = "cultural"

class RiskLevel(Enum):
    """Risk levels for impact assessment."""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class FutureScenario:
    """Container for a future scenario analysis."""
    name: str
    description: str
    probability: float  # 0-1 probability of occurrence
    time_horizon: TimeHorizon
    impacts: Dict[ImpactCategory, str]
    risks: List[Tuple[str, RiskLevel]]
    mitigation_strategies: List[str]

@dataclass
class SustainabilityMetrics:
    """Container for sustainability metrics."""
    environmental_impact: float  # 0-1 score
    social_impact: float  # 0-1 score
    economic_impact: float  # 0-1 score
    resource_efficiency: float  # 0-1 score
    resilience_score: float  # 0-1 score
    adaptation_capacity: float  # 0-1 score

@dataclass
class IntergenerationalImpact:
    """Container for intergenerational impact analysis."""
    future_generations_affected: List[str]
    resource_availability: Dict[str, float]  # 0-1 scores
    legacy_effects: List[str]
    adaptation_requirements: List[str]
    equity_considerations: List[str]

@dataclass
class LongTermImpact:
    """Container for complete long-term impact analysis."""
    scenarios: List[FutureScenario]
    sustainability: SustainabilityMetrics
    intergenerational: IntergenerationalImpact
    risk_assessment: Dict[str, RiskLevel]
    confidence_score: float  # 0-1 score
    recommendations: List[str]

class LongTermImpactAnalyzer:
    """Analyzes long-term impacts of decisions and policies."""
    
    def __init__(self):
        """Initialize the long-term impact analyzer."""
        self.impact_indicators = self._initialize_impact_indicators()
        self.risk_factors = self._initialize_risk_factors()
    
    def _initialize_impact_indicators(self) -> Dict[ImpactCategory, List[str]]:
        """Initialize indicators for each impact category."""
        return {
            ImpactCategory.ENVIRONMENTAL: [
                'carbon emissions', 'biodiversity', 'resource depletion',
                'pollution', 'climate change', 'ecosystem health'
            ],
            ImpactCategory.SOCIAL: [
                'community well-being', 'social equity', 'public health',
                'education', 'cultural preservation', 'social cohesion'
            ],
            ImpactCategory.ECONOMIC: [
                'economic growth', 'job creation', 'market stability',
                'resource efficiency', 'innovation', 'competitiveness'
            ],
            ImpactCategory.TECHNOLOGICAL: [
                'technological advancement', 'digital divide',
                'infrastructure development', 'innovation capacity',
                'technological dependency', 'cybersecurity'
            ],
            ImpactCategory.POLITICAL: [
                'policy stability', 'governance effectiveness',
                'international relations', 'regulatory framework',
                'political stability', 'democratic processes'
            ],
            ImpactCategory.CULTURAL: [
                'cultural preservation', 'heritage protection',
                'cultural diversity', 'social values',
                'traditions', 'identity'
            ]
        }
    
    def _initialize_risk_factors(self) -> Dict[str, List[str]]:
        """Initialize risk factors for different categories."""
        return {
            'environmental': [
                'climate change', 'resource scarcity', 'pollution',
                'biodiversity loss', 'natural disasters'
            ],
            'social': [
                'inequality', 'social unrest', 'health crises',
                'demographic changes', 'cultural conflicts'
            ],
            'economic': [
                'market volatility', 'resource depletion',
                'technological disruption', 'global competition',
                'financial instability'
            ],
            'technological': [
                'obsolescence', 'security threats', 'dependency',
                'access inequality', 'ethical concerns'
            ],
            'political': [
                'policy changes', 'regulatory uncertainty',
                'international conflicts', 'governance challenges',
                'public opposition'
            ]
        }
    
    def analyze_long_term_impact(
        self,
        decision: str,
        context: List[str]
    ) -> LongTermImpact:
        """
        Perform a comprehensive long-term impact analysis.
        
        Args:
            decision: The decision or policy to analyze
            context: List of relevant contexts
            
        Returns:
            LongTermImpact object containing the analysis
        """
        # Generate future scenarios
        scenarios = self._generate_future_scenarios(decision, context)
        
        # Calculate sustainability metrics
        sustainability = self._calculate_sustainability_metrics(decision, context)
        
        # Analyze intergenerational impacts
        intergenerational = self._analyze_intergenerational_impacts(decision, context)
        
        # Perform risk assessment
        risk_assessment = self._assess_risks(decision, context)
        
        # Calculate confidence score
        confidence_score = self._calculate_confidence_score(
            decision, scenarios, sustainability, intergenerational, risk_assessment
        )
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            scenarios, sustainability, intergenerational, risk_assessment
        )
        
        return LongTermImpact(
            scenarios=scenarios,
            sustainability=sustainability,
            intergenerational=intergenerational,
            risk_assessment=risk_assessment,
            confidence_score=confidence_score,
            recommendations=recommendations
        )
    
    def _generate_future_scenarios(
        self,
        decision: str,
        context: List[str]
    ) -> List[FutureScenario]:
        """Generate potential future scenarios."""
        scenarios = []
        
        # Define base scenarios
        base_scenarios = [
            ("Optimistic", 0.3, "Positive outcomes with successful implementation"),
            ("Realistic", 0.5, "Mixed outcomes with some challenges"),
            ("Pessimistic", 0.2, "Negative outcomes with significant challenges")
        ]
        
        for name, probability, description in base_scenarios:
            # Generate impacts for each category
            impacts = {}
            for category in ImpactCategory:
                impacts[category] = self._generate_category_impact(
                    decision, category, name.lower()
                )
            
            # Generate risks
            risks = self._generate_scenario_risks(decision, name.lower())
            
            # Generate mitigation strategies
            mitigation = self._generate_mitigation_strategies(risks)
            
            # Create scenario for each time horizon
            for horizon in TimeHorizon:
                scenarios.append(FutureScenario(
                    name=f"{name} ({horizon.value})",
                    description=description,
                    probability=probability * self._get_horizon_weight(horizon),
                    time_horizon=horizon,
                    impacts=impacts,
                    risks=risks,
                    mitigation_strategies=mitigation
                ))
        
        return scenarios
    
    def _calculate_sustainability_metrics(
        self,
        decision: str,
        context: List[str]
    ) -> SustainabilityMetrics:
        """Calculate sustainability metrics."""
        # Calculate environmental impact
        environmental_impact = self._calculate_category_score(
            decision, ImpactCategory.ENVIRONMENTAL
        )
        
        # Calculate social impact
        social_impact = self._calculate_category_score(
            decision, ImpactCategory.SOCIAL
        )
        
        # Calculate economic impact
        economic_impact = self._calculate_category_score(
            decision, ImpactCategory.ECONOMIC
        )
        
        # Calculate resource efficiency
        resource_efficiency = self._calculate_resource_efficiency(decision)
        
        # Calculate resilience score
        resilience_score = self._calculate_resilience_score(decision)
        
        # Calculate adaptation capacity
        adaptation_capacity = self._calculate_adaptation_capacity(decision)
        
        return SustainabilityMetrics(
            environmental_impact=environmental_impact,
            social_impact=social_impact,
            economic_impact=economic_impact,
            resource_efficiency=resource_efficiency,
            resilience_score=resilience_score,
            adaptation_capacity=adaptation_capacity
        )
    
    def _analyze_intergenerational_impacts(
        self,
        decision: str,
        context: List[str]
    ) -> IntergenerationalImpact:
        """Analyze impacts on future generations."""
        # Identify affected future generations
        future_generations = self._identify_affected_generations(decision)
        
        # Assess resource availability
        resource_availability = self._assess_resource_availability(decision)
        
        # Identify legacy effects
        legacy_effects = self._identify_legacy_effects(decision)
        
        # Determine adaptation requirements
        adaptation_requirements = self._determine_adaptation_requirements(decision)
        
        # Consider equity implications
        equity_considerations = self._analyze_equity_considerations(decision)
        
        return IntergenerationalImpact(
            future_generations_affected=future_generations,
            resource_availability=resource_availability,
            legacy_effects=legacy_effects,
            adaptation_requirements=adaptation_requirements,
            equity_considerations=equity_considerations
        )
    
    def _assess_risks(
        self,
        decision: str,
        context: List[str]
    ) -> Dict[str, RiskLevel]:
        """Assess risks across different categories."""
        risks = {}
        
        for category, factors in self.risk_factors.items():
            # Calculate risk level for each category
            risk_level = self._calculate_category_risk(decision, factors)
            risks[category] = risk_level
        
        return risks
    
    def _calculate_confidence_score(
        self,
        decision: str,
        scenarios: List[FutureScenario],
        sustainability: SustainabilityMetrics,
        intergenerational: IntergenerationalImpact,
        risk_assessment: Dict[str, RiskLevel]
    ) -> float:
        """Calculate confidence score for the analysis."""
        factors = [
            # More specific decision text indicates higher confidence
            min(len(decision.split()) / 100, 1.0),
            
            # More scenarios indicate higher confidence
            min(len(scenarios) / 10, 1.0),
            
            # Higher sustainability scores indicate higher confidence
            np.mean([
                sustainability.environmental_impact,
                sustainability.social_impact,
                sustainability.economic_impact
            ]),
            
            # More identified legacy effects indicate higher confidence
            min(len(intergenerational.legacy_effects) / 5, 1.0),
            
            # Lower risk levels indicate higher confidence
            1.0 - (list(RiskLevel).index(max(risk_assessment.values())) + 1) / len(RiskLevel)
        ]
        
        return np.mean(factors)
    
    def _generate_recommendations(
        self,
        scenarios: List[FutureScenario],
        sustainability: SustainabilityMetrics,
        intergenerational: IntergenerationalImpact,
        risk_assessment: Dict[str, RiskLevel]
    ) -> List[str]:
        """Generate recommendations based on the analysis."""
        recommendations = []
        
        # Add recommendations based on scenarios
        for scenario in scenarios:
            if scenario.probability > 0.3:  # Focus on more likely scenarios
                recommendations.extend(scenario.mitigation_strategies)
        
        # Add recommendations based on sustainability metrics
        if sustainability.environmental_impact < 0.5:
            recommendations.append(
                "Implement additional environmental protection measures"
            )
        if sustainability.social_impact < 0.5:
            recommendations.append(
                "Strengthen social impact mitigation strategies"
            )
        
        # Add recommendations based on intergenerational impacts
        if len(intergenerational.legacy_effects) > 0:
            recommendations.append(
                "Develop long-term monitoring and adaptation plans"
            )
        
        # Add recommendations based on risk assessment
        for category, risk_level in risk_assessment.items():
            if risk_level in [RiskLevel.HIGH, RiskLevel.CRITICAL]:
                recommendations.append(
                    f"Implement specific risk mitigation measures for {category} risks"
                )
        
        return list(set(recommendations))  # Remove duplicates
    
    def _get_horizon_weight(self, horizon: TimeHorizon) -> float:
        """Get weight for different time horizons."""
        weights = {
            TimeHorizon.SHORT_TERM: 1.0,
            TimeHorizon.MEDIUM_TERM: 0.8,
            TimeHorizon.LONG_TERM: 0.6,
            TimeHorizon.FUTURE_GENERATIONS: 0.4
        }
        return weights[horizon]
    
    def _calculate_category_score(
        self,
        decision: str,
        category: ImpactCategory
    ) -> float:
        """Calculate impact score for a category."""
        indicators = self.impact_indicators[category]
        decision_lower = decision.lower()
        
        # Count indicator occurrences
        matches = sum(1 for indicator in indicators 
                     if any(term in decision_lower 
                           for term in indicator.lower().split()))
        
        # Normalize score
        return min(matches / len(indicators), 1.0)
    
    def _calculate_resource_efficiency(self, decision: str) -> float:
        """Calculate resource efficiency score."""
        efficiency_terms = [
            'efficient', 'sustainable', 'renewable', 'recycled',
            'conservation', 'optimization', 'reduction', 'minimization'
        ]
        
        decision_lower = decision.lower()
        matches = sum(1 for term in efficiency_terms if term in decision_lower)
        
        return min(matches / len(efficiency_terms), 1.0)
    
    def _calculate_resilience_score(self, decision: str) -> float:
        """Calculate resilience score."""
        resilience_terms = [
            'resilient', 'adaptive', 'flexible', 'robust',
            'sustainable', 'durable', 'reliable', 'stable'
        ]
        
        decision_lower = decision.lower()
        matches = sum(1 for term in resilience_terms if term in decision_lower)
        
        return min(matches / len(resilience_terms), 1.0)
    
    def _calculate_adaptation_capacity(self, decision: str) -> float:
        """Calculate adaptation capacity score."""
        adaptation_terms = [
            'adapt', 'adjust', 'modify', 'evolve',
            'transform', 'innovate', 'learn', 'improve'
        ]
        
        decision_lower = decision.lower()
        matches = sum(1 for term in adaptation_terms if term in decision_lower)
        
        return min(matches / len(adaptation_terms), 1.0)
    
    def _identify_affected_generations(self, decision: str) -> List[str]:
        """Identify future generations affected by the decision."""
        generations = []
        decision_lower = decision.lower()
        
        if any(term in decision_lower for term in ['future', 'long-term', 'generations']):
            generations.append("Next generation (20-40 years)")
        if any(term in decision_lower for term in ['climate', 'environmental', 'sustainable']):
            generations.append("Future generations (40+ years)")
        if any(term in decision_lower for term in ['resource', 'depletion', 'conservation']):
            generations.append("Distant future generations (100+ years)")
        
        return generations
    
    def _assess_resource_availability(self, decision: str) -> Dict[str, float]:
        """Assess availability of key resources."""
        resources = {
            'natural_resources': 0.0,
            'financial_resources': 0.0,
            'human_resources': 0.0,
            'technological_resources': 0.0
        }
        
        decision_lower = decision.lower()
        
        # Assess natural resources
        if any(term in decision_lower for term in ['sustainable', 'renewable', 'conservation']):
            resources['natural_resources'] = 0.8
        elif any(term in decision_lower for term in ['depletion', 'scarcity', 'exhaustion']):
            resources['natural_resources'] = 0.2
        
        # Assess financial resources
        if any(term in decision_lower for term in ['investment', 'funding', 'budget']):
            resources['financial_resources'] = 0.7
        elif any(term in decision_lower for term in ['cost', 'expense', 'budget constraint']):
            resources['financial_resources'] = 0.3
        
        # Assess human resources
        if any(term in decision_lower for term in ['training', 'education', 'capacity building']):
            resources['human_resources'] = 0.8
        elif any(term in decision_lower for term in ['shortage', 'lack of expertise']):
            resources['human_resources'] = 0.2
        
        # Assess technological resources
        if any(term in decision_lower for term in ['innovation', 'technology', 'digital']):
            resources['technological_resources'] = 0.7
        elif any(term in decision_lower for term in ['obsolete', 'outdated']):
            resources['technological_resources'] = 0.3
        
        return resources
    
    def _identify_legacy_effects(self, decision: str) -> List[str]:
        """Identify potential legacy effects of the decision."""
        effects = []
        decision_lower = decision.lower()
        
        if any(term in decision_lower for term in ['environmental', 'climate', 'pollution']):
            effects.append("Environmental legacy")
        if any(term in decision_lower for term in ['social', 'community', 'cultural']):
            effects.append("Social legacy")
        if any(term in decision_lower for term in ['economic', 'financial', 'market']):
            effects.append("Economic legacy")
        if any(term in decision_lower for term in ['technological', 'infrastructure', 'digital']):
            effects.append("Technological legacy")
        
        return effects
    
    def _determine_adaptation_requirements(self, decision: str) -> List[str]:
        """Determine adaptation requirements for future changes."""
        requirements = []
        decision_lower = decision.lower()
        
        if any(term in decision_lower for term in ['climate', 'environmental', 'weather']):
            requirements.append("Climate change adaptation")
        if any(term in decision_lower for term in ['technological', 'digital', 'innovation']):
            requirements.append("Technological adaptation")
        if any(term in decision_lower for term in ['social', 'demographic', 'cultural']):
            requirements.append("Social adaptation")
        if any(term in decision_lower for term in ['economic', 'market', 'financial']):
            requirements.append("Economic adaptation")
        
        return requirements
    
    def _analyze_equity_considerations(self, decision: str) -> List[str]:
        """Analyze equity considerations for future generations."""
        considerations = []
        decision_lower = decision.lower()
        
        if any(term in decision_lower for term in ['equity', 'fairness', 'justice']):
            considerations.append("Intergenerational equity")
        if any(term in decision_lower for term in ['resource', 'distribution', 'access']):
            considerations.append("Resource distribution")
        if any(term in decision_lower for term in ['opportunity', 'access', 'inclusion']):
            considerations.append("Equal opportunities")
        if any(term in decision_lower for term in ['burden', 'responsibility', 'cost']):
            considerations.append("Burden sharing")
        
        return considerations
    
    def _calculate_category_risk(
        self,
        decision: str,
        risk_factors: List[str]
    ) -> RiskLevel:
        """Calculate risk level for a category."""
        decision_lower = decision.lower()
        matches = sum(1 for factor in risk_factors 
                     if any(term in decision_lower 
                           for term in factor.lower().split()))
        
        # Map to risk level
        if matches >= 4:
            return RiskLevel.CRITICAL
        elif matches >= 3:
            return RiskLevel.HIGH
        elif matches >= 2:
            return RiskLevel.MODERATE
        else:
            return RiskLevel.LOW
    
    def format_impact_analysis(self, impact: LongTermImpact) -> str:
        """Format the long-term impact analysis results."""
        report = "Long-Term Impact Analysis Report\n"
        report += "=" * 50 + "\n\n"
        
        # Format scenarios
        report += "Future Scenarios:\n"
        report += "-" * 30 + "\n"
        for scenario in impact.scenarios:
            report += f"\nScenario: {scenario.name}\n"
            report += f"Probability: {scenario.probability:.1%}\n"
            report += f"Time Horizon: {scenario.time_horizon.value}\n"
            report += f"Description: {scenario.description}\n"
            
            report += "\nImpacts:\n"
            for category, description in scenario.impacts.items():
                report += f"• {category.value}: {description}\n"
            
            report += "\nRisks:\n"
            for risk, level in scenario.risks:
                report += f"• {risk} ({level.value})\n"
            
            report += "\nMitigation Strategies:\n"
            for strategy in scenario.mitigation_strategies:
                report += f"• {strategy}\n"
        
        # Format sustainability metrics
        report += "\nSustainability Metrics:\n"
        report += "-" * 30 + "\n"
        report += f"Environmental Impact: {impact.sustainability.environmental_impact:.1%}\n"
        report += f"Social Impact: {impact.sustainability.social_impact:.1%}\n"
        report += f"Economic Impact: {impact.sustainability.economic_impact:.1%}\n"
        report += f"Resource Efficiency: {impact.sustainability.resource_efficiency:.1%}\n"
        report += f"Resilience Score: {impact.sustainability.resilience_score:.1%}\n"
        report += f"Adaptation Capacity: {impact.sustainability.adaptation_capacity:.1%}\n"
        
        # Format intergenerational impacts
        report += "\nIntergenerational Impacts:\n"
        report += "-" * 30 + "\n"
        report += "Affected Generations:\n"
        for generation in impact.intergenerational.future_generations_affected:
            report += f"• {generation}\n"
        
        report += "\nResource Availability:\n"
        for resource, score in impact.intergenerational.resource_availability.items():
            report += f"• {resource}: {score:.1%}\n"
        
        report += "\nLegacy Effects:\n"
        for effect in impact.intergenerational.legacy_effects:
            report += f"• {effect}\n"
        
        report += "\nAdaptation Requirements:\n"
        for requirement in impact.intergenerational.adaptation_requirements:
            report += f"• {requirement}\n"
        
        report += "\nEquity Considerations:\n"
        for consideration in impact.intergenerational.equity_considerations:
            report += f"• {consideration}\n"
        
        # Format risk assessment
        report += "\nRisk Assessment:\n"
        report += "-" * 30 + "\n"
        for category, level in impact.risk_assessment.items():
            report += f"• {category}: {level.value}\n"
        
        # Format confidence score and recommendations
        report += f"\nConfidence Score: {impact.confidence_score:.1%}\n"
        
        report += "\nRecommendations:\n"
        report += "-" * 30 + "\n"
        for recommendation in impact.recommendations:
            report += f"• {recommendation}\n"
        
        return report 