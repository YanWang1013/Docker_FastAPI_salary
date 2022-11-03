import datetime as _dt
from typing import Union, List

import pydantic as _pydantic


class _BaseModel(_pydantic.BaseModel):
    class Config:
        orm_mode = True


class Token(_pydantic.BaseModel):
    access_token: str
    token_type: str


class TokenData(_pydantic.BaseModel):
    username: Union[str, None] = None


class _UserBase(_BaseModel):
    username: str


class UserCreate(_UserBase):
    full_name: str
    email: _pydantic.EmailStr
    password: str


class User(_UserBase):
    id: int
    full_name: str
    email: str
    is_active: bool


class UserInDB(User):
    hashed_password: str


class _SalaryBase(_BaseModel):
    name: str
    salary: int
    currency: str
    department: str
    sub_department: str
    on_contract: bool


class SalaryCreate(_SalaryBase):
    pass


class Salary(_SalaryBase):
    id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime


class SS(_BaseModel):
    max: int
    min: int
    avg: float


class DepartmentSS(_BaseModel):
    department: str
    max: int
    min: int
    avg: float


class SubDepartmentSS(_BaseModel):
    sub_department: str
    max: int
    min: int
    avg: float
