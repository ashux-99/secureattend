"""Generate PKI-signed QR codes for attendance."""

import qrcode
from qrcode.image.pil import PilImage
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime
import json
import base64
from app.crypto.keys import KeyManager


def generate_signed_qr(student_id: str, subject: str, key_manager: KeyManager = None) -> tuple[str, PilImage]:
    """
    Generate a PKI-signed QR code for attendance.
    
    Returns:
        tuple: (QR data string, QR code image)
    """
    if key_manager is None:
        key_manager = KeyManager()
    
    # Create attendance data
    timestamp = datetime.now().isoformat()
    data = {
        "student_id": student_id,
        "subject": subject,
        "timestamp": timestamp
    }
    
    # Serialize data
    data_json = json.dumps(data, sort_keys=True)
    data_bytes = data_json.encode('utf-8')
    
    # Sign the data with private key
    private_key = key_manager.get_private_key()
    signature = private_key.sign(
        data_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    # Encode signature
    signature_b64 = base64.b64encode(signature).decode('utf-8')
    
    # Create QR payload
    qr_payload = {
        "data": data,
        "signature": signature_b64
    }
    
    qr_data = json.dumps(qr_payload)
    
    # Generate QR code image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    return qr_data, img
