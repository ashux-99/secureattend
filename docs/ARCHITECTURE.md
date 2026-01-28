# Architecture

## Overview

SecureAttend is built with a modular architecture separating concerns into distinct packages.

## Package Structure

### `app/crypto/`
PKI-based cryptographic operations:
- Key generation and management
- QR code signing
- Signature verification

### `app/gui/`
PySide6-based user interface:
- Main window with tabs
- Student view for QR generation
- QR decoder for verification
- Reusable components

### `app/models/`
Data models:
- Attendance records
- Data structures

### `app/storage/`
Data persistence:
- File-based storage
- Export functionality

### `app/utils/`
Utility functions:
- Validation
- Formatting
- Helpers

## Data Flow

1. Student generates QR code → PKI signature applied
2. QR code scanned → Signature verified
3. Valid records stored → File-based persistence

## Security

- RSA 2048-bit keys
- PKI signature verification
- Secure key storage
