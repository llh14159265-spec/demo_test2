<<<<<<< HEAD
# demo_test2
=======
# FastAPI 管理系统

一个基于 FastAPI 的全栈管理系统，包含前后端分离架构、SQLite 数据库和完整的 CRUD 功能。

## 项目结构

```
FastApi_T1/
├── backend/
│   ├── main.py          # FastAPI 主程序
│   ├── database.py      # 数据库配置
│   ├── models.py        # 数据库模型
│   └── schemas.py       # Pydantic 数据验证
├── frontend/
│   ├── index.html       # 前端页面
│   ├── style.css        # 样式文件
│   └── app.js           # JavaScript 逻辑
├── pyproject.toml       # 项目配置和依赖
└── README.md            # 项目说明
```

## 快速开始

### 1. 安装依赖（使用 uv）

```bash
# 初始化项目并安装依赖
uv sync
```

### 2. 运行后端服务

```bash
# 使用 uv 运行
uv run uvicorn backend.main:app --reload

# 或者传统方式
uvicorn backend.main:app --reload
```

后端服务将在 `http://localhost:8000` 启动。

### 3. 访问 API 文档

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 4. 访问前端

在浏览器中打开 `frontend/index.html` 文件，或者通过后端静态文件服务访问。

## 技术栈

- **后端**: FastAPI 0.104.1
- **服务器**: Uvicorn 0.24.0
- **数据库**: SQLite + SQLAlchemy 2.0.23
- **数据验证**: Pydantic 2.5.0
- **前端**: 原生 HTML + CSS + JavaScript

## 功能特性

- ✅ RESTful API 设计
- ✅ 自动生成 API 文档
- ✅ 数据验证和错误处理
- ✅ CORS 跨域支持
- ✅ 完整的 CRUD 操作
- ✅ 现代化前端界面

## 开发进度

- [x] 项目初始化
- [ ] 数据库模型定义
- [ ] API 接口 - 创建（POST）
- [ ] API 接口 - 查询（GET）
- [ ] API 接口 - 更新（PUT）
- [ ] API 接口 - 删除（DELETE）
- [ ] 前端界面开发
- [ ] 功能测试

## 许可证

MIT
>>>>>>> feature_2
