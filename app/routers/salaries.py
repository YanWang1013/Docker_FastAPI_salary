from fastapi import APIRouter, HTTPException, Depends
from typing import List, Union

import sqlalchemy.orm as _orm

from .. import schemas as _schemas
from ..services import auth as auth_services
from ..services import base as base_services
from ..services import salaries as salary_services

router = APIRouter(
    prefix="/salaries",
    tags=["salaries"],
    dependencies=[Depends(auth_services.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=_schemas.Salary)
def create_salary(
    salary: _schemas.SalaryCreate,
    db: _orm.Session = Depends(base_services.get_db),
):
    return salary_services.create_salary(db=db, salary=salary)


@router.get("/", response_model=List[_schemas.Salary])
def get_salaries(
    on_contract: Union[bool, None] = None,
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = Depends(base_services.get_db),
):
    salaries = salary_services.get_salaries(db=db, on_contract=on_contract,  skip=skip, limit=limit)
    return salaries


@router.get("/ss/", response_model=_schemas.SS)
def get_salary_ss(
    db: _orm.Session = Depends(base_services.get_db)
):
    return salary_services.get_salary_ss(db=db)


@router.get("/department-ss/", response_model=List[Union[_schemas.DepartmentSS, _schemas.SubDepartmentSS]])
def get_salary_department_ss(
    department: Union[str, None] = None,
    db: _orm.Session = Depends(base_services.get_db)
):
    return salary_services.get_salary_department_ss(db=db, department=department)


@router.get("/{salary_id}", response_model=_schemas.Salary)
def get_salary(salary_id: int, db: _orm.Session = Depends(base_services.get_db)):
    salary = salary_services.get_salary(db=db, salary_id=salary_id)
    if salary is None:
        raise HTTPException(
            status_code=404, detail="sorry this salary does not exist"
        )

    return salary


@router.delete("/{salary_id}")
def delete_salary(salary_id: int, db: _orm.Session = Depends(base_services.get_db)):
    salary_services.delete_salary(db=db, salary_id=salary_id)
    return {"message": f"successfully deleted salary with id: {salary_id}"}


@router.put("/{salary_id}", response_model=_schemas.Salary)
def update_salary(
    salary_id: int,
    salary: _schemas.SalaryCreate,
    db: _orm.Session = Depends(base_services.get_db),
):
    return salary_services.update_salary(db=db, salary=salary, salary_id=salary_id)

