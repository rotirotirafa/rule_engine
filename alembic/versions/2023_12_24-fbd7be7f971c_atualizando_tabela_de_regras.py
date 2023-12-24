"""atualizando tabela de regras

Revision ID: fbd7be7f971c
Revises: 1bf235ce4bfc
Create Date: 2023-12-24 14:20:46.207942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.src.core.domain.rules.model import RulesModel

# revision identifiers, used by Alembic.
revision: str = 'fbd7be7f971c'
down_revision: Union[str, None] = '1bf235ce4bfc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        RulesModel.__tablename__,
        sa.Column("code", sa.Integer)
    )

    op.add_column(
        RulesModel.__tablename__,
        sa.Column("message", sa.String),
    )

    op.add_column(
        RulesModel.__tablename__,
        sa.Column("description", sa.String),
    )


def downgrade() -> None:
    op.drop_column(RulesModel.__tablename__, "code")
    op.drop_column(RulesModel.__tablename__, "message")
    op.drop_column(RulesModel.__tablename__, "description")
