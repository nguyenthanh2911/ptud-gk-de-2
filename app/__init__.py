from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

# Import cấu hình từ config.py
from config import config

# Khởi tạo các extension
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Vui lòng đăng nhập để truy cập trang này.'
login_manager.login_message_category = 'info'

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Cấu hình ứng dụng từ config dictionary
    app.config.from_object(config[config_name])
    
    # Khởi tạo các extension với app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Import và đăng ký các blueprint
    from app.routes.auth import bp as auth_bp
    from app.routes.tasks import bp as tasks_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    # Tạo thư mục lưu avatar nếu chưa tồn tại
    avatar_dir = os.path.join(app.static_folder, 'avatars')
    if not os.path.exists(avatar_dir):
        os.makedirs(avatar_dir)
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))
    
    return app