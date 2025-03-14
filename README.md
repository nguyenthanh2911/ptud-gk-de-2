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

1. khởi chạy
```

2. Tạo môi trường ảo:
```
python -m venv venv
```

3. Kích hoạt môi trường ảo:
- Trên Windows:
```
venv\Scripts\activate
```
- Trên macOS/Linux:
```
source venv/bin/activate
```

4. Cài đặt các gói cần thiết:
```
pip install -r requirements.txt
```

5. Thiết lập cơ sở dữ liệu:
```
flask db init
flask db migrate
flask db upgrade
```

6. Chạy ứng dụng:
```
flask run
```
7. Có thể thay đổi bước 5,6 bằng cách chạy file
```
run.py
```
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
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── tasks.py
│   ├── static
│   │   ├── css
│   │   │   ├── main.css
│   │   │   └── styles.css
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
│   └── README.md
├── tests
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_tasks.py
├── .gitignore
├── README.md
└── requirements.txt
```


