from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserIn, UserUpdate


class CRUDUser(CRUDBase[User, UserIn, UserUpdate]):
    def create(self, db: Session, *, obj_in: UserIn) -> User:
        db_obj = User(
            user_name = obj_in.user_name,
            full_name = obj_in.full_name,
            password = obj_in.password,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
user=CRUDUser(User)