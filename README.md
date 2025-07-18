🛒 ShopperSmart Backend API
This is a FastAPI backend for ShopperSmart, an e-commerce system designed to:
✅ Manage customer, product, and transaction data
✅ Prepare structured datasets for building ML-powered product recommendation systems

📦 Features
RESTful API for CRUD operations:

Customers

Products

Transactions

SQLAlchemy ORM with SQLite (easily swappable for PostgreSQL/MySQL)

Swagger UI for API testing

Ready for integration with machine learning models:

Collaborative filtering

Content-based recommendations

Demographic analysis

🚀 Getting Started
🖥 Requirements
Python 3.8+

FastAPI, SQLAlchemy, Uvicorn

📂 Folder Structure
css
Copy
Edit
shopsmart_app/
├── models/

├── routes/

├── database.py

├── main.py

└── requirements.txt


▶️ Run Locally
bash
Copy
Edit
# Clone the repository
git clone https://github.com/Niraj13-py/Prac.git
cd shopsmart_app

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs for Swagger U
