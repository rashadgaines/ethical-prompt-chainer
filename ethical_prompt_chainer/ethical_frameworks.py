from typing import Dict, List, Optional, Set
from dataclasses import dataclass
import json
import logging
from pathlib import Path
from enum import Enum

logger = logging.getLogger(__name__)

class FrameworkType(Enum):
    """Types of ethical frameworks for guiding model behavior."""
    UTILITARIAN = "utilitarian"
    DEONTOLOGICAL = "deontological"
    VIRTUE = "virtue"
    CARE = "care"
    SUSTAINABLE = "sustainable"

@dataclass
class EthicalFramework:
    """Framework for guiding model's ethical reasoning."""
    type: FrameworkType
    principles: List[str]
    guidance_prompts: Dict[str, str]
    evaluation_criteria: List[str]

class EthicalFrameworkManager:
    """Manager for ethical frameworks that guide model behavior."""
    
    def __init__(self):
        """Initialize the framework manager."""
        self.frameworks = {
            FrameworkType.UTILITARIAN: EthicalFramework(
                type=FrameworkType.UTILITARIAN,
                principles=[
                    "Maximize overall happiness",
                    "Minimize suffering",
                    "Consider consequences for all affected parties"
                ],
                guidance_prompts={
                    "analysis": """
Consider the consequences of different actions:
1. What are the potential benefits and harms?
2. How many people would be affected?
3. What is the magnitude of impact?
4. How can we maximize overall well-being?
""",
                    "evaluation": """
Evaluate the action based on:
1. Net impact on happiness
2. Distribution of benefits and harms
3. Long-term consequences
4. Alternative approaches
"""
                },
                evaluation_criteria=[
                    "Overall utility",
                    "Distribution of benefits",
                    "Long-term impact",
                    "Alternative options"
                ]
            ),
            
            FrameworkType.DEONTOLOGICAL: EthicalFramework(
                type=FrameworkType.DEONTOLOGICAL,
                principles=[
                    "Respect for autonomy",
                    "Duty to act morally",
                    "Universal moral rules"
                ],
                guidance_prompts={
                    "analysis": """
Consider the moral duties and rules:
1. What are the fundamental moral duties?
2. Are there universal rules that apply?
3. How does this respect autonomy?
4. What are the categorical imperatives?
""",
                    "evaluation": """
Evaluate the action based on:
1. Adherence to moral duties
2. Universalizability
3. Respect for autonomy
4. Moral consistency
"""
                },
                evaluation_criteria=[
                    "Moral duty adherence",
                    "Rule universality",
                    "Autonomy respect",
                    "Moral consistency"
                ]
            ),
            
            FrameworkType.VIRTUE: EthicalFramework(
                type=FrameworkType.VIRTUE,
                principles=[
                    "Cultivate virtuous character",
                    "Act with wisdom and courage",
                    "Develop moral excellence"
                ],
                guidance_prompts={
                    "analysis": """
Consider the virtuous approach:
1. What virtues are relevant?
2. How would a virtuous person act?
3. What character traits are important?
4. How can we cultivate moral excellence?
""",
                    "evaluation": """
Evaluate the action based on:
1. Virtue cultivation
2. Character development
3. Moral wisdom
4. Excellence in practice
"""
                },
                evaluation_criteria=[
                    "Virtue alignment",
                    "Character development",
                    "Moral wisdom",
                    "Excellence in practice"
                ]
            ),
            
            FrameworkType.CARE: EthicalFramework(
                type=FrameworkType.CARE,
                principles=[
                    "Prioritize relationships",
                    "Consider context and needs",
                    "Show empathy and compassion"
                ],
                guidance_prompts={
                    "analysis": """
Consider the caring approach:
1. Who is affected and how?
2. What are their specific needs?
3. How can we show care and empathy?
4. What relationships are important?
""",
                    "evaluation": """
Evaluate the action based on:
1. Relationship impact
2. Care and empathy shown
3. Context sensitivity
4. Need responsiveness
"""
                },
                evaluation_criteria=[
                    "Relationship quality",
                    "Care demonstrated",
                    "Context sensitivity",
                    "Need responsiveness"
                ]
            ),
            
            FrameworkType.SUSTAINABLE: EthicalFramework(
                type=FrameworkType.SUSTAINABLE,
                principles=[
                    "Consider long-term impact",
                    "Balance present and future needs",
                    "Maintain ecological integrity"
                ],
                guidance_prompts={
                    "analysis": """
Consider sustainability:
1. What are the long-term implications?
2. How does this affect future generations?
3. What ecological impacts are there?
4. How can we ensure sustainability?
""",
                    "evaluation": """
Evaluate the action based on:
1. Long-term viability
2. Future impact
3. Ecological balance
4. Resource sustainability
"""
                },
                evaluation_criteria=[
                    "Long-term viability",
                    "Future impact",
                    "Ecological balance",
                    "Resource sustainability"
                ]
            )
        }
    
    def get_framework(self, framework_type: FrameworkType) -> EthicalFramework:
        """
        Get a framework for guiding model behavior.
        
        Args:
            framework_type: The type of framework to get
            
        Returns:
            The ethical framework for guiding model behavior
        """
        return self.frameworks[framework_type]
    
    def get_applicable_frameworks(self, dilemma: str) -> List[EthicalFramework]:
        """
        Get frameworks applicable to the dilemma for guiding model behavior.
        
        Args:
            dilemma: The ethical dilemma to analyze
            
        Returns:
            List of applicable ethical frameworks
        """
        # Implementation would analyze the dilemma to determine applicable frameworks
        return list(self.frameworks.values())
    
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