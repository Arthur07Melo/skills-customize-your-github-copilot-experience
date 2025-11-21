from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="FastAPI - Assignment Example")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


# simple in-memory store
items: Dict[int, Item] = {}
next_id = 1


@app.get("/items")
def list_items():
    return [{"id": i, **items[i].dict()} for i in items]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items[item_id].dict()}


@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    items[next_id] = item
    response = {"id": next_id, **item.dict()}
    next_id += 1
    return response


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter_code:app", host="127.0.0.1", port=8000, reload=True)
