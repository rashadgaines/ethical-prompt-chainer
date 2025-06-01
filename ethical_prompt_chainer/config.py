from typing import Dict, Any, Optional
from pydantic import Field
from pydantic_settings import BaseSettings
from pathlib import Path

class ModelConfig(BaseSettings):
    """Configuration for language model settings."""
    model_name: str = Field(default="distilgpt2", description="Name of the model to use")
    device: str = Field(default="cpu", description="Device to run the model on")
    max_length: int = Field(default=2048, description="Maximum sequence length")
    temperature: float = Field(default=0.7, description="Sampling temperature")
    top_p: float = Field(default=0.95, description="Top-p sampling parameter")
    repetition_penalty: float = Field(default=1.15, description="Repetition penalty")

class ChainConfig(BaseSettings):
    """Configuration for chain settings."""
    log_file: Optional[Path] = Field(default=None, description="Path to log file")
    log_level: str = Field(default="INFO", description="Logging level")
    cache_dir: Optional[Path] = Field(default=None, description="Cache directory for models")

class Settings(BaseSettings):
    """Main settings class."""
    model: ModelConfig = Field(default_factory=ModelConfig)
    chain: ChainConfig = Field(default_factory=ChainConfig)
    
    class Config:
        env_prefix = "ETHICAL_CHAINER_"
        env_nested_delimiter = "__"

def get_settings() -> Settings:
    """Get the current settings."""
    return Settings() 