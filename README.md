# Thông tin sinh viên  
Nguyễn Văn Thành  
MSSV: 22724071  




# Flask Task Manager

Flask Task Manager là một ứng dụng quản lý tác vụ đơn giản được xây dựng bằng Flask và SQLite. Nó cho phép người dùng tạo, chỉnh sửa và quản lý các tác vụ trong khi theo dõi trạng thái hoàn thành và dấu thời gian của chúng. Người dùng cũng có thể tải lên ảnh đại diện và xem số lượng tác vụ quá hạn.

## chức năng

- Xác thực người dùng (đăng nhập, đăng ký, quản lý hồ sơ)
- Quản lý tác vụ (tạo, chỉnh sửa, xem tác vụ)
- Theo dõi trạng thái hoàn thành
- Theo dõi dấu thời gian cho các tác vụ
- Tải lên ảnh đại diện cho người dùng
- Hiển thị các tác vụ quá hạn với chỉ báo cảnh báo

## cài đặt

### Cài đặt tự động (Nếu lỗi Thầy hãy cài đăt thủ công)

#### Windows:
```
run.bat
```


### Cài đặt thủ công

1. Tạo môi trường ảo:
```
python -m venv venv
```

2. Kích hoạt môi trường ảo:
- Trên Windows:
```
venv\Scripts\activate
```
- Trên macOS/Linux:
```
source venv/bin/activate
```

3. Cài đặt các gói cần thiết:
```
pip install -r requirements.txt
```

4. Thiết lập cơ sở dữ liệu:
```
flask db init
flask db migrate
flask db upgrade
```

5. Chạy ứng dụng:
```
flask run
```
hoặc
```
python run.py
```

## Tài khoản mặc định

Sau khi chạy script tự động, hệ thống sẽ được tạo với các tài khoản mặc định:

- **Admin**: admin@example.com / admin123
- **User**: user@example.com / user123

## Sử dụng 

- Đăng ký tài khoản mới hoặc đăng nhập bằng tài khoản hiện có.
- Quản lý nhiệm vụ của bạn và xem hồ sơ của bạn, bao gồm cả ảnh đại diện và nhiệm vụ quá hạn.

## Cấu trúc cây

```
flask-task-manager
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── forms.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── tasks.py
│   ├── static
│   │   ├── css
│   │   │   ├── main.css
│   │   │   └── styles.css
│   │   ├── avatars
│   │   └── js
│   │       └── main.js
│   └── templates
│       ├── auth
│       │   ├── login.html
│       │   ├── profile.html
│       │   └── register.html
│       ├── base.html
│       └── tasks
│           ├── create.html
│           ├── edit.html
│           ├── index.html
│           └── view.html
├── instance
│   └── tasks.db
├── migrations
├── .gitignore
├── run.bat
├── run.py
├── README.md
└── requirements.txt
```
