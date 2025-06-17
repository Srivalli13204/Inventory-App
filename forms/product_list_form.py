from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QGroupBox
)
from style import app_stylesheet
import sqlite3

class ProductListForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master List")
        self.setGeometry(100, 100, 900, 500)
        self.setStyleSheet(app_stylesheet())

        layout = QVBoxLayout(self)

        group = QGroupBox("All Registered Products")
        group.setStyleSheet("font-size: 18px; font-weight: bold;")
        group_layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 4px;
            }
            QHeaderView::section {
                background-color: #0066cc;
                font-weight: bold;
                padding: 6px;
                border: 1px solid #ddd;
            }
            QTableWidget::item {
            border: 1px solid white;
            padding: 6px;
            }
        """)

        group_layout.addWidget(self.table)
        group.setLayout(group_layout)

        layout.addWidget(group)

        self.load_products()

    def load_products(self):
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("""
            SELECT barcode, sku, name, category, subcategory, description, tax, price, unit
            FROM products
        """)
        rows = cur.fetchall()
        conn.close()

        headers = ["Barcode", "SKU ID", "Name", "Category", "Subcategory", "Description", "Tax (%)", "Price", "Unit"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(rows))

        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        self.table.resizeColumnsToContents()
