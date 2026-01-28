"""Configuration settings for SecureAttend."""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Data directory
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Keys directory
KEYS_DIR = DATA_DIR / "keys"
KEYS_DIR.mkdir(parents=True, exist_ok=True)

# Default subjects
DEFAULT_SUBJECTS = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "Computer Science",
    "English",
    "History",
    "Geography",
    "Economics",
    "Physical Education"
]

# Application settings
APP_NAME = "SecureAttend"
APP_VERSION = "1.0.0"
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

# QR Code settings
QR_VERSION = 1
QR_ERROR_CORRECTION = "L"  # L, M, Q, H
QR_BOX_SIZE = 10
QR_BORDER = 4

# Cryptographic settings
RSA_KEY_SIZE = 2048
RSA_PUBLIC_EXPONENT = 65537
