"""Add days_to_birthday function.

Revision ID: 4c048ca802f9
Revises: ceff926b3275
Create Date: 2023-09-20 16:39:37.891692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from alembic_utils.pg_function import PGFunction
from sqlalchemy import text as sql_text

# revision identifiers, used by Alembic.
revision: str = '4c048ca802f9'
down_revision: Union[str, None] = 'ceff926b3275'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    public_days_to_birthday = PGFunction(
        schema="public",
        signature="days_to_birthday(born date, curr date)",
        definition="RETURNS integer\n    LANGUAGE 'plpgsql'\n    COST 100\n    VOLATILE PARALLEL UNSAFE\nAS $BODY$\n    DECLARE\n        diff INT = 0; \n        days INT = 0;\n        birth_year INT = 0;\n        birth_month INT = 0;\n        birth_day INT = 0;\n        is_leap BOOL = False;\n        birth_date DATE;\n    BEGIN\n        birth_year = DATE_PART('year', curr);\n        IF birth_year % 4 = 0 and (birth_year % 100 != 0 or birth_year % 400 = 0) THEN\n            is_leap = True;\n        ELSE\n            is_leap = False;\n        END IF;\n        birth_day = DATE_PART('day', born);\n        birth_month = DATE_PART('month', born);\n        IF birth_day = 29 and birth_month = 2 and not is_leap THEN\n            birth_date = make_date(birth_year, birth_month, 28);\n        ELSE\n            birth_date = make_date(birth_year, birth_month, birth_day);\n        END IF;\n        days = birth_date - curr;\n        --days = DATE_PART('year', diff);\n        --RETURN diff;\n        IF days < 0 THEN\n            birth_year = birth_year + 1;\n            IF birth_year % 4 = 0 and (birth_year % 100 != 0 or birth_year % 400 = 0) THEN\n                is_leap = True;\n            ELSE\n                is_leap = False;\n            END IF;\n            IF birth_day = 29 and birth_month = 2 and not is_leap THEN\n                birth_date = make_date(birth_year, birth_month, 28);\n            ELSE\n                birth_date = make_date(birth_year, birth_month, birth_day);\n            days = birth_date - curr;\n            --days = DATE_PART('day', diff);\n            END IF;\n        END IF;\n        RETURN days;\n    END;\n    $BODY$"
    )
    op.create_entity(public_days_to_birthday)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    public_days_to_birthday = PGFunction(
        schema="public",
        signature="days_to_birthday(born date, curr date)",
        definition="RETURNS integer\n    LANGUAGE 'plpgsql'\n    COST 100\n    VOLATILE PARALLEL UNSAFE\nAS $BODY$\n    DECLARE\n        diff INT = 0; \n        days INT = 0;\n        birth_year INT = 0;\n        birth_month INT = 0;\n        birth_day INT = 0;\n        is_leap BOOL = False;\n        birth_date DATE;\n    BEGIN\n        birth_year = DATE_PART('year', curr);\n        IF birth_year % 4 = 0 and (birth_year % 100 != 0 or birth_year % 400 = 0) THEN\n            is_leap = True;\n        ELSE\n            is_leap = False;\n        END IF;\n        birth_day = DATE_PART('day', born);\n        birth_month = DATE_PART('month', born);\n        IF birth_day = 29 and birth_month = 2 and not is_leap THEN\n            birth_date = make_date(birth_year, birth_month, 28);\n        ELSE\n            birth_date = make_date(birth_year, birth_month, birth_day);\n        END IF;\n        days = birth_date - curr;\n        --days = DATE_PART('year', diff);\n        --RETURN diff;\n        IF days < 0 THEN\n            birth_year = birth_year + 1;\n            IF birth_year % 4 = 0 and (birth_year % 100 != 0 or birth_year % 400 = 0) THEN\n                is_leap = True;\n            ELSE\n                is_leap = False;\n            END IF;\n            IF birth_day = 29 and birth_month = 2 and not is_leap THEN\n                birth_date = make_date(birth_year, birth_month, 28);\n            ELSE\n                birth_date = make_date(birth_year, birth_month, birth_day);\n            days = birth_date - curr;\n            --days = DATE_PART('day', diff);\n            END IF;\n        END IF;\n        RETURN days;\n    END;\n    $BODY$"
    )
    op.drop_entity(public_days_to_birthday)
    # ### end Alembic commands ###