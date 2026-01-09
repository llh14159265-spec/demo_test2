from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# ============ 请求模型 ============

class UserCreate(BaseModel):
    """
    创建用户时的请求模型
    用于接收客户端提交的数据
    """
    name: str = Field(..., min_length=1, max_length=50, description="用户姓名")
    email: str = Field(..., description="用户邮箱")
    age: Optional[int] = Field(None, ge=0, le=150, description="用户年龄")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "张三",
                "email": "zhangsan@example.com",
                "age": 25
            }
        }


class UserUpdate(BaseModel):
    """
    更新用户时的请求模型
    所有字段都是可选的
    """
    name: Optional[str] = Field(None, min_length=1, max_length=50, description="用户姓名")
    email: Optional[str] = Field(None, description="用户邮箱")
    age: Optional[int] = Field(None, ge=0, le=150, description="用户年龄")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "李四",
                "email": "lisi@example.com",
                "age": 30
            }
        }


# ============ 响应模型 ============

class UserResponse(BaseModel):
    """
    用户响应模型
    返回给客户端的数据格式
    """
    id: int
    name: str
    email: str
    age: Optional[int]
    created_at: datetime
    
    class Config:
        from_attributes = True  # 允许从 ORM 模型创建
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "张三",
                "email": "zhangsan@example.com",
                "age": 25,
                "created_at": "2024-01-09T12:00:00"
            }
        }
