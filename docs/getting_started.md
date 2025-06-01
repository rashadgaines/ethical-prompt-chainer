# Getting Started with Ethical Prompt Chainer

This guide will help you get started with the Ethical Prompt Chainer system.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ethical-prompt-chainer.git
cd ethical-prompt-chainer
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API keys in a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
GROK_API_KEY=your_grok_api_key_here
```

## Basic Usage

### Initializing the Chainer

```python
from ethical_prompt_chainer import EthicalPromptChainer
from ethical_prompt_chainer.models import ModelType

# Initialize with default settings
chainer = EthicalPromptChainer()

# Or customize the initialization
chainer = EthicalPromptChainer(
    model_type=ModelType.GPT4,
    include_benchmark=True,
    include_explanation=True
)
```

### Analyzing a Dilemma

```python
# Basic analysis
dilemma = "Should universal basic income be implemented to reduce inequality?"
analysis = chainer.analyze_dilemma(dilemma)

# Analysis with context
context = ["economic", "social", "political"]
analysis = chainer.analyze_dilemma(
    dilemma,
    context=context,
    include_benchmark=True,
    explanation_level=ExplanationLevel.DETAILED
)

# Print the formatted analysis
print(chainer.format_analysis(analysis))
```

### Understanding the Analysis Output

The analysis output includes:
- Ethical principles identified
- Detailed analysis of the dilemma
- Recommendations
- Confidence score
- Stakeholder impacts
- Long-term consequences
- AI explanation of the reasoning

## Configuration

### Model Selection

The system supports multiple model types:
- GPT-4 (default)
- GPT-3.5
- Grok
- Custom models

### Analysis Options

You can customize the analysis by:
- Including/excluding benchmarking
- Adjusting explanation detail level
- Adding specific contexts
- Selecting ethical frameworks

## Quick Start Example

Here's a complete example that demonstrates the basic functionality:

```python
from ethical_prompt_chainer import EthicalPromptChainer
from ethical_prompt_chainer.models import ModelType
from ethical_prompt_chainer.explainable_ai import ExplanationLevel

# Initialize the chainer
chainer = EthicalPromptChainer(
    model_type=ModelType.GPT4,
    include_benchmark=True,
    include_explanation=True
)

# Define a dilemma
dilemma = """
Should a company implement AI-based hiring systems that could potentially 
reduce human bias but might introduce new forms of algorithmic bias?
"""

# Define context
context = [
    "technology",
    "employment",
    "social justice",
    "business ethics"
]

# Perform analysis
analysis = chainer.analyze_dilemma(
    dilemma,
    context=context,
    include_benchmark=True,
    explanation_level=ExplanationLevel.DETAILED
)

# Print the results
print(chainer.format_analysis(analysis))
```

## Next Steps

After getting started, you might want to:
1. Explore [Core Concepts](core_concepts.md) to understand the system better
2. Check out [Examples](examples.md) for more complex use cases
3. Read the [API Reference](api_reference.md) for detailed information
4. Learn about [Contributing](contributing.md) to the project

## Troubleshooting

Common issues and solutions:

1. **API Key Errors**
   - Ensure your `.env` file is properly configured
   - Check that the API keys are valid
   - Verify the environment variables are loaded

2. **Model Loading Issues**
   - Check your internet connection
   - Verify model availability
   - Ensure sufficient API quota

3. **Analysis Errors**
   - Check the dilemma format
   - Verify context validity
   - Ensure proper error handling

For more help, check the [FAQ](faq.md) or create an issue on GitHub. 