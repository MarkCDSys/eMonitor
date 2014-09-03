"""
1.0

Revision ID: 4bf22f29acfa
Revises: 22dbd57d8271
Create Date: 2014-09-03 17:59:11.617000

"""

# revision identifiers, used by Alembic.
revision = '4bf22f29acfa'
down_revision = '22dbd57d8271'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    try:
        op.add_column('departments', sa.Column('shortname', sa.VARCHAR(length=10), nullable=True))
        op.add_column('cities', sa.Column('osmname', sa.VARCHAR(length=30), default=""))
    except:
        pass
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('departments', 'shortname')
    op.drop_column('cities', 'osmname')
    ### end Alembic commands ###