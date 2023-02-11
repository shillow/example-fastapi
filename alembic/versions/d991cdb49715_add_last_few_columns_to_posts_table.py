"""add last few columns to posts table

Revision ID: d991cdb49715
Revises: 67b7ec8c5487
Create Date: 2023-02-09 16:40:19.195513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d991cdb49715"
down_revision = "67b7ec8c5487"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column(
            "published",
            sa.Boolean(),
            nullable=False,
            server_default="True",
        ),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
