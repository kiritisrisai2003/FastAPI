from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):  # 'num' was a typo
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: Optional[str] = None  # ✅ give a default
    gender: Gender
    roles: List[Role]
class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name:Optional[str]
    middle_name:Optional[str]
    roles:Optional[List[Role]]