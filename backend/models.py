from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.database import Base

class User(Base):
    """
    用户数据模型
    对应数据库中的 users 表
    """
    __tablename__ = "users"
    
    # 主键，自增
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # 用户姓名，不能为空
    name = Column(String(50), nullable=False, index=True)
    
    # 用户邮箱，唯一，不能为空
    email = Column(String(100), unique=True, nullable=False, index=True)
    
    # 用户年龄
    age = Column(Integer, nullable=True)
    
    # 创建时间，默认为当前时间
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
