"""create post table

Revision ID: f1c2cfc3e303
Revises: 
Create Date: 2023-02-14 20:12:59.036404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1c2cfc3e303'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id' , sa.Integer , nullable= False , primary_key= True),
        sa.Column('title' , sa.String , nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
