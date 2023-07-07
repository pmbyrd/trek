"""Working on user changes

Revision ID: 24967b9b443f
Revises: a2045b9f2f7c
Create Date: 2023-07-06 17:55:36.527094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24967b9b443f'
down_revision = 'a2045b9f2f7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.Text(length=64), nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.TEXT(), nullable=False))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
