"""add foreign-key to posts tale

Revision ID: 93e6b2e2d559
Revises: 69f46f748b5d
Create Date: 2023-02-09 16:22:49.219100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "93e6b2e2d559"
down_revision = "69f46f748b5d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
