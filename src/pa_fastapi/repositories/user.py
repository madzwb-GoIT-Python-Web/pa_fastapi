from redis          import Redis as Cache
from sqlalchemy.orm import Session

from typing import List

from pa_fastapi.database.schema import User as DBType
from pa_fastapi.schema import User as Type

from .common import repository
exec(repository, globals(), locals())
