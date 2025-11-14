from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services import item_service
from app.schemas.item_schema import ItemResponse, ItemCreate

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/")
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db, payload.name, payload.description)

@router.get('/')
def list_items(db: Session = Depends(get_db)):
    return item_service.view_items(db)

@router.get('/{item_id}')
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = item_service.get_item(db, item_id)
    if not item:
        return JSONResponse(status_code=404, content = {
            "status": 404,
            "message": "Item not found"
        })
    return JSONResponse(status_code=200, content={
        "status": 200,
        "message": "Item found",
        "data": ItemResponse.model_validate(item).model_dump()
    })

@router.put('/{item_id}')
def update_item(item_id: int, name: str, description: str, db: Session = Depends(get_db)):
    updated = item_service.update_item(db, item_id, name, description)
    if not updated:
        return JSONResponse(status_code=404, content={
            "status": 404,
            "message": "Item not found"
        })
    return JSONResponse(status_code=200, content={
        "status": 200,
        "message": "Item updated successfully",
        "data": ItemResponse.model_validate(updated).model_dump()
    })

@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted = item_service.delete_item(db, item_id)
    if not deleted:
        return JSONResponse(status_code=404, content={
            "status": 404,
            "message": "Item not found"
        })
    return JSONResponse(status_code=200, content={
        "status": 200,
        "message": "Item deleted successfully",
    })