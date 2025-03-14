from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from datetime import datetime

from app.models import Task, User, db
from app.forms import TaskForm


bp = Blueprint('tasks', __name__)

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    # Lấy các task dựa trên vai trò người dùng
    if current_user.is_admin:
        tasks = Task.query.all()
    else:
        tasks = Task.query.filter_by(user_id=current_user.id).all()
    
    # Đếm số lượng task quá hạn
    overdue_count = 0
    for task in tasks:
        if not task.finished and task.deadline and task.deadline < datetime.now():
            overdue_count += 1
    
    return render_template('tasks/index.html', title='Quản lý công việc', tasks=tasks, overdue_count=overdue_count)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = TaskForm()
    
    if request.method == 'POST':
        print(f"Form data: {request.form}")  # Debug: in dữ liệu form
        print(f"Form errors: {form.errors}")  # Debug: in lỗi form
        
        if form.validate_on_submit():
            print("Form validated successfully")  # Debug: kiểm tra form đã được xác thực
            
            task = Task(
                title=form.title.data,
                description=form.description.data,
                deadline=form.deadline.data,
                status=form.status.data,
                user_id=current_user.id,
                created=datetime.now()
            )
            
            if form.status.data == 'completed':
                task.finished = datetime.now()
                
            db.session.add(task)
            db.session.commit()
            flash('Công việc đã được tạo thành công!', 'success')
            return redirect(url_for('tasks.index'))
    
    return render_template('tasks/create.html', title='Tạo công việc mới', form=form)

@bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Kiểm tra quyền chỉnh sửa task
    if not current_user.is_admin and task.user_id != current_user.id:
        flash('Bạn không có quyền chỉnh sửa công việc này.', 'danger')
        return redirect(url_for('tasks.index'))
    
    form = TaskForm(obj=task)
    
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.deadline = form.deadline.data
        task.status = form.status.data
        
        if form.status.data == 'completed' and not task.finished:
            task.finished = datetime.now()
        elif form.status.data != 'completed' and task.finished:
            task.finished = None
            
        db.session.commit()
        flash('Công việc đã được cập nhật thành công!', 'success')
        return redirect(url_for('tasks.index'))
    
    return render_template('tasks/edit.html', title='Chỉnh sửa công việc', form=form, task=task)

@bp.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Kiểm tra quyền xóa task
    if not current_user.is_admin and task.user_id != current_user.id:
        flash('Bạn không có quyền xóa công việc này.', 'danger')
        return redirect(url_for('tasks.index'))
    
    db.session.delete(task)
    db.session.commit()
    flash('Công việc đã được xóa thành công!', 'success')
    return redirect(url_for('tasks.index'))

@bp.route('/view/<int:task_id>')
@login_required
def view(task_id):
    task = Task.query.get_or_404(task_id)
    
    # Kiểm tra quyền xem task
    if not current_user.is_admin and task.user_id != current_user.id:
        flash('Bạn không có quyền xem công việc này.', 'danger')
        return redirect(url_for('tasks.index'))
    
    return render_template('tasks/view.html', title=task.title, task=task)