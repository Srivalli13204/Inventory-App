from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QToolBar
from PySide6.QtGui import QAction
from forms.login_form import LoginForm
from forms.product_form import ProductForm
from forms.goods_form import GoodsForm
from forms.sales_form import SalesForm
from forms.product_list_form import ProductListForm
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory App")
        self.setGeometry(100, 100, 1000, 600)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.login = LoginForm(self)
        self.stack.addWidget(self.login)

        self.init_toolbar()

    def init_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        # Toolbar buttons (appear after login)
        self.product_action = QAction("Add Product", self)
        self.product_action.triggered.connect(lambda: self.stack.setCurrentIndex(1))

        self.goods_action = QAction("Goods Receiving", self)
        self.goods_action.triggered.connect(lambda: self.stack.setCurrentIndex(2))

        self.sales_action = QAction("Sales Entry", self)
        self.sales_action.triggered.connect(lambda: self.stack.setCurrentIndex(3))

        self.view_action = QAction("View Products", self)
        self.view_action.triggered.connect(lambda: self.stack.setCurrentIndex(4))

        toolbar.addAction(self.product_action)
        toolbar.addAction(self.goods_action)
        toolbar.addAction(self.sales_action)
        toolbar.addAction(self.view_action)

        # Hide buttons initially
        toolbar.setVisible(False)
        self.toolbar = toolbar

    def show_dashboard(self):
        # Show the forms and make toolbar visible
        self.stack.addWidget(ProductForm())        # index 1
        self.stack.addWidget(GoodsForm())          # index 2
        self.stack.addWidget(SalesForm())          # index 3
        self.stack.addWidget(ProductListForm())    # index 4
        self.stack.setCurrentIndex(1)
        self.toolbar.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
