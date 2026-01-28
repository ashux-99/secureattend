"""Key management for PKI-based attendance system."""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from pathlib import Path
import os


class KeyManager:
    """Manages RSA key pairs for PKI operations."""
    
    def __init__(self, keys_dir: str = "data/keys"):
        self.keys_dir = Path(keys_dir)
        self.keys_dir.mkdir(parents=True, exist_ok=True)
        self.private_key_path = self.keys_dir / "private_key.pem"
        self.public_key_path = self.keys_dir / "public_key.pem"
    
    def generate_key_pair(self, key_size: int = 2048) -> None:
        """Generate a new RSA key pair."""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        
        # Save private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(self.private_key_path, 'wb') as f:
            f.write(private_pem)
        
        # Save public key
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(self.public_key_path, 'wb') as f:
            f.write(public_pem)
    
    def get_private_key(self):
        """Load the private key."""
        if not self.private_key_path.exists():
            self.generate_key_pair()
        
        with open(self.private_key_path, 'rb') as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )
        return private_key
    
    def get_public_key(self):
        """Load the public key."""
        if not self.public_key_path.exists():
            self.generate_key_pair()
        
        with open(self.public_key_path, 'rb') as f:
            public_key = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )
        return public_key
