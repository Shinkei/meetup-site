"""add events

Revision ID: 1c3d22081b37
Revises: 8bfb5e2e01a9
Create Date: 2018-09-01 17:49:48.438356

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2.types import Geometry
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "1c3d22081b37"
down_revision = "8bfb5e2e01a9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('CREATE EXTENSION IF NOT EXISTS "postgis"')

    # Events
    op.create_table(
        "events",
        sa.Column(
            "id",
            postgresql.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column(
            "location", Geometry(geometry_type="POINT", srid=4326), nullable=True
        ),
        sa.Column("title_content", sa.String(), nullable=True),
        sa.Column("description_title", sa.String(), nullable=True),
        sa.Column("description_content", sa.String(), nullable=True),
        sa.Column("agenda_title", sa.String(), nullable=True),
        sa.Column("agenda_content", sa.String(), nullable=True),
        sa.Column("presenter_title", sa.String(), nullable=True),
        sa.Column("presenter_content", sa.String(), nullable=True),
        sa.Column("requirement_title", sa.String(), nullable=True),
        sa.Column("requirement_content", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_events_date"), "events", ["date"], unique=True)

    # Events <-> Users
    op.create_table(
        "event_user_mappings",
        sa.Column("user_id", postgresql.UUID(), nullable=False),
        sa.Column("event_id", postgresql.UUID(), nullable=False),
        sa.ForeignKeyConstraint(["event_id"], ["events.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("user_id", "event_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("event_user_mappings")
    op.drop_index(op.f("ix_events_date"), table_name="events")
    op.drop_table("events")
    op.execute('DROP EXTENSION IF EXISTS "postgis"')
    # ### end Alembic commands ###
