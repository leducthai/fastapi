"""add more columns to posts table

Revision ID: aea29fc2e6c6
Revises: b9718e3d446c
Create Date: 2023-02-14 21:09:42.039829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aea29fc2e6c6'
down_revision = 'b9718e3d446c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('published' , sa.Boolean , nullable=False , server_default='True'),
    )
    op.add_column(
        'posts',
        sa.Column('create_at' , sa.TIMESTAMP(timezone=True) , nullable=False , server_default=sa.text('now()'))
    )
    pass


def downgrade() -> None:
    op.drop_column('posts' , 'published')
    op.drop_column('posts' , 'create_at')
    pass
