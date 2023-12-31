import os

from fastapi        import APIRouter, HTTPException, Depends, status, Security
from sqlalchemy.orm import Session
from typing         import List

import pa_fastapi.repositories.role as repository

from pa_fastapi.database.connection    import get_db
from pa_fastapi.routes.rates           import *
from pa_fastapi.schema                 import Role as Type
from pa_fastapi.services.auth          import auth

names = os.path.splitext(os.path.basename(__file__))[0]
name = names[0:-1].capitalize() if names[-1] == 's' else names.capitalize()
error_not_found = f"{name} not found."

router = APIRouter(prefix=f"/{name}", tags=[name])

create_scope    = Security(auth.get_user, scopes=["admin"])
read_scope      = Security(auth.get_user, scopes=["moder"])
update_scope    = Security(auth.get_user, scopes=["admin"])
delete_scope    = Security(auth.get_user, scopes=["admin"])

from .common import route
exec(route, globals(), locals())
