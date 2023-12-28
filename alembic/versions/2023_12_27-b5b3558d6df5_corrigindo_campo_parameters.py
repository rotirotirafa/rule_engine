"""corrigindo campo parameters

Revision ID: b5b3558d6df5
Revises: 92f02f8a4ed9
Create Date: 2023-12-27 11:12:15.937485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.src.core.domain.rules.model import RulesModel

# revision identifiers, used by Alembic.
revision: str = 'b5b3558d6df5'
down_revision: Union[str, None] = '92f02f8a4ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column(
        RulesModel.__tablename__,
        'parameters'),
    op.add_column(
        RulesModel.__tablename__,
        sa.Column("parameters", sa.String)
    )


def downgrade() -> None:
    op.drop_column(RulesModel.__tablename__, 'parameters')
