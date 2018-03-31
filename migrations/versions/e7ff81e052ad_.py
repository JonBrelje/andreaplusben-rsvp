"""empty message

Revision ID: e7ff81e052ad
Revises: 06737aa91e07
Create Date: 2018-03-30 21:00:21.310051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7ff81e052ad'
down_revision = '06737aa91e07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guests3',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('party', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('rehearsalInvite', sa.Integer(), nullable=True),
    sa.Column('welcomeReceptionInvite', sa.Integer(), nullable=True),
    sa.Column('rehearsalFoodChoice', sa.String(), nullable=True),
    sa.Column('receptionFoodChoice', sa.String(), nullable=True),
    sa.Column('rehearsalRSVPStatus', sa.String(), nullable=True),
    sa.Column('welcomeReceptionRSVPStatus', sa.String(), nullable=True),
    sa.Column('receptionRSVPStatus', sa.String(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guests3')
    # ### end Alembic commands ###
