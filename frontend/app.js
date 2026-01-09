// API 基础地址
const API_BASE_URL = 'http://127.0.0.1:8000';

// 全局变量
let currentDeleteUserId = null;

// ==================== 初始化 ====================
document.addEventListener('DOMContentLoaded', () => {
    // 加载用户列表
    loadUsers();
    
    // 绑定事件
    document.getElementById('userForm').addEventListener('submit', handleCreateUser);
    document.getElementById('editForm').addEventListener('submit', handleUpdateUser);
    document.getElementById('refreshBtn').addEventListener('click', loadUsers);
});

// ==================== 显示提示消息 ====================
function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast ${type} show`;
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// ==================== 加载用户列表 ====================
async function loadUsers() {
    const userList = document.getElementById('userList');
    userList.innerHTML = '<div class="loading">加载中</div>';
    
    try {
        const response = await fetch(`${API_BASE_URL}/users`);
        
        if (!response.ok) {
            throw new Error('获取用户列表失败');
        }
        
        const users = await response.json();
        
        if (users.length === 0) {
            userList.innerHTML = '<div class="empty-state">暂无用户数据</div>';
            return;
        }
        
        // 渲染用户卡片
        userList.innerHTML = users.map(user => createUserCard(user)).join('');
        
    } catch (error) {
        console.error('加载用户失败:', error);
        userList.innerHTML = '<div class="empty-state">加载失败，请稍后重试</div>';
        showToast('加载用户列表失败', 'error');
    }
}

// ==================== 创建用户卡片 HTML ====================
function createUserCard(user) {
    const createdDate = new Date(user.created_at).toLocaleString('zh-CN');
    const age = user.age !== null ? `${user.age} 岁` : '未填写';
    
    return `
        <div class="user-card">
            <div class="user-id">#${user.id}</div>
            <h3 class="user-name">${escapeHtml(user.name)}</h3>
            <div class="user-info">
                <div class="user-info-item">邮箱: ${escapeHtml(user.email)}</div>
                <div class="user-info-item">年龄: ${age}</div>
                <div class="user-info-item">创建时间: ${createdDate}</div>
            </div>
            <div class="user-actions">
                <button class="btn btn-secondary" onclick="openEditModal(${user.id})">
                    <span class="btn-icon">✎</span>
                    编辑
                </button>
                <button class="btn btn-danger" onclick="openDeleteModal(${user.id}, '${escapeHtml(user.name)}')">
                    <span class="btn-icon">✕</span>
                    删除
                </button>
            </div>
        </div>
    `;
}

// ==================== HTML 转义（防止 XSS）====================
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ==================== 创建用户 ====================
async function handleCreateUser(e) {
    e.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value.trim(),
        email: document.getElementById('email').value.trim(),
        age: document.getElementById('age').value ? parseInt(document.getElementById('age').value) : null
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}/users`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8'
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || '创建用户失败');
        }
        
        const newUser = await response.json();
        
        // 清空表单
        document.getElementById('userForm').reset();
        
        // 刷新列表
        await loadUsers();
        
        showToast(`用户 ${newUser.name} 创建成功！`, 'success');
        
    } catch (error) {
        console.error('创建用户失败:', error);
        showToast(error.message, 'error');
    }
}

// ==================== 打开编辑模态框 ====================
async function openEditModal(userId) {
    try {
        const response = await fetch(`${API_BASE_URL}/users/${userId}`);
        
        if (!response.ok) {
            throw new Error('获取用户信息失败');
        }
        
        const user = await response.json();
        
        // 填充表单
        document.getElementById('editUserId').value = user.id;
        document.getElementById('editName').value = user.name;
        document.getElementById('editEmail').value = user.email;
        document.getElementById('editAge').value = user.age || '';
        
        // 显示模态框
        document.getElementById('editModal').classList.add('show');
        
    } catch (error) {
        console.error('获取用户信息失败:', error);
        showToast('获取用户信息失败', 'error');
    }
}

// ==================== 关闭编辑模态框 ====================
function closeEditModal() {
    document.getElementById('editModal').classList.remove('show');
    document.getElementById('editForm').reset();
}

// ==================== 更新用户 ====================
async function handleUpdateUser(e) {
    e.preventDefault();
    
    const userId = document.getElementById('editUserId').value;
    const formData = {
        name: document.getElementById('editName').value.trim(),
        email: document.getElementById('editEmail').value.trim(),
        age: document.getElementById('editAge').value ? parseInt(document.getElementById('editAge').value) : null
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}/users/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json; charset=utf-8'
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || '更新用户失败');
        }
        
        const updatedUser = await response.json();
        
        // 关闭模态框
        closeEditModal();
        
        // 刷新列表
        await loadUsers();
        
        showToast(`用户 ${updatedUser.name} 更新成功！`, 'success');
        
    } catch (error) {
        console.error('更新用户失败:', error);
        showToast(error.message, 'error');
    }
}

// ==================== 打开删除确认模态框 ====================
function openDeleteModal(userId, userName) {
    currentDeleteUserId = userId;
    document.getElementById('deleteUserName').textContent = userName;
    document.getElementById('deleteModal').classList.add('show');
}

// ==================== 关闭删除确认模态框 ====================
function closeDeleteModal() {
    currentDeleteUserId = null;
    document.getElementById('deleteModal').classList.remove('show');
}

// ==================== 确认删除用户 ====================
async function confirmDelete() {
    if (!currentDeleteUserId) return;
    
    try {
        const response = await fetch(`${API_BASE_URL}/users/${currentDeleteUserId}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || '删除用户失败');
        }
        
        const result = await response.json();
        
        // 关闭模态框
        closeDeleteModal();
        
        // 刷新列表
        await loadUsers();
        
        showToast(result.message || '用户删除成功！', 'success');
        
    } catch (error) {
        console.error('删除用户失败:', error);
        showToast(error.message, 'error');
    }
}

// ==================== 点击模态框外部关闭 ====================
window.addEventListener('click', (e) => {
    const editModal = document.getElementById('editModal');
    const deleteModal = document.getElementById('deleteModal');
    
    if (e.target === editModal) {
        closeEditModal();
    }
    
    if (e.target === deleteModal) {
        closeDeleteModal();
    }
});
