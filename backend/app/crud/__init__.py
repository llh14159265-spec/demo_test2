"""数据访问层"""
from app.crud.employee import (
    create_employee,
    get_employee,
    get_employees,
    get_employee_by_email,
    update_employee,
    delete_employee,
    delete_employees_batch,
    get_employees_count,
)

__all__ = [
    "create_employee",
    "get_employee",
    "get_employees",
    "get_employee_by_email",
    "update_employee",
    "delete_employee",
    "delete_employees_batch",
    "get_employees_count",
]
