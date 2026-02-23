# 📘 Lecture: FastAPI First Steps
### FastAPI From Zero to Production — Udemy Course

---

## 🎯 What You'll Learn

By the end of this lecture you will be able to:
- Set up a FastAPI project using **UV** (the modern Python package manager)
- Write and understand your first FastAPI application
- Run a local development server with auto-reload
- Use the automatic interactive API docs (Swagger UI & ReDoc)
- Understand what **OpenAPI** is and why it matters

---

## 🖥️ Prerequisites

Make sure you have the following installed before starting:

| Tool | Version | Check Command |
|---|---|---|
| Python | 3.10+ | `python --version` |
| UV | Latest | `uv --version` |
| VS Code | Latest | — |

**Install UV** (if you haven't already):

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## 🚀 Quick Start

Follow these steps exactly. Each command is run in your terminal.

### Step 1 — Create the project

```bash
uv init fastapi-course
cd fastapi-course
```

### Step 2 — Add FastAPI

```bash
uv add fastapi
```

This installs FastAPI and all required dependencies (including Uvicorn, the ASGI server).

### Step 3 — Create your main file

Create a file called `main.py` in the project root with this content:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### Step 4 — Run the development server

```bash
fastapi dev main.py
```

You should see:

```
FastAPI  Starting development server 🚀
server   Server started at http://127.0.0.1:8000
server   Documentation at http://127.0.0.1:8000/docs
```

### Step 5 — Open in your browser

| URL | What You'll See |
|---|---|
| `http://127.0.0.1:8000` | Your API response (JSON) |
| `http://127.0.0.1:8000/docs` | Swagger UI (interactive docs) |
| `http://127.0.0.1:8000/redoc` | ReDoc (alternative docs) |
| `http://127.0.0.1:8000/openapi.json` | Raw OpenAPI schema |

---

## 📂 Project Structure

After completing this lecture, your project should look like this:

```
fastapi-course/
├── .venv/              ← Virtual environment (auto-created by UV)
├── main.py             ← Your FastAPI application
├── pyproject.toml      ← Project config and dependencies
└── README.md           ← This file
```

---

## 🧠 Code Explained

```python
from fastapi import FastAPI       # Import the FastAPI class
```
Imports the main `FastAPI` class — the core of the entire framework.

```python
app = FastAPI()                   # Create an app instance
```
Creates your web application. All routes, middleware, and config go through this object.

```python
@app.get("/")                     # A path operation decorator
```
Registers the function below as the handler for `GET` requests to the `/` path.

```python
async def root():                 # The path operation function
    return {"message": "Hello World"}  # Auto-converted to JSON
```
An async function that returns a Python dict. FastAPI converts it to a JSON response automatically.

---

## 🔑 Key Concepts

### Path
The part of the URL after the domain. For `http://example.com/users/42`, the path is `/users/42`.

### Operation (HTTP Method)
The action being performed. The most common ones:

| Method | Purpose | Example |
|---|---|---|
| `GET` | Read data | Fetch a user profile |
| `POST` | Create data | Register a new user |
| `PUT` | Update data | Edit a profile |
| `DELETE` | Delete data | Remove an account |

### OpenAPI
An industry-standard specification for describing REST APIs in machine-readable JSON/YAML. FastAPI generates this automatically from your code. Tools like Swagger UI and ReDoc use it to display interactive documentation.

---

## 🛑 Common Errors & Fixes

**`fastapi: command not found`**
```bash
# Use UV to run it instead
uv run fastapi dev main.py
```

**`Address already in use` (port 8000 busy)**
```bash
fastapi dev main.py --port 8001
```

**Server doesn't reload when I save the file**
Make sure you saved the file (`Ctrl+S` / `Cmd+S`) and that `main.py` is in the same directory where you ran the command.

**I see `{"detail":"Not Found"}` in the browser**
You're visiting a path that doesn't exist. Make sure you're at `http://127.0.0.1:8000/` (with the trailing slash or without — both work for the root).

---

## 🧪 Extra Challenge (Optional)

Once the lecture is done, try adding these endpoints on your own:

1. A `/hello` endpoint that returns `{"message": "Hello, FastAPI!"}`
2. A `/health` endpoint that returns `{"status": "ok"}`
3. A `/about` endpoint that returns info about yourself

Check `/docs` after adding each one to see them appear automatically.

---

## 📚 Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [OpenAPI Specification](https://swagger.io/specification/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)
- [ReDoc](https://redocly.com/redoc/)

---

## ⏭️ Next Lecture

**Path Parameters** — Learn how to create dynamic routes like `/users/42` or `/products/laptop` where part of the URL is a variable your function receives as an argument.

---

*Happy coding! If you get stuck, post in the course Q&A and include the exact error message from your terminal.* 🚀
