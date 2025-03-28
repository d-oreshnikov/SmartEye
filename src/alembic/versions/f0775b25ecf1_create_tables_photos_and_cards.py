"""Create tables photos and cards

Revision ID: f0775b25ecf1
Revises:
Create Date: 2025-03-22 00:14:07.743152

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f0775b25ecf1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'CARDS_META',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('middle_name', sa.String(), nullable=True),
        sa.Column('date_of_birth', sa.DateTime(), nullable=True),
        sa.Column('comment', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'CARDS_PHOTO',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('photo_bytea', sa.LargeBinary(), nullable=True),
        sa.Column('embedding', postgresql.ARRAY(sa.Float()), nullable=True),
        sa.Column('card_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['card_id'],
            ['CARDS_META.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('CARDS_PHOTO')
    op.drop_table('CARDS_META')
    # ### end Alembic commands ###
