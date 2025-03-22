"""Repo for work with DB."""

from datetime import datetime
from typing import Self

from sqlalchemy.orm import Session

from db.models import CardsMeta
from db.session import SessionLocal


ValidFieldType = str | int | float | datetime | list[float] | None


class CardsMetaRepository:
    """Class to work with Cards table in db."""

    def __init__(self: Self, session: Session | None = None) -> None:
        self.session = session or SessionLocal()

    def add(
        self: Self,
        last_name: str,
        first_name: str,
        middle_name: str,
        date_of_birth: datetime,
        comment: str,
        embedding: list[float],
    ) -> CardsMeta:
        """Add new card to table."""
        new_card = CardsMeta(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            date_of_birth=date_of_birth,
            comment=comment,
            embedding=embedding,
        )
        self.session.add(new_card)
        self.session.commit()
        self.session.refresh(new_card)
        return new_card

    def get_by_id(self: Self, card_id: int) -> CardsMeta | None:
        """Get card by id."""
        return self.session.query(CardsMeta).filter(CardsMeta.id == card_id).first()

    def list_all(self: Self) -> list[CardsMeta]:
        """List all cards."""
        return self.session.query(CardsMeta).all()

    def update(self: Self, card_id: int, **kwargs: ValidFieldType) -> CardsMeta | None:
        """Update card by id."""
        card = self.get_by_id(card_id)
        if not card:
            return None
        for key, value in kwargs.items():
            setattr(card, key, value)
        self.session.commit()
        self.session.refresh(card)
        return card

    def delete(self, card_id: int) -> bool:
        """Delete card by id."""
        card = self.get_by_id(card_id)
        if not card:
            return False
        self.session.delete(card)
        self.session.commit()
        return True
