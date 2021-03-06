"""empty message

Revision ID: 29b0cc556d1d
Revises: 5def8464afbf
Create Date: 2021-09-18 15:52:00.844511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29b0cc556d1d'
down_revision = '5def8464afbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('starships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('model', sa.String(length=10), nullable=False),
    sa.Column('manufacturer', sa.String(length=20), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=100), nullable=False),
    sa.Column('length', sa.String(length=100), nullable=False),
    sa.Column('max_atmosphering_speed', sa.String(length=100), nullable=False),
    sa.Column('crew', sa.String(length=100), nullable=False),
    sa.Column('passengers', sa.String(length=20), nullable=False),
    sa.Column('cargo_capacity', sa.String(length=20), nullable=False),
    sa.Column('consumables', sa.String(length=20), nullable=False),
    sa.Column('hyperdrive_rating', sa.String(length=50), nullable=False),
    sa.Column('MGLT', sa.String(length=50), nullable=False),
    sa.Column('starship_class', sa.String(length=50), nullable=False),
    sa.Column('pilots', sa.String(length=50), nullable=False),
    sa.Column('created', sa.String(length=50), nullable=False),
    sa.Column('edited', sa.String(length=50), nullable=False),
    sa.Column('url', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('starships')
    # ### end Alembic commands ###
