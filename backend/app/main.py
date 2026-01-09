"""FastAPI 应用主文件"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.config import settings
from app.database import init_db

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建 FastAPI 应用
app = FastAPI(
    title=settings.APP_NAME,
    description="一个基于 FastAPI 的全栈管理系统",
    version="0.1.0"
)

# 配置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """应用启动事件"""
    logger.info("初始化数据库...")
    init_db()
    logger.info("应用启动完成")


@app.get("/")
async def root():
    """根路由"""
    return {"message": "欢迎使用 FastAPI 管理系统"}


@app.get("/health")
async def health_check():
    """健康检查端点"""
    return {"status": "healthy"}
