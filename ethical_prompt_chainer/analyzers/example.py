from typing import List, Dict, Any
from .base import BaseAnalyzer, AnalysisResult

class ExampleAnalyzer(BaseAnalyzer):
    """
    Example analyzer that demonstrates how to extend the framework.
    This analyzer performs a simple sentiment-based analysis of ethical dilemmas.
    """
    
    def analyze(self, dilemma: str, context: List[str]) -> AnalysisResult:
        """
        Analyze a dilemma using sentiment analysis.
        
        Args:
            dilemma: The ethical dilemma to analyze
            context: List of relevant contexts
            
        Returns:
            AnalysisResult containing the sentiment analysis
        """
        # This is a simplified example - in practice, you would use
        # a proper sentiment analysis model or other analysis method
        positive_words = ["should", "benefit", "improve", "help", "support"]
        negative_words = ["shouldn't", "harm", "hurt", "damage", "risk"]
        
        # Count positive and negative words
        positive_count = sum(1 for word in positive_words if word in dilemma.lower())
        negative_count = sum(1 for word in negative_words if word in dilemma.lower())
        
        # Calculate confidence score (simplified)
        total_words = len(dilemma.split())
        confidence_score = min(1.0, (positive_count + negative_count) / total_words)
        
        # Create analysis details
        details = {
            "positive_aspects": positive_count,
            "negative_aspects": negative_count,
            "context_relevance": {ctx: 0.5 for ctx in context},  # Simplified
            "analysis_type": "sentiment"
        }
        
        return AnalysisResult(
            confidence_score=confidence_score,
            details=details
        )
    
    def format_result(self, result: AnalysisResult) -> str:
        """
        Format the analysis result into a readable string.
        
        Args:
            result: The analysis result to format
            
        Returns:
            Formatted string representation of the analysis
        """
        details = result.details
        return f"""
Example Analysis Results:
------------------------
Confidence Score: {result.confidence_score:.2f}
Positive Aspects: {details['positive_aspects']}
Negative Aspects: {details['negative_aspects']}
Analysis Type: {details['analysis_type']}

Context Relevance:
{chr(10).join(f'- {ctx}: {score:.2f}' for ctx, score in details['context_relevance'].items())}
""" 