"""empty message

Revision ID: 04747c525102
Revises: b65e9cdb71b4
Create Date: 2022-11-04 12:11:21.165284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04747c525102'
down_revision = 'b65e9cdb71b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('moon', sa.Column('planet_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'moon', 'planet', ['planet_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'moon', type_='foreignkey')
    op.drop_column('moon', 'planet_id')
    # ### end Alembic commands ###
