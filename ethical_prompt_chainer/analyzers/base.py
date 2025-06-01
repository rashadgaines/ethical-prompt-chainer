from abc import ABC, abstractmethod
from typing import List, Any, Dict
from dataclasses import dataclass

@dataclass
class AnalysisResult:
    """Base class for analysis results."""
    confidence_score: float
    details: Dict[str, Any]

class BaseAnalyzer(ABC):
    """Base class for all analyzers in the framework."""
    
    @abstractmethod
    def analyze(self, dilemma: str, context: List[str]) -> AnalysisResult:
        """
        Analyze a dilemma using the analyzer's specific approach.
        
        Args:
            dilemma: The ethical dilemma to analyze
            context: List of relevant contexts
            
        Returns:
            AnalysisResult containing the analysis and confidence score
        """
        pass
    
    @abstractmethod
    def format_result(self, result: AnalysisResult) -> str:
        """
        Format the analysis result into a readable string.
        
        Args:
            result: The analysis result to format
            
        Returns:
            Formatted string representation of the analysis
        """
        pass 