"""empty message

Revision ID: 1eb2e775d161
Revises: 
Create Date: 2020-05-03 14:13:16.772338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eb2e775d161'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('LinRegResults',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('YearsExperience', sa.Float(), nullable=True),
    sa.Column('Prediction', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('LinRegResults')
    # ### end Alembic commands ###
