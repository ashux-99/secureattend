"""Reusable QR code display widget."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PIL.ImageQt import ImageQt


class QRCodeWidget(QWidget):
    """Widget for displaying QR code images."""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.qr_label = QLabel("QR Code will appear here")
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setMinimumHeight(250)
        self.qr_label.setStyleSheet("""
            QLabel {
                border: 2px dashed #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
        """)
        
        layout.addWidget(self.qr_label)
        self.setLayout(layout)
    
    def set_qr_image(self, qr_image):
        """Set the QR code image to display."""
        if qr_image:
            qimg = ImageQt(qr_image)
            pixmap = QPixmap.fromImage(qimg)
            scaled_pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.qr_label.setPixmap(scaled_pixmap)
            self.qr_label.setStyleSheet("""
                QLabel {
                    border: 2px solid #4CAF50;
                    border-radius: 5px;
                    background-color: #f0f8f0;
                    padding: 10px;
                }
            """)
        else:
            self.qr_label.clear()
            self.qr_label.setText("QR Code will appear here")
            self.qr_label.setStyleSheet("""
                QLabel {
                    border: 2px dashed #ccc;
                    border-radius: 5px;
                    background-color: #f9f9f9;
                }
            """)
