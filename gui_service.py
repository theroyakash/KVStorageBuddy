import sys
import shelve
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt
from KVStoreMainWindow import KeyValueStoreApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyValueStoreApp()
    window.show()
    sys.exit(app.exec())