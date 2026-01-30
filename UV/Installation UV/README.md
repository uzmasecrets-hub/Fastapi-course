# 🚀 UV Documentation & Installation Guide

**UV** is a fast, modern Python package and project manager by **Astral**. It automatically manages Python versions, virtual environments, and dependencies.

**Official Documentation:** https://docs.astral.sh/uv/getting-started/installation/

---

## 📌 Installation Methods Overview
- **Method 1:** Standalone Installer (Recommended)
- **Method 2:** Using `pip` / `pipx` (Python already installed)

---

## 🧩 Method 1 — Standalone Installation (Recommended)

### 🪟 Installation on Windows

#### Install latest version
Run PowerShell **as Administrator**:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Install a specific version (example: v0.9.21)
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.9.21/install.ps1 | iex"
```

#### Verify installation
```
uv -V
```

If you see:
```
'uv' is not recognized as an internal or external command
```
then `uv` is installed but not added to PATH.

---

### ✅ Permanent PATH Fix (Recommended)

1. Press **Win + R**
2. Type `sysdm.cpl` → Enter  
3. Go to **Advanced** → **Environment Variables**
4. Under **User variables**, select `Path` → **Edit**
5. Click **New** and add:
```
C:\Users\pc\.local\bin
```
6. Click **OK** on all windows
7. Restart PowerShell
8. Verify again:
```
uv -V
```

---

### 🔄 Update UV

**Standalone installation**
```
uv self update
```

**Installed via pip**
```
pip install --upgrade uv
```

---

### 🆕 Initialize a New Project with Specific Python Version
(If the Python version is not installed, UV installs it automatically)
```
uv init my-project --python 3.9
```

---

## 🧩 Method 2 — If Python Is Already Installed

### Using pip (PATH issues may occur)
```
pip install uv
```

### Recommended: Using pipx (Better PATH management)
```
pip install pipx
pipx ensurepath
pipx install uv
```

### Check installed Python versions managed by UV
```
uv python list
```

---

## 🍎 Installation on macOS

### Using curl
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Using wget (if curl is not available)
```
wget -qO- https://astral.sh/uv/install.sh | sh
```

### Install a specific version (example: v0.9.21)
```
curl -LsSf https://astral.sh/uv/0.9.21/install.sh | sh
```

---

## ✅ Notes
- Standalone installer is **recommended**
- `pipx` is safer than `pip` for global installs
- UV automatically manages Python versions
- Ideal replacement for `pip`, `venv`, and `pyenv`
