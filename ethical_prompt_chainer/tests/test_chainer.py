import pytest
from ethical_prompt_chainer import EthicalPromptChainer, EthicalAnalysis
from ethical_prompt_chainer.logging import ModelInitializationError, ChainExecutionError

def test_chainer_initialization():
    """Test chainer initialization with default settings."""
    chainer = EthicalPromptChainer(model_name="distilgpt2", device="cpu")
    assert chainer is not None
    assert hasattr(chainer, "model")
    assert hasattr(chainer, "templates")

def test_chainer_initialization_invalid_model():
    """Test chainer initialization with invalid model."""
    with pytest.raises(ModelInitializationError):
        EthicalPromptChainer(model_name="invalid_model", device="cpu")

def test_analyze_dilemma():
    """Test basic dilemma analysis."""
    chainer = EthicalPromptChainer(model_name="distilgpt2", device="cpu")
    dilemma = "Should I lie to protect someone's feelings?"
    
    analysis = chainer.analyze_dilemma(dilemma)
    
    assert isinstance(analysis, EthicalAnalysis)
    assert analysis.dilemma == dilemma
    assert analysis.stakeholders
    assert analysis.consequences
    assert analysis.principles
    assert analysis.solution

def test_format_analysis():
    """Test analysis formatting."""
    chainer = EthicalPromptChainer(model_name="distilgpt2", device="cpu")
    analysis = EthicalAnalysis(
        dilemma="Test dilemma",
        stakeholders="Test stakeholders",
        consequences="Test consequences",
        principles="Test principles",
        solution="Test solution"
    )
    
    formatted = chainer.format_analysis(analysis)
    
    assert isinstance(formatted, str)
    assert "Test dilemma" in formatted
    assert "Test stakeholders" in formatted
    assert "Test consequences" in formatted
    assert "Test principles" in formatted
    assert "Test solution" in formatted 