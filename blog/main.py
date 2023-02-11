from enum import Enum
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import Optional, Literal, Union
from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status
from uuid import UUID
from datetime import datetime, time, timedelta

app = FastAPI()

# @app.get('/')
# async def base_get_route():
#     return {'message': 'Hello world'}


# @app.post('/')
# async def post():
#     return {'message': 'hellow from the post route'}


# @app.put('/')
# async def put():
#     return {'message': 'Hello from the put route'}


# @app.get('/users')
# async def list_users():
#     return {'message': 'list users route'}


# @app.get('/users/me')
# async def get_current_user():
#     return {'message': 'this is the current user'}


# @app.get('/users/{user_id}')
# async def get_user(user_id: str):
#     return {'item_id': user_id}


# class FoodEnum(str, Enum):
#     fruits = 'fruits'
#     vegetables = 'vegetables'
#     dairy = 'dairy'


# @app.get('/foods/{food_name}')
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {'food_name': food_name, 'message': 'You are healthy'}
#     if food_name.value == 'fruits':
#         return {'food_name': food_name, 'message': 'You are still healthy, but like sweet things'}
#     return {"food_name": food_name, 'message': 'I like chocolate milk'}


# fake_items_db = [
#     {'items_name': 'Foo'},
#     {'items_name': 'Bar'},
#     {'items_name': 'Baz'}
#     ]

# @app.get('/items')
# async def list_items(skip: int = 0, limit: int = 10):   # Query parameters are added to the path operation function as a parameter but not added to the path decorator
#     return fake_items_db[skip: skip + limit]


# @app.get('/items/{item_id}')
# async def get_item(item_id: str, sample_query_params: str, q: str | None = None, short: bool = False): # To declare query parametr q as optional in Python 3.10
#     item = {'item_id': item_id, 'sample_query_param': sample_query_params}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update(
#             {
#                 'description': "ShiloMed will be great enti moda aa monna"
#             }
#         )
#     return item


# @app.get('/users/{user_id}/items/{item_id}')
# async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {'item_id': item_id, 'owner_id': user_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update(
#             {
#                 'description': "ShiloMed will be great enti moda aa monna"
#             }
#         )
#         return item


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float | None = None   # for Python 3.10 and above


# @app.post('/items')
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({'price_with_tax': price_with_tax})
#     return item_dict


# @app.put('/items/{item_id')
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result =  {'item_id': item_id, **item.dict()}
#     if q:
#         result.update({'q': q})
#     return result


# @app.get("/read_items")
# async def read_items(
#     q: str
#     | None = Query(
#         None,
#         min_length= 3,
#         max_length= 10,
#         title="Sample Query String",
#         description="This is a sample query string",
#         alias="item-query",   # this changes the variable name from q to item-query since python does not accept the minus nomenclature which is mostly the case for backend apps.
#     )
# ):
#     #q: list[str] |None  = Query(["foo", "bar"])):
#     # q:str = Query(..., min_length=3, max_length=10)):
#     # the elipsis (...) makes the Query parameter a required field.
#     # q:str | None = Query(None)):
#     # #Query('FixedQuery', min_length = 3, max_length=10)):
#     results = {"items": [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get('/items_hidden')
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hiddens_query": "Not found"}


# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#             *, # this makes the rest of the arguments key word arguments, so optional parameters can come before non-optional ones
#             item_id: int = Path(..., title="The ID of the item to get", ge=10, le=100),
#             size: float = Query(..., gt=0, lt=7.75),
#             q: str = "hello",
#         ):
#     results = {"item_id": item_id, "size": size}
#     if q:
#         results.update({'q': q})
#     return results


# Part 7 - Body -> Multiple Parameters


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class User(BaseModel):
#     username: str
#     password: str | None = None


# # class Importance(BaseModel):
# #     importance: int


# @app.put("/items/{item_id}")
# async def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
#         q: str | None = None,
#         item: Item | None = None,
#         # item: Item = Body(..., embed=True) = this will make the entire body be one key pair value "item": {"name": "string", "des...":...and so on}
#         user: User,
#         # importance: Importance
#         importance: int = Body(...)
#     ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({'q': q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     if importance:
#         results.update({'importance': importance})
#     print(results)
#     return results


# Part 8 -> Body - Fields

# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero.")
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {'item_id': item_id, "item": item}
#     return results


# Part 9 -> Body - Nested Models

# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     image: Image | None = None


# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]

# @app.put("/items/{item_id}")
# async def update_item(item_id:int, item:Item):
#     results = {"item_id": item_id, 'item': item}
#     return results


# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer


# @app.post("/images/multiple")
# async def create_multiple_images(images: list[Image]):
#     return images


# @app.post("/blah")
# async def create_some_blahs(blahs: dict[int, float]):
#     return blahs


# Part 10 -> - Declare Request Example Data

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     # name: str = Field(..., example="Foo")
#     # description: str | None = Field(None, example="A very nice Item")
#     # price: float = Field(..., example=16.25)
#     # tax: float | None = Field(None, example=1.67)

#     # class Config:
#     #     schema_extra = {
#     #         "example": {
#     #             "name": "Foo",
#     #             "description": "A very nice Item",
#     #             "price": 16.25,
#     #             "tax": 1.67
#     #         }
#     #     }   # class Config give a default/example value. alternate way is using the Fields like done above

#     # the third way to populate the body request with examples is by using the Body class like seen below

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Item=  Body(
#         ...,
#         examples={
#             "normal":{
#                 "summary": "A normal example",
#                 "description": "A __normal__ item works correctly",
#                 "value":{
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 1.67,
#                     "tax": 1.67
#                 }
#             },
#             "converted":{
#                 "summary": "An example with converted data",
#                 "description": "FastAPI can convert price stirngs to integer",
#                 "value": {"name": "Bar", "price": "16.25"},
#             },
#             "invalid":{
#                 "summary": "Invalid data is rejected with an error",
#                 "description": "Hello Youtubers",
#                 "value": {"name": "Baz", "price": "sixteen point two five"},
#             },
#         },
#     )
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


# Part 11 -> Extra Data Types

# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_date: datetime | None = Body(None),
#     end_date: datetime | None = Body(None),
#     repeate_at: time | None = Body(None),
#     process_after: timedelta | None = Body(None),
# ):
#     start_process = start_date + process_after
#     duration = end_date - start_process
#     return {
#         "item_id": item_id,
#         "start_date": start_date,
#         "end_date": end_date,
#         "repeat_at": repeate_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration
#         }


# Part 12 -> Cookie and Header Parameters

# @app.get("/items")
# async def read_items(
#     cookie_id: str | None = Cookie(None),
#     accept_encoding: str | None = Header(None),  # convert_underscores=False),
#     sec_ch_ua: str | None = Header(None),
#     user_agent: str | None = Header(None),
#     x_token: list[str] | None = Header(None),
# ):
#     return {
#         "cookie_id": cookie_id,
#         "Accept-Encoding": accept_encoding,
#         "sec-ch-ua": sec_ch_ua,
#         "User-Agent": user_agent,
#         "X-Token values": x_token,
#         }


# # Part 13 -> Response Model


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(
#     item_id: Literal["foo", "bar", "baz"]
# ):  # Literal give access to a drop down of the items, from which one can be selected
#     return items[item_id]


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return Item


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# class UserIn(UserBase):
#     password: str


# class UserOut(UserBase):
#     pass


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# @app.get(
#     "/items/{item_id}/name",
#     response_model=Item,
#     response_model_include={"name", "description"},
# )
# async def read_item_name(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]


# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# async def read_items_public_data(item_id: Literal["foo", "bar", "baz"]):
#     return items[item_id]


## Part 14 -> Extra Models
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# class UserIn(UserBase):
#     password: str


# class UserOut(UserBase):
#     pass


# class UserInDB(UserBase):
#     hashed_password: str


# def fake_password_hasher(raw_password: str):
#     return f"supersecre{raw_password}"


# def fake_save_user(user_in: UserIn):
#     hased_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hased_password)
#     print("userin.dict", user_in.dict())
#     print("User 'saved")
#     return user_in_db


# @app.post("/users/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved


# class BaseItem(BaseModel):
#     description: str
#     type: str


# class CarItem(BaseItem):
#     type = "car"


# class PlaneItem(BaseItem):
#     type = "plane"
#     size: int


# items = {
#     "item1": {
#         "description": "All my friends drive a low rider",
#         "type": "car",
#     },
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }


# @app.get("/items/{items_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: Literal["item1", "item2"]):
#     return items[item_id]


# class ListItem(BaseModel):
#     nae: str
#     description: str


# list_items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]


# @app.get("/list_items/", response_model=list[ListItem])
# async def read_items():
#     return items


# @app.get("/arbitrary", response_model=dict[str, float])
# async def get_arbitrary():
#     return {"foo": 1, "bar": "2"}


## Part 15 -> Response Status Codes

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}


@app.delete("/items/{pd}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(pk:str):
    print("pk", pk)
    return pk  # content will not be shown becos the status code is 204 which indicates no content


@app.get("/items/", status_code=status.HTTP_302_FOUND)
async def read_items_redirect():
    return {"hello": "world"}  # results showed but it was not supposed to becos the status code is 301 which is a redirect, to move permanently
