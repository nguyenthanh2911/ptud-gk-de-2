from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SelectField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Optional, Email, EqualTo, Length, ValidationError
from flask_wtf.file import FileField, FileAllowed
from datetime import datetime

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email không được để trống'), Email(message='Email không hợp lệ')])
    password = PasswordField('Mật khẩu', validators=[DataRequired(message='Mật khẩu không được để trống')])
    remember_me = BooleanField('Ghi nhớ đăng nhập')
    submit = SubmitField('Đăng nhập')

class RegistrationForm(FlaskForm):
    username = StringField('Tên người dùng', validators=[
        DataRequired(message='Tên người dùng không được để trống'), 
        Length(min=3, max=64, message='Tên người dùng phải có từ 3 đến 64 ký tự')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email không được để trống'), 
        Email(message='Email không hợp lệ')
    ])
    password = PasswordField('Mật khẩu', validators=[
        DataRequired(message='Mật khẩu không được để trống'),
        Length(min=6, message='Mật khẩu phải có ít nhất 6 ký tự')
    ])
    confirm_password = PasswordField('Xác nhận mật khẩu', validators=[
        DataRequired(message='Vui lòng xác nhận mật khẩu'),
        EqualTo('password', message='Mật khẩu không khớp')
    ])
    submit = SubmitField('Đăng ký')

class ProfileUpdateForm(FlaskForm):
    username = StringField('Tên người dùng', validators=[
        DataRequired(message='Tên người dùng không được để trống'), 
        Length(min=3, max=64, message='Tên người dùng phải có từ 3 đến 64 ký tự')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email không được để trống'), 
        Email(message='Email không hợp lệ')
    ])
    avatar = FileField('Cập nhật ảnh đại diện', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], message='Chỉ chấp nhận file hình ảnh (jpg, jpeg, png)')
    ])
    submit = SubmitField('Cập nhật')

class TaskForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[
        DataRequired(message='Tiêu đề không được để trống'),
        Length(min=3, max=100, message='Tiêu đề phải có từ 3 đến 100 ký tự')
    ])
    description = TextAreaField('Mô tả', validators=[Optional()])
    deadline = DateTimeField('Hạn chót', format='%Y-%m-%dT%H:%M', validators=[
        DataRequired(message='Hạn chót không được để trống')
    ])
    status = SelectField('Trạng thái', choices=[
        ('pending', 'Chờ xử lý'),
        ('in_progress', 'Đang thực hiện'),
        ('completed', 'Hoàn thành')
    ], validators=[DataRequired(message='Trạng thái không được để trống')])
    submit = SubmitField('Lưu')
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Đặt giá trị mặc định là thời gian hiện tại khi tạo form mới
        if not args and 'obj' not in kwargs:
            self.deadline.data = datetime.now()