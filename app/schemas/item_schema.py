from pydantic import BaseModel, Field

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100) # "..." means required
    description: str = Field(..., min_length=1, max_length=100)
    