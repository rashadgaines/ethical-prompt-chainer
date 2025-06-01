# Ethical Prompt Chainer

A standalone tool that uses LangChain and language models to reason through ethical dilemmas step-by-step using chain-of-thought prompting.

## Features

- Step-by-step ethical reasoning using chain-of-thought prompting
- Support for various language models (LLaMA-7B, DistilGPT-2, etc.)
- Structured analysis of ethical dilemmas including:
  - Stakeholder identification
  - Consequence evaluation
  - Ethical principle consideration
  - Solution proposal
- Configurable prompting templates
- Extensible architecture for custom ethical frameworks

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from ethical_prompt_chainer import EthicalPromptChainer

# Initialize the chainer with your preferred model
chainer = EthicalPromptChainer(model_name="distilgpt2")

# Analyze an ethical dilemma
result = chainer.analyze_dilemma(
    "Should I lie to protect someone's feelings?"
)

# Print the step-by-step analysis
print(result)
```

## Project Structure

```
ethical-prompt-chainer/
├── requirements.txt
├── README.md
├── ethical_prompt_chainer/
│   ├── __init__.py
│   ├── chainer.py
│   ├── prompts.py
│   └── models.py
└── examples/
    └── dilemmas.py
```

## Ethical Framework

The tool uses a structured approach to ethical reasoning:

1. **Stakeholder Identification**: Identify all parties affected by the decision
2. **Consequence Analysis**: Evaluate potential outcomes and their impacts
3. **Principle Consideration**: Apply relevant ethical principles
4. **Solution Development**: Propose and justify a course of action

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License 