from typing import Optional, Dict, Any
from abc import ABC, abstractmethod
import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class BaseModel(ABC):
    """Base class for models that can be guided through ethical reasoning."""
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response using the model.
        
        Args:
            prompt: The prompt to guide model behavior
            **kwargs: Additional keyword arguments for the model
            
        Returns:
            The model's response
        """
        pass

class GrokModel(BaseModel):
    """Grok model implementation."""
    
    def __init__(self, model_name: str = "grok-3"):
        """Initialize the Grok model."""
        api_key = os.getenv("GROK_API_KEY")
        if not api_key:
            raise ValueError("GROK_API_KEY environment variable not set. Please add it to your .env file.")
        self.api_key = api_key
        self.model_name = model_name
        self.api_url = "https://api.x.ai/v1/chat/completions"
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate a response using Grok's API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 2000,
            **kwargs
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error calling Grok API: {str(e)}")
        except (KeyError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Error parsing Grok API response: {str(e)}")

def create_model(model_name: str = "grok-3", **kwargs) -> BaseModel:
    """
    Create a model instance.
    
    Args:
        model_name: Name of the model to use (currently only "grok-3" is supported)
        **kwargs: Additional keyword arguments for the model
        
    Returns:
        Model instance
    """
    if model_name.startswith("grok-"):
        return GrokModel(model_name=model_name)
    else:
        raise ValueError(f"Unsupported model: {model_name}. Currently only Grok-3 is supported.") 