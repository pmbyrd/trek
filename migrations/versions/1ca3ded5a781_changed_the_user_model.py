"""Changed the user model

Revision ID: 1ca3ded5a781
Revises: d8876f6f6df3
Create Date: 2023-08-06 20:24:49.123306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ca3ded5a781'
down_revision = 'd8876f6f6df3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.Text(length=32), nullable=True),
    sa.Column('first_name', sa.Text(length=32), nullable=True),
    sa.Column('last_name', sa.Text(length=32), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('profile_pic', sa.Text(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.TEXT(length=32), nullable=False),
    sa.Column('first_name', sa.TEXT(length=32), nullable=False),
    sa.Column('last_name', sa.TEXT(length=32), nullable=False),
    sa.Column('email', sa.TEXT(), nullable=False),
    sa.Column('avatar', sa.TEXT(), nullable=False),
    sa.Column('bio', sa.TEXT(), nullable=True),
    sa.Column('location', sa.TEXT(), nullable=True),
    sa.Column('password', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
