from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime
from .models import create_model, BaseModel

@dataclass
class ModelReasoning:
    """Container for model's reasoning process."""
    dilemma: str
    reasoning: str
    solution: str
    model_used: str
    timestamp: datetime

class EthicalPromptChainer:
    """Main class for improving model behavior through prompt engineering."""
    
    def __init__(self, model_name: str = "grok-3"):
        """
        Initialize the prompt chainer.
        
        Args:
            model_name: The name of the model to use
        """
        self.model = create_model(model_name)
    
    def analyze_dilemma(self, dilemma: str) -> ModelReasoning:
        """
        Guide the model through ethical reasoning.
        
        Args:
            dilemma: The ethical dilemma to analyze
            
        Returns:
            ModelReasoning object containing the model's reasoning process
        """
        # Step 1: Gather Context
        context_prompt = f"""Analyze the following ethical dilemma by gathering context:

{dilemma}

Consider:
1. Who are the key stakeholders and how are they affected?
2. What are their intentions and motivations?
3. What are the potential consequences of different actions?
4. What are the relevant facts and constraints?
5. What values are at stake (e.g., fairness, harm, autonomy)?

Please provide a comprehensive context analysis:"""

        context = self.model.generate(context_prompt)
        
        # Step 2: Apply Ethical Principles
        principles_prompt = f"""Evaluate the following scenario through multiple ethical frameworks:

Dilemma:
{dilemma}

Context:
{context}

Consider each of these ethical perspectives:
1. Consequentialism: What outcomes would maximize overall well-being or minimize harm?
2. Deontology: What universal rules or duties should guide this decision?
3. Virtue Ethics: What response would reflect traits like compassion, integrity, or justice?
4. Care Ethics: How do relationships and responsibilities shape the best course of action?

Please analyze the situation through each of these lenses:"""

        principles = self.model.generate(principles_prompt)
        
        # Step 3: Weigh Trade-offs
        tradeoffs_prompt = f"""Analyze the trade-offs in this ethical dilemma:

Dilemma:
{dilemma}

Context:
{context}

Ethical Analysis:
{principles}

Consider:
1. What are the short-term and long-term impacts?
2. What is the scale of potential harm or benefit?
3. How certain are we about the outcomes?
4. How do we balance conflicting values (e.g., individual autonomy vs. collective safety)?
5. What are the opportunity costs of each option?

Please provide a detailed trade-off analysis:"""

        tradeoffs = self.model.generate(tradeoffs_prompt)
        
        # Step 4: Check for Bias and Assumptions
        bias_check_prompt = f"""Review the analysis for potential biases and assumptions:

Dilemma:
{dilemma}

Context:
{context}

Ethical Analysis:
{principles}

Trade-off Analysis:
{tradeoffs}

Consider:
1. What cultural or personal biases might be influencing the analysis?
2. What assumptions are being made about the situation or stakeholders?
3. Are there any gaps in our understanding?
4. What additional information might be needed?
5. How might different cultural perspectives view this situation?

Please identify potential biases and assumptions:"""

        bias_check = self.model.generate(bias_check_prompt)
        
        # Step 5: Align with Human Values
        values_prompt = f"""Ensure the analysis aligns with core human values:

Dilemma:
{dilemma}

Context:
{context}

Ethical Analysis:
{principles}

Trade-off Analysis:
{tradeoffs}

Bias Check:
{bias_check}

Consider:
1. How does this analysis reflect values like fairness and empathy?
2. How does it respect diversity and avoid harm?
3. How does it promote truth-seeking and human flourishing?
4. Is the reasoning honest and constructive?
5. Does it avoid dogmatism while providing clear guidance?

Please evaluate the alignment with human values:"""

        values = self.model.generate(values_prompt)
        
        # Step 6: Propose Solution
        solution_prompt = f"""Based on the comprehensive analysis, propose a solution:

Dilemma:
{dilemma}

Context:
{context}

Ethical Analysis:
{principles}

Trade-off Analysis:
{tradeoffs}

Bias Check:
{bias_check}

Values Alignment:
{values}

Consider:
1. What is the most ethically sound course of action?
2. How does it address the concerns raised in each step of the analysis?
3. What specific steps should be taken to implement this solution?
4. How can we monitor and evaluate the outcomes?
5. What contingencies should be planned for?

Please provide a detailed solution:"""

        solution = self.model.generate(solution_prompt)
        
        # Combine all steps into a final reasoning
        reasoning = f"""Context Analysis:
{context}

Ethical Framework Analysis:
{principles}

Trade-off Analysis:
{tradeoffs}

Bias and Assumption Check:
{bias_check}

Values Alignment:
{values}"""
        
        return ModelReasoning(
            dilemma=dilemma,
            reasoning=reasoning,
            solution=solution,
            model_used=self.model.model_name,
            timestamp=datetime.now()
        )
    
    def format_analysis(self, reasoning: ModelReasoning) -> str:
        """Format the model's reasoning process into a readable string."""
        return f"""
Ethical Analysis
===============

Model Used: {reasoning.model_used}

User Prompt:
-----------
{reasoning.dilemma}

Reasoning Chain:
--------------
{reasoning.reasoning}

Solution:
--------
{reasoning.solution}

Timestamp: {reasoning.timestamp}
"""