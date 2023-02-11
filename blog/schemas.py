from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body:str

class ShowBlog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True

class CreateUser(BaseModel):
    name: str
    email: str
    password: str