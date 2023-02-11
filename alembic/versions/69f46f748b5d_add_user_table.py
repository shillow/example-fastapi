"""add user table

Revision ID: 69f46f748b5d
Revises: 0a4a47a4dbfc
Create Date: 2023-02-08 09:45:45.629265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "69f46f748b5d"
down_revision = "0a4a47a4dbfc"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
