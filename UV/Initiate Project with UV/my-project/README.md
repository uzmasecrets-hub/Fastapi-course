# Getting Started with uv

## 🐣 First uv Program

This section walks you through running your **first Python script using uv**.  
uv automatically creates an isolated environment and installs dependencies when required.

---

### 1️⃣ Create a Python Script

Create a file named **`hello.py`** with the following content:

```python
print("Hello from uv!")
```

---

### 2️⃣ Run the Script Using uv

Execute the script using uv:

```bash
uv run hello.py
```

uv will automatically resolve and install any required dependencies and then execute the script in an isolated environment.

📖 Reference: Astral Docs

---

## 📌 Common uv Commands

| Command | Purpose |
|------|--------|
| `uv init` | Initialize a new project |
| `uv add <package>` | Add a dependency |
| `uv lock` | Generate a lockfile |
| `uv sync` | Install dependencies from the lockfile |
| `where uv` | Give Location where UV installed (works in cmd not powershel[in powershel command is 'Get-Command uv']))|
| `where python` | Give Location where python all versions installed but if you installed using UV, it will not work |
| `uv python list` | List Python versions available to uv (if you installed Pyhton using UV) |
| `uv run <script>` | Run a Python script |
| `uv venv` | Create a virtual environment |
| `uv tool install <tool>` | Install a CLI tool |
| `uv tool run <tool>` | Run a tool from the environment |

These commands provide a **modern, efficient Python development workflow** using uv.

📖 Reference: Astral Docs

---

## 📂 Project Workflow Example

A typical workflow for starting and running a new Python project with uv:

```bash
# Initialize project
uv init my-project

cd my-project

# Avtivate a Pyton environment
uv venv

(you will see line like this 
"Activate with: .venv\Scripts\activate"
copy this ".venv\Scripts\activate" and paste in your terminal)

now your environment is ready to use

# Add dependencies
uv add requests

# Lock resolved dependencies
uv lock

# Sync environment
uv sync

# Run script
uv run script.py
```

---

## 💡 Getting Help

View all available commands:

```bash
uv help
```

Get help for a specific command:

```bash
uv help <command>
```

Example:

```bash
uv help python
```

---

## 📚 Learn More

Explore the complete uv documentation and advanced guides:

🌐 https://docs.astral.sh/uv/

📖 Official Source: Astral Docs

---

## Author

**Asif Imran**

Happy Coding 🚀




