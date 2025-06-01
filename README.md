# Ethical Prompt Chainer

A framework for improving AI model behavior through structured prompt engineering. This system uses a chain-of-thought approach to guide models through complex ethical reasoning, helping them develop more nuanced 
and consistent responses to ethical dilemmas.

## Core Purpose

The Ethical Prompt Chainer helps improve AI model behavior by:
- Using carefully engineered prompts to guide model reasoning
- Structuring ethical dilemmas to encourage deeper thinking
- Providing frameworks for consistent ethical consideration
- Enabling transparent and explainable model responses

## Key Features

- **Structured Prompt Engineering**: Carefully crafted prompts that guide models through ethical reasoning
- **Multiple Model Support**: Works with GPT-4, GPT-3.5, and Grok models
- **Ethical Frameworks**: Built-in frameworks (Utilitarian, Deontological, Virtue, Care, Sustainable) to guide model behavior
- **Transparent Reasoning**: Models explain their thought process and confidence levels
- **Extensible Design**: Easy to add new prompts, frameworks, or model support

## Quick Start

```python
from ethical_prompt_chainer import EthicalPromptChainer, ModelType

# Initialize the chainer with GPT-4
chainer = EthicalPromptChainer(model_type=ModelType.GPT4)

# Create an ethical dilemma
dilemma = "Should AI be used for hiring decisions?"
context = [
    "AI can reduce human bias in hiring",
    "AI may perpetuate existing biases in training data",
    "AI can process more applications than humans",
    "AI may miss nuanced human qualities"
]

# Guide the model's reasoning
result = chainer.guide_reasoning(dilemma, context)

# Print the guided response
print(result.formatted_response)
```

## Framework Structure

```
ethical_prompt_chainer/
├── chainer.py          # Main class for guiding model behavior
├── prompts.py          # Engineered prompts for each reasoning step
├── models.py           # Model interfaces and implementations
└── ethical_frameworks.py  # Frameworks for guiding ethical reasoning
```

## Extending the Framework

### Adding a New Prompt Template

```python
from ethical_prompt_chainer.prompts import PromptType, PromptTemplate

# Create a new prompt template
new_template = PromptTemplate(
    type=PromptType.REASONING_GUIDANCE,
    template="""Your custom prompt template here...""",
    expected_format="Expected format...",
    guidance_notes="Notes for guiding model behavior..."
)

# Add to EthicalPromptTemplates
templates = EthicalPromptTemplates()
templates.templates[PromptType.REASONING_GUIDANCE] = new_template
```

### Adding a New Ethical Framework

```python
from ethical_prompt_chainer.ethical_frameworks import FrameworkType, EthicalFramework

# Create a new framework
new_framework = EthicalFramework(
    type=FrameworkType.CUSTOM,
    principles=["Your principles here..."],
    guidance_prompts={
        "analysis": "Your analysis prompt...",
        "evaluation": "Your evaluation prompt..."
    },
    evaluation_criteria=["Your criteria here..."]
)

# Add to EthicalFrameworkManager
framework_manager = EthicalFrameworkManager()
framework_manager.frameworks[FrameworkType.CUSTOM] = new_framework
```

## Example Use Case: AI Ethics Analysis

```python
from ethical_prompt_chainer import EthicalPromptChainer, ModelType

# Initialize with GPT-4
chainer = EthicalPromptChainer(model_type=ModelType.GPT4)

# Define an AI ethics dilemma
dilemma = "Should AI systems be allowed to make life-or-death decisions in healthcare?"
context = [
    "AI can process more medical data than humans",
    "AI may make faster decisions in emergencies",
    "AI lacks human empathy and intuition",
    "AI decisions may be difficult to explain"
]

# Guide the model's reasoning
result = chainer.guide_reasoning(dilemma, context)

# The result includes:
# - Guided reasoning process
# - Ethical principles considered
# - Confidence assessment
# - Formatted response
```

## Installation

```bash
pip install ethical-prompt-chainer
```

## Documentation

- [Architecture Overview](docs/architecture.md)
- [Prompt Engineering Guide](docs/prompt_engineering.md)
- [Ethical Frameworks](docs/ethical_frameworks.md)
- [Model Integration Guide](docs/model_integration.md)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 