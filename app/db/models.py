from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from datetime import datetime

class Base(DeclarativeBase):
    pass

class Message(Base):

    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        String,
        index=True
    )

    role = Column(
        String
    )

    content = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    
class Feedback(Base):

    __tablename__ = "feedbacks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        String,
        index=True
    )

    question = Column(
        Text
    )

    answer = Column(
        Text
    )

    feedback = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )