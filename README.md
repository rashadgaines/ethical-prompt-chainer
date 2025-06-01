# Ethical Prompt Chaining System

A sophisticated system for analyzing ethical dilemmas using chain-of-thought prompting and constitutional principles.

## Features

### Enhanced Prompt Diversity and Contextual Adaptation
- Dynamic prompt generation based on dilemma context (economic, social, environmental, etc.)
- Context-specific value mappings and considerations
- Automatic identification of dilemma type and relevant ethical principles
- Customized prompts for different types of analysis (framing, stakeholder analysis, etc.)

### Automated Data Validation
- Comprehensive validation of dilemma inputs
- Checks for minimum length, question format, and completeness
- Detailed error reporting and logging
- Integration with the main analysis pipeline

### Core Functionality
- Constitutional principle-based ethical analysis
- Stakeholder impact assessment
- Legal feasibility evaluation
- Comprehensive solution recommendations
- Monitoring plan generation

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API keys in a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
GROK_API_KEY=your_grok_api_key_here
```

## Usage

```python
from ethical_prompt_chainer import EthicalPromptChainer

# Initialize the chainer
chainer = EthicalPromptChainer(model_name="gpt-4")

# Analyze a dilemma
dilemma = "Should universal basic income be implemented to reduce inequality, or should we maintain targeted welfare programs to avoid disincentivizing work?"
analysis = chainer.analyze_dilemma(dilemma)

# Print the formatted analysis
print(chainer.format_analysis(analysis))
```

## Example Output

```
Ethical Analysis Report

Dilemma:
Should universal basic income be implemented to reduce inequality, or should we maintain targeted welfare programs to avoid disincentivizing work?

Validation Status: ✓ Valid
Context: economic, social

1. Dilemma Framing:
[Analysis of constitutional principles and legal frameworks...]

2. Stakeholder Analysis:
[Detailed stakeholder impact assessment...]

3. Consequence Analysis:
[Ethical balancing test results...]

4. Ethical and Legal Principles:
[Legal feasibility evaluation...]

5. Proposed Solution:
[Comprehensive recommendation with safeguards...]
```

## Testing

Run the test suite:

```bash
python -m unittest discover ethical_prompt_chainer/tests
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
│   ├── models.py
│   ├── data_validator.py
│   ├── config.py
│   └── logging.py
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

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details 