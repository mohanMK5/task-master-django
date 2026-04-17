# TaskMaster - Task Management (To-Do List) Application

A simple and elegant Task Management web application built with Django.

## Features

- **Add Tasks**: Create new tasks with title and optional description
- **View Tasks**: See all your tasks in a clean, organized list
- **Mark Complete**: Toggle task completion status with a single click
- **Delete Tasks**: Remove tasks you no longer need

## Technical Stack

- **Framework**: Django 5.x
- **Language**: Python 3.11
- **Database**: SQLite (built-in)
- **Frontend**: HTML5, CSS3

## Project Structure

```
taskmaster/
├── manage.py                 # Django management script
├── taskmaster/               # Main Django project folder
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── ...
├── tasks/                    # Tasks app
│   ├── models.py            # Task model (database schema)
│   ├── views.py             # View functions (business logic)
│   ├── urls.py              # URL routing for tasks
│   ├── admin.py             # Admin configuration
│   └── ...
├── templates/               # HTML templates
│   └── tasks/
│       ├── base.html        # Base template
│       └── task_list.html   # Main task list page
└── static/                  # Static files (CSS)
    └── tasks/
        └── style.css        # Application styles
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Django 5.x

### Step 1: Install Django

If Django is not installed, run:

```bash
pip install django
```

### Step 2: Navigate to Project Directory

```bash
cd taskmaster
```

### Step 3: Run Migrations

Create the database tables:

```bash
python manage.py migrate
```

### Step 4: Start the Development Server

```bash
python manage.py runserver
```

### Step 5: Open the Application

Open your web browser and go to:

```
http://127.0.0.1:8000/
```

## How to Use

### Adding a Task

1. Enter a task title in the input field (required)
2. Optionally add a description
3. Click "Add Task" button

### Marking a Task Complete

- Click the checkbox next to any task to toggle its completion status
- Completed tasks will show with a strikethrough style

### Deleting a Task

- Click the "Delete" button on any task
- Confirm the deletion in the popup dialog

## Creating an Admin User (Optional)

To access the Django admin interface:

```bash
python manage.py createsuperuser
```

Then go to `http://127.0.0.1:8000/admin/` and log in.

## Database

The application uses SQLite by default. The database file (`db.sqlite3`) is automatically created when you run migrations.

## Customization

### Changing the Database

To use a different database (e.g., PostgreSQL, MySQL), update the `DATABASES` setting in `taskmaster/settings.py`.

### Adding More Features

- Edit `tasks/models.py` to add new fields to Task
- Edit `tasks/views.py` to add new functionality
- Edit `templates/tasks/task_list.html` to modify the UI

## Code Overview

### models.py

The Task model defines the database schema:
- `title`: Task name (required)
- `description`: Detailed description (optional)
- `created_at`: Auto-generated timestamp
- `completed`: Boolean flag for completion status

### views.py

View functions handle the application logic:
- `task_list`: Displays all tasks
- `add_task`: Creates new tasks
- `toggle_task`: Toggles completion status
- `delete_task`: Removes tasks

### urls.py

URL routing connects URLs to views:
- `/`: Home page (task list)
- `/add/`: Add new task
- `/toggle/<id>/`: Toggle task completion
- `/delete/<id>/`: Delete a task

## License

This project is open source and available for educational purposes.

## Author

Created as a demonstration of Django fundamentals.
