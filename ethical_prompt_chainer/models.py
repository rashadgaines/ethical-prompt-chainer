from typing import Optional, Dict, Any
from openai import OpenAI as OpenAIClient
from xai_grok import Grok
import os

class ModelFactory:
    """Factory class for creating language model instances."""
    
    @staticmethod
    def create_model(
        model_name: str,
        device: str = "cpu",
        model_kwargs: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Create a language model instance.
        
        Args:
            model_name: Name of the model to use (e.g., "gpt-4", "grok-3")
            device: Device to run the model on (not used for API-based models)
            model_kwargs: Additional keyword arguments for the model
            
        Returns:
            Language model instance
        """
        if model_kwargs is None:
            model_kwargs = {}
            
        # Handle OpenAI models
        if model_name.startswith("gpt-"):
            if not os.getenv("OPENAI_API_KEY"):
                raise ValueError("OPENAI_API_KEY environment variable not set")
            return OpenAIClient(
                api_key=os.getenv("OPENAI_API_KEY")
            )
            
        # Handle Grok models
        elif model_name.startswith("grok-"):
            if not os.getenv("GROK_API_KEY"):
                raise ValueError("GROK_API_KEY environment variable not set")
            return OpenAIClient(
                api_key=os.getenv("GROK_API_KEY"),
                base_url="https://api.x.ai/v1"
            )
            
        else:
            raise ValueError(f"Unsupported model: {model_name}. Currently supported models are GPT-4 and Grok-3.")
    
    @staticmethod
    def get_default_model_kwargs(model_name: str) -> Dict[str, Any]:
        """Get default model-specific keyword arguments."""
        if model_name.startswith("gpt-"):
            return {
                "temperature": 0.7,
                "max_tokens": 2048
            }
        elif model_name.startswith("grok-"):
            return {
                "temperature": 0.7,
                "max_tokens": 2048
            }
        return {} 