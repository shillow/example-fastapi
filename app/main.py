from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# since we have Alembic now, we don't need this line of code anymore to create our tables from here...
# alembic revision --autogenerate -m "your message" will look into the model.py and create the database p3p33p3
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "*"
]  # provide a list of domains you want to access the API, else use that to allow everything

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}
