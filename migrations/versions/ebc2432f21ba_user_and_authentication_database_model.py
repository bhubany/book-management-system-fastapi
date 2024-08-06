"""user and authentication database model

Revision ID: ebc2432f21ba
Revises: 3f20e44704a4
Create Date: 2024-08-06 20:02:19.534916

"""
from typing import Sequence, Union

import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ebc2432f21ba'
down_revision: Union[str, None] = '3f20e44704a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Uuid(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('created_by', sa.Uuid(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_by', sa.Uuid(), nullable=True),
                    sa.Column('status', sa.VARCHAR(length=20), nullable=False),
                    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column(
                        'address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)

    op.create_table('authentications',
                    sa.Column('id', sa.Uuid(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('created_by', sa.Uuid(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_by', sa.Uuid(), nullable=True),
                    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column(
                        'email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
                    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(),
                              nullable=False),
                    sa.Column('provider', sa.VARCHAR(
                        length=True), nullable=False),
                    sa.Column(
                        'user_id', sa.UUID, nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_authentications_email'),
                    'authentications', ['email'], unique=True)
    op.create_index(op.f('ix_authentications_id'),
                    'authentications', ['id'], unique=False)
    op.create_index(op.f('ix_authentications_username'),
                    'authentications', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_authentications_username'),
                  table_name='authentications')
    op.drop_index(op.f('ix_authentications_id'), table_name='authentications')
    op.drop_index(op.f('ix_authentications_email'),
                  table_name='authentications')
    op.drop_table('authentications')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
