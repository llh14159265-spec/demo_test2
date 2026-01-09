"""员工数据验证模型"""
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class EmployeeCreate(BaseModel):
    """创建/更新员工的请求模型"""
    name: str = Field(..., min_length=1, max_length=100, description="员工名称")
    email: EmailStr = Field(..., description="员工邮箱")
    position: str = Field(..., min_length=1, max_length=100, description="职位")
    salary: float = Field(..., gt=0, description="薪资（必须大于0）")


class EmployeeResponse(BaseModel):
    """员工响应模型"""
    id: int
    name: str
    email: str
    position: str
    salary: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class EmployeeUpdate(BaseModel):
    """更新员工的请求模型（所有字段可选）"""
    name: str | None = Field(None, min_length=1, max_length=100, description="员工名称")
    email: EmailStr | None = Field(None, description="员工邮箱")
    position: str | None = Field(None, min_length=1, max_length=100, description="职位")
    salary: float | None = Field(None, gt=0, description="薪资（必须大于0）")
