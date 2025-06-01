from typing import Dict, List, Optional
import re

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