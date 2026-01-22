from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = [
    {'id':1, 'data':'apple', 'category': 'fruit'},
    {'id':2, 'data':'banana', 'category': 'fruit'},
    {'id':3, 'data':'cherry', 'category': 'fruit'}
]

class ItemCreate(BaseModel):
    data: str
    category: str

@app.post('/items')
def create_item(payload: ItemCreate):
    item = {'id': len(items)+1, **payload.model_dump()}
    items.append(item)
    return item

@app.get('/items')
def get_items():
    return {"data": items}

@app.get('/items/{item_id}')
def get_item_by_id(item_id: int):
    for item in items:
        if item.get('id') == item_id:
            return item
    raise HTTPException(status_code=404, detail='Item not found')
@app.get('/search')
def search_items(q: str):
    results = [item for item in items if q.lower() in item.get('data').lower()]
    if not results:
        raise HTTPException(status_code=404, detail='No items found matching the query')
    return results