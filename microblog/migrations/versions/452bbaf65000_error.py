"""error?

Revision ID: 452bbaf65000
Revises: fa1bb67d07b4
Create Date: 2018-12-12 11:33:38.768746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '452bbaf65000'
down_revision = 'fa1bb67d07b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
