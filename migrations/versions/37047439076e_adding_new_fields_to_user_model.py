"""adding new fields to user model

Revision ID: 37047439076e
Revises: f5a5fc94e508
Create Date: 2019-06-11 11:17:45.248442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37047439076e'
down_revision = 'f5a5fc94e508'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
