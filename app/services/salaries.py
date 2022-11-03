from typing import Union

import sqlalchemy.orm as _orm
from sqlalchemy import func

from .. import schemas as _schemas
from ..models.salary import Salary



def get_salaries(db: _orm.Session, on_contract: Union[bool, None] = None, skip: int = 0, limit: int = 10):
    if on_contract is not None:
        return db.query(Salary).filter(Salary.on_contract == on_contract).offset(skip).limit(limit).all()
    else:
        return db.query(Salary).offset(skip).limit(limit).all()


def create_salary(db: _orm.Session, salary: _schemas.SalaryCreate):
    salary = Salary(**salary.dict())
    db.add(salary)
    db.commit()
    db.refresh(salary)
    return salary


def get_salary(db: _orm.Session, salary_id: int):
    return db.query(Salary).filter(Salary.id == salary_id).first()


def delete_salary(db: _orm.Session, salary_id: int):
    db.query(Salary).filter(Salary.id == salary_id).delete()
    db.commit()


def update_salary(db: _orm.Session, salary_id: int, salary: _schemas.SalaryCreate):
    db_salary = get_salary(db=db, salary_id=salary_id)
    db_salary.name = salary.name
    db_salary.salary = salary.salary
    db_salary.currency = salary.currency
    db_salary.on_contract = salary.on_contract
    db_salary.department = salary.department
    db_salary.sub_department = salary.sub_department
    db.commit()
    db.refresh(db_salary)
    return db_salary


def get_salary_ss(db: _orm.Session):
    ss = db.query(
        func.max(Salary.salary).label("max"),
        func.min(Salary.salary).label("min"),
        func.avg(Salary.salary).label("avg")
    ).first()
    return ss


def get_salary_department_ss(db: _orm.Session, department: Union[str, None]=None):
    if department is None or department == "":
        ss = db.query(
            Salary.department,
            func.max(Salary.salary).label("max"),
            func.min(Salary.salary).label("min"),
            func.avg(Salary.salary).label("avg"),
        ).group_by(Salary.department).all()
    else:
        ss = db.query(
            Salary.sub_department,
            func.max(Salary.salary).label("max"),
            func.min(Salary.salary).label("min"),
            func.avg(Salary.salary).label("avg"),
        ).filter(Salary.department == department).group_by(Salary.sub_department).all()
    return ss
