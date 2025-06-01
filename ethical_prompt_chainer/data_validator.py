import pandas as pd
import logging
from typing import List, Dict, Tuple
from pathlib import Path

logger = logging.getLogger(__name__)

class DilemmaValidator:
    """Validates dilemma data for completeness and quality."""
    
    MIN_DILEMMA_LENGTH = 50  # Minimum characters for a valid dilemma
    REQUIRED_FIELDS = ['dilemma', 'issue_a', 'issue_b', 'value_1', 'value_2']
    
    def __init__(self, min_dilemma_length: int = MIN_DILEMMA_LENGTH):
        self.min_dilemma_length = min_dilemma_length
    
    def validate_dilemma_text(self, dilemma: str) -> Tuple[bool, str]:
        """Validate a single dilemma text entry."""
        if not dilemma or not isinstance(dilemma, str):
            return False, "Dilemma must be a non-empty string"
        
        if len(dilemma) < self.min_dilemma_length:
            return False, f"Dilemma text too short (minimum {self.min_dilemma_length} characters)"
        
        if not "?" in dilemma:
            return False, "Dilemma must be a question"
        
        return True, "Valid dilemma text"
    
    def validate_dilemmas_file(self, file_path: str) -> Tuple[bool, List[str]]:
        """Validate all dilemmas in a file."""
        errors = []
        
        try:
            with open(file_path, 'r') as f:
                dilemmas = f.readlines()
            
            for i, dilemma in enumerate(dilemmas, 1):
                dilemma = dilemma.strip()
                if not dilemma:  # Skip empty lines
                    continue
                    
                is_valid, error_msg = self.validate_dilemma_text(dilemma)
                if not is_valid:
                    errors.append(f"Line {i}: {error_msg}")
            
            return len(errors) == 0, errors
            
        except Exception as e:
            error_msg = f"Error reading dilemmas file: {str(e)}"
            logger.error(error_msg)
            return False, [error_msg]
    
    def log_validation_errors(self, errors: List[str], log_file: str = "validation_errors.log"):
        """Log validation errors to a file."""
        with open(log_file, 'w') as f:
            f.write("Dilemma Validation Errors:\n")
            f.write("=" * 50 + "\n")
            for error in errors:
                f.write(f"{error}\n")
            f.write("=" * 50 + "\n") 