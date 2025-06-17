# style.py

def app_stylesheet():
    return """
        QWidget {
            font-family: 'Segoe UI', sans-serif;
            font-size: 14px;
        }
        QLineEdit, QTextEdit, QComboBox {
            padding: 6px;
            border-radius: 6px;
            border: 1px solid #ccc;
        }
        QPushButton {
            background-color: #0066cc;
            color: white;
            padding: 8px 16px;
            border-radius: 6px;
        }
        QPushButton:hover {
            background-color: #0055aa;
        }
        QLabel {
            font-weight: normal;
        }
    """
