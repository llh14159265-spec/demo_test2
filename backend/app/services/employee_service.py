"""员工业务逻辑服务"""
from sqlalchemy.orm import Session
from app.crud import (
    create_employee,
    get_employee,
    get_employees,
    update_employee,
    delete_employee,
    delete_employees_batch,
)
from app.schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate


class EmployeeService:
    """员工服务类"""

    @staticmethod
    def create_employee(db: Session, employee_data: EmployeeCreate) -> EmployeeResponse:
        """创建员工"""
        employee = create_employee(db, employee_data)
        return EmployeeResponse.model_validate(employee)

    @staticmethod
    def get_employee(db: Session, employee_id: int) -> EmployeeResponse | None:
        """获取员工详情"""
        employee = get_employee(db, employee_id)
        if not employee:
            return None
        return EmployeeResponse.model_validate(employee)

    @staticmethod
    def get_employees(db: Session, skip: int = 0, limit: int = 10) -> list[EmployeeResponse]:
        """获取员工列表"""
        employees = get_employees(db, skip, limit)
        return [EmployeeResponse.model_validate(emp) for emp in employees]

    @staticmethod
    def update_employee(db: Session, employee_id: int, employee_data: EmployeeUpdate) -> EmployeeResponse | None:
        """更新员工"""
        employee = update_employee(db, employee_id, employee_data)
        if not employee:
            return None
        return EmployeeResponse.model_validate(employee)

    @staticmethod
    def delete_employee(db: Session, employee_id: int) -> bool:
        """删除员工"""
        return delete_employee(db, employee_id)

    @staticmethod
    def delete_employees_batch(db: Session, employee_ids: list[int]) -> int:
        """批量删除员工"""
        return delete_employees_batch(db, employee_ids)
