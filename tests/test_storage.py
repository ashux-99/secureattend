"""Tests for storage functionality."""

import pytest
import tempfile
import shutil
from pathlib import Path
from app.storage.attendance_db import AttendanceStorage


@pytest.fixture
def temp_storage():
    """Create a temporary storage instance."""
    temp_dir = tempfile.mkdtemp()
    storage = AttendanceStorage(db_file=str(Path(temp_dir) / "test_attendance.json"))
    yield storage
    shutil.rmtree(temp_dir)


def test_add_record(temp_storage):
    """Test adding attendance records."""
    record = temp_storage.add_record("STU001", "Mathematics")
    
    assert record["student_id"] == "STU001"
    assert record["subject"] == "Mathematics"
    assert "timestamp" in record
    assert record["verified"] is True


def test_get_student_records(temp_storage):
    """Test retrieving student records."""
    temp_storage.add_record("STU001", "Mathematics")
    temp_storage.add_record("STU001", "Physics")
    temp_storage.add_record("STU002", "Mathematics")
    
    records = temp_storage.get_student_records("STU001")
    assert len(records) == 2
    assert all(r["student_id"] == "STU001" for r in records)


def test_get_subject_records(temp_storage):
    """Test retrieving subject records."""
    temp_storage.add_record("STU001", "Mathematics")
    temp_storage.add_record("STU002", "Mathematics")
    temp_storage.add_record("STU001", "Physics")
    
    records = temp_storage.get_subject_records("Mathematics")
    assert len(records) == 2
    assert all(r["subject"] == "Mathematics" for r in records)
