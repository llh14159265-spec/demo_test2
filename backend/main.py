from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from pathlib import Path
from backend.database import engine, Base, get_db
from backend.models import User
from backend.schemas import UserCreate, UserUpdate, UserResponse

# 创建 FastAPI 应用实例
app = FastAPI(
    title="用户管理系统 API",
    description="一个简单的用户管理系统，支持完整的 CRUD 操作",
    version="1.0.0"
)

# 配置 CORS（跨域资源共享）
# 允许前端从不同端口访问后端 API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该指定具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建数据库表
# 在应用启动时，根据模型定义创建所有表
Base.metadata.create_all(bind=engine)

# 前端文件路径
frontend_path = Path(__file__).parent.parent / "frontend"

# 健康检查接口
@app.get("/health")
async def health_check():
    """
    健康检查接口
    用于检查服务是否正常运行
    """
    return {"status": "ok", "message": "服务运行正常"}

# API 信息接口
@app.get("/api")
async def api_info():
    """
    API 信息
    """
    return {
        "message": "欢迎使用用户管理系统 API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


# ============ CRUD 路由 ============

# 第三步：创建用户（POST /users）
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    创建新用户
    
    - **name**: 用户姓名（必填，1-50字符）
    - **email**: 用户邮箱（必填，唯一）
    - **age**: 用户年龄（可选，0-150）
    
    返回创建的用户信息
    """
    # 检查邮箱是否已存在
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"邮箱 {user.email} 已被注册"
        )
    
    # 创建新用户对象
    db_user = User(
        name=user.name,
        email=user.email,
        age=user.age
    )
    
    try:
        # 添加到数据库
        db.add(db_user)
        db.commit()
        db.refresh(db_user)  # 刷新以获取自动生成的 id 和 created_at
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="创建用户失败，请检查数据是否有效"
        )


# 第四步：查询用户（GET /users, GET /users/{id}）

@app.get("/users", response_model=List[UserResponse])
async def get_users(
    skip: int = Query(0, ge=0, description="跳过的记录数"),
    limit: int = Query(100, ge=1, le=1000, description="返回的最大记录数"),
    db: Session = Depends(get_db)
):
    """
    获取所有用户列表
    
    - **skip**: 跳过的记录数（用于分页，默认 0）
    - **limit**: 返回的最大记录数（默认 100，最大 1000）
    
    返回用户列表
    """
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    根据 ID 获取单个用户
    
    - **user_id**: 用户 ID
    
    返回用户信息，如果不存在则返回 404 错误
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"用户 ID {user_id} 不存在"
        )
    return user


# 第五步：更新用户（PUT /users/{id}）

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
):
    """
    更新用户信息
    
    - **user_id**: 用户 ID
    - **name**: 新的姓名（可选）
    - **email**: 新的邮箱（可选）
    - **age**: 新的年龄（可选）
    
    支持部分更新，只更新提供的字段
    返回更新后的用户信息
    """
    # 查询用户是否存在
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"用户 ID {user_id} 不存在"
        )
    
    # 如果要更新邮箱，检查新邮箱是否已被其他用户使用
    if user_update.email is not None:
        existing_user = db.query(User).filter(
            User.email == user_update.email,
            User.id != user_id  # 排除当前用户
        ).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"邮箱 {user_update.email} 已被其他用户使用"
            )
    
    # 更新字段（只更新提供的字段）
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="更新用户失败，请检查数据是否有效"
        )


# 第六步：删除用户（DELETE /users/{id}）

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    删除用户
    
    - **user_id**: 用户 ID
    
    删除成功返回确认信息，如果用户不存在则返回 404 错误
    """
    # 查询用户是否存在
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"用户 ID {user_id} 不存在"
        )
    
    # 删除用户
    try:
        db.delete(db_user)
        db.commit()
        return {
            "message": "用户删除成功",
            "deleted_user": {
                "id": db_user.id,
                "name": db_user.name,
                "email": db_user.email
            }
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"删除用户失败: {str(e)}"
        )


# ============ 静态文件和前端页面 ============
# 注意：这必须放在最后，否则会覆盖其他路由

# 挂载静态文件（CSS, JS）
app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")

# 根路径 - 返回前端页面
@app.get("/")
async def serve_frontend():
    """
    根路径，返回前端页面
    """
    return FileResponse(str(frontend_path / "index.html"))
