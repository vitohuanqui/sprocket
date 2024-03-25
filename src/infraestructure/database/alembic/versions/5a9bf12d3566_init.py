"""init

Revision ID: 5a9bf12d3566
Revises: 1fa805423f61
Create Date: 2024-03-25 20:16:00.346635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a9bf12d3566'
down_revision: Union[str, None] = '1fa805423f61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sprocket_factory_data', sa.Column('goal', sa.Integer(), nullable=True))
    op.drop_column('sprocket_factory_data', 'is_goal')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sprocket_factory_data', sa.Column('is_goal', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('sprocket_factory_data', 'goal')
    # ### end Alembic commands ###