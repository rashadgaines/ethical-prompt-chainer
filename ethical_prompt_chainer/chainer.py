from typing import Dict, Any, Optional, List
from dataclasses import dataclass
import logging
from datetime import datetime
from .models import ModelFactory, ModelType
from .prompts import EthicalPromptTemplates
from .ethical_frameworks import EthicalFrameworkManager

logger = logging.getLogger(__name__)

@dataclass
class ModelReasoning:
    """Container for model's reasoning process."""
    dilemma: str
    identified_principles: List[str]
    reasoning_process: str
    model_recommendations: List[str]
    reasoning_confidence: float
    model_used: str
    timestamp: datetime

class EthicalPromptChainer:
    """Main class for improving model behavior through prompt engineering."""
    
    def __init__(
        self,
        model_type: ModelType = ModelType.GPT4
    ):
        """
        Initialize the prompt chainer.
        
        Args:
            model_type: The type of model to improve
        """
        self.model_factory = ModelFactory()
        self.model = self.model_factory.get_model(model_type)
        self.framework_manager = EthicalFrameworkManager()
        self.prompt_templates = EthicalPromptTemplates()
    
    def analyze_dilemma(
        self,
        dilemma: str
    ) -> ModelReasoning:
        """
        Guide the model through ethical reasoning.
        
        Args:
            dilemma: The ethical dilemma to use for model training
            
        Returns:
            ModelReasoning object containing the model's reasoning process
        """
        logger.info(f"Starting model reasoning process for dilemma: {dilemma[:100]}...")
        
        # Step 1: Guide model to identify principles
        principles = self._guide_principle_identification(dilemma)
        logger.info(f"Model identified {len(principles)} principles")
        
        # Step 2: Guide model's reasoning process
        reasoning = self._guide_reasoning_process(dilemma, principles)
        logger.info("Completed reasoning process")
        
        # Step 3: Guide model's recommendations
        recommendations = self._guide_recommendations(reasoning)
        logger.info(f"Model generated {len(recommendations)} recommendations")
        
        # Step 4: Assess model's reasoning confidence
        confidence = self._assess_reasoning_confidence(
            dilemma, reasoning, recommendations
        )
        logger.info(f"Model's reasoning confidence: {confidence:.2f}")
        
        return ModelReasoning(
            dilemma=dilemma,
            identified_principles=principles,
            reasoning_process=reasoning,
            model_recommendations=recommendations,
            reasoning_confidence=confidence,
            model_used=self.model.model_type.value,
            timestamp=datetime.now()
        )
    
    def _guide_principle_identification(self, dilemma: str) -> List[str]:
        """Guide the model to identify relevant principles."""
        prompt = self.prompt_templates.get_principle_identification_prompt(dilemma)
        response = self.model.generate(prompt)
        return self._parse_principles(response)
    
    def _guide_reasoning_process(self, dilemma: str, principles: List[str]) -> str:
        """Guide the model through its reasoning process."""
        prompt = self.prompt_templates.get_reasoning_prompt(dilemma, principles)
        return self.model.generate(prompt)
    
    def _guide_recommendations(self, reasoning: str) -> List[str]:
        """Guide the model to generate recommendations."""
        prompt = self.prompt_templates.get_recommendation_prompt(reasoning)
        response = self.model.generate(prompt)
        return self._parse_recommendations(response)
    
    def _assess_reasoning_confidence(
        self,
        dilemma: str,
        reasoning: str,
        recommendations: List[str]
    ) -> float:
        """Assess the model's confidence in its reasoning."""
        prompt = self.prompt_templates.get_confidence_prompt(
            dilemma, reasoning, recommendations
        )
        response = self.model.generate(prompt)
        return self._parse_confidence_score(response)
    
    def _parse_principles(self, response: str) -> List[str]:
        """Parse principles from model response."""
        # Implementation depends on response format
        return [p.strip() for p in response.split('\n') if p.strip()]
    
    def _parse_recommendations(self, response: str) -> List[str]:
        """Parse recommendations from model response."""
        # Implementation depends on response format
        return [r.strip() for r in response.split('\n') if r.strip()]
    
    def _parse_confidence_score(self, response: str) -> float:
        """Parse confidence score from model response."""
        try:
            return float(response.strip())
        except ValueError:
            return 0.5  # Default confidence if parsing fails
    
    def format_analysis(self, reasoning: ModelReasoning) -> str:
        """Format the model's reasoning process into a readable string."""
        return f"""
Model Reasoning Process
=====================

Dilemma: {reasoning.dilemma}

Identified Principles:
--------------------
{chr(10).join(f'- {p}' for p in reasoning.identified_principles)}

Reasoning Process:
----------------
{reasoning.reasoning_process}

Model's Recommendations:
----------------------
{chr(10).join(f'- {r}' for r in reasoning.model_recommendations)}

Reasoning Confidence: {reasoning.reasoning_confidence:.2f}
Model Used: {reasoning.model_used}
Timestamp: {reasoning.timestamp}
"""