"""Fix contacts unique.

Revision ID: 1eb2f6c7f8dd
Revises: 4312ea33ffd6
Create Date: 2023-09-25 20:16:53.798789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1eb2f6c7f8dd'
down_revision: Union[str, None] = '4312ea33ffd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('contacts_value_key', 'contacts', type_='unique')
    op.create_unique_constraint('uc_contacts', 'contacts', ['person_id', 'value'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uc_contacts', 'contacts', type_='unique')
    op.create_unique_constraint('contacts_value_key', 'contacts', ['value'])
    # ### end Alembic commands ###
