import pytest
from ethical_prompt_chainer.models import (
    ModelConfig,
    ModelError,
    BaseModel,
    ModelFactory
)

class TestModel(BaseModel):
    """Test model implementation."""
    def generate(self, prompt: str, **kwargs) -> str:
        return f"Test response for: {prompt}"

def test_model_config():
    """Test model configuration."""
    config = ModelConfig(
        name="test-model",
        provider="test-provider",
        version="1.0",
        parameters={"temperature": 0.7},
        capabilities={"reasoning": True, "analysis": True}
    )
    
    assert config.name == "test-model"
    assert config.provider == "test-provider"
    assert config.version == "1.0"
    assert config.parameters["temperature"] == 0.7
    assert config.capabilities["reasoning"] is True

def test_model_config_validation():
    """Test model configuration validation."""
    with pytest.raises(ModelError):
        ModelConfig(
            name="test-model",
            provider="test-provider",
            version="1.0",
            parameters={},  # Missing capabilities
            capabilities=None
        )

def test_model_factory():
    """Test model factory functionality."""
    # Register test model
    ModelFactory.register_model("test-provider", TestModel)
    
    # Create model instance
    config = ModelConfig(
        name="test-model",
        provider="test-provider",
        version="1.0",
        parameters={"temperature": 0.7},
        capabilities={"reasoning": True, "analysis": True}
    )
    model = ModelFactory.create_model(config)
    
    assert isinstance(model, TestModel)
    assert model.config == config
    
    # Test unknown provider
    with pytest.raises(ModelError):
        config.provider = "unknown-provider"
        ModelFactory.create_model(config)

def test_model_capabilities():
    """Test model capabilities."""
    config = ModelConfig(
        name="test-model",
        provider="test-provider",
        version="1.0",
        parameters={"temperature": 0.7},
        capabilities={
            "reasoning": True,
            "analysis": True,
            "generation": True
        }
    )
    model = TestModel(config)
    
    capabilities = model.get_capabilities()
    assert capabilities["reasoning"] is True
    assert capabilities["analysis"] is True
    assert capabilities["generation"] is True

def test_model_generation():
    """Test model response generation."""
    config = ModelConfig(
        name="test-model",
        provider="test-provider",
        version="1.0",
        parameters={"temperature": 0.7},
        capabilities={"reasoning": True, "analysis": True}
    )
    model = TestModel(config)
    
    prompt = "Test prompt"
    response = model.generate(prompt, temperature=0.8)
    assert response == f"Test response for: {prompt}" 