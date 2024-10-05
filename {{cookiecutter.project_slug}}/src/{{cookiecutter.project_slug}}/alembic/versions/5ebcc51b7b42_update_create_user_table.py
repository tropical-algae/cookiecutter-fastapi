"""update: create user table

Revision ID: 5ebcc51b7b42
Revises: 
Create Date: 2024-08-14 12:33:39.292076

"""
import uuid
import json
from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union
from passlib.hash import pbkdf2_sha256

from {{cookiecutter.project_slug}}.common.config import settings
# from sqlalchemy import TIMESTAMP


# revision identifiers, used by Alembic.
revision: str = '5ebcc51b7b42'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    user_table = op.create_table('user',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('full_name', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('scopes', sa.String(length=128), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('profile', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.bulk_insert(
        user_table,
        [
            {
                "id": uuid.uuid4().hex,
                "full_name": settings.DEFAULT_SUPERUSER,
                "email": "admin@test.com",
                "is_active": True,
                "is_superuser": True,
                "password": pbkdf2_sha256.hash(settings.DEFAULT_SUPERUSER_PASSWD),
                "scopes": json.dumps(["ADMIN"]),
                "profile": None,
            }
        ],
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
