# Ethical Prompt Chainer

A reusable framework for ethical analysis using chain-of-thought prompting. This framework provides a structured approach to analyzing ethical dilemmas through a series of interconnected prompts that guide the analysis process.

## Core Features

- **Modular Analysis Pipeline**: Chain together different types of ethical analysis
- **Extensible Framework**: Easily add new analysis types or ethical frameworks
- **Transparent Reasoning**: Step-by-step explanation of ethical decisions
- **Customizable Output**: Format results for different use cases

## Quick Start

```python
from ethical_prompt_chainer import EthicalPromptChainer

# Initialize the chainer
chainer = EthicalPromptChainer()

# Analyze a dilemma
dilemma = "Should AI be used for hiring decisions?"
analysis = chainer.analyze_dilemma(dilemma)

# Get formatted results
print(chainer.format_analysis(analysis))
```

## Framework Structure

```
ethical_prompt_chainer/
├── chainer.py          # Main analysis pipeline
├── prompts.py          # Prompt templates
├── models.py           # Model interfaces
├── ethical_frameworks.py  # Ethical framework definitions
└── analyzers/          # Analysis modules
    ├── stakeholder.py
    ├── long_term.py
    └── explainable.py
```

## Extending the Framework

### Adding a New Analysis Type

```python
from ethical_prompt_chainer import BaseAnalyzer

class CustomAnalyzer(BaseAnalyzer):
    def analyze(self, dilemma: str, context: List[str]) -> AnalysisResult:
        # Implement your analysis logic
        pass
```

### Creating a New Ethical Framework

```python
from ethical_prompt_chainer import EthicalFramework

class CustomFramework(EthicalFramework):
    def __init__(self):
        self.principles = [
            "Principle 1",
            "Principle 2"
        ]
        self.weights = {
            "Principle 1": 0.6,
            "Principle 2": 0.4
        }
```

## Example Use Case: AI Ethics Analysis

```python
from ethical_prompt_chainer import EthicalPromptChainer

# Initialize with specific configuration
chainer = EthicalPromptChainer(
    model_type="gpt-4",
    include_explanation=True
)

# Define an AI ethics dilemma
dilemma = """
Should an AI system be deployed for automated hiring decisions,
considering both efficiency gains and potential bias concerns?
"""

# Perform analysis
analysis = chainer.analyze_dilemma(
    dilemma,
    context=["technology", "employment", "fairness"]
)

# Access specific aspects of the analysis
print("Ethical Principles:", analysis.ethical_principles)
print("Stakeholder Impacts:", analysis.stakeholder_impacts)
print("Long-term Effects:", analysis.long_term_impact)
```

## Installation

```bash
pip install ethical-prompt-chainer
```

## Documentation

For detailed documentation, see the [docs](docs/) directory:
- [Getting Started](docs/getting_started.md)
- [API Reference](docs/api_reference.md)
- [Architecture](docs/architecture.md)
- [Examples](docs/examples.md)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details. 