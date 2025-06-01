# API Reference

This document provides detailed information about the Ethical Prompt Chainer API.

## EthicalPromptChainer

The main class for performing ethical analysis.

### Initialization

```python
def __init__(
    self,
    model_type: ModelType = ModelType.GPT4,
    benchmark_models: Optional[List[ModelType]] = None,
    include_benchmark: bool = False,
    include_explanation: bool = True
)
```

**Parameters:**
- `model_type`: The type of model to use for analysis (default: GPT4)
- `benchmark_models`: Optional list of models to benchmark against
- `include_benchmark`: Whether to include benchmarking in analysis
- `include_explanation`: Whether to include AI explanations

### Methods

#### analyze_dilemma

```python
def analyze_dilemma(
    self,
    dilemma: str,
    context: Optional[List[str]] = None,
    include_benchmark: bool = False,
    explanation_level: ExplanationLevel = ExplanationLevel.DETAILED
) -> EthicalAnalysis
```

Analyzes an ethical dilemma and returns a comprehensive analysis.

**Parameters:**
- `dilemma`: The ethical dilemma to analyze
- `context`: Optional list of relevant contexts
- `include_benchmark`: Whether to include benchmarking
- `explanation_level`: Level of detail for AI explanations

**Returns:**
- `EthicalAnalysis` object containing the complete analysis

#### format_analysis

```python
def format_analysis(self, analysis: EthicalAnalysis) -> str
```

Formats the analysis results into a readable report.

**Parameters:**
- `analysis`: The EthicalAnalysis object to format

**Returns:**
- Formatted analysis report as a string

## EthicalAnalysis

Dataclass containing the results of an ethical analysis.

### Attributes

- `dilemma`: str - The analyzed dilemma
- `context`: List[str] - Relevant contexts
- `ethical_principles`: List[str] - Identified principles
- `analysis`: str - Detailed analysis
- `recommendations`: List[str] - Generated recommendations
- `confidence_score`: float - Analysis confidence
- `model_used`: str - Model used for analysis
- `timestamp`: datetime - Analysis timestamp
- `benchmark_results`: Optional[BenchmarkMetrics] - Benchmark results
- `ethical_alignment`: Optional[Dict[str, float]] - Ethical alignment scores
- `stakeholder_impacts`: Optional[List[StakeholderImpact]] - Stakeholder impacts
- `long_term_impact`: Optional[LongTermImpact] - Long-term impact analysis
- `ai_explanation`: Optional[AIExplanation] - AI explanation of the analysis

## EthicalFrameworkManager

Manages ethical frameworks and their application.

### Methods

#### get_framework

```python
def get_framework(self, framework_name: str) -> EthicalFramework
```

Retrieves a specific ethical framework.

**Parameters:**
- `framework_name`: Name of the framework to retrieve

**Returns:**
- `EthicalFramework` object

#### get_applicable_frameworks

```python
def get_applicable_frameworks(self, context: List[str]) -> List[EthicalFramework]
```

Gets frameworks applicable to the given context.

**Parameters:**
- `context`: List of relevant contexts

**Returns:**
- List of applicable `EthicalFramework` objects

## StakeholderAnalyzer

Analyzes impacts on different stakeholder groups.

### Methods

#### analyze_impact

```python
def analyze_impact(
    self,
    decision: str,
    stakeholder: str,
    context: List[str]
) -> StakeholderImpact
```

Analyzes the impact of a decision on a stakeholder.

**Parameters:**
- `decision`: The decision to analyze
- `stakeholder`: The stakeholder to analyze
- `context`: Relevant contexts

**Returns:**
- `StakeholderImpact` object

## LongTermImpactAnalyzer

Analyzes long-term impacts of decisions.

### Methods

#### analyze_long_term_impact

```python
def analyze_long_term_impact(
    self,
    decision: str,
    context: List[str]
) -> LongTermImpact
```

Analyzes the long-term impact of a decision.

**Parameters:**
- `decision`: The decision to analyze
- `context`: Relevant contexts

**Returns:**
- `LongTermImpact` object

## ExplainableAI

Provides explanations for AI-driven ethical analysis.

### Methods

#### explain_analysis

```python
def explain_analysis(
    self,
    analysis: Any,
    explanation_type: ExplanationType,
    level: ExplanationLevel = ExplanationLevel.DETAILED
) -> AIExplanation
```

Generates explanations for the ethical analysis.

**Parameters:**
- `analysis`: The analysis to explain
- `explanation_type`: Type of explanation to generate
- `level`: Level of detail for the explanation

**Returns:**
- `AIExplanation` object

## Enums

### ModelType

```python
class ModelType(Enum):
    GPT4 = "gpt-4"
    GPT35 = "gpt-3.5-turbo"
    GROK = "grok"
```

### ExplanationType

```python
class ExplanationType(Enum):
    FEATURE_IMPORTANCE = "feature_importance"
    DECISION_PATH = "decision_path"
    COUNTERFACTUAL = "counterfactual"
    SIMILAR_CASES = "similar_cases"
    CONFIDENCE_BREAKDOWN = "confidence_breakdown"
    ETHICAL_REASONING = "ethical_reasoning"
```

### ExplanationLevel

```python
class ExplanationLevel(Enum):
    BASIC = "basic"
    DETAILED = "detailed"
    TECHNICAL = "technical"
```

## Data Classes

### FeatureImportance

```python
@dataclass
class FeatureImportance:
    feature: str
    importance_score: float
    contribution: str
    confidence: float
```

### DecisionPath

```python
@dataclass
class DecisionPath:
    steps: List[str]
    reasoning: List[str]
    alternatives: List[str]
    confidence_scores: List[float]
```

### CounterfactualAnalysis

```python
@dataclass
class CounterfactualAnalysis:
    scenario: str
    outcome: str
    changed_factors: List[str]
    confidence: float
```

### SimilarCase

```python
@dataclass
class SimilarCase:
    case_id: str
    similarity_score: float
    key_similarities: List[str]
    key_differences: List[str]
    outcome: str
```

### ConfidenceBreakdown

```python
@dataclass
class ConfidenceBreakdown:
    factors: Dict[str, float]
    reasoning: Dict[str, str]
    overall_confidence: float
```

### EthicalReasoning

```python
@dataclass
class EthicalReasoning:
    principles_applied: List[str]
    reasoning_steps: List[str]
    tradeoffs: List[str]
    justification: str
```

### AIExplanation

```python
@dataclass
class AIExplanation:
    feature_importance: List[FeatureImportance]
    decision_path: DecisionPath
    counterfactuals: List[CounterfactualAnalysis]
    similar_cases: List[SimilarCase]
    confidence_breakdown: ConfidenceBreakdown
    ethical_reasoning: EthicalReasoning
    timestamp: datetime
``` 