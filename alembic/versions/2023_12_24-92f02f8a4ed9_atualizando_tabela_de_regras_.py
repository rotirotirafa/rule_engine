"""atualizando tabela de regras parametrizacao

Revision ID: 92f02f8a4ed9
Revises: fbd7be7f971c
Create Date: 2023-12-24 14:33:07.598360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.src.core.domain.rules.model import RulesModel

# revision identifiers, used by Alembic.
revision: str = '92f02f8a4ed9'
down_revision: Union[str, None] = 'fbd7be7f971c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        RulesModel.__tablename__,
        sa.Column("parameters", sa.Integer)
    )


def downgrade() -> None:
    op.drop_column(RulesModel.__tablename__, "parameters")
