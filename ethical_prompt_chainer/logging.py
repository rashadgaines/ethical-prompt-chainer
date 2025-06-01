import logging
from typing import Optional
from pathlib import Path

def setup_logging(
    log_file: Optional[str] = None,
    level: int = logging.INFO
) -> logging.Logger:
    """
    Set up logging configuration.
    
    Args:
        log_file: Optional path to log file
        level: Logging level
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger("ethical_prompt_chainer")
    logger.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Add console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Add file handler if log file specified
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

class EthicalPromptChainerError(Exception):
    """Base exception class for EthicalPromptChainer."""
    pass

class ModelInitializationError(EthicalPromptChainerError):
    """Raised when there's an error initializing the language model."""
    pass

class ChainExecutionError(EthicalPromptChainerError):
    """Raised when there's an error executing a reasoning chain."""
    pass 