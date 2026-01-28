"""Script to generate RSA key pairs."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.crypto.keys import KeyManager
from app.config import KEYS_DIR


def main():
    """Generate RSA key pair."""
    print("Generating RSA key pair...")
    key_manager = KeyManager(keys_dir=str(KEYS_DIR))
    key_manager.generate_key_pair()
    print(f"Keys generated successfully in {KEYS_DIR}")
    print(f"Private key: {KEYS_DIR / 'private_key.pem'}")
    print(f"Public key: {KEYS_DIR / 'public_key.pem'}")


if __name__ == "__main__":
    main()
