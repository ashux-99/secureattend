"""Utility functions for key management."""

from pathlib import Path
from app.crypto.keys import KeyManager
from app.config import KEYS_DIR


def ensure_keys_exist() -> KeyManager:
    """
    Ensure that RSA keys exist, generating them if necessary.
    
    Returns:
        KeyManager instance with keys ready to use
    """
    key_manager = KeyManager(keys_dir=str(KEYS_DIR))
    
    # Generate keys if they don't exist
    if not Path(KEYS_DIR / "private_key.pem").exists():
        key_manager.generate_key_pair()
    
    return key_manager
