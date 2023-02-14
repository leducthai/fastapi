"""add foreignkey to posts table

Revision ID: b9718e3d446c
Revises: 33d107d96fa6
Create Date: 2023-02-14 20:57:22.015555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9718e3d446c'
down_revision = '33d107d96fa6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts' , sa.Column('owner_id' , sa.Integer , nullable=False))
    op.create_foreign_key('posts_users_fk' , source_table='posts' , referent_table='users' , local_cols=['owner_id'] , remote_cols=['id'], ondelete= 'CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk' , table_name='posts')
    op.drop_column('posts' , 'owner_id')
    pass
