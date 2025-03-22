"""DB models module."""

from typing import ClassVar, Self

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, LargeBinary, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, relationship

from config import DATABASE_CARDS_META_TABLE_NAME, DATABASE_CARDS_PHOTO_TABLE_NAME
from db.base import Base


class CardsMeta(Base):
    """Personal info."""

    __tablename__: ClassVar[str] = DATABASE_CARDS_META_TABLE_NAME

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    last_name: Column = Column(String)
    first_name: Column = Column(String)
    middle_name: Column = Column(String)
    date_of_birth: Column = Column(DateTime)
    comment: Column = Column(String)

    photos_id: Mapped[list["CardsPhoto"]] = relationship("CardsPhoto", back_populates="card", cascade="all, delete-orphan")  # type: ignore[assignment]

    def __repr__(self: Self) -> str:
        return (
            f"CardsMeta(id={self.id}\n"
            f"last_name={self.last_name}\n"
            f"first_name={self.first_name}\n"
            f"middle_name={self.middle_name}\n"
            f"date_of_birth={self.date_of_birth}\n"
            f"comment={self.comment}\n"
        )


class CardsPhoto(Base):
    """Personal photo."""

    __tablename__: ClassVar[str] = DATABASE_CARDS_PHOTO_TABLE_NAME
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    photo_bytea: Column = Column(LargeBinary)
    embedding: Column = Column(ARRAY(Float))

    card_id = Column(Integer, ForeignKey(f"{DATABASE_CARDS_META_TABLE_NAME}.id"), nullable=False)

    card: Mapped[list["CardsMeta"]] = relationship("CardsMeta", back_populates="photos_id")  # type: ignore[assignment]

    def __repr__(self: Self) -> str:
        return f"CardsPhoto(id={self.id}, card_id={self.card_id}, embedding={self.embedding})"
