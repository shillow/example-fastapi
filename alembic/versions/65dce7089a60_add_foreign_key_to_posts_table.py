"""add foreign-key to posts table

It did not work

Revision ID: 65dce7089a60
Revises: 69f46f748b5d
Create Date: 2023-02-09 15:32:02.110282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "65dce7089a60"
down_revision = "69f46f748b5d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk", "posts", "users", ["owner_id"], ["id"], ondelete="CASCADE"
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
