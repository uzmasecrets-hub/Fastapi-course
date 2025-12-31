# UV Documentation

[Official Documentation](https://docs.astral.sh/uv/getting-started/installation/)

---

## Table of Contents
- [Installation on Windows](#installation-on-windows)
  - [Install Using PowerShell](#install-using-powershell)
  - [Install a Specific Version](#install-a-specific-version)
  - [Verify UV Installation](#verify-uv-installation)
  - [Update UV](#update-uv-to-the-latest-version)
  - [Initialize a New Project](#initialize-a-new-project-with-a-specific-python-version)
  - [Install UV with Python Already Installed](#install-uv-when-python-is-already-installed)
  - [List Installed Python Versions](#list-installed-python-versions)
- [Installation on macOS](#installation-on-macos)
  - [Install Using curl](#install-using-curl-recommended)
  - [Install Using wget](#install-using-wget-alternative)
  - [Install a Specific Version](#install-a-specific-version-1)

---

## Installation on Windows

### Install Using PowerShell

Download and execute the installer script:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install a Specific Version

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.9.21/install.ps1 | iex"
```

### Verify UV Installation

```powershell
uv -V
```

### Update UV to the Latest Version

Standalone installer:

```bash
uv self update
```

Installed via pip:

```bash
pip install --upgrade uv
```

### Initialize a New Project with a Specific Python Version

```bash
uv init my-project --python 3.9
```

### Install UV When Python Is Already Installed

Using `pip`:

```bash
pip install uv
```

Using `pipx`:

```bash
pipx install uv
```

### List Installed Python Versions

```bash
uv python list
```

---

## Installation on macOS

### Install Using curl (Recommended)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install Using wget (Alternative)

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

### Install a Specific Version

```bash
curl -LsSf https://ast