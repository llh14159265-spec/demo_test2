# FastAPI 管理系统

一个基于 FastAPI 的全栈管理系统，包含前后端分离架构、数据库集成和完整的 CRUD 功能。

## 项目结构

```
fastapi-management-system/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI 应用入口
│   │   ├── config.py               # 配置管理
│   │   ├── database.py             # 数据库连接
│   │   ├── models/                 # 数据库模型
│   │   ├── schemas/                # Pydantic 验证模型
│   │   ├── routes/                 # API 路由
│   │   ├── services/               # 业务逻辑
│   │   └── crud/                   # 数据访问层
│   ├── requirements.txt            # Python 依赖
│   └── run.py                      # 启动脚本
├── frontend/
│   ├── index.html                  # 主页面
│   ├── css/
│   │   └── style.css               # 样式文件
│   └── js/
│       └── app.js                  # 前端逻辑
├── docs/
│   ├── requirements.md             # 需求文档
│   ├── design.md                   # 设计文档
│   ├── tasks.md                    # 任务列表
│   ├── task-1-summary.md           # 任务 1 总结
│   └── task-2-summary.md           # 任务 2 总结
├── tests/
│   ├── test_api.py                 # API 测试
│   └── test_models.py              # 模型测试
├── pyproject.toml                  # uv 项目配置
├── .env                            # 环境变量
├── .gitignore                      # Git 忽略文件
└── README.md                       # 项目文档
```

## 快速开始

### 1. 激活虚拟环境

```bash
# Windows PowerShell
.venv\Scripts\activate

# 或者使用 uv
uv venv
```

### 2. 安装依赖

```bash
# 使用 uv（推荐）
uv pip install -e .

# 或者使用 pip
pip install -r requirements.txt
```

### 3. 运行后端服务

```bash
python backend/run.py
```

后端服务将在 `http://localhost:8000` 启动。

### 4. 访问 API 文档

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 5. 运行前端

在浏览器中打开 `frontend/index.html` 文件。

## 功能特性

- ✅ FastAPI 后端框架
- ✅ SQLite 数据库集成
- ✅ RESTful API 设计
- ✅ 数据验证和错误处理
- ✅ CORS 跨域支持
- ✅ 前端用户界面
- ✅ 完整的 CRUD 功能

## 开发进度

- [x] 项目初始化
- [x] 数据库模型定义
- [x] 数据验证模型
- [ ] 员工创建功能
- [ ] 员工列表查询
- [ ] 员工详情查询
- [ ] 员工更新功能
- [ ] 员工删除功能
- [ ] 批量删除功能
- [ ] 前端页面
- [ ] 前端样式
- [ ] 前端逻辑
- [ ] 集成测试

## 许可证

MIT
