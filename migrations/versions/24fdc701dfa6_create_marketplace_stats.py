"""create marketplace_stats
Revision ID: 24fdc701dfa6
Revises: 024c5c121f57
Create Date: 2023-07-12 08:31:56.353080
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '24fdc701dfa6'
down_revision = '024c5c121f57'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marketplace_stats',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('reference_id', sa.Integer(), nullable=True),
    sa.Column('reference_name', sa.String(), nullable=True),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('marketplace_state')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marketplace_state',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('reference_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('reference_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('key', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('value', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='marketplace_state_pkey')
    )
    op.drop_table('marketplace_stats')
    # ### end Alembic commands ###