# Ethical Prompt Chainer

A research tool for training and evaluating ethical reasoning in AI models through structured prompt engineering.

## Purpose

This tool enables research teams to:
- Train models on complex ethical reasoning through a structured chain-of-thought approach
- Evaluate model performance on diverse ethical dilemmas
- Collect consistent, structured responses for model comparison
- Build datasets of ethical reasoning patterns

## Core Features

- **Structured Reasoning Chain**: Guides models through a 6-step ethical analysis:
  1. Context Gathering
  2. Ethical Principle Application
  3. Trade-off Analysis
  4. Bias Checking
  5. Values Alignment
  6. Solution Proposal

- **Standardized Dilemmas**: Pre-configured ethical scenarios covering:
  - AI Ethics
  - Medical Ethics
  - Autonomous Systems
  - Data Privacy
  - Algorithmic Bias
  - And more...

- **Consistent Output Format**: Structured responses for easy:
  - Model comparison
  - Performance tracking
  - Dataset building
  - Pattern analysis

## Quick Start

1. Install:
```bash
pip install ethical-prompt-chainer
```

2. Set up your API key:
```bash
# Create .env file
echo "GROK_API_KEY=your_api_key_here" > .env
```

3. Run analysis:
```bash
python -m ethical_prompt_chainer.run_analysis
```

## Research Applications

- **Model Training**: Use the structured prompts to train models on ethical reasoning
- **Performance Evaluation**: Compare model responses across different ethical scenarios
- **Dataset Creation**: Build datasets of ethical reasoning patterns
- **Pattern Analysis**: Study how models handle different types of ethical dilemmas
- **Bias Detection**: Identify potential biases in model reasoning

## Contributing

We welcome contributions to:
- New ethical dilemmas
- Improved reasoning chains
- Additional model integrations
- Analysis tools

## License

MIT License - See LICENSE file for details 