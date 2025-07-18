from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.customer import Customer

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create customer
@router.post("/customers/")
def create_customer(name: str, email: str, phone_number: str, db: Session = Depends(get_db)):
    new_customer = Customer(name=name, email=email, phone_number=phone_number)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

# Get all customers
@router.get("/customers/")
def read_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

# Get customer by ID
@router.get("/customers/{customer_id}")
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# Update customer
@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, name: str, email: str, phone_number: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer.name = name
    customer.email = email
    customer.phone_number = phone_number
    db.commit()
    return customer

# Delete customer
@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"detail": "Customer deleted"}
