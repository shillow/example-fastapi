"""add content column to posts table

Revision ID: 0a4a47a4dbfc
Revises: d0f7b064d17a
Create Date: 2023-02-05 20:17:50.549833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0a4a47a4dbfc"
down_revision = "d0f7b064d17a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
