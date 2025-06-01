from typing import Dict, List, Optional
import re
from dataclasses import dataclass
from enum import Enum

class PromptType(Enum):
    """Types of prompts used to guide model behavior."""
    PRINCIPLE_IDENTIFICATION = "principle_identification"
    REASONING_GUIDANCE = "reasoning_guidance"
    RECOMMENDATION_GUIDANCE = "recommendation_guidance"
    CONFIDENCE_ASSESSMENT = "confidence_assessment"

@dataclass
class PromptTemplate:
    """Template for engineering model behavior through prompts."""
    type: PromptType
    template: str
    expected_format: str
    guidance_notes: str

class EthicalPromptTemplates:
    """Templates for ethical reasoning steps in policy dilemmas."""
    
    # Dilemma-specific keywords and contexts
    DILEMMA_CONTEXTS = {
        'economic': ['income', 'welfare', 'tax', 'cost', 'funding', 'budget', 'employment'],
        'social': ['rights', 'equality', 'access', 'healthcare', 'education', 'housing'],
        'environmental': ['climate', 'emissions', 'pollution', 'conservation', 'sustainability'],
        'security': ['safety', 'defense', 'crime', 'enforcement', 'protection'],
        'technology': ['innovation', 'digital', 'cybersecurity', 'infrastructure']
    }
    
    # Value mappings for different dilemma types
    VALUE_MAPPINGS = {
        'economic': {
            'equity': ['fairness', 'distribution', 'access'],
            'efficiency': ['productivity', 'growth', 'optimization'],
            'stability': ['security', 'predictability', 'sustainability']
        },
        'social': {
            'equality': ['fairness', 'justice', 'inclusion'],
            'liberty': ['freedom', 'autonomy', 'rights'],
            'welfare': ['well-being', 'health', 'safety']
        },
        'environmental': {
            'sustainability': ['conservation', 'preservation', 'renewal'],
            'responsibility': ['stewardship', 'accountability', 'duty'],
            'adaptation': ['resilience', 'flexibility', 'preparation']
        }
    }
    
    def __init__(self):
        self.base_templates = {
            "frame_dilemma": self.FRAME_DILEMMA,
            "stakeholder_analysis": self.STAKEHOLDER_ANALYSIS,
            "ethical_balancing": self.ETHICAL_BALANCING,
            "legal_feasibility": self.LEGAL_FEASIBILITY,
            "recommendation": self.RECOMMENDATION
        }
        self.templates = {
            PromptType.PRINCIPLE_IDENTIFICATION: PromptTemplate(
                type=PromptType.PRINCIPLE_IDENTIFICATION,
                template="""
Consider the following ethical dilemma:
{dilemma}

Your task is to identify the key ethical principles that should guide the reasoning process.
Think step by step:
1. What are the fundamental ethical values at stake?
2. Which ethical frameworks are most relevant?
3. What principles should guide the decision-making process?

List each principle on a new line, starting with a bullet point.
""",
                expected_format="""- Principle 1
- Principle 2
...""",
                guidance_notes="Guide the model to identify relevant ethical principles systematically."
            ),
            
            PromptType.REASONING_GUIDANCE: PromptTemplate(
                type=PromptType.REASONING_GUIDANCE,
                template="""
Given the ethical dilemma:
{dilemma}

And the identified principles:
{principles}

Guide your reasoning process through these steps:
1. How does each principle apply to this situation?
2. What are the potential conflicts between principles?
3. How should these conflicts be resolved?
4. What are the implications of different approaches?

Provide your reasoning in a clear, structured format.
""",
                expected_format="""Step 1: [Analysis of first principle]
Step 2: [Analysis of conflicts]
Step 3: [Resolution approach]
Step 4: [Implications]""",
                guidance_notes="Guide the model through a structured reasoning process."
            ),
            
            PromptType.RECOMMENDATION_GUIDANCE: PromptTemplate(
                type=PromptType.RECOMMENDATION_GUIDANCE,
                template="""
Based on your reasoning:
{reasoning}

Generate specific, actionable recommendations that:
1. Address the core ethical concerns
2. Provide clear guidance for implementation
3. Consider potential challenges
4. Include monitoring and evaluation steps

List each recommendation on a new line, starting with a bullet point.
""",
                expected_format="""- Recommendation 1
- Recommendation 2
...""",
                guidance_notes="Guide the model to generate practical, ethical recommendations."
            ),
            
            PromptType.CONFIDENCE_ASSESSMENT: PromptTemplate(
                type=PromptType.CONFIDENCE_ASSESSMENT,
                template="""
Review your analysis of the dilemma:
{dilemma}

Your reasoning process:
{reasoning}

Your recommendations:
{recommendations}

On a scale of 0.0 to 1.0, how confident are you in your reasoning process?
Consider:
1. The clarity of your analysis
2. The consistency of your approach
3. The strength of your recommendations
4. Any remaining uncertainties

Provide a single number between 0.0 and 1.0.
""",
                expected_format="0.85",
                guidance_notes="Guide the model to assess its own reasoning confidence."
            )
        }
    
    def identify_dilemma_context(self, dilemma: str) -> List[str]:
        """Identify the context(s) of a dilemma based on keywords."""
        contexts = []
        for context, keywords in self.DILEMMA_CONTEXTS.items():
            if any(keyword in dilemma.lower() for keyword in keywords):
                contexts.append(context)
        return contexts if contexts else ['general']
    
    def get_relevant_values(self, context: str) -> Dict[str, List[str]]:
        """Get relevant values for a given context."""
        return self.VALUE_MAPPINGS.get(context, self.VALUE_MAPPINGS['social'])
    
    def generate_contextual_prompt(self, template: str, dilemma: str, 
                                 issue_a: str, issue_b: str) -> str:
        """Generate a contextual prompt based on the dilemma type."""
        contexts = self.identify_dilemma_context(dilemma)
        primary_context = contexts[0]
        
        # Get relevant values for the context
        values = self.get_relevant_values(primary_context)
        value_1 = next(iter(values.keys()))
        value_2 = list(values.keys())[1] if len(values) > 1 else 'efficiency'
        
        # Enhance template with context-specific language
        enhanced_template = template.replace("{value_1}", value_1)
        enhanced_template = enhanced_template.replace("{value_2}", value_2)
        
        # Add context-specific considerations
        if primary_context == 'economic':
            enhanced_template += "\nConsider economic impacts on GDP, employment, and market stability."
        elif primary_context == 'environmental':
            enhanced_template += "\nEvaluate long-term environmental sustainability and climate impact."
        elif primary_context == 'social':
            enhanced_template += "\nAnalyze effects on social equity and community well-being."
        
        return enhanced_template.format(
            issue_a=issue_a,
            issue_b=issue_b,
            value_1=value_1,
            value_2=value_2
        )
    
    def get_template(self, template_name: str, dilemma: str, 
                    issue_a: str, issue_b: str) -> str:
        """Get a contextual template for a specific dilemma."""
        if template_name not in self.base_templates:
            raise ValueError(f"Unknown template: {template_name}")
            
        base_template = self.base_templates[template_name]
        return self.generate_contextual_prompt(
            base_template, dilemma, issue_a, issue_b
        )

    # Base templates remain unchanged
    FRAME_DILEMMA = """Given a policy dilemma involving {issue_a} (e.g., funding universal basic income) versus {issue_b} (e.g., targeted welfare programs), identify the core constitutional principles at stake (e.g., general welfare, equal protection) and the relevant legal frameworks (e.g., existing welfare laws).

Describe the primary benefits of {issue_a} in promoting {value_1} (e.g., equality) and the primary benefits of {issue_b} in promoting {value_2} (e.g., economic incentives).

List at least two potential harms or risks associated with each option, considering impacts on individual liberties, public safety, or economic stability.

Think step by step and explain your reasoning."""

    STAKEHOLDER_ANALYSIS = """Building on the identified dilemma, map the key stakeholders affected by {issue_a} and {issue_b} (e.g., low-income individuals, taxpayers, businesses).

For each stakeholder group:
1. Evaluate how each option aligns with their constitutional rights (e.g., life, liberty, property) and current legal protections
2. Assess the short-term and long-term consequences of each option on these groups
3. Focus on ethical considerations such as fairness, autonomy, and harm prevention
4. Highlight any disparities in impact that could raise concerns under the Equal Protection Clause or other constitutional guarantees

Think step by step and explain your reasoning."""

    ETHICAL_BALANCING = """Using the stakeholder analysis, apply an ethical balancing test rooted in constitutional values:

1. Weigh the benefits of {issue_a} against its harms, considering principles like promoting the general welfare (Article I, Section 8) versus protecting individual liberties (Bill of Rights)
2. Repeat for {issue_b}
3. Determine which option better minimizes harm while maximizing public benefit
4. Ensure compliance with due process and equal protection
5. Identify any trade-offs that require legal or policy safeguards to mitigate negative impacts on vulnerable groups or constitutional rights

Think step by step and explain your reasoning."""

    LEGAL_FEASIBILITY = """Evaluate the feasibility of implementing {issue_a} and {issue_b} under current U.S. laws and constitutional constraints:

1. Identify any legal barriers (e.g., Second Amendment for gun control, Commerce Clause for environmental regulations) and propose how they could be addressed through legislation or judicial interpretation
2. Assess practical challenges (funding, enforcement, public support)
3. Suggest mechanisms to overcome challenges while upholding ethical principles like transparency and accountability
4. Ensure alignment with precedents from the Supreme Court or federal statutes

Think step by step and explain your reasoning."""

    RECOMMENDATION = """Synthesize the findings to recommend either {issue_a}, {issue_b}, or a hybrid approach:

1. Justify the recommendation by demonstrating how it balances:
   - Constitutional principles
   - Ethical considerations
   - Stakeholder impacts
   - Legal viability

2. Propose specific safeguards (e.g., oversight mechanisms, phased implementation, compensatory measures) to address identified risks or harms, ensuring protection of constitutional rights and compliance with laws

3. Outline a monitoring plan to evaluate the policy's effectiveness and ethical outcomes over time

Think step by step and explain your reasoning."""

    @classmethod
    def get_all_templates(cls) -> Dict[str, str]:
        """Get all prompt templates."""
        return {
            "frame_dilemma": cls.FRAME_DILEMMA,
            "stakeholder_analysis": cls.STAKEHOLDER_ANALYSIS,
            "ethical_balancing": cls.ETHICAL_BALANCING,
            "legal_feasibility": cls.LEGAL_FEASIBILITY,
            "recommendation": cls.RECOMMENDATION
        }

    def get_principle_identification_prompt(self, dilemma: str) -> str:
        """Get prompt to guide model in identifying ethical principles."""
        template = self.templates[PromptType.PRINCIPLE_IDENTIFICATION]
        return template.template.format(dilemma=dilemma)
    
    def get_reasoning_prompt(self, dilemma: str, principles: List[str]) -> str:
        """Get prompt to guide model's reasoning process."""
        template = self.templates[PromptType.REASONING_GUIDANCE]
        principles_text = "\n".join(f"- {p}" for p in principles)
        return template.template.format(
            dilemma=dilemma,
            principles=principles_text
        )
    
    def get_recommendation_prompt(self, reasoning: str) -> str:
        """Get prompt to guide model's recommendation generation."""
        template = self.templates[PromptType.RECOMMENDATION_GUIDANCE]
        return template.template.format(reasoning=reasoning)
    
    def get_confidence_prompt(
        self,
        dilemma: str,
        reasoning: str,
        recommendations: List[str]
    ) -> str:
        """Get prompt to guide model's confidence assessment."""
        template = self.templates[PromptType.CONFIDENCE_ASSESSMENT]
        recommendations_text = "\n".join(f"- {r}" for r in recommendations)
        return template.template.format(
            dilemma=dilemma,
            reasoning=reasoning,
            recommendations=recommendations_text
        ) 