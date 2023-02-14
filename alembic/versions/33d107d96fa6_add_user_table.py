"""add user table

Revision ID: 33d107d96fa6
Revises: 94c6dfa62cbb
Create Date: 2023-02-14 20:38:02.479473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33d107d96fa6'
down_revision = '94c6dfa62cbb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id' , sa.Integer , nullable=False),
        sa.Column('email' , sa.String , nullable=False),
        sa.Column('password' , sa.String , nullable=False),
        sa.Column('create_at' , sa.TIMESTAMP(timezone=True) , server_default=sa.text('now()') , nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
