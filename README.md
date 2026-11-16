# Task Manager API

A RESTful Task Manager API built with **FastAPI, Python, MySQL, and SQLAlchemy**. It allows users to register, log in, and manage their personal tasks securely using JWT authentication.

## Features

- User registration and login
- Secure password hashing using Argon2
- JWT-based authentication
- Create, read, update, and delete tasks
- Partial task updates using PATCH
- User-specific task management
- MySQL database integration
- SQLAlchemy ORM
- Automatic API documentation with Swagger UI
- Environment variable configuration for sensitive information

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API framework |
| MySQL | Database |
| SQLAlchemy | ORM and database operations |
| Pydantic | Request data validation |
| PyJWT | JWT authentication |
| pwdlib (Argon2) | Password hashing |
| Uvicorn | ASGI server |

## Project Structure

```text
task-manager-api/
│
├── main.py
├── models.py
├── database.py
├── security.py
├── create_tables.py
├── test_db.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Pritam-5603/task-manager-api.git
cd task-manager-api
```

### 2. Create a virtual environment

```bash
py -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

Add your own MySQL database credentials and a secure JWT secret key.

### 5. Create the MySQL database

Create a database named:

```sql
CREATE DATABASE task_manager;
```

Make sure your MySQL server is running and your `.env` configuration is correct.

### 6. Create database tables

```bash
python create_tables.py
```

### 7. Run the application

```bash
python -m uvicorn main:app --reload
```

The API will run at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

`http://127.0.0.1:8000/docs`

You can test the endpoints directly from your browser.

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a new user |
| POST | `/login` | Log in and receive an access token |

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Get all your tasks |
| GET | `/tasks/{task_id}` | Get a specific task |
| PUT | `/tasks/{task_id}` | Replace a task |
| PATCH | `/tasks/{task_id}` | Partially update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### General

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API home |
| GET | `/about` | API information |

## Authentication

The API uses JSON Web Tokens (JWT) to protect task management endpoints.

1. Register an account.
2. Log in using your credentials.
3. Copy the access token returned by the login endpoint.
4. Click **Authorize** in Swagger UI.
5. Enter your token using the Bearer authentication scheme.
6. Access your protected task endpoints.

Each user can access and manage only their own tasks.

## Security

- Passwords are hashed before being stored.
- JWT tokens are used for authentication.
- Protected endpoints require a valid access token.
- Users cannot access another user's tasks.
- Sensitive configuration values are stored in environment variables.
- The `.env` file is excluded from Git.

## Future Improvements

- Frontend integration
- Task deadlines and priorities
- Task search and filtering
- Automated testing
- Deployment and production configuration

## Author

**Pritam Das**

GitHub: [Pritam-5603](https://github.com/Pritam-5603)