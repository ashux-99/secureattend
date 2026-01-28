# SecureAttend

SecureAttend is a PKI-based QR authentication and attendance demo system.

## Features

- **PKI-Based Security**: Uses RSA cryptography for signing and verifying QR codes
- **Student Portal**: Generate attendance QR codes for 10+ subjects
- **QR Decoder**: Verify and decode attendance QR codes with cryptographic validation
- **Modern GUI**: Minimal white UI built with PySide6
- **Docker Support**: Containerized deployment with Docker and docker-compose
- **CI/CD**: Automated testing and builds with GitHub Actions

## Subjects

The system supports the following subjects:
- Mathematics
- Physics
- Chemistry
- Biology
- Computer Science
- English
- History
- Geography
- Economics
- Physical Education

## Installation

### Requirements

- Python 3.9+
- PySide6
- cryptography
- qrcode
- Pillow

### Setup

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

### Docker

```bash
# Build image
docker build -t secureattend .

# Run container
docker run -it secureattend

# Or use docker-compose
docker-compose up
```

## Architecture

- `app/crypto/`: PKI-based cryptographic functions
- `app/gui/`: PySide6 GUI components
- `app/models/`: Data models
- `tests/`: Unit tests

## Development

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
flake8 .
```

## License

MIT License
