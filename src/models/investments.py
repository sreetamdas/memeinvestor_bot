import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Investment(Base):
    __tablename__ = "Investments"

    id = Column(Integer, primary_key=True)
    post = Column(String(11), nullable=False)
    upvotes = Column(Integer, default=0)
    comment = Column(String(11), nullable=False, unique=True)
    name = Column(String(20), nullable=False)
    amount = Column(Integer, default=100)
    time = Column(DateTime, server_default=func.utcnow())
    done = Column(Boolean, default=False, nullable=False)
    response = Column(String(11))
    success = Column(Boolean, default=False)
