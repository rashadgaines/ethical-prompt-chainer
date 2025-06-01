"""
Ethical Prompt Chainer - A framework for improving AI model behavior through structured prompt engineering.
"""

from .chainer import EthicalPromptChainer
from .models import BaseModel, create_model

__version__ = "0.1.0"

__all__ = [
    "EthicalPromptChainer",
    "BaseModel",
    "create_model",
] 