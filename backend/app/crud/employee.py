"""员工 CRUD 操作"""
from sqlalchemy.orm import Session
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate


def create_employee(db: Session, employee: EmployeeCreate) -> Employee:
    """创建新员工"""
    db_employee = Employee(
        name=employee.name,
        email=employee.email,
        position=employee.position,
        salary=employee.salary
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_employee(db: Session, employee_id: int) -> Employee | None:
    """获取单个员工"""
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 10) -> list[Employee]:
    """获取员工列表"""
    return db.query(Employee).offset(skip).limit(limit).all()


def get_employee_by_email(db: Session, email: str) -> Employee | None:
    """通过邮箱获取员工"""
    return db.query(Employee).filter(Employee.email == email).first()


def update_employee(db: Session, employee_id: int, employee_update: EmployeeUpdate) -> Employee | None:
    """更新员工信息"""
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    
    update_data = employee_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)
    
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: int) -> bool:
    """删除员工"""
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return False
    
    db.delete(db_employee)
    db.commit()
    return True


def delete_employees_batch(db: Session, employee_ids: list[int]) -> int:
    """批量删除员工"""
    count = db.query(Employee).filter(Employee.id.in_(employee_ids)).delete()
    db.commit()
    return count


def get_employees_count(db: Session) -> int:
    """获取员工总数"""
    return db.query(Employee).count()
