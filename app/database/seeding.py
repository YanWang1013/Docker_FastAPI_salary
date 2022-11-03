from sqlalchemy import event

from ..services import auth as auth_services
from ..models.salary import Salary
from ..models.user import User

INITIAL_DATA = {
      'users': [
            {
                  'username': 'admin',
                  'full_name': 'admin',
                  'email': 'admin@example.com',
                  'hashed_password': auth_services.get_password_hash('123456')
            },
      ],
      'salaries': [
            {
                "name": "Abhishek",
                "salary": "145000",
                "currency": "USD",
                "on_contract": False,
                "department": "Engineering",
                "sub_department": "Platform"
            },
            {
                "name": "Anurag",
                "salary": "90000",
                "currency": "USD",
                "on_contract": True,
                "department": "Banking",
                "sub_department": "Loan"
            },
            {
                "name": "Himani",
                "salary": "240000",
                "currency": "USD",
                "on_contract": False,
                "department": "Engineering",
                "sub_department": "Platform"
            },
            {
                "name": "Yatendra",
                "salary": "30",
                "currency": "USD",
                "on_contract": False,
                "department": "Operations",
                "sub_department": "CustomerOnboarding"
            },
            {
                "name": "Ragini",
                "salary": "30",
                "currency": "USD",
                "on_contract": False,
                "department": "Engineering",
                "sub_department": "Platform"
            },
            {
                "name": "Nikhil",
                "salary": "110000",
                "currency": "USD",
                "on_contract": True,
                "department": "Engineering",
                "sub_department": "Platform"
            },
            {
                "name": "Guljit",
                "salary": "30",
                "currency": "USD",
                "on_contract": True,
                "department": "Administration",
                "sub_department": "Agriculture"
            },
            {
                "name": "Himanshu",
                "salary": "70000",
                "currency": "EUR",
                "on_contract": False,
                "department": "Operations",
                "sub_department": "CustomerOnboarding"
            },
            {
                "name": "Anupam",
                "salary": "200000000",
                "currency": "INR",
                "on_contract": False,
                "department": "Engineering",
                "sub_department": "Platform"
            }
      ]
}

def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])



event.listen(User.__table__, 'after_create', initialize_table)
event.listen(Salary.__table__, 'after_create', initialize_table)
