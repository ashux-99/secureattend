"""Logging configuration for SecureAttend."""

import logging
import sys
from pathlib import Path
from app.config import DATA_DIR


def setup_logging(log_level: str = "INFO", log_file: str = None) -> None:
    """
    Configure logging for the application.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Optional path to log file
    """
    if log_file is None:
        log_file = DATA_DIR / "secureattend.log"
    
    # Create log directory if needed
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
