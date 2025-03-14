from app import create_app, db
from app.models import User, Task
import os

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Task': Task}

if __name__ == '__main__':
    # Trong môi trường phát triển
    if app.config.get('DEBUG', False):
        app.run(debug=True)
    # Trong môi trường sản xuất
    else:
        # Sử dụng production server configuration
        # host='0.0.0.0' cho phép truy cập từ các máy khác
        app.run(host='0.0.0.0', port=5000, debug=False)