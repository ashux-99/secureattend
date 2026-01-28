"""Custom exceptions for crypto module."""


class CryptoError(Exception):
    """Base exception for crypto operations."""
    pass


class KeyGenerationError(CryptoError):
    """Raised when key generation fails."""
    pass


class SignatureError(CryptoError):
    """Raised when signature operations fail."""
    pass


class VerificationError(CryptoError):
    """Raised when verification fails."""
    pass
