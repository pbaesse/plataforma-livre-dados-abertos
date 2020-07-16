"""upgrade tables user post

Revision ID: 6b422fae93fc
Revises: e9d3a715514c
Create Date: 2020-07-10 00:26:15.207822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b422fae93fc'
down_revision = 'e9d3a715514c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_post_id_post', type_='foreignkey')
        batch_op.drop_column('post_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_user_post_id_post', 'post', ['post_id'], ['id'])

    # ### end Alembic commands ###