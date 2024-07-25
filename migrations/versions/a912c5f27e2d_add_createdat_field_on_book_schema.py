"""add createdat field on book schema

Revision ID: a912c5f27e2d
Revises: 2390ee7dec63
Create Date: 2024-07-25 21:29:49.422495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a912c5f27e2d'
down_revision: Union[str, None] = '2390ee7dec63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'created_at')
    # ### end Alembic commands ###
