# Ethical Prompt Chainer

A Python package that implements a structured approach to ethical analysis using language models.

## Core Functionality

The package processes ethical dilemmas through a sequential analysis chain:

1. Context Gathering
   - Stakeholder identification
   - Intention analysis
   - Consequence mapping
   - Value identification

2. Ethical Framework Analysis
   - Consequentialism evaluation
   - Deontological assessment
   - Virtue ethics consideration
   - Care ethics perspective

3. Trade-off Analysis
   - Short-term impact assessment
   - Long-term impact evaluation
   - Harm/benefit quantification
   - Value conflict resolution

4. Bias Checking
   - Cultural bias identification
   - Assumption verification
   - Knowledge gap analysis
   - Perspective diversity check

5. Values Alignment
   - Fairness verification
   - Empathy assessment
   - Diversity consideration
   - Human flourishing evaluation

6. Solution Proposal
   - Action recommendation
   - Implementation steps
   - Monitoring plan
   - Contingency preparation

## Technical Requirements

- Python 3.7+
- Grok API access
- python-dotenv
- requests

## Installation

```bash
pip install ethical-prompt-chainer
```

## Basic Usage

```python
from ethical_prompt_chainer import EthicalPromptChainer

# Initialize with default model
chainer = EthicalPromptChainer()

# Analyze a dilemma
dilemma = "Your ethical dilemma here..."
analysis = chainer.analyze_dilemma(dilemma)

# Format and display results
print(chainer.format_analysis(analysis))
```

## Configuration

1. Environment Setup
```
GROK_API_KEY=your_api_key_here
```

2. Optional Parameters
```python
chainer = EthicalPromptChainer(
    model_name="grok-3",  # Model selection
    temperature=0.7,      # Response variation
    max_tokens=2000       # Response length
)
```

## Output Structure

The analysis returns a structured response containing:
- Context analysis
- Ethical framework evaluation
- Trade-off assessment
- Bias and assumption review
- Values alignment check
- Solution with implementation steps

## Development

### Project Structure
```
ethical_prompt_chainer/
├── __init__.py
├── chainer.py
├── models.py
├── prompts.py
└── run_analysis.py
```

### Testing
```bash
pytest -v --cov=ethical_prompt_chainer
```

### Code Quality
- Type hints required
- Black formatting
- MyPy type checking
- Pytest coverage reporting

## License

MIT