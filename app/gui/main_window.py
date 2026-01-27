from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import sys


def run_app() -> None:
    """Temporary placeholder GUI entry point."""
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("SecureAttend")
    label = QLabel("SecureAttend GUI will be implemented here.")
    window.setCentralWidget(label)
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())

