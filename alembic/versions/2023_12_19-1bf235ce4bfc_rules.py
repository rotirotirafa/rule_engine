"""Rules

Revision ID: 1bf235ce4bfc
Revises: 
Create Date: 2023-12-19 16:09:53.741255

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.src.core.domain.rules.model import RulesModel

# revision identifiers, used by Alembic.
revision: str = '1bf235ce4bfc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        RulesModel.__tablename__,
        sa.Column("rule_id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, unique=True),
        sa.Column("condition", sa.String),
        sa.Column("action", sa.String),
        sa.Column("created_date", sa.DateTime, default=datetime.now()),
    )


def downgrade() -> None:
    op.drop_table(RulesModel.__tablename__)
