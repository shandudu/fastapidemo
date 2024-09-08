from typing import Union, List
from fastapi import FastAPI, Query
from pydantic import BaseModel
from pydantic.v1 import Required

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict


# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# @app.get("/get/items/")
# async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50, pattern="^fixedquery$")):
#     results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


@app.get("/get/items/")
async def read_items(q: Union[str, None] = Query(default='fixedquery', min_length=3, max_length=50)):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/get/items2/")
async def read_items(q: str = Query(min_length=3)):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/get/items3/")
async def read_items(q: str = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/get/items4/")
async def read_items(q: Union[str, None] = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/get/items5/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/get/items6/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items