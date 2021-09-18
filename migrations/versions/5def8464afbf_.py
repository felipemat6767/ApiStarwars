"""empty message

Revision ID: 5def8464afbf
Revises: bf8c56801f37
Create Date: 2021-09-18 15:27:08.188376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5def8464afbf'
down_revision = 'bf8c56801f37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('rotation_period', sa.String(length=10), nullable=False),
    sa.Column('orbital_period', sa.String(length=20), nullable=False),
    sa.Column('diameter', sa.String(length=100), nullable=False),
    sa.Column('climate', sa.String(length=100), nullable=False),
    sa.Column('gravity', sa.String(length=100), nullable=False),
    sa.Column('terrain', sa.String(length=100), nullable=False),
    sa.Column('surface_water', sa.String(length=20), nullable=False),
    sa.Column('population', sa.String(length=20), nullable=False),
    sa.Column('residents', sa.String(length=20), nullable=False),
    sa.Column('films', sa.String(length=50), nullable=False),
    sa.Column('created', sa.String(length=50), nullable=False),
    sa.Column('edited', sa.String(length=50), nullable=False),
    sa.Column('url', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
