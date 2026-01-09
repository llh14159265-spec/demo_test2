from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 数据库文件路径
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

# 创建数据库引擎
# connect_args={"check_same_thread": False} 是 SQLite 特有的配置
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类
Base = declarative_base()

# 依赖注入：获取数据库会话
def get_db():
    """
    数据库会话依赖
    使用 yield 确保请求结束后关闭数据库连接
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
