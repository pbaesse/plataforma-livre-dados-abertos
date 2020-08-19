"""atualizei nome source

Revision ID: 31c4df2f17df
Revises: 6e4e57c80338
Create Date: 2020-08-19 19:40:37.433382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31c4df2f17df'
down_revision = '6e4e57c80338'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('text', sa.String(length=600), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_comment'))
    )
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_comment_text'), ['text'], unique=False)
        batch_op.create_index(batch_op.f('ix_comment_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_comment_username'), ['username'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password_hash', sa.String(length=150), nullable=True),
    sa.Column('about_me', sa.String(length=300), nullable=True),
    sa.Column('nickname', sa.String(length=150), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('software',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('tag', sa.String(length=200), nullable=True),
    sa.Column('category', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('officialLink', sa.String(length=300), nullable=True),
    sa.Column('license', sa.String(length=200), nullable=True),
    sa.Column('owner', sa.String(length=200), nullable=True),
    sa.Column('dateCreation', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_software_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_software'))
    )
    with op.batch_alter_table('software', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_software_category'), ['category'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_dateCreation'), ['dateCreation'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_license'), ['license'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_officialLink'), ['officialLink'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_owner'), ['owner'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_tag'), ['tag'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_software_title'), ['title'], unique=True)

    op.create_table('source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('tag', sa.String(length=200), nullable=True),
    sa.Column('category', sa.String(length=200), nullable=True),
    sa.Column('sphere', sa.String(length=200), nullable=True),
    sa.Column('city', sa.String(length=200), nullable=True),
    sa.Column('state', sa.String(length=200), nullable=True),
    sa.Column('country', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=800), nullable=True),
    sa.Column('officialLink', sa.String(length=300), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_source_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_source'))
    )
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_source_category'), ['category'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_city'), ['city'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_country'), ['country'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_officialLink'), ['officialLink'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_sphere'), ['sphere'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_state'), ['state'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_tag'), ['tag'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_source_title'), ['title'], unique=True)

    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('type', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('software_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['software_id'], ['software.id'], name=op.f('fk_report_software_id_software')),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], name=op.f('fk_report_source_id_source')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_report'))
    )
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_report_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_report_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_report_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_report_type'), ['type'], unique=False)

    op.create_table('similar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('software_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['software_id'], ['software.id'], name=op.f('fk_similar_software_id_software')),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], name=op.f('fk_similar_source_id_source')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_similar'))
    )
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_similar_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_similar_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_similar_timestamp'))
        batch_op.drop_index(batch_op.f('ix_similar_name'))

    op.drop_table('similar')
    with op.batch_alter_table('report', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_report_type'))
        batch_op.drop_index(batch_op.f('ix_report_timestamp'))
        batch_op.drop_index(batch_op.f('ix_report_name'))
        batch_op.drop_index(batch_op.f('ix_report_description'))

    op.drop_table('report')
    with op.batch_alter_table('source', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_source_title'))
        batch_op.drop_index(batch_op.f('ix_source_timestamp'))
        batch_op.drop_index(batch_op.f('ix_source_tag'))
        batch_op.drop_index(batch_op.f('ix_source_state'))
        batch_op.drop_index(batch_op.f('ix_source_sphere'))
        batch_op.drop_index(batch_op.f('ix_source_officialLink'))
        batch_op.drop_index(batch_op.f('ix_source_description'))
        batch_op.drop_index(batch_op.f('ix_source_country'))
        batch_op.drop_index(batch_op.f('ix_source_city'))
        batch_op.drop_index(batch_op.f('ix_source_category'))

    op.drop_table('source')
    with op.batch_alter_table('software', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_software_title'))
        batch_op.drop_index(batch_op.f('ix_software_timestamp'))
        batch_op.drop_index(batch_op.f('ix_software_tag'))
        batch_op.drop_index(batch_op.f('ix_software_owner'))
        batch_op.drop_index(batch_op.f('ix_software_officialLink'))
        batch_op.drop_index(batch_op.f('ix_software_license'))
        batch_op.drop_index(batch_op.f('ix_software_description'))
        batch_op.drop_index(batch_op.f('ix_software_dateCreation'))
        batch_op.drop_index(batch_op.f('ix_software_category'))

    op.drop_table('software')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_comment_username'))
        batch_op.drop_index(batch_op.f('ix_comment_timestamp'))
        batch_op.drop_index(batch_op.f('ix_comment_text'))

    op.drop_table('comment')
    # ### end Alembic commands ###
