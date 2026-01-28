"""Style definitions for the GUI."""

MINIMAL_WHITE_STYLE = """
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
QPushButton {
    border-radius: 5px;
    font-size: 14px;
    font-weight: bold;
    padding: 8px 16px;
}
QLineEdit, QTextEdit, QComboBox {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 5px;
}
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
"""

SUCCESS_BUTTON_STYLE = """
QPushButton {
    background-color: #4CAF50;
    color: white;
    border: none;
}
QPushButton:hover {
    background-color: #45a049;
}
QPushButton:pressed {
    background-color: #3d8b40;
}
"""

PRIMARY_BUTTON_STYLE = """
QPushButton {
    background-color: #2196F3;
    color: white;
    border: none;
}
QPushButton:hover {
    background-color: #0b7dda;
}
QPushButton:pressed {
    background-color: #0a6bc2;
}
"""

SUCCESS_LABEL_STYLE = """
QLabel {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
    border-radius: 5px;
    padding: 10px;
    font-size: 14px;
    font-weight: bold;
}
"""

ERROR_LABEL_STYLE = """
QLabel {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    border-radius: 5px;
    padding: 10px;
    font-size: 14px;
    font-weight: bold;
}
"""
