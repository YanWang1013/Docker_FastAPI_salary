from fastapi import APIRouter, HTTPException, status, Depends
from datetime import timedelta

import sqlalchemy.orm as _orm
from fastapi.security import OAuth2PasswordRequestForm

from .. import schemas as _schemas
from ..services import auth as auth_services
from ..services import base as base_services

router = APIRouter()


@router.post("/token", response_model=_schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: _orm.Session = Depends(base_services.get_db)):
    user = auth_services.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth_services.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_services.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}