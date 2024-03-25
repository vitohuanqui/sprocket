"""init

Revision ID: 4cafd0c9c9ec
Revises: 
Create Date: 2024-03-22 04:25:52.501519

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '4cafd0c9c9ec'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'factory',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_factory')),
    )
    op.create_table(
        'sprocket_factory_data',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('sprocket_type_id', sa.Integer(), nullable=True),
        sa.Column('factory_id', sa.Integer(), nullable=True),
        sa.Column('production', sa.Integer(), nullable=True),
        sa.Column('is_goal', sa.Boolean(), nullable=True),
        sa.Column('time', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_sprocket_factory_data')),
    )
    op.create_table(
        'sprocket_type',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('teeth', sa.Integer(), nullable=True),
        sa.Column('pitch_diameter', sa.Integer(), nullable=True),
        sa.Column('outside_diameter', sa.Integer(), nullable=True),
        sa.Column('pitch', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_sprocket_type')),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sprocket_type')
    op.drop_table('sprocket_factory_data')
    op.drop_table('factory')
    # ### end Alembic commands ###
