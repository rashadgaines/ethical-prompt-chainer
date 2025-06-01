"""
Ethical Prompt Chainer - A framework for improving AI model behavior through structured prompt engineering.
"""

from ethical_prompt_chainer.chainer import EthicalPromptChainer
from ethical_prompt_chainer.models import ModelConfig, ModelError, BaseModel, ModelFactory
from ethical_prompt_chainer.ethical_frameworks import (
    FrameworkType,
    EthicalFramework,
    EthicalFrameworkManager
)

__version__ = "0.1.0"

__all__ = [
    "EthicalPromptChainer",
    "ModelConfig",
    "ModelError",
    "BaseModel",
    "ModelFactory",
    "FrameworkType",
    "EthicalFramework",
    "EthicalFrameworkManager",
] 