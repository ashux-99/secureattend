"""Tests for validation functions."""

import pytest
from app.utils.validators import validate_student_id, validate_subject


def test_validate_student_id_valid():
    """Test valid student IDs."""
    valid_ids = ["STU001", "student123", "ABC-123", "test_student"]
    for student_id in valid_ids:
        is_valid, error = validate_student_id(student_id)
        assert is_valid is True
        assert error is None


def test_validate_student_id_empty():
    """Test empty student ID."""
    is_valid, error = validate_student_id("")
    assert is_valid is False
    assert error is not None


def test_validate_student_id_too_short():
    """Test student ID that's too short."""
    is_valid, error = validate_student_id("AB")
    assert is_valid is False
    assert "at least 3" in error.lower()


def test_validate_student_id_invalid_chars():
    """Test student ID with invalid characters."""
    is_valid, error = validate_student_id("STU@123")
    assert is_valid is False
    assert error is not None


def test_validate_subject_valid():
    """Test valid subjects."""
    allowed = ["Mathematics", "Physics", "Chemistry"]
    for subject in allowed:
        is_valid, error = validate_subject(subject, allowed)
        assert is_valid is True
        assert error is None


def test_validate_subject_invalid():
    """Test invalid subject."""
    allowed = ["Mathematics", "Physics"]
    is_valid, error = validate_subject("InvalidSubject", allowed)
    assert is_valid is False
    assert error is not None
