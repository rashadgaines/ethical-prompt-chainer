from typing import Dict, List, Optional, Set
from dataclasses import dataclass
import json
import logging
from pathlib import Path
from enum import Enum

logger = logging.getLogger(__name__)

class EthicalPrinciple(Enum):
    """Enumeration of core ethical principles."""
    AUTONOMY = "autonomy"
    BENEFICENCE = "beneficence"
    NON_MALEFICENCE = "non_maleficence"
    JUSTICE = "justice"
    FAIRNESS = "fairness"
    TRANSPARENCY = "transparency"
    ACCOUNTABILITY = "accountability"
    PRIVACY = "privacy"
    EQUITY = "equity"
    SUSTAINABILITY = "sustainability"

@dataclass
class EthicalFramework:
    """Container for an ethical framework definition."""
    name: str
    description: str
    principles: List[EthicalPrinciple]
    guidelines: List[str]
    application_contexts: List[str]
    priority_weights: Dict[EthicalPrinciple, float]

class EthicalFrameworkManager:
    """Manages ethical frameworks and their application."""
    
    # Predefined ethical frameworks
    FRAMEWORKS = {
        'utilitarian': EthicalFramework(
            name="Utilitarian",
            description="Focuses on maximizing overall happiness and minimizing suffering.",
            principles=[
                EthicalPrinciple.BENEFICENCE,
                EthicalPrinciple.NON_MALEFICENCE,
                EthicalPrinciple.JUSTICE
            ],
            guidelines=[
                "Consider the greatest good for the greatest number",
                "Evaluate consequences for all affected parties",
                "Balance short-term and long-term impacts"
            ],
            application_contexts=[
                "public policy",
                "resource allocation",
                "social programs"
            ],
            priority_weights={
                EthicalPrinciple.BENEFICENCE: 0.4,
                EthicalPrinciple.NON_MALEFICENCE: 0.3,
                EthicalPrinciple.JUSTICE: 0.3
            }
        ),
        'deontological': EthicalFramework(
            name="Deontological",
            description="Focuses on duties and rules rather than consequences.",
            principles=[
                EthicalPrinciple.AUTONOMY,
                EthicalPrinciple.JUSTICE,
                EthicalPrinciple.ACCOUNTABILITY
            ],
            guidelines=[
                "Respect individual rights and autonomy",
                "Follow universal moral rules",
                "Maintain consistency in decision-making"
            ],
            application_contexts=[
                "individual rights",
                "legal frameworks",
                "professional ethics"
            ],
            priority_weights={
                EthicalPrinciple.AUTONOMY: 0.4,
                EthicalPrinciple.JUSTICE: 0.3,
                EthicalPrinciple.ACCOUNTABILITY: 0.3
            }
        ),
        'virtue': EthicalFramework(
            name="Virtue Ethics",
            description="Focuses on character and moral virtues.",
            principles=[
                EthicalPrinciple.ACCOUNTABILITY,
                EthicalPrinciple.TRANSPARENCY,
                EthicalPrinciple.FAIRNESS
            ],
            guidelines=[
                "Cultivate moral character",
                "Consider virtuous behavior",
                "Promote ethical leadership"
            ],
            application_contexts=[
                "leadership",
                "education",
                "professional development"
            ],
            priority_weights={
                EthicalPrinciple.ACCOUNTABILITY: 0.4,
                EthicalPrinciple.TRANSPARENCY: 0.3,
                EthicalPrinciple.FAIRNESS: 0.3
            }
        ),
        'care': EthicalFramework(
            name="Ethics of Care",
            description="Focuses on relationships and care for others.",
            principles=[
                EthicalPrinciple.BENEFICENCE,
                EthicalPrinciple.EQUITY,
                EthicalPrinciple.PRIVACY
            ],
            guidelines=[
                "Consider relationships and dependencies",
                "Address needs of vulnerable populations",
                "Promote caring relationships"
            ],
            application_contexts=[
                "healthcare",
                "social services",
                "family policy"
            ],
            priority_weights={
                EthicalPrinciple.BENEFICENCE: 0.4,
                EthicalPrinciple.EQUITY: 0.3,
                EthicalPrinciple.PRIVACY: 0.3
            }
        ),
        'sustainable': EthicalFramework(
            name="Sustainable Ethics",
            description="Focuses on long-term sustainability and environmental impact.",
            principles=[
                EthicalPrinciple.SUSTAINABILITY,
                EthicalPrinciple.EQUITY,
                EthicalPrinciple.JUSTICE
            ],
            guidelines=[
                "Consider long-term environmental impact",
                "Balance present and future needs",
                "Promote sustainable practices"
            ],
            application_contexts=[
                "environmental policy",
                "resource management",
                "climate action"
            ],
            priority_weights={
                EthicalPrinciple.SUSTAINABILITY: 0.4,
                EthicalPrinciple.EQUITY: 0.3,
                EthicalPrinciple.JUSTICE: 0.3
            }
        )
    }
    
    def __init__(self):
        """Initialize the ethical framework manager."""
        self.frameworks = self.FRAMEWORKS.copy()
    
    def get_framework(self, name: str) -> Optional[EthicalFramework]:
        """Get an ethical framework by name."""
        return self.frameworks.get(name.lower())
    
    def get_applicable_frameworks(self, context: str) -> List[EthicalFramework]:
        """Get frameworks applicable to a specific context."""
        return [
            framework for framework in self.frameworks.values()
            if context.lower() in [c.lower() for c in framework.application_contexts]
        ]
    
    def get_principle_weights(self, framework_name: str) -> Dict[EthicalPrinciple, float]:
        """Get the priority weights for principles in a framework."""
        framework = self.get_framework(framework_name)
        if not framework:
            raise ValueError(f"Framework '{framework_name}' not found")
        return framework.priority_weights
    
    def analyze_ethical_alignment(
        self,
        text: str,
        framework_name: str
    ) -> Dict[EthicalPrinciple, float]:
        """
        Analyze how well a text aligns with an ethical framework.
        
        Args:
            text: The text to analyze
            framework_name: Name of the framework to use
            
        Returns:
            Dictionary mapping principles to alignment scores
        """
        framework = self.get_framework(framework_name)
        if not framework:
            raise ValueError(f"Framework '{framework_name}' not found")
        
        # Calculate alignment scores for each principle
        alignment_scores = {}
        for principle in framework.principles:
            # Count occurrences of principle-related terms
            principle_terms = self._get_principle_terms(principle)
            term_count = sum(1 for term in principle_terms 
                           if term.lower() in text.lower())
            
            # Normalize score
            max_expected_terms = 5  # Maximum expected occurrences
            alignment_scores[principle] = min(term_count / max_expected_terms, 1.0)
        
        return alignment_scores
    
    def _get_principle_terms(self, principle: EthicalPrinciple) -> List[str]:
        """Get relevant terms for an ethical principle."""
        principle_terms = {
            EthicalPrinciple.AUTONOMY: [
                'autonomy', 'self-determination', 'independence',
                'freedom', 'choice', 'consent'
            ],
            EthicalPrinciple.BENEFICENCE: [
                'benefit', 'well-being', 'welfare', 'good',
                'improve', 'enhance', 'promote'
            ],
            EthicalPrinciple.NON_MALEFICENCE: [
                'harm', 'prevent', 'avoid', 'protect',
                'safety', 'security', 'risk'
            ],
            EthicalPrinciple.JUSTICE: [
                'justice', 'fairness', 'equality', 'rights',
                'entitlement', 'desert', 'merit'
            ],
            EthicalPrinciple.FAIRNESS: [
                'fair', 'equitable', 'impartial', 'balanced',
                'unbiased', 'objective', 'neutral'
            ],
            EthicalPrinciple.TRANSPARENCY: [
                'transparent', 'open', 'clear', 'disclosure',
                'visibility', 'accountability', 'honesty'
            ],
            EthicalPrinciple.ACCOUNTABILITY: [
                'accountable', 'responsible', 'answerable',
                'liable', 'duty', 'obligation'
            ],
            EthicalPrinciple.PRIVACY: [
                'privacy', 'confidential', 'private',
                'personal', 'sensitive', 'secure'
            ],
            EthicalPrinciple.EQUITY: [
                'equity', 'equal', 'fair', 'just',
                'balanced', 'proportional', 'appropriate'
            ],
            EthicalPrinciple.SUSTAINABILITY: [
                'sustainable', 'sustainability', 'environmental',
                'ecological', 'long-term', 'future'
            ]
        }
        return principle_terms.get(principle, [])
    
    def format_alignment_analysis(
        self,
        alignment_scores: Dict[EthicalPrinciple, float],
        framework_name: str
    ) -> str:
        """Format the ethical alignment analysis results."""
        framework = self.get_framework(framework_name)
        if not framework:
            raise ValueError(f"Framework '{framework_name}' not found")
        
        report = f"Ethical Alignment Analysis - {framework.name} Framework\n"
        report += "=" * 50 + "\n\n"
        report += f"Description: {framework.description}\n\n"
        
        report += "Principle Alignment Scores:\n"
        report += "-" * 30 + "\n"
        for principle, score in alignment_scores.items():
            report += f"{principle.value.title()}: {score:.2%}\n"
        
        report += "\nGuidelines:\n"
        report += "-" * 30 + "\n"
        for guideline in framework.guidelines:
            report += f"• {guideline}\n"
        
        return report 