"""About dialog for SecureAttend."""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QTextEdit
)
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont, QDesktopServices
from app import __version__


class AboutDialog(QDialog):
    """About dialog showing application information."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About SecureAttend")
        self.setMinimumSize(500, 450)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("SecureAttend")
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Version
        version = QLabel(f"Version {__version__}")
        version_font = QFont()
        version_font.setPointSize(12)
        version.setFont(version_font)
        version.setAlignment(Qt.AlignCenter)
        layout.addWidget(version)
        
        # Description
        description = QTextEdit()
        description.setReadOnly(True)
        description.setMaximumHeight(150)
        description.setHtml("""
        <p style='text-align: center;'>
        <b>PKI-based QR Authentication and Attendance System</b>
        </p>
        <p style='text-align: center;'>
        SecureAttend is a comprehensive attendance management system that uses 
        Public Key Infrastructure (PKI) cryptography to ensure secure and 
        tamper-proof QR code generation and verification.
        </p>
        <p style='text-align: center;'>
        Built with PySide6, Python cryptography, and modern software engineering practices.
        </p>
        """)
        description.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
                padding: 10px;
            }
        """)
        layout.addWidget(description)
        
        # Features
        features_label = QLabel("Key Features:")
        features_label.setFont(QFont("", 11, QFont.Bold))
        layout.addWidget(features_label)
        
        features_text = QTextEdit()
        features_text.setReadOnly(True)
        features_text.setMaximumHeight(120)
        features_text.setPlainText("""
• PKI-based cryptographic QR code signing
• Secure attendance verification
• Support for 10+ subjects
• Modern, minimal white UI
• Cross-platform compatibility
• Docker containerization
• Comprehensive CI/CD workflows
• Automated testing and security scanning
        """)
        features_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: white;
                padding: 10px;
            }
        """)
        layout.addWidget(features_text)
        
        # Links section
        links_layout = QHBoxLayout()
        links_layout.setAlignment(Qt.AlignCenter)
        
        github_btn = QPushButton("GitHub Repository")
        github_btn.clicked.connect(lambda: QDesktopServices.openUrl(
            QUrl("https://github.com/ashux-99/secureattend")
        ))
        github_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        links_layout.addWidget(github_btn)
        
        layout.addLayout(links_layout)
        
        # License
        license_label = QLabel("License: MIT")
        license_label.setAlignment(Qt.AlignCenter)
        license_label.setStyleSheet("color: #666;")
        layout.addWidget(license_label)
        
        # Copyright
        copyright_label = QLabel("© 2025 SecureAttend Team")
        copyright_label.setAlignment(Qt.AlignCenter)
        copyright_label.setStyleSheet("color: #666; font-size: 10px;")
        layout.addWidget(copyright_label)
        
        # Close button
        close_btn = QPushButton("Close")
        close_btn.setMinimumHeight(35)
        close_btn.clicked.connect(self.accept)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(close_btn)
        
        self.setLayout(layout)
