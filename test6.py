from datetime import datetime
from typing import Union, List

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []

app = FastAPI()


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    print(items.get(item_id))
    print(items)
    return update_item_encoded


@app.patch("/items2/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    """
    使用PATCH方法更新指定ID的物品信息。

    此函数通过从items字典中获取已存储的物品数据，将其与传入的Item对象进行部分更新，
    然后将更新后的物品数据保存回items字典中。

    参数:
    - item_id: str, 要更新的物品的唯一标识符。
    - item: Item, 包含要更新的物品信息的对象。

    返回:
    - 更新后的Item对象。
    """
    # 从items字典中获取指定ID的已存储物品数据
    stored_item_data = items[item_id]

    # 将已存储的物品数据转换为Item对象
    stored_item_model = Item(**stored_item_data)

    # 将传入的Item对象转换为字典，并排除未设置的值
    update_data = item.dict(exclude_unset=True)

    # 使用传入数据更新已存储的Item对象
    updated_item = stored_item_model.copy(update=update_data)

    # 将更新后的Item对象转换为JSON格式，并保存到items字典中
    items[item_id] = jsonable_encoder(updated_item)

    # 返回更新后的Item对象
    return updated_item


@app.patch("/items3/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item


@app.patch("/items4/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item