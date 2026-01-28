from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QLineEdit, QTextEdit, QComboBox, QMessageBox, QHeaderView, QMenuBar, QMenu
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap, QAction
import sys
from datetime import datetime
from app.crypto.qr_generator import generate_signed_qr
from app.crypto.qr_verifier import verify_qr_signature
from app.crypto.keys import KeyManager
from app.gui.about_dialog import AboutDialog


class StudentViewTab(QWidget):
    """Tab for students to view their attendance and generate QR codes."""
    
    def __init__(self):
        super().__init__()
        self.key_manager = KeyManager()
        self.subjects = [
            "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science",
            "English", "History", "Geography", "Economics", "Physical Education"
        ]
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("Student Attendance Portal")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Student ID input
        id_layout = QHBoxLayout()
        id_label = QLabel("Student ID:")
        id_label.setMinimumWidth(100)
        self.student_id_input = QLineEdit()
        self.student_id_input.setPlaceholderText("Enter your student ID")
        self.student_id_input.setMinimumHeight(35)
        id_layout.addWidget(id_label)
        id_layout.addWidget(self.student_id_input)
        layout.addLayout(id_layout)
        
        # Subject selection
        subject_layout = QHBoxLayout()
        subject_label = QLabel("Subject:")
        subject_label.setMinimumWidth(100)
        self.subject_combo = QComboBox()
        self.subject_combo.addItems(self.subjects)
        self.subject_combo.setMinimumHeight(35)
        subject_layout.addWidget(subject_label)
        subject_layout.addWidget(self.subject_combo)
        layout.addLayout(subject_layout)
        
        # Generate QR button
        self.generate_btn = QPushButton("Generate QR Code")
        self.generate_btn.setMinimumHeight(40)
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.generate_btn.clicked.connect(self.generate_qr)
        layout.addWidget(self.generate_btn)
        
        # QR Code display area
        self.qr_display = QLabel("QR Code will appear here")
        self.qr_display.setAlignment(Qt.AlignCenter)
        self.qr_display.setMinimumHeight(250)
        self.qr_display.setStyleSheet("""
            QLabel {
                border: 2px dashed #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
        """)
        layout.addWidget(self.qr_display)
        
        # Attendance table
        table_label = QLabel("Your Attendance Record")
        table_label.setFont(title_font)
        table_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(table_label)
        
        self.attendance_table = QTableWidget()
        self.attendance_table.setColumnCount(3)
        self.attendance_table.setHorizontalHeaderLabels(["Subject", "Date", "Status"])
        self.attendance_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.attendance_table.setAlternatingRowColors(True)
        self.attendance_table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                border-radius: 5px;
                gridline-color: #e0e0e0;
            }
            QHeaderView::section {
                background-color: #f5f5f5;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.attendance_table)
        
        self.setLayout(layout)
    
    def generate_qr(self):
        student_id = self.student_id_input.text().strip()
        subject = self.subject_combo.currentText()
        
        if not student_id:
            QMessageBox.warning(self, "Input Required", "Please enter your Student ID.")
            return
        
        try:
            # Generate PKI-signed QR code
            qr_data, qr_image = generate_signed_qr(student_id, subject, self.key_manager)
            
            # Convert PIL image to QPixmap
            from PIL.ImageQt import ImageQt
            qimg = ImageQt(qr_image)
            pixmap = QPixmap.fromImage(qimg)
            scaled_pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            self.qr_display.setPixmap(scaled_pixmap)
            self.qr_display.setStyleSheet("""
                QLabel {
                    border: 2px solid #4CAF50;
                    border-radius: 5px;
                    background-color: #f0f8f0;
                    padding: 10px;
                }
            """)
            
            # Update attendance table
            row = self.attendance_table.rowCount()
            self.attendance_table.insertRow(row)
            self.attendance_table.setItem(row, 0, QTableWidgetItem(subject))
            self.attendance_table.setItem(row, 1, QTableWidgetItem(datetime.now().strftime("%Y-%m-%d %H:%M")))
            self.attendance_table.setItem(row, 2, QTableWidgetItem("Present"))
            
            QMessageBox.information(self, "Success", f"PKI-signed QR code generated for {subject}!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate QR code: {str(e)}")


class QRDecoderTab(QWidget):
    """Tab for teachers/admins to scan and decode QR codes."""
    
    def __init__(self):
        super().__init__()
        self.key_manager = KeyManager()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title = QLabel("QR Code Decoder")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Instructions
        instructions = QLabel("Paste or enter QR code data below to decode and verify attendance:")
        instructions.setWordWrap(True)
        instructions.setStyleSheet("color: #666; padding: 10px;")
        layout.addWidget(instructions)
        
        # QR data input
        input_label = QLabel("QR Code Data:")
        input_label.setFont(QFont("", 10, QFont.Bold))
        layout.addWidget(input_label)
        
        self.qr_input = QTextEdit()
        self.qr_input.setPlaceholderText("Paste QR code data here (JSON format)...")
        self.qr_input.setMinimumHeight(100)
        self.qr_input.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        layout.addWidget(self.qr_input)
        
        # Decode button
        self.decode_btn = QPushButton("Decode & Verify")
        self.decode_btn.setMinimumHeight(40)
        self.decode_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
            QPushButton:pressed {
                background-color: #0a6bc2;
            }
        """)
        self.decode_btn.clicked.connect(self.decode_qr)
        layout.addWidget(self.decode_btn)
        
        # Results display
        results_label = QLabel("Decoded Information:")
        results_label.setFont(QFont("", 10, QFont.Bold))
        layout.addWidget(results_label)
        
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        self.results_display.setMinimumHeight(200)
        self.results_display.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                background-color: #f9f9f9;
            }
        """)
        layout.addWidget(self.results_display)
        
        # Verification status
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setMinimumHeight(50)
        self.status_label.setStyleSheet("""
            QLabel {
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
    
    def decode_qr(self):
        qr_data = self.qr_input.toPlainText().strip()
        
        if not qr_data:
            QMessageBox.warning(self, "Input Required", "Please enter QR code data to decode.")
            return
        
        # Verify PKI signature
        is_valid, attendance_data, error_msg = verify_qr_signature(qr_data, self.key_manager)
        
        if is_valid and attendance_data:
            result_text = f"""Student ID: {attendance_data.get('student_id', 'Unknown')}
Subject: {attendance_data.get('subject', 'Unknown')}
Timestamp: {attendance_data.get('timestamp', 'Unknown')}

Verification Status: ✓ Valid PKI Signature
The QR code has been cryptographically verified and is authentic.
"""
            self.results_display.setText(result_text)
            self.status_label.setText("✓ QR Code Verified Successfully")
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #d4edda;
                    color: #155724;
                    border: 1px solid #c3e6cb;
                    border-radius: 5px;
                    padding: 10px;
                    font-size: 14px;
                    font-weight: bold;
                }
            """)
        else:
            error_display = f"Verification Failed\n\nError: {error_msg or 'Unknown error'}"
            if attendance_data:
                error_display += f"\n\nData found:\nStudent ID: {attendance_data.get('student_id', 'Unknown')}\nSubject: {attendance_data.get('subject', 'Unknown')}"
            self.results_display.setText(error_display)
            self.status_label.setText("✗ QR Code Verification Failed")
            self.status_label.setStyleSheet("""
                QLabel {
                    background-color: #f8d7da;
                    color: #721c24;
                    border: 1px solid #f5c6cb;
                    border-radius: 5px;
                    padding: 10px;
                    font-size: 14px;
                    font-weight: bold;
                }
            """)


def run_app() -> None:
    """Main application entry point with minimal white UI."""
    app = QApplication(sys.argv)
    
    # Set application-wide style for minimal white theme
    app.setStyle("Fusion")
    app.setStyleSheet("""
        QMainWindow {
            background-color: white;
        }
        QWidget {
            background-color: white;
            color: #333;
        }
        QTabWidget::pane {
            border: 1px solid #ddd;
            background-color: white;
        }
        QTabBar::tab {
            background-color: #f5f5f5;
            color: #666;
            padding: 10px 20px;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
            margin-right: 2px;
        }
        QTabBar::tab:selected {
            background-color: white;
            color: #2196F3;
            border-bottom: 2px solid #2196F3;
        }
        QTabBar::tab:hover {
            background-color: #fafafa;
        }
    """)
    
    window = QMainWindow()
    window.setWindowTitle("SecureAttend - PKI-Based Attendance System")
    window.setMinimumSize(900, 700)
    
    # Create menu bar
    menubar = window.menuBar()
    
    # Help menu
    help_menu = menubar.addMenu("Help")
    about_action = QAction("About SecureAttend", window)
    about_action.triggered.connect(lambda: AboutDialog(window).exec())
    help_menu.addAction(about_action)
    
    # Create tab widget
    tabs = QTabWidget()
    tabs.addTab(StudentViewTab(), "Student View")
    tabs.addTab(QRDecoderTab(), "QR Decoder")
    
    window.setCentralWidget(tabs)
    window.show()
    
    sys.exit(app.exec())
