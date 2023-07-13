"""Working on user changes

Revision ID: 4aae54e52caa
Revises: 24967b9b443f
Create Date: 2023-07-06 17:58:47.978573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aae54e52caa'
down_revision = '24967b9b443f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_users')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.Text(length=64), nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.TEXT(), nullable=False))
        batch_op.drop_column('password_hash')

    op.create_table('_alembic_tmp_users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.TEXT(), nullable=False),
    sa.Column('first_name', sa.TEXT(), nullable=False),
    sa.Column('last_name', sa.TEXT(), nullable=False),
    sa.Column('email', sa.TEXT(), nullable=False),
    sa.Column('avatar', sa.TEXT(), nullable=False),
    sa.Column('bio', sa.TEXT(), nullable=True),
    sa.Column('location', sa.TEXT(), nullable=True),
    sa.Column('password_hash', sa.TEXT(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###