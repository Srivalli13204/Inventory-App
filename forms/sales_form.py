from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox,
    QMessageBox, QFormLayout, QGroupBox
)
from style import app_stylesheet
import sqlite3

class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(app_stylesheet())
        self.setWindowTitle("Sales Entry Form")
        self.setGeometry(100, 100, 500, 500)

        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        group = QGroupBox("New Sales Entry")
        group.setStyleSheet("font-size: 18px; font-weight: bold;")

        form_layout = QFormLayout()

        self.product_dropdown = QComboBox()
        self.customer_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.unit_input = QComboBox()
        self.unit_input.addItems(["Piece", "Kg", "Litre", "Box", "Pack", "Meter"])
        self.rate_input = QLineEdit()
        self.tax_input = QLineEdit()
        self.total_label = QLabel("₹0.00")
        self.total_label.setStyleSheet("font-weight: bold; color: green;")

        form_layout.addRow("Select Product:", self.product_dropdown)
        form_layout.addRow("Customer Name:", self.customer_input)
        form_layout.addRow("Quantity:", self.quantity_input)
        form_layout.addRow("Unit of Measurement:", self.unit_input)
        form_layout.addRow("Rate per Unit:", self.rate_input)
        form_layout.addRow("Tax (%):", self.tax_input)
        form_layout.addRow("Total:", self.total_label)

        group.setLayout(form_layout)
        layout.addWidget(group)

        self.save_button = QPushButton("Save Sale")
        self.save_button.clicked.connect(self.save_sale)
        layout.addWidget(self.save_button)

        self.rate_input.textChanged.connect(self.update_total)
        self.quantity_input.textChanged.connect(self.update_total)
        self.tax_input.textChanged.connect(self.update_total)

    def load_products(self):
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM products")
        self.products = cur.fetchall()
        conn.close()

        self.product_dropdown.clear()
        for pid, name in self.products:
            self.product_dropdown.addItem(name, pid)

    def update_total(self):
        try:
            quantity = float(self.quantity_input.text())
            rate = float(self.rate_input.text())
            tax = float(self.tax_input.text())
            subtotal = quantity * rate
            total = subtotal + (subtotal * tax / 100)
            self.total_label.setText(f"₹{total:.2f}")
        except:
            self.total_label.setText("₹0.00")

    def save_sale(self):
        try:
            product_id = self.product_dropdown.currentData()
            customer = self.customer_input.text()
            quantity = float(self.quantity_input.text())
            unit = self.unit_input.currentText()
            rate = float(self.rate_input.text())
            tax = float(self.tax_input.text())
            total = quantity * rate + (quantity * rate * tax / 100)

            conn = sqlite3.connect("inventory.db")
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO sales (product_id, customer, quantity, unit, rate, total, tax)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (product_id, customer, quantity, unit, rate, total, tax))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Sale recorded successfully.")
            self.clear_form()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not save sale.\n{e}")

    def clear_form(self):
        self.customer_input.clear()
        self.quantity_input.clear()
        self.rate_input.clear()
        self.tax_input.clear()
        self.total_label.setText("₹0.00")
