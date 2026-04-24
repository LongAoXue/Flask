# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # 用于session加密

# 主页路由
@app.route('/')
def index():
    return render_template('index.html', title='首页')

# 带参数的路由
@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello, {name}!</h1>'

# 带类型转换的路由
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

# 支持多种HTTP方法
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # 简单验证
        if username == 'admin' and password == '123456':
            session['user'] = username
            flash('登录成功！', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('用户名或密码错误！', 'error')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('您已登出', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)