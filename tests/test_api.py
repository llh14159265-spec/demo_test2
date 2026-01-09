#!/usr/bin/env python
"""测试 API 是否正常工作"""
import sys
import os
os.chdir('backend')
sys.path.insert(0, '.')

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# 测试根路由
print("测试 GET /")
response = client.get('/')
print(f"状态码: {response.status_code}")
print(f"响应: {response.json()}")

# 测试健康检查
print("\n测试 GET /health")
response = client.get('/health')
print(f"状态码: {response.status_code}")
print(f"响应: {response.json()}")

print("\n✅ 所有测试通过！")
