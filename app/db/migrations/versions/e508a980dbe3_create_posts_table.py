"""create posts table

Revision ID: e508a980dbe3
Revises: 
Create Date: 2024-07-05 15:28:10.873782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e508a980dbe3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(255), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
