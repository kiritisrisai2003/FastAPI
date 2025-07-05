from fastapi import FastAPI ,HTTPException
from uuid import uuid4 ,UUID
from typing import List
from models import User, Gender, Role ,UpdateUser

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),  # ✅ Call uuid4
        first_name="Kiriti Sri Sai",
        last_name="Tadepalli",
        middle_name=None,  # ✅ Optional, but safe to include
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Sujith Sri Sai",
        last_name="Tadepalli",
        middle_name=None,
        gender=Gender.female,
        roles=[Role.student]
    )
]

@app.get("/")
def root():
    return {"hello": "Kiriti"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_users(user:User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id :{user_id} is not found"
    )

@app.put("/api/v1/users{user_id}")
async def Update_User(user_update:UpdateUser ,user_id:UUID):
    for user in db:
        if user.first_name is not None:
            user.first_name=user_update.first_name
    raise HTTPException(
        status_code=404,
        details=f"user with id :{user_id} is not found"

    )        


     