from pydantic import BaseModel
from typing import List, Optional

class UserIn(BaseModel):
    user_name: str
    full_name: str
    password: str

class UserOut(UserIn):
    id: str

class User(UserOut):
    pass

class UserUpdate(UserIn):
    user_name: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
