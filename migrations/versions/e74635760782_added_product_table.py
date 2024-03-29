"""added product table

Revision ID: e74635760782
Revises: 2e34bc0a481c
Create Date: 2024-02-07 11:57:44.380879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e74635760782'
down_revision = '2e34bc0a481c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('prod_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('prod_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
