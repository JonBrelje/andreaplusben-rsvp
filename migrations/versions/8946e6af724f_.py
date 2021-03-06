"""empty message

Revision ID: 8946e6af724f
Revises: 
Create Date: 2018-03-27 22:01:19.784625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8946e6af724f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('party', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('rehearsalInvite', sa.Integer(), nullable=True),
    sa.Column('welcomeReceptionInvite', sa.Integer(), nullable=True),
    sa.Column('rehearsalFoodChoice', sa.String(), nullable=True),
    sa.Column('receptionFoodChoice', sa.String(), nullable=True),
    sa.Column('rehearsalRSVPStatus', sa.Integer(), nullable=True),
    sa.Column('welcomeReceptionRSVPStatus', sa.Integer(), nullable=True),
    sa.Column('receptionRSVPStatus', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guests')
    # ### end Alembic commands ###
