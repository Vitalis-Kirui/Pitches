"""adding time column to pitch class model

Revision ID: 6fc83d4856e1
Revises: 4dcf9df98eb2
Create Date: 2021-09-19 10:37:00.324941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fc83d4856e1'
down_revision = '4dcf9df98eb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'posted')
    # ### end Alembic commands ###
