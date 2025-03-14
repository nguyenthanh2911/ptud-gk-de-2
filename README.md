# Flask Task Manager

Flask Task Manager is a simple task management application built using Flask and SQLite. It allows users to create, edit, and manage tasks while tracking their completion status and timestamps. Users can also upload avatars and view the number of overdue tasks.

## Features

- User authentication (login, registration, profile management)
- Task management (create, edit, view tasks)
- Completion status tracking
- Timestamp tracking for tasks
- Avatar upload for users
- Display of overdue tasks with a warning indicator

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-task-manager
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```
   flask run
   ```

## Usage

- Navigate to `http://127.0.0.1:5000` in your web browser.
- Register a new account or log in with an existing account.
- Manage your tasks and view your profile, including your avatar and overdue tasks.

## Directory Structure

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.# ptud-gk-de-2
