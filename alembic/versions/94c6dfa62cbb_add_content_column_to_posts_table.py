"""add content column to posts table

Revision ID: 94c6dfa62cbb
Revises: f1c2cfc3e303
Create Date: 2023-02-14 20:26:35.783356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94c6dfa62cbb'
down_revision = 'f1c2cfc3e303'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content' , sa.String() , nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts' , 'content')
    pass
