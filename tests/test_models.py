#!/usr/bin/env python
"""测试数据库模型"""
import sys
import os
os.chdir('backend')
sys.path.insert(0, '.')

from app.database import init_db, SessionLocal
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeResponse
from app.crud import create_employee, get_employee, get_employees

# 初始化数据库
print("初始化数据库...")
init_db()
print("✅ 数据库初始化成功")

# 获取数据库会话
db = SessionLocal()

try:
    # 测试创建员工
    print("\n测试创建员工...")
    employee_data = EmployeeCreate(
        name="张三",
        email="zhangsan@example.com",
        position="工程师",
        salary=15000.0
    )
    employee = create_employee(db, employee_data)
    print(f"✅ 创建员工成功: {employee}")
    print(f"   ID: {employee.id}")
    print(f"   名称: {employee.name}")
    print(f"   邮箱: {employee.email}")
    print(f"   职位: {employee.position}")
    print(f"   薪资: {employee.salary}")

    # 测试查询单个员工
    print("\n测试查询单个员工...")
    fetched_employee = get_employee(db, employee.id)
    if fetched_employee:
        print(f"✅ 查询成功: {fetched_employee}")
    else:
        print("❌ 查询失败")

    # 测试查询列表
    print("\n测试查询员工列表...")
    employees = get_employees(db, skip=0, limit=10)
    print(f"✅ 查询成功，共 {len(employees)} 个员工")
    for emp in employees:
        print(f"   - {emp.name} ({emp.email})")

    # 测试 Pydantic 验证
    print("\n测试 Pydantic 验证...")
    response = EmployeeResponse.model_validate(employee)
    print(f"✅ 验证成功: {response}")

    print("\n✅ 所有测试通过！")

finally:
    db.close()
