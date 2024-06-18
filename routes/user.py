from fastapi import APIRouter
from config.db import  engine 
from models.userModel import users
from schemas.userSchema import User


user_router = APIRouter()



@user_router.get("/users")
def getUsers():
    connection = engine.connect()
    data = connection.execute(users.select()).fetchall()
    connection.close()
    return data

@user_router.post("/users")
def store(user:User):
    connection = engine.connect()
    data = connection.execute(users.insert().values(id=user.id,name=user.name,email=user.email))
    connection.close()
    return data.is_insert
 
