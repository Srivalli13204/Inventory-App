from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit,
    QPushButton, QComboBox, QTextEdit, QFileDialog, QGroupBox, QHBoxLayout
)
from PySide6.QtGui import QPixmap
import sqlite3
from style import app_stylesheet
import os

class ProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setStyleSheet(app_stylesheet())

        layout = QVBoxLayout(self)
        group = QGroupBox("Add New Product")
        group.setStyleSheet("font-size: 18px; font-weight: bold;")

        form_layout = QFormLayout()

        self.barcode_input = QLineEdit()
        self.sku_input = QLineEdit()
        self.category_input = QLineEdit()
        self.subcategory_input = QLineEdit()
        self.name_input = QLineEdit()
        self.description_input = QTextEdit()
        self.tax_input = QLineEdit()
        self.price_input = QLineEdit()
        self.unit_input = QComboBox()
        self.unit_input.addItems(["Piece", "Kg", "Litre", "Box", "Packet"])

        self.image_path = ""
        self.image_label = QLabel("No image selected")
        self.image_label.setFixedHeight(120)
        self.image_label.setStyleSheet("border: 1px solid #ccc;")

        image_btn = QPushButton("Upload Image")
        image_btn.clicked.connect(self.upload_image)

        form_layout.addRow("Barcode:", self.barcode_input)
        form_layout.addRow("SKU ID:", self.sku_input)
        form_layout.addRow("Category:", self.category_input)
        form_layout.addRow("Subcategory:", self.subcategory_input)
        form_layout.addRow("Product Name:", self.name_input)
        form_layout.addRow("Description:", self.description_input)
        form_layout.addRow("Tax (%):", self.tax_input)
        form_layout.addRow("Price:", self.price_input)
        form_layout.addRow("Unit of Measurement:", self.unit_input)
        form_layout.addRow("Product Image:", image_btn)
        form_layout.addRow("", self.image_label)

        group.setLayout(form_layout)
        layout.addWidget(group)

        save_btn = QPushButton("Save Product")
        save_btn.clicked.connect(self.save_product)
        layout.addWidget(save_btn)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Product Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path).scaledToHeight(100)
            self.image_label.setPixmap(pixmap)

    def save_product(self):
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO products (barcode, sku, category, subcategory, name, description, tax, price, unit, image)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.barcode_input.text(),
            self.sku_input.text(),
            self.category_input.text(),
            self.subcategory_input.text(),
            self.name_input.text(),
            self.description_input.toPlainText(),
            self.tax_input.text(),
            self.price_input.text(),
            self.unit_input.currentText(),
            self.image_path
        ))
        conn.commit()
        conn.close()
        self.clear_form()

    def clear_form(self):
        self.barcode_input.clear()
        self.sku_input.clear()
        self.category_input.clear()
        self.subcategory_input.clear()
        self.name_input.clear()
        self.description_input.clear()
        self.tax_input.clear()
        self.price_input.clear()
        self.image_label.clear()
        self.image_label.setText("No image selected")