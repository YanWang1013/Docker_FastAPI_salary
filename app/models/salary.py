import datetime as _dt
import sqlalchemy as _sql

from ..database.database import Base


class Salary(Base):
    __tablename__ = "salaries"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, index=True)
    salary = _sql.Column(_sql.Integer)
    currency = _sql.Column(_sql.String)
    on_contract = _sql.Column(_sql.Boolean, default=False)
    department = _sql.Column(_sql.String, index=True)
    sub_department = _sql.Column(_sql.String, index=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
