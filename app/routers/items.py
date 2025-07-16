from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


# Example: curl http://localhost:8000/items/1
# Example: curl "http://localhost:8000/items/1?q=somequery"
@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# Example: curl -X PUT -H "Content-Type: application/json" -d '{"name": "Foo", "price": 12.3, "is_offer": true}' http://localhost:8000/items/1
@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}
