from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.transaction import Transaction

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transactions/")
def create_transaction(customer_id: int, product_id: int, db: Session = Depends(get_db)):
    new_transaction = Transaction(customer_id=customer_id, product_id=product_id)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@router.get("/transactions/")
def read_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()

@router.get("/transactions/{transaction_id}")
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction
