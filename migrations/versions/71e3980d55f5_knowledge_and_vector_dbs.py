"""Knowledge and Vector dbs

Revision ID: 71e3980d55f5
Revises: cac478732572
Create Date: 2023-07-26 07:18:06.492832

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "71e3980d55f5"
down_revision = "cac478732572"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "knowledge_configs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("knowledge_id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(), nullable=True),
        sa.Column("value", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "knowledges",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("vector_db_index_id", sa.Integer(), nullable=True),
        sa.Column("organisation_id", sa.Integer(), nullable=True),
        sa.Column("contributed_by", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "marketplace_stats",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("reference_id", sa.Integer(), nullable=True),
        sa.Column("reference_name", sa.String(), nullable=True),
        sa.Column("key", sa.String(), nullable=True),
        sa.Column("value", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "vector_db_configs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("vector_db_id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(), nullable=True),
        sa.Column("value", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "vector_db_indices",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("vector_db_id", sa.Integer(), nullable=True),
        sa.Column("dimensions", sa.Integer(), nullable=True),
        sa.Column("state", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "vector_dbs",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("db_type", sa.String(), nullable=True),
        sa.Column("organisation_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("vector_dbs")
    op.drop_table("vector_db_indices")
    op.drop_table("vector_db_configs")
    op.drop_table("knowledges")
    op.drop_table("knowledge_configs")
