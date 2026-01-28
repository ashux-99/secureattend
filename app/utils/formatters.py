"""Formatting utilities."""

from datetime import datetime
from typing import Optional


def format_timestamp(timestamp: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format an ISO timestamp string.
    
    Args:
        timestamp: ISO format timestamp string
        format_str: Desired output format
    
    Returns:
        Formatted timestamp string
    """
    try:
        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        return dt.strftime(format_str)
    except (ValueError, AttributeError):
        return timestamp


def format_student_id(student_id: str) -> str:
    """
    Format student ID for display.
    
    Args:
        student_id: Raw student ID
    
    Returns:
        Formatted student ID
    """
    return student_id.upper().strip()
