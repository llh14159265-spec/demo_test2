# 上传指南

这个文件夹 `fastapi-management-system/` 包含了所有需要上传到 Git 仓库的文件。

## 文件夹结构

```
fastapi-management-system/
├── backend/                        # 后端代码
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                # FastAPI 应用
│   │   ├── config.py              # 配置管理
│   │   ├── database.py            # 数据库连接
│   │   ├── models/                # 数据库模型
│   │   ├── schemas/               # Pydantic 验证模型
│   │   ├── routes/                # API 路由（待实现）
│   │   ├── services/              # 业务逻辑
│   │   └── crud/                  # 数据访问层
│   ├── run.py                     # 启动脚本
│   └── requirements.txt           # 依赖列表
├── frontend/                      # 前端代码（待实现）
├── docs/                          # 文档
│   ├── requirements.md            # 需求文档
│   ├── design.md                  # 设计文档
│   ├── tasks.md                   # 任务列表
│   ├── task-1-summary.md          # 任务 1 总结
│   └── task-2-summary.md          # 任务 2 总结
├── tests/                         # 测试文件
│   ├── test_api.py                # API 测试
│   └── test_models.py             # 模型测试
├── pyproject.toml                 # uv 项目配置
├── .env                           # 环境变量
├── .gitignore                     # Git 忽略文件
├── README.md                      # 项目文档
└── UPLOAD_GUIDE.md               # 本文件
```

## Git 操作步骤

### 1. 初始化 Git 仓库（如果还没有）

```bash
git init
git config user.name "你的名字"
git config user.email "你的邮箱"
```

### 2. 创建 feature 分支

```bash
git checkout -b feature/database-setup
```

### 3. 添加所有文件

```bash
git add .
```

### 4. 查看要提交的文件

```bash
git status
```

### 5. 提交代码

```bash
git commit -m "feat: 初始化项目和数据库模型

- 项目初始化和依赖配置（任务 1）
- 数据库配置和模型定义（任务 2）
- Pydantic 数据验证模型（任务 3）
- FastAPI 应用主文件和基础配置（任务 4）

包含：
- FastAPI 应用框架
- SQLAlchemy ORM 模型
- Pydantic 数据验证
- CRUD 操作层
- 业务逻辑服务层
- 数据库初始化脚本
- 测试脚本验证"
```

### 6. 推送到远程仓库

```bash
git push origin feature/database-setup
```

### 7. 创建 Pull Request

在 GitHub/GitLab 上创建 PR，使用以下模板：

**标题：**
```
feat: 初始化项目和数据库模型
```

**描述：**
```markdown
## 功能描述
初始化 FastAPI 管理系统的基础框架和数据库层

## 完成的任务
- [x] 任务 1: 项目初始化和依赖配置
- [x] 任务 2: 数据库配置和模型定义
- [x] 任务 3: Pydantic 数据验证模型
- [x] 任务 4: FastAPI 应用主文件和基础配置

## 验证
- ✅ 所有模型测试通过
- ✅ API 端点正常工作
- ✅ 数据库初始化成功

## 相关文件
- backend/app/models/employee.py - Employee 数据库模型
- backend/app/schemas/employee.py - Pydantic 验证模型
- backend/app/crud/employee.py - CRUD 操作
- backend/app/services/employee_service.py - 业务逻辑服务
- backend/app/main.py - FastAPI 应用
- docs/ - 完整的需求、设计和任务文档
```

## 后续功能添加

当你完成新的功能时，按照以下步骤添加到这个文件夹：

1. **创建新的 feature 分支**
   ```bash
   git checkout -b feature/create-employee-api
   ```

2. **在相应的文件夹中添加代码**
   - 新的路由放在 `backend/app/routes/`
   - 新的模型放在 `backend/app/models/`
   - 新的验证模型放在 `backend/app/schemas/`
   - 新的测试放在 `tests/`

3. **更新文档**
   - 更新 `docs/tasks.md` 标记完成的任务
   - 创建新的任务总结文档（如 `docs/task-3-summary.md`）

4. **提交并推送**
   ```bash
   git add .
   git commit -m "feat: 实现员工创建功能"
   git push origin feature/create-employee-api
   ```

5. **创建 Pull Request**

## 文件说明

### 核心文件

| 文件 | 说明 |
|------|------|
| `backend/app/main.py` | FastAPI 应用主文件，包含路由和中间件配置 |
| `backend/app/config.py` | 应用配置，支持环境变量 |
| `backend/app/database.py` | 数据库连接和会话管理 |
| `backend/app/models/` | SQLAlchemy ORM 模型 |
| `backend/app/schemas/` | Pydantic 数据验证模型 |
| `backend/app/crud/` | 数据访问层（CRUD 操作） |
| `backend/app/services/` | 业务逻辑层 |
| `backend/app/routes/` | API 路由（待实现） |

### 配置文件

| 文件 | 说明 |
|------|------|
| `pyproject.toml` | uv 项目配置和依赖定义 |
| `.env` | 环境变量（数据库 URL、应用名称等） |
| `.gitignore` | Git 忽略文件列表 |
| `backend/requirements.txt` | pip 依赖列表 |

### 文档文件

| 文件 | 说明 |
|------|------|
| `README.md` | 项目概览和快速开始 |
| `docs/requirements.md` | 需求文档 |
| `docs/design.md` | 设计文档 |
| `docs/tasks.md` | 任务列表 |
| `docs/task-1-summary.md` | 任务 1 实现总结 |
| `docs/task-2-summary.md` | 任务 2 实现总结 |

### 测试文件

| 文件 | 说明 |
|------|------|
| `tests/test_api.py` | API 端点测试 |
| `tests/test_models.py` | 数据库模型测试 |

## 注意事项

1. **不要上传的文件**
   - `.venv/` - 虚拟环境（已在 .gitignore 中）
   - `*.db` - SQLite 数据库文件（已在 .gitignore 中）
   - `__pycache__/` - Python 缓存（已在 .gitignore 中）
   - `.env.local` - 本地环境变量（已在 .gitignore 中）

2. **环境变量**
   - `.env` 文件包含默认配置
   - 生产环境应使用 `.env.production` 或环境变量

3. **依赖管理**
   - 使用 `pyproject.toml` 定义依赖
   - 使用 `uv pip install -e .` 安装
   - 更新依赖后更新 `backend/requirements.txt`

4. **代码风格**
   - 遵循 PEP 8 规范
   - 使用类型提示
   - 添加文档字符串

## 常见问题

**Q: 如何添加新的依赖？**
A: 编辑 `pyproject.toml`，然后运行 `uv pip install -e .`

**Q: 如何运行测试？**
A: 运行 `pytest tests/`

**Q: 如何启动应用？**
A: 运行 `python backend/run.py`

**Q: 如何访问 API 文档？**
A: 启动应用后访问 `http://localhost:8000/docs`

## 联系方式

如有问题，请查看相关文档或提交 Issue。
