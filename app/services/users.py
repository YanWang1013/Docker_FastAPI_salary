import sqlalchemy.orm as _orm

from .. import schemas as _schemas
from ..services import auth as auth_services
from ..models.user import User


def get_user_by_id(db: _orm.Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: _orm.Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: _orm.Session, user: _schemas.UserCreate):
    hashed_password = auth_services.get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user