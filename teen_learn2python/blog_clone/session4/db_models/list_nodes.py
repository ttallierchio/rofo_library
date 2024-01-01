from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, create_engine


class Base(DeclarativeBase):
    pass


class ListNode(Base):
    __tablename__ = "list_nodes"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column("id", Integer, primary_key=True)
    text = Column("desc", String(500))


def create_all(engine):
    Base.metadata.create_all(engine)
