import sys
import shelve
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
)
from PySide6.QtCore import Qt


class KeyValueStoreApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key-Value Store")

        # Create UI elements
        self.key_label = QLabel("Key")
        self.key_entry = QLineEdit()

        self.value_label = QLabel("Value")
        self.value_entry = QLineEdit()

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_key_value)

        self.get_button = QPushButton("Get")
        self.get_button.clicked.connect(self.get_value)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_key)

        self.show_all_button = QPushButton("Show All")
        self.show_all_button.clicked.connect(self.show_all_key_values)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        # Layout setup
        layout = QVBoxLayout()

        key_layout = QHBoxLayout()
        key_layout.addWidget(self.key_label)
        key_layout.addWidget(self.key_entry)

        value_layout = QHBoxLayout()
        value_layout.addWidget(self.value_label)
        value_layout.addWidget(self.value_entry)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.get_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.show_all_button)

        layout.addLayout(key_layout)
        layout.addLayout(value_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

        self.db = shelve.open("db", writeback=True)

    def add_key_value(self):
        key = self.key_entry.text()
        value = self.value_entry.text()
        if key and value:
            self.db[key] = value
            self.db.sync()
            self.output_text.append(f"Added: {key} -> {value}")

    def get_value(self):
        key = self.key_entry.text()
        if key in self.db:
            value = self.db[key]
            self.output_text.append(f"{key} -> {value}")
        else:
            self.output_text.append(f"Key '{key}' not found")

    def delete_key(self):
        key = self.key_entry.text()
        if key in self.db:
            del self.db[key]
            self.db.sync()
            self.output_text.append(f"Deleted: {key}")
        else:
            self.output_text.append(f"Key '{key}' not found")

    def show_all_key_values(self):
        self.output_text.clear()
        if self.db:
            for key, value in self.db.items():
                self.output_text.append(f"{key} -> {value}")
        else:
            self.output_text.append("No key-value pairs found")
