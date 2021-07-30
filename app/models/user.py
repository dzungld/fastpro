from sqlalchemy import Column, Integer, MetaData, String, Table, Text, text
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID

metadata = Base.metadata


class User(Base):
    __tablename__ = "users"
    id = Column("id", UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    user_name = Column("user_name", String, unique=True, index=True, nullable=False)
    full_name = Column("full_name", String)
    password = Column("password", String, nullable=False)
