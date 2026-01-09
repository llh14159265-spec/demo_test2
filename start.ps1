# FastAPI 用户管理系统 - 启动脚本

Write-Host "================================" -ForegroundColor Cyan
Write-Host "  用户管理系统启动中..." -ForegroundColor Yellow
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# 启动后端服务
Write-Host "[1/2] 启动后端服务..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "uv run uvicorn backend.main:app --reload"

# 等待服务启动
Write-Host "[2/2] 等待服务启动..." -ForegroundColor Green
Start-Sleep -Seconds 3

# 打开浏览器
Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "  服务已启动！" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "前端地址: http://127.0.0.1:8000" -ForegroundColor Yellow
Write-Host "API 文档: http://127.0.0.1:8000/docs" -ForegroundColor Yellow
Write-Host ""
Write-Host "正在打开浏览器..." -ForegroundColor Green

Start-Process "http://127.0.0.1:8000"

Write-Host ""
Write-Host "按任意键退出..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
