"""refactor user model

Revision ID: 2c86bc99dc4f
Revises: ebc2432f21ba
Create Date: 2024-08-09 23:09:00.665828

"""
from typing import Sequence, Union

import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c86bc99dc4f'
down_revision: Union[str, None] = 'ebc2432f21ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column(
        'last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))


def downgrade() -> None:
    op.drop_column('users', 'last_name')
