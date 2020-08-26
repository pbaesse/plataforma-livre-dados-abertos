"""update source and software

Revision ID: 4d753390905a
Revises: 6ace8eed9708
Create Date: 2020-08-20 02:03:17.353363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d753390905a'
down_revision = '6ace8eed9708'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('software', schema=None) as batch_op:
        batch_op.drop_index('ix_software_category')
        batch_op.drop_index('ix_software_tag')
        batch_op.drop_column('category')
        batch_op.drop_column('tag')

    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.drop_index('ix_source_category')
        batch_op.drop_index('ix_source_tag')
        batch_op.drop_column('category')
        batch_op.drop_column('tag')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag', sa.VARCHAR(length=200), nullable=True))
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=200), nullable=True))
        batch_op.create_index('ix_source_tag', ['tag'], unique=False)
        batch_op.create_index('ix_source_category', ['category'], unique=False)

    with op.batch_alter_table('software', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag', sa.VARCHAR(length=200), nullable=True))
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=200), nullable=True))
        batch_op.create_index('ix_software_tag', ['tag'], unique=False)
        batch_op.create_index('ix_software_category', ['category'], unique=False)

    # ### end Alembic commands ###
