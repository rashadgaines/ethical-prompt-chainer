from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
import json
import logging
from pathlib import Path
from enum import Enum
import numpy as np

logger = logging.getLogger(__name__)

class ImpactType(Enum):
    """Types of impacts on stakeholders."""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    MIXED = "mixed"

class ImpactSeverity(Enum):
    """Severity levels of impacts."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class StakeholderImpact:
    """Container for stakeholder impact analysis."""
    stakeholder: str
    impact_type: ImpactType
    severity: ImpactSeverity
    description: str
    affected_aspects: List[str]
    mitigation_suggestions: List[str]
    confidence_score: float  # 0-1 score indicating confidence in the analysis

@dataclass
class StakeholderGroup:
    """Container for stakeholder group definition."""
    name: str
    description: str
    key_interests: List[str]
    typical_concerns: List[str]
    power_level: float  # 0-1 score indicating relative power/influence
    vulnerability_level: float  # 0-1 score indicating relative vulnerability

class StakeholderAnalyzer:
    """Analyzes impacts on different stakeholder groups."""
    
    # Predefined stakeholder groups
    STAKEHOLDER_GROUPS = {
        'individuals': StakeholderGroup(
            name="Individual Citizens",
            description="General public and individual citizens",
            key_interests=[
                "personal rights",
                "quality of life",
                "access to resources",
                "safety and security"
            ],
            typical_concerns=[
                "privacy",
                "autonomy",
                "fair treatment",
                "access to services"
            ],
            power_level=0.3,
            vulnerability_level=0.7
        ),
        'businesses': StakeholderGroup(
            name="Businesses and Corporations",
            description="Private sector organizations and companies",
            key_interests=[
                "profitability",
                "market stability",
                "regulatory environment",
                "resource access"
            ],
            typical_concerns=[
                "compliance costs",
                "market competition",
                "resource availability",
                "regulatory burden"
            ],
            power_level=0.8,
            vulnerability_level=0.4
        ),
        'government': StakeholderGroup(
            name="Government Entities",
            description="Public sector organizations and agencies",
            key_interests=[
                "public welfare",
                "policy implementation",
                "resource management",
                "regulatory control"
            ],
            typical_concerns=[
                "budget constraints",
                "public opinion",
                "implementation challenges",
                "legal compliance"
            ],
            power_level=0.9,
            vulnerability_level=0.2
        ),
        'vulnerable': StakeholderGroup(
            name="Vulnerable Populations",
            description="Groups requiring special consideration",
            key_interests=[
                "basic needs",
                "protection",
                "access to services",
                "social inclusion"
            ],
            typical_concerns=[
                "discrimination",
                "access barriers",
                "resource scarcity",
                "social exclusion"
            ],
            power_level=0.2,
            vulnerability_level=0.9
        ),
        'environment': StakeholderGroup(
            name="Environmental Stakeholders",
            description="Natural environment and future generations",
            key_interests=[
                "sustainability",
                "resource conservation",
                "biodiversity",
                "climate stability"
            ],
            typical_concerns=[
                "pollution",
                "resource depletion",
                "habitat loss",
                "climate change"
            ],
            power_level=0.1,
            vulnerability_level=0.8
        )
    }
    
    def __init__(self):
        """Initialize the stakeholder analyzer."""
        self.stakeholder_groups = self.STAKEHOLDER_GROUPS.copy()
    
    def get_stakeholder_group(self, name: str) -> Optional[StakeholderGroup]:
        """Get a stakeholder group by name."""
        return self.stakeholder_groups.get(name.lower())
    
    def identify_stakeholders(self, context: str) -> List[StakeholderGroup]:
        """Identify relevant stakeholder groups for a context."""
        # Simple keyword-based matching
        context_keywords = context.lower().split()
        relevant_groups = []
        
        for group in self.stakeholder_groups.values():
            # Check if any keywords match group interests or concerns
            group_terms = (
                [term.lower() for term in group.key_interests] +
                [term.lower() for term in group.typical_concerns]
            )
            
            if any(keyword in group_terms for keyword in context_keywords):
                relevant_groups.append(group)
        
        return relevant_groups
    
    def analyze_impact(
        self,
        decision: str,
        stakeholder_group: StakeholderGroup
    ) -> StakeholderImpact:
        """
        Analyze the impact of a decision on a stakeholder group.
        
        Args:
            decision: The decision or policy to analyze
            stakeholder_group: The stakeholder group to analyze
            
        Returns:
            StakeholderImpact object containing the analysis
        """
        # Analyze impact type
        impact_type = self._determine_impact_type(decision, stakeholder_group)
        
        # Analyze severity
        severity = self._determine_impact_severity(decision, stakeholder_group)
        
        # Generate impact description
        description = self._generate_impact_description(
            decision, stakeholder_group, impact_type, severity
        )
        
        # Identify affected aspects
        affected_aspects = self._identify_affected_aspects(
            decision, stakeholder_group
        )
        
        # Generate mitigation suggestions
        mitigation_suggestions = self._generate_mitigation_suggestions(
            decision, stakeholder_group, impact_type, severity
        )
        
        # Calculate confidence score
        confidence_score = self._calculate_confidence_score(
            decision, stakeholder_group, impact_type, severity
        )
        
        return StakeholderImpact(
            stakeholder=stakeholder_group.name,
            impact_type=impact_type,
            severity=severity,
            description=description,
            affected_aspects=affected_aspects,
            mitigation_suggestions=mitigation_suggestions,
            confidence_score=confidence_score
        )
    
    def _determine_impact_type(
        self,
        decision: str,
        stakeholder_group: StakeholderGroup
    ) -> ImpactType:
        """Determine the type of impact on a stakeholder group."""
        # Count positive and negative indicators
        positive_terms = [
            'benefit', 'improve', 'enhance', 'support', 'protect',
            'promote', 'facilitate', 'enable', 'strengthen', 'empower'
        ]
        negative_terms = [
            'harm', 'damage', 'restrict', 'limit', 'burden',
            'cost', 'risk', 'threat', 'vulnerable', 'expose'
        ]
        
        decision_lower = decision.lower()
        positive_count = sum(1 for term in positive_terms 
                           if term in decision_lower)
        negative_count = sum(1 for term in negative_terms 
                           if term in decision_lower)
        
        if positive_count > negative_count:
            return ImpactType.POSITIVE
        elif negative_count > positive_count:
            return ImpactType.NEGATIVE
        elif positive_count == negative_count and positive_count > 0:
            return ImpactType.MIXED
        else:
            return ImpactType.NEUTRAL
    
    def _determine_impact_severity(
        self,
        decision: str,
        stakeholder_group: StakeholderGroup
    ) -> ImpactSeverity:
        """Determine the severity of impact on a stakeholder group."""
        # Consider stakeholder vulnerability and power
        base_severity = stakeholder_group.vulnerability_level
        
        # Adjust based on impact type indicators
        severity_terms = {
            ImpactSeverity.CRITICAL: [
                'critical', 'severe', 'extreme', 'urgent', 'immediate',
                'existential', 'fundamental', 'irreversible'
            ],
            ImpactSeverity.HIGH: [
                'significant', 'major', 'substantial', 'serious',
                'considerable', 'important', 'notable'
            ],
            ImpactSeverity.MEDIUM: [
                'moderate', 'medium', 'some', 'partial',
                'limited', 'controlled', 'managed'
            ],
            ImpactSeverity.LOW: [
                'minor', 'minimal', 'slight', 'negligible',
                'insignificant', 'trivial', 'marginal'
            ]
        }
        
        decision_lower = decision.lower()
        max_severity = ImpactSeverity.LOW
        
        for severity, terms in severity_terms.items():
            if any(term in decision_lower for term in terms):
                max_severity = severity
                break
        
        # Combine base severity with term-based severity
        final_severity = max(
            base_severity,
            (list(ImpactSeverity).index(max_severity) + 1) / len(ImpactSeverity)
        )
        
        # Map to severity level
        if final_severity >= 0.75:
            return ImpactSeverity.CRITICAL
        elif final_severity >= 0.5:
            return ImpactSeverity.HIGH
        elif final_severity >= 0.25:
            return ImpactSeverity.MEDIUM
        else:
            return ImpactSeverity.LOW
    
    def _generate_impact_description(
        self,
        decision: str,
        stakeholder_group: StakeholderGroup,
        impact_type: ImpactType,
        severity: ImpactSeverity
    ) -> str:
        """Generate a description of the impact."""
        template = (
            f"This decision has a {impact_type.value} impact of {severity.value} "
            f"severity on {stakeholder_group.name.lower()}. "
        )
        
        if impact_type == ImpactType.POSITIVE:
            template += "It aligns with their key interests in "
            template += ", ".join(stakeholder_group.key_interests[:2])
        elif impact_type == ImpactType.NEGATIVE:
            template += "It raises concerns about "
            template += ", ".join(stakeholder_group.typical_concerns[:2])
        elif impact_type == ImpactType.MIXED:
            template += "It presents both opportunities and challenges for "
            template += stakeholder_group.name.lower()
        else:
            template += "It has minimal direct impact on "
            template += stakeholder_group.name.lower()
        
        return template
    
    def _identify_affected_aspects(
        self,
        decision: str,
        stakeholder_group: StakeholderGroup
    ) -> List[str]:
        """Identify aspects of stakeholder interests affected by the decision."""
        affected_aspects = []
        decision_lower = decision.lower()
        
        # Check key interests
        for interest in stakeholder_group.key_interests:
            if any(term in decision_lower for term in interest.lower().split()):
                affected_aspects.append(interest)
        
        # Check typical concerns
        for concern in stakeholder_group.typical_concerns:
            if any(term in decision_lower for term in concern.lower().split()):
                affected_aspects.append(concern)
        
        return affected_aspects
    
    def _generate_mitigation_suggestions(
        self,
        decision: str,
        stakeholder_group: StakeholderGroup,
        impact_type: ImpactType,
        severity: ImpactSeverity
    ) -> List[str]:
        """Generate suggestions for mitigating negative impacts."""
        suggestions = []
        
        if impact_type in [ImpactType.NEGATIVE, ImpactType.MIXED]:
            if severity in [ImpactSeverity.HIGH, ImpactSeverity.CRITICAL]:
                suggestions.append(
                    f"Implement immediate measures to address {stakeholder_group.name.lower()}'s concerns"
                )
                suggestions.append(
                    "Develop a comprehensive monitoring and feedback system"
                )
            
            if stakeholder_group.vulnerability_level > 0.5:
                suggestions.append(
                    "Provide additional support and resources for vulnerable stakeholders"
                )
            
            if stakeholder_group.power_level < 0.5:
                suggestions.append(
                    "Ensure adequate representation and participation in decision-making"
                )
        
        return suggestions
    
    def _calculate_confidence_score(
        self,
        decision: str,
        stakeholder_group: StakeholderGroup,
        impact_type: ImpactType,
        severity: ImpactSeverity
    ) -> float:
        """Calculate confidence score for the impact analysis."""
        # Base confidence on various factors
        factors = [
            # More specific decision text indicates higher confidence
            min(len(decision.split()) / 100, 1.0),
            
            # Clear impact type indicates higher confidence
            1.0 if impact_type != ImpactType.MIXED else 0.7,
            
            # Higher severity often indicates more certainty
            (list(ImpactSeverity).index(severity) + 1) / len(ImpactSeverity),
            
            # More affected aspects indicates higher confidence
            min(len(self._identify_affected_aspects(decision, stakeholder_group)) / 5, 1.0)
        ]
        
        return np.mean(factors)
    
    def format_impact_analysis(self, impact: StakeholderImpact) -> str:
        """Format the stakeholder impact analysis results."""
        report = f"Stakeholder Impact Analysis - {impact.stakeholder}\n"
        report += "=" * 50 + "\n\n"
        
        report += f"Impact Type: {impact.impact_type.value.title()}\n"
        report += f"Severity: {impact.severity.value.title()}\n"
        report += f"Confidence Score: {impact.confidence_score:.2%}\n\n"
        
        report += "Description:\n"
        report += "-" * 30 + "\n"
        report += f"{impact.description}\n\n"
        
        report += "Affected Aspects:\n"
        report += "-" * 30 + "\n"
        for aspect in impact.affected_aspects:
            report += f"• {aspect}\n"
        
        if impact.mitigation_suggestions:
            report += "\nMitigation Suggestions:\n"
            report += "-" * 30 + "\n"
            for suggestion in impact.mitigation_suggestions:
                report += f"• {suggestion}\n"
        
        return report 