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

## Screenshots

### Login Screen
![Login Form](https://github.com/user-attachments/assets/ef621216-377d-4277-96d2-9176c0e0a999)

### Product Form
![Product Form](https://github.com/user-attachments/assets/4723307a-8841-4217-b326-04ff08ad09e3)

### Goods Receiving Form
![Goods Receiving Form](https://github.com/user-attachments/assets/9eb58040-ef25-44af-a791-0e4af2ecd3d5)

### Sales Form
![Sales Form](https://github.com/user-attachments/assets/ff37a79c-6d95-4455-a09f-85917b6e70fa)

### Products List 
![Products List](https://github.com/user-attachments/assets/3798cdc7-c25e-436b-8570-147c2bd7887a)

## Demo Video
A short walkthrough video of the application's usage:

👉 [Click Here](https://drive.google.com/file/d/13ZwJ0PG0dWXeS6VAmAk3jnaHayoUAqCI/view?usp=sharing)

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
