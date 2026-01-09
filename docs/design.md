# FastAPI 管理系统 - 设计文档

## 概述

这是一个基于 FastAPI 的全栈管理系统，采用前后端分离架构。后端使用 FastAPI 框架提供 RESTful API，前端使用 HTML/CSS/JavaScript 实现用户界面，数据库使用 SQLite（开发环境）或 PostgreSQL（生产环境）。

系统采用渐进式开发方式，逐步实现各项功能，确保每个阶段都能正常工作。

## 架构

```
┌─────────────────────────────────────────────────────────────┐
│                     前端应用 (Frontend)                      │
│              HTML/CSS/JavaScript 用户界面                    │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/JSON
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   后端 API (FastAPI)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              路由层 (Routes)                          │  │
│  │  - 资源创建、读取、更新、删除端点                    │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              业务逻辑层 (Services)                    │  │
│  │  - 数据验证、业务规则处理                            │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              数据访问层 (DAL)                         │  │
│  │  - 数据库操作、ORM 映射                              │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │ SQL
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   数据库 (SQLite/PostgreSQL)                 │
│              存储系统数据的持久化层                          │
└─────────────────────────────────────────────────────────────┘
```

## 组件和接口

### 1. 后端项目结构

```
fastapi-management-system/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI 应用入口
│   │   ├── config.py               # 配置管理
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── employee.py         # 数据库模型（以员工为例）
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── employee.py         # Pydantic 数据验证模型
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── employees.py        # 员工相关路由
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── employee_service.py # 员工业务逻辑
│   │   ├── database.py             # 数据库连接和会话管理
│   │   └── crud/
│   │       ├── __init__.py
│   │       └── employee.py         # 员工数据访问操作
│   ├── requirements.txt            # Python 依赖
│   └── run.py                      # 启动脚本
├── frontend/
│   ├── index.html                  # 主页面
│   ├── css/
│   │   └── style.css               # 样式文件
│   └── js/
│       └── app.js                  # 前端逻辑
└── README.md
```

### 2. 数据模型

#### Employee（员工）模型

```python
# 数据库模型
class Employee(Base):
    __tablename__ = "employees"
    
    id: int (主键，自增)
    name: str (员工名称，非空)
    email: str (邮箱，唯一)
    position: str (职位)
    salary: float (薪资)
    created_at: datetime (创建时间)
    updated_at: datetime (更新时间)
```

#### Pydantic 验证模型

```python
# 创建/更新请求
class EmployeeCreate(BaseModel):
    name: str (非空，长度 1-100)
    email: str (有效邮箱格式)
    position: str (非空)
    salary: float (大于 0)

# 响应模型
class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    position: str
    salary: float
    created_at: datetime
    updated_at: datetime
```

### 3. API 端点设计

| 方法 | 端点 | 功能 | 请求体 | 响应 |
|------|------|------|--------|------|
| POST | /api/employees | 创建员工 | EmployeeCreate | EmployeeResponse |
| GET | /api/employees | 获取员工列表 | - | List[EmployeeResponse] |
| GET | /api/employees/{id} | 获取员工详情 | - | EmployeeResponse |
| PUT | /api/employees/{id} | 更新员工 | EmployeeCreate | EmployeeResponse |
| DELETE | /api/employees/{id} | 删除员工 | - | {message: "success"} |
| DELETE | /api/employees | 批量删除 | {ids: [1,2,3]} | {message: "success"} |

### 4. 前端页面结构

#### 主页面 (index.html)
- 员工列表表格
- 创建/编辑表单
- 删除确认对话框
- 操作按钮（新增、编辑、删除）

#### 前端 API 调用 (app.js)
- 获取员工列表
- 创建新员工
- 更新员工信息
- 删除员工
- 错误处理和用户提示

## 数据模型

### 数据库表结构

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    position VARCHAR(100) NOT NULL,
    salary FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 数据流

1. **创建流程**: 前端表单 → 验证 → API 请求 → 业务逻辑 → 数据库插入 → 返回新记录
2. **读取流程**: 前端请求 → API 查询 → 数据库检索 → 返回列表/详情
3. **更新流程**: 前端表单 → 验证 → API 请求 → 业务逻辑 → 数据库更新 → 返回更新记录
4. **删除流程**: 前端确认 → API 请求 → 业务逻辑 → 数据库删除 → 返回成功信息

## 正确性属性

一个属性是一个特征或行为，应该在系统的所有有效执行中保持真实——本质上是关于系统应该做什么的正式陈述。属性充当人类可读规范和机器可验证正确性保证之间的桥梁。

### 属性 1: 创建后资源存在

**验证: 需求 3.3**

对于任何有效的员工数据，创建该员工后，通过 ID 查询应该返回相同的员工信息。

### 属性 2: 更新后数据一致

**验证: 需求 5.1**

对于任何现有员工，更新其信息后，查询该员工应该返回更新后的数据。

### 属性 3: 删除后资源不存在

**验证: 需求 6.1**

对于任何现有员工，删除该员工后，通过 ID 查询应该返回 404 错误。

### 属性 4: 列表包含所有资源

**验证: 需求 4.1**

对于任何创建的员工，获取员工列表应该包含该员工。

### 属性 5: 无效数据被拒绝

**验证: 需求 3.2**

对于任何无效的员工数据（如空名字、无效邮箱），创建请求应该返回验证错误。

### 属性 6: 不存在资源返回 404

**验证: 需求 4.3, 5.2, 6.2**

对于任何不存在的员工 ID，查询、更新或删除请求应该返回 404 错误。

## 错误处理

### HTTP 状态码

- **200 OK**: 请求成功
- **201 Created**: 资源创建成功
- **400 Bad Request**: 请求数据验证失败
- **404 Not Found**: 资源不存在
- **500 Internal Server Error**: 服务器错误

### 错误响应格式

```json
{
    "detail": "错误描述信息",
    "status_code": 400
}
```

### 验证错误

```json
{
    "detail": [
        {
            "loc": ["body", "email"],
            "msg": "invalid email format",
            "type": "value_error.email"
        }
    ]
}
```

## 测试策略

### 单元测试

- 测试数据验证模型（Pydantic schemas）
- 测试业务逻辑函数
- 测试数据访问层（CRUD 操作）
- 测试错误处理

### 属性测试

- 属性 1: 创建后资源存在 - 验证创建的资源可以被查询到
- 属性 2: 更新后数据一致 - 验证更新操作正确修改了数据
- 属性 3: 删除后资源不存在 - 验证删除操作成功移除了资源
- 属性 4: 列表包含所有资源 - 验证列表查询返回所有创建的资源
- 属性 5: 无效数据被拒绝 - 验证验证层正确拒绝无效输入
- 属性 6: 不存在资源返回 404 - 验证对不存在资源的操作返回正确错误

### 集成测试

- 测试完整的 CRUD 流程
- 测试前后端通信
- 测试数据库事务

### 测试框架

- **单元测试**: pytest
- **属性测试**: hypothesis
- **API 测试**: pytest + httpx
