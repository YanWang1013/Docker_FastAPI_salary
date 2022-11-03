from typing import List

from fastapi import APIRouter, HTTPException, status, Depends
import sqlalchemy.orm as _orm

from .. import schemas as _schemas
from ..services import auth as auth_services
from ..services import base as base_services
from ..services import users as user_services


router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(auth_services.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=_schemas.User)
def create_user(
    user: _schemas.UserCreate, db: _orm.Session = Depends(base_services.get_db)
):
    db_user = user_services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="woops the email is in use"
        )
    return user_services.create_user(db=db, user=user)


@router.get("/", response_model=List[_schemas.User])
def get_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = Depends(base_services.get_db),
):
    users = user_services.get_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=_schemas.User)
def get_user(user_id: int, db: _orm.Session = Depends(base_services.get_db)):
    db_user = user_services.get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user

