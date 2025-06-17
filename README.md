# Inventory Management System – PySide6

This is a desktop-based inventory management system developed using **Python** and **PySide6**. The system is designed to manage products, goods received, and sales, all stored in a local **SQLite** database. The app includes login for operators, forms for product management, and a user-friendly interface.

---

## Features

### 1. Operator Login
- Secure login for operators.
- Two default operator accounts:
  
| Username | Password |
|----------|----------|
|  admin1  | admin123 |
|  admin2  | admin234 |

### 2. Goods Receiving Form
- Enter product details such as:
  - Supplier Name
  - Quantity
  - Unit of Measurement
  - Rate/Unit
  - Total Amount
  - Tax

### 3. Sales Form
- Record sales with:
  - Product Name
  - Customer Name
  - Quantity
  - Unit
  - Rate
  - Total
  - Tax

### 4. Product Master List
- Add/view product details:
  - Barcode, SKU ID
  - Category & Subcategory
  - Product Image
  - Product Name & Description
  - Tax, Price, Default Unit

---

## Database

- **SQLite** used for lightweight local storage.
- Automatically creates tables on first run if they don’t exist.

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Srivalli13204/Inventory-App.git
cd Inventory-App
```

### 2. Create Virtual Environment

```bash
python -m venv App
App\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python main.py
```
---

## Download Executable
👉 [Click here to download the windows EXE](https://drive.google.com/file/d/1H9KBt6P8Px9euE9y02ASxobkz55rip09/view?usp=sharing)

---

## Demo Video
A short walkthrough video of the application's usage:

👉()

---

## Project Structure
INVENTORYAPP/

├── main.py

├── setup_db.py

├── inventory.db

├── forms/

│   └── login_form.py

│   └── product_form.py

|   └── goods_form.py

│   └── sales_form.py

│   └── product_list_form.py

├── assets/

│   └── product_images

├── README.md

└── requirements.txt

---

### Building the Executable

To build an .exe for windows using PyInstaller
```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

---

### Author
Developed by Pichika Parimala Durga Srivalli as part of an assignment
