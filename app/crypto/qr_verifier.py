"""Verify PKI-signed QR codes."""

import json
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from app.crypto.keys import KeyManager
from typing import Dict, Tuple, Optional


def verify_qr_signature(qr_data: str, key_manager: KeyManager = None) -> Tuple[bool, Optional[Dict], Optional[str]]:
    """
    Verify a PKI-signed QR code.
    
    Returns:
        tuple: (is_valid, attendance_data, error_message)
    """
    if key_manager is None:
        key_manager = KeyManager()
    
    try:
        # Parse QR data
        payload = json.loads(qr_data)
        
        if "data" not in payload or "signature" not in payload:
            return False, None, "Invalid QR code format: missing data or signature"
        
        attendance_data = payload["data"]
        signature_b64 = payload["signature"]
        
        # Reconstruct the signed data
        data_json = json.dumps(attendance_data, sort_keys=True)
        data_bytes = data_json.encode('utf-8')
        
        # Decode signature
        signature = base64.b64decode(signature_b64)
        
        # Verify signature with public key
        public_key = key_manager.get_public_key()
        
        try:
            public_key.verify(
                signature,
                data_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True, attendance_data, None
        except InvalidSignature:
            return False, attendance_data, "Signature verification failed: QR code may be tampered"
    
    except json.JSONDecodeError:
        return False, None, "Invalid QR code format: not valid JSON"
    except Exception as e:
        return False, None, f"Verification error: {str(e)}"
