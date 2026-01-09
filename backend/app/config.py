"""应用配置文件"""
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用设置"""
    
    # 数据库配置
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # 应用配置
    APP_NAME: str = "FastAPI Management System"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"


settings = Settings()
