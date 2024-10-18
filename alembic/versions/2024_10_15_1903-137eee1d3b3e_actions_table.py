"""actions table

Revision ID: 137eee1d3b3e
Revises: 12fb2dede685
Create Date: 2024-10-15 19:03:29.086340+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "137eee1d3b3e"
down_revision: Union[str, None] = "12fb2dede685"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "actions",
        sa.Column("action_id", sa.String(), nullable=False),
        sa.Column("action_type", sa.String(), nullable=False),
        sa.Column("source_action_id", sa.String(), nullable=True),
        sa.Column("organization_id", sa.String(), nullable=True),
        sa.Column("workflow_run_id", sa.String(), nullable=True),
        sa.Column("task_id", sa.String(), nullable=False),
        sa.Column("step_id", sa.String(), nullable=False),
        sa.Column("step_order", sa.Integer(), nullable=False),
        sa.Column("action_order", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("reasoning", sa.String(), nullable=True),
        sa.Column("intention", sa.String(), nullable=True),
        sa.Column("response", sa.String(), nullable=True),
        sa.Column("element_id", sa.String(), nullable=True),
        sa.Column("skyvern_element_hash", sa.String(), nullable=True),
        sa.Column("skyvern_element_data", sa.JSON(), nullable=True),
        sa.Column("action_json", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organizations.organization_id"],
        ),
        sa.ForeignKeyConstraint(
            ["source_action_id"],
            ["actions.action_id"],
        ),
        sa.ForeignKeyConstraint(
            ["step_id"],
            ["steps.step_id"],
        ),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["tasks.task_id"],
        ),
        sa.ForeignKeyConstraint(
            ["workflow_run_id"],
            ["workflow_runs.workflow_run_id"],
        ),
        sa.PrimaryKeyConstraint("action_id"),
    )
    op.create_index("action_org_task_step_index", "actions", ["organization_id", "task_id", "step_id"], unique=False)
    op.create_index(op.f("ix_actions_action_id"), "actions", ["action_id"], unique=False)
    op.create_index(op.f("ix_actions_source_action_id"), "actions", ["source_action_id"], unique=False)
    op.create_index(op.f("ix_actions_task_id"), "actions", ["task_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_actions_task_id"), table_name="actions")
    op.drop_index(op.f("ix_actions_source_action_id"), table_name="actions")
    op.drop_index(op.f("ix_actions_action_id"), table_name="actions")
    op.drop_index("action_org_task_step_index", table_name="actions")
    op.drop_table("actions")
    # ### end Alembic commands ###