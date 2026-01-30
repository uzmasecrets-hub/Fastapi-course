# UV Documentation

https://docs.astral.sh/uv/getting-started/installation/

# Method 1 (Stand Alon)

## Installation on Windows

### Use irm to download the script and execute it with iex:

`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

### Request a specific version by including it in the URL:

`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.9.21/install.ps1 | iex"`

### check installed uv versionS

`uv -V`
If you are installing 1st time you will found error
`uv not recognized......`

### Permanent fix (recommended)

Add uv to PATH permanently:

Press `Win + R`

Type: `sysdm.cpl`

Go to `Advanced` tab → `Environment Variables`

Under `User variables`, select `Path` → `Edit`

Click `New`

Add:`C:\Users\pc\.local\bin`

Click `OK` on all windows

Close PowerShell and open a new one

Then run: `uv -V`

### UV update latest version
When uv is installed via the standalone installer, it can update itself on-demand:
`uv self update`

When uv is installed via pip, it can update itself on-demand:
`pip install --upgrade uv`

### Initialize a new project with Specific Python version (if that python version is not installed on your system, it will installed automatically)

 uv init my-project --python 3.9

# Method 2 (if Python is already installed)

# With pip (Some Time Manage Path some time not).
`pip install uv`

# Or better with pipx (Ensure Path management).
`pip install pipx`

`pipx ensurepath`

`pipx install uv`

```

### check installed python versions

```
uv python list 

```




## Installation on MAC

```
#Use curl to download the script and execute it with sh:


curl -LsSf https://astral.sh/uv/install.sh | sh

#If your system doesn't have curl, you can use wget:


wget -qO- https://astral.sh/uv/install.sh | sh

#Request a specific version by including it in the URL:


curl -LsSf https://astral.sh/uv/0.9.21/install.sh | sh

```


