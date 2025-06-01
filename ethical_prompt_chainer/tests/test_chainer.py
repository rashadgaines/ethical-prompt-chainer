import pytest
from ethical_prompt_chainer import EthicalPromptChainer
from ethical_prompt_chainer.models import ModelConfig, ModelError

def test_chainer_initialization():
    """Test chainer initialization with default settings."""
    config = ModelConfig(
        name="test-model",
        provider="test-provider",
        version="1.0",
        parameters={"temperature": 0.7},
        capabilities={"reasoning": True, "analysis": True}
    )
    chainer = EthicalPromptChainer(model_config=config)
    assert chainer is not None
    assert hasattr(chainer, "model")
    assert hasattr(chainer, "templates")

def test_chainer_initialization_invalid_model():
    """Test chainer initialization with invalid model."""
    with pytest.raises(ModelError):
        config = ModelConfig(
            name="invalid-model",
            provider="invalid-provider",
            version="1.0",
            parameters={},
            capabilities={}
        )
        EthicalPromptChainer(model_config=config)

def test_guide_reasoning():
    """Test guiding model reasoning through a dilemma."""
    config = ModelConfig(
        name="test-model",
        provider="test-provider",
        version="1.0",
        parameters={"temperature": 0.7},
        capabilities={"reasoning": True, "analysis": True}
    )
    chainer = EthicalPromptChainer(model_config=config)
    dilemma = "Should AI be used for hiring decisions?"
    context = [
        "AI can reduce human bias in hiring",
        "AI may perpetuate existing biases in training data"
    ]
    
    result = chainer.guide_reasoning(dilemma, context)
    
    assert result is not None
    assert hasattr(result, "reasoning")
    assert hasattr(result, "principles")
    assert hasattr(result, "confidence")
    assert hasattr(result, "formatted_response")

def test_chain_of_thought():
    """Test chain-of-thought reasoning process."""
    config = ModelConfig(
        name="test-model",
        provider="test-provider",
        version="1.0",
        parameters={"temperature": 0.7},
        capabilities={"reasoning": True, "analysis": True}
    )
    chainer = EthicalPromptChainer(model_config=config)
    dilemma = "Should AI be used for hiring decisions?"
    
    # Test each step in the chain
    principles = chainer.identify_principles(dilemma)
    assert principles is not None
    assert len(principles) > 0
    
    reasoning = chainer.guide_reasoning(dilemma, principles=principles)
    assert reasoning is not None
    assert hasattr(reasoning, "steps")
    assert len(reasoning.steps) > 0
    
    confidence = chainer.assess_confidence(reasoning)
    assert confidence is not None
    assert 0 <= confidence <= 1

def test_prompt_templates():
    """Test prompt template generation."""
    config = ModelConfig(
        name="test-model",
        provider="test-provider",
        version="1.0",
        parameters={"temperature": 0.7},
        capabilities={"reasoning": True, "analysis": True}
    )
    chainer = EthicalPromptChainer(model_config=config)
    dilemma = "Should AI be used for hiring decisions?"
    
    # Test different prompt types
    principle_prompt = chainer.get_principle_identification_prompt(dilemma)
    assert principle_prompt is not None
    assert dilemma in principle_prompt
    
    reasoning_prompt = chainer.get_reasoning_prompt(dilemma, ["fairness", "transparency"])
    assert reasoning_prompt is not None
    assert dilemma in reasoning_prompt
    assert "fairness" in reasoning_prompt
    assert "transparency" in reasoning_prompt
    
    recommendation_prompt = chainer.get_recommendation_prompt("detailed reasoning here")
    assert recommendation_prompt is not None
    assert "detailed reasoning here" in recommendation_prompt 