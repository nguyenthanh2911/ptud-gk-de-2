<!-- filepath: c:\Users\nguye\Downloads\flask-task-manager\run.bat -->
@echo off
echo === KHOI DONG FLASK TASK MANAGER ===
echo.

REM Kiem tra va tao moi truong ao neu chua co
if not exist venv\ (
    echo Dang tao moi truong ao...
    python -m venv venv
    echo Moi truong ao da duoc tao.
) else (
    echo Moi truong ao da ton tai.
)

REM Kich hoat moi truong ao
echo Dang kich hoat moi truong ao...
call venv\Scripts\activate

REM Kiem tra va cai dat cac goi can thiet
if not exist requirements.txt (
    echo Tao file requirements.txt co ban...
    echo flask==2.3.3 > requirements.txt
    echo flask-sqlalchemy==3.1.1 >> requirements.txt
    echo flask-migrate==4.0.5 >> requirements.txt
    echo flask-login==0.6.3 >> requirements.txt
    echo flask-wtf==1.2.1 >> requirements.txt
    echo email_validator==2.1.0 >> requirements.txt
)

echo Dang cai dat cac goi can thiet...
pip install -r requirements.txt

REM Kiem tra thu muc instance
if not exist instance\ (
    mkdir instance
    echo Thu muc instance da duoc tao.
)

REM Kiem tra va khoi tao co so du lieu
echo Dang khoi tao co so du lieu...

if not exist instance\tasks.db (
    echo Khoi tao co so du lieu moi...
    python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all();"
    echo Co so du lieu da duoc tao.
    
    REM Tao tai khoan admin va user mac dinh
    echo Dang tao tai khoan mac dinh...
    python -c "from app import create_app, db; from app.models import User; app = create_app(); app.app_context().push(); admin = User(username='admin', email='admin@example.com', is_admin=True); admin.set_password('admin123'); db.session.add(admin); user = User(username='user', email='user@example.com'); user.set_password('user123'); db.session.add(user); db.session.commit();"
    echo Tai khoan mac dinh da duoc tao.
) else (
    echo Co so du lieu da ton tai.
)

REM Chay ung dung
echo.
echo === KHOI DONG UNG DUNG ===
echo.
echo Truy cap: http://127.0.0.1:5000
echo Tai khoan admin mac dinh: admin@example.com / admin123
echo Tai khoan user mac dinh: user@example.com / user123
echo.
echo Nhan Ctrl+C de dung ung dung.
echo.

python run.py