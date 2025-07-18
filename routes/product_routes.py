from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.product import Product

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products/")
def create_product(name: str, description: str, price: float, db: Session = Depends(get_db)):
    new_product = Product(name=name, description=description, price=price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/products/")
def read_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/products/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}")
def update_product(product_id: int, name: str, description: str, price: float, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = name
    product.description = description
    product.price = price
    db.commit()
    return product

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}
