"""Tests for cryptographic functions."""

import pytest
from app.crypto.keys import KeyManager
from app.crypto.qr_generator import generate_signed_qr
from app.crypto.qr_verifier import verify_qr_signature
import tempfile
import shutil


@pytest.fixture
def temp_key_dir():
    """Create a temporary directory for keys."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


def test_key_generation(temp_key_dir):
    """Test RSA key pair generation."""
    key_manager = KeyManager(keys_dir=temp_key_dir)
    key_manager.generate_key_pair()
    
    private_key = key_manager.get_private_key()
    public_key = key_manager.get_public_key()
    
    assert private_key is not None
    assert public_key is not None


def test_qr_generation_and_verification(temp_key_dir):
    """Test QR code generation and verification."""
    key_manager = KeyManager(keys_dir=temp_key_dir)
    
    student_id = "STU001"
    subject = "Mathematics"
    
    # Generate QR code
    qr_data, qr_image = generate_signed_qr(student_id, subject, key_manager)
    
    assert qr_data is not None
    assert qr_image is not None
    
    # Verify QR code
    is_valid, attendance_data, error = verify_qr_signature(qr_data, key_manager)
    
    assert is_valid is True
    assert attendance_data is not None
    assert attendance_data["student_id"] == student_id
    assert attendance_data["subject"] == subject
    assert error is None


def test_qr_verification_fails_with_tampered_data(temp_key_dir):
    """Test that tampered QR data fails verification."""
    key_manager = KeyManager(keys_dir=temp_key_dir)
    
    student_id = "STU001"
    subject = "Mathematics"
    
    # Generate valid QR code
    qr_data, _ = generate_signed_qr(student_id, subject, key_manager)
    
    # Tamper with the data
    tampered_data = qr_data.replace("STU001", "STU999")
    
    # Verification should fail
    is_valid, _, error = verify_qr_signature(tampered_data, key_manager)
    
    assert is_valid is False
    assert error is not None
