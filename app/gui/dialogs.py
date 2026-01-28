"""Dialog widgets for the GUI."""

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class QRDataDialog(QDialog):
    """Dialog to display QR code data as text."""
    
    def __init__(self, qr_data: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QR Code Data")
        self.setMinimumSize(500, 300)
        self.init_ui(qr_data)
    
    def init_ui(self, qr_data: str):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        label = QLabel("QR Code Data (JSON):")
        label.setFont(QFont("", 10, QFont.Bold))
        layout.addWidget(label)
        
        text_edit = QTextEdit()
        text_edit.setPlainText(qr_data)
        text_edit.setReadOnly(True)
        text_edit.setFont(QFont("Courier", 9))
        layout.addWidget(text_edit)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn)
        
        self.setLayout(layout)
