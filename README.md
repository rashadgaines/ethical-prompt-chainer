# Ethical Prompt Chainer

A sophisticated Python library that implements structured ethical reasoning chains for AI models, enabling systematic analysis of complex ethical dilemmas through advanced prompt engineering and chain-of-thought methodologies.

## Overview

This tool implements a 6-step ethical reasoning chain that guides AI models through complex ethical dilemmas:

1. **Context Gathering**: Identify stakeholders, intentions, consequences, and values
2. **Ethical Framework Analysis**: Evaluate through consequentialism, deontology, virtue ethics, and care ethics
3. **Trade-off Analysis**: Assess short/long-term impacts, harm/benefit scales, and value conflicts
4. **Bias Checking**: Review for cultural biases, assumptions, and knowledge gaps
5. **Values Alignment**: Ensure alignment with fairness, empathy, diversity, and human flourishing
6. **Solution Proposal**: Provide actionable steps with monitoring and contingencies

## Installation

```bash
pip install ethical-prompt-chainer
```

## Usage

```python
from ethical_prompt_chainer import EthicalPromptChainer

# Initialize with Grok-3 model
chainer = EthicalPromptChainer()

# Analyze an ethical dilemma
dilemma = "Your ethical dilemma here..."
analysis = chainer.analyze_dilemma(dilemma)

# Get formatted output
print(chainer.format_analysis(analysis))
```

## Example Output

```python
dilemma = """
A tech company has developed an AI system that can predict employee performance 
and likelihood of leaving. The system uses data from work patterns, communication 
styles, and even social media activity. Should the company use this system to make 
decisions about promotions, raises, and retention efforts?
"""

analysis = chainer.analyze_dilemma(dilemma)
print(chainer.format_analysis(analysis))
```

Output:
```
Model Used: grok-3
User Prompt: [dilemma text]

Reasoning Chain:

1. Context Analysis:
   - Key Stakeholders: Employees, management, company shareholders
   - Intentions: Improve retention, optimize workforce, reduce bias
   - Consequences: Privacy concerns, potential discrimination, workplace culture impact
   - Values at Stake: Privacy, fairness, transparency, employee autonomy

2. Ethical Framework Analysis:
   - Consequentialism: Weighing benefits of efficiency against potential harms
   - Deontology: Respecting employee privacy and dignity
   - Virtue Ethics: Promoting trust and fairness in workplace
   - Care Ethics: Considering impact on employee well-being

3. Trade-off Analysis:
   - Short-term: Improved retention vs. employee trust
   - Long-term: Workforce optimization vs. workplace culture
   - Certainty: High accuracy claims vs. potential biases
   - Value Conflicts: Efficiency vs. privacy, optimization vs. autonomy

4. Bias and Assumption Check:
   - Potential Biases: Socioeconomic, cultural, communication style
   - Assumptions: Data accuracy, prediction reliability
   - Knowledge Gaps: Long-term impact on workplace dynamics
   - Cultural Perspectives: Varying views on workplace monitoring

5. Values Alignment:
   - Fairness: Ensuring equal opportunity regardless of background
   - Empathy: Considering employee concerns and well-being
   - Diversity: Avoiding discrimination in predictions
   - Transparency: Clear communication about system use

Solution:
1. Primary Recommendation:
   - Implement system with strict limitations and oversight
   - Use only for retention efforts, not promotions/raises
   - Require employee consent and opt-out options

2. Implementation Steps:
   - Develop clear usage guidelines
   - Create oversight committee
   - Implement regular audits
   - Establish employee feedback channels

3. Monitoring and Evaluation:
   - Track system accuracy and bias
   - Monitor employee satisfaction
   - Regular impact assessments
   - Adjust based on feedback

4. Contingency Plans:
   - Immediate suspension if bias detected
   - Alternative retention strategies
   - Employee support programs
   - Regular policy reviews

Timestamp: 2024-03-21T14:30:00Z
```

## Configuration

1. Create a `.env` file:
```
GROK_API_KEY=your_api_key_here
```

2. Optional parameters:
```python
chainer = EthicalPromptChainer(
    model_name="grok-3",  # Default model
    temperature=0.7,      # Response creativity
    max_tokens=2000       # Response length
)
```

## Output Format

The analysis returns a structured response containing:
- Context analysis
- Ethical framework evaluation
- Trade-off assessment
- Bias and assumption review
- Values alignment check
- Detailed solution with implementation steps

## Requirements

- Python 3.7+
- Grok API access
- `python-dotenv`
- `requests`

## License

MIT 