@echo off
echo === KHOI DONG FLASK TASK MANAGER ===
echo.

REM Tao moi truong ao neu chua co
if not exist venv\ (
    echo Dang tao moi truong ao...
    python -m venv venv
    echo Moi truong ao da duoc tao.
)

REM Kich hoat moi truong ao
call venv\Scripts\activate

REM Cai dat cac goi can thiet
echo Dang cai dat cac goi can thiet...
pip install flask flask-sqlalchemy flask-migrate flask-login flask-wtf email_validator waitress

REM Tao thu muc instance neu chua co
if not exist instance\ (
    mkdir instance
)

REM Khoi tao co so du lieu
if not exist instance\tasks.db (
    echo Khoi tao co so du lieu...
    python -c "from app import create_app, db; from app.models import User; app = create_app(); app.app_context().push(); db.create_all(); admin = User(username='admin', email='admin@example.com', is_admin=True); admin.set_password('admin123'); db.session.add(admin); user = User(username='user', email='user@example.com'); user.set_password('user123'); db.session.add(user); db.session.commit(); print('Da tao xong csdl va tai khoan!')"
)

REM Chay ung dung
echo.
echo === KHOI DONG UNG DUNG ===
echo.
echo Truy cap: http://127.0.0.1:5000
echo Tai khoan: admin@example.com / admin123
echo.

python run.py