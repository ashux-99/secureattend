"""Validation utilities."""

import re
from typing import Optional


def validate_student_id(student_id: str) -> tuple[bool, Optional[str]]:
    """
    Validate student ID format.
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not student_id:
        return False, "Student ID cannot be empty"
    
    if len(student_id) < 3:
        return False, "Student ID must be at least 3 characters"
    
    if len(student_id) > 20:
        return False, "Student ID must be less than 20 characters"
    
    # Allow alphanumeric and common separators
    if not re.match(r'^[A-Za-z0-9_-]+$', student_id):
        return False, "Student ID can only contain letters, numbers, hyphens, and underscores"
    
    return True, None


def validate_subject(subject: str, allowed_subjects: list[str]) -> tuple[bool, Optional[str]]:
    """
    Validate subject name.
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not subject:
        return False, "Subject cannot be empty"
    
    if subject not in allowed_subjects:
        return False, f"Subject must be one of: {', '.join(allowed_subjects)}"
    
    return True, None
