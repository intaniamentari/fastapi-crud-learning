from sqlalchemy.orm import Session
from app.models.item_model import Item

# create
def create_item(db: Session, name: str, description: str):
    new_item = Item(name= name, description = description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# read
def view_items(db: Session):
    return db.query(Item).all()

# get items by id
def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

# update
def update_item(db: Session, item_id: int, name: str, description:str):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        item.name = name
        item.description = description
        db.commit()
        db.refresh(item)
    return item

# delete
def delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
