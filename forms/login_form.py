from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGroupBox, QFormLayout
from style import app_stylesheet
import sqlite3

class LoginForm(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setStyleSheet(app_stylesheet())

        layout = QVBoxLayout(self)
        group = QGroupBox("Operator Login")
        group.setStyleSheet("font-size: 18px; font-weight: bold;")
        form_layout = QFormLayout()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.handle_login)

        self.message = QLabel()

        form_layout.addRow("Username:", self.username_input)
        form_layout.addRow("Password:", self.password_input)
        form_layout.addRow("", login_btn)
        form_layout.addRow("", self.message)

        group.setLayout(form_layout)
        layout.addWidget(group)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cur.fetchone()
        conn.close()

        if result:
            self.main_window.show_dashboard()
        else:
            self.message.setText("Invalid credentials.")
