from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from app.forms import LoginForm, RegistrationForm, ProfileUpdateForm
from app.models import User, db

from app.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

# Tạo các form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    remember_me = BooleanField('Ghi nhớ đăng nhập')
    submit = SubmitField('Đăng nhập')

class RegistrationForm(FlaskForm):
    username = StringField('Tên người dùng', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    confirm_password = PasswordField('Xác nhận mật khẩu', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Đăng ký')

class ProfileUpdateForm(FlaskForm):
    username = StringField('Tên người dùng', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    avatar = FileField('Cập nhật ảnh đại diện', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Cập nhật')

# Tạo blueprint cho phần xác thực
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Đăng nhập thành công!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('tasks.index'))
        flash('Email hoặc mật khẩu không chính xác', 'danger')
    return render_template('auth/login.html', title='Đăng nhập', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bạn đã đăng xuất thành công.', 'success')
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.password_hash = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Tài khoản của bạn đã được tạo!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Đăng ký', form=form)

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileUpdateForm()
    
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        
        if form.avatar.data:
            filename = secure_filename(form.avatar.data.filename)
            # Nếu không có avatar, có thể tạo avatar từ API bên ngoài
            if not filename:
                import requests
                response = requests.get('https://avatar-placeholder.iran.liara.run/')
                if response.status_code == 200:
                    filename = f"avatar_{current_user.id}.png"
            
            avatar_path = os.path.join(current_app.root_path, 'static/avatars', filename)
            if not os.path.exists(os.path.dirname(avatar_path)):
                os.makedirs(os.path.dirname(avatar_path))
                
            form.avatar.data.save(avatar_path)
            current_user.avatar = filename
        
        db.session.commit()
        flash('Hồ sơ của bạn đã được cập nhật!', 'success')
        return redirect(url_for('auth.profile'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    return render_template('auth/profile.html', title='Hồ sơ', form=form)