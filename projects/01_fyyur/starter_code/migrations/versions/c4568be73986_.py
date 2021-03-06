"""empty message

Revision ID: c4568be73986
Revises: f90c59af2764
Create Date: 2021-04-27 23:27:38.631017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4568be73986'
down_revision = 'f90c59af2764'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'website_link')
    op.drop_column('Venue', 'seeking_description')
    # ### end Alembic commands ###
