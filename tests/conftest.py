"""Pytest configuration and fixtures."""

import pytest
import tempfile
import shutil
from pathlib import Path
from app.crypto.keys import KeyManager
from app.storage.attendance_db import AttendanceStorage


@pytest.fixture
def temp_dir():
    """Create a temporary directory."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def key_manager(temp_dir):
    """Create a KeyManager with temporary keys."""
    keys_dir = temp_dir / "keys"
    key_manager = KeyManager(keys_dir=str(keys_dir))
    key_manager.generate_key_pair()
    return key_manager


@pytest.fixture
def attendance_storage(temp_dir):
    """Create an AttendanceStorage with temporary database."""
    db_file = temp_dir / "attendance.json"
    return AttendanceStorage(db_file=str(db_file))
