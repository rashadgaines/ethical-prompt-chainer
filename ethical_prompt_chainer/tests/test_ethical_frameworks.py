import pytest
from ethical_prompt_chainer.ethical_frameworks import (
    FrameworkType,
    EthicalFramework,
    EthicalFrameworkManager
)

def test_framework_initialization():
    """Test framework initialization."""
    framework = EthicalFramework(
        type=FrameworkType.UTILITARIAN,
        principles=["Maximize overall happiness", "Minimize suffering"],
        guidance_prompts={
            "analysis": "Consider the consequences...",
            "evaluation": "Evaluate based on..."
        },
        evaluation_criteria=["Net impact", "Distribution of effects"]
    )
    
    assert framework.type == FrameworkType.UTILITARIAN
    assert len(framework.principles) == 2
    assert "analysis" in framework.guidance_prompts
    assert "evaluation" in framework.guidance_prompts
    assert len(framework.evaluation_criteria) == 2

def test_framework_manager():
    """Test framework manager functionality."""
    manager = EthicalFrameworkManager()
    
    # Test getting a framework
    framework = manager.get_framework(FrameworkType.UTILITARIAN)
    assert framework is not None
    assert framework.type == FrameworkType.UTILITARIAN
    
    # Test getting applicable frameworks
    frameworks = manager.get_applicable_frameworks(
        context=["AI ethics", "fairness", "transparency"]
    )
    assert len(frameworks) > 0
    assert all(isinstance(f, EthicalFramework) for f in frameworks)

def test_framework_guidance():
    """Test framework guidance for model behavior."""
    framework = EthicalFramework(
        type=FrameworkType.UTILITARIAN,
        principles=["Maximize overall happiness", "Minimize suffering"],
        guidance_prompts={
            "analysis": """
Consider the consequences of different actions:
1. What are the potential benefits and harms?
2. How many people would be affected?
3. What is the magnitude of impact?
4. How can we maximize overall well-being?
""",
            "evaluation": """
Evaluate the action based on:
1. Net impact on happiness
2. Distribution of benefits and harms
3. Long-term consequences
4. Alternative approaches
"""
        },
        evaluation_criteria=["Net impact", "Distribution of effects"]
    )
    
    # Test analysis prompt
    analysis_prompt = framework.guidance_prompts["analysis"]
    assert "Consider the consequences" in analysis_prompt
    assert "benefits and harms" in analysis_prompt
    assert "maximize overall well-being" in analysis_prompt
    
    # Test evaluation prompt
    evaluation_prompt = framework.guidance_prompts["evaluation"]
    assert "Evaluate the action" in evaluation_prompt
    assert "Net impact" in evaluation_prompt
    assert "Distribution" in evaluation_prompt

def test_framework_combination():
    """Test combining multiple frameworks."""
    manager = EthicalFrameworkManager()
    
    # Get multiple frameworks
    utilitarian = manager.get_framework(FrameworkType.UTILITARIAN)
    deontological = manager.get_framework(FrameworkType.DEONTOLOGICAL)
    
    # Test framework combination
    combined_principles = utilitarian.principles + deontological.principles
    assert len(combined_principles) > len(utilitarian.principles)
    assert len(combined_principles) > len(deontological.principles)
    
    # Test combined guidance
    combined_guidance = {
        "analysis": utilitarian.guidance_prompts["analysis"] + "\n" + 
                   deontological.guidance_prompts["analysis"],
        "evaluation": utilitarian.guidance_prompts["evaluation"] + "\n" + 
                     deontological.guidance_prompts["evaluation"]
    }
    assert "Consider the consequences" in combined_guidance["analysis"]
    assert "moral duties" in combined_guidance["analysis"] 