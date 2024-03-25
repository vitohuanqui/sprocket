"""add url to faactory

Revision ID: 1fa805423f61
Revises: 4cafd0c9c9ec
Create Date: 2024-03-23 23:02:46.781780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fa805423f61'
down_revision: Union[str, None] = '4cafd0c9c9ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('factory', sa.Column('url', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('factory', 'url')
    # ### end Alembic commands ###
