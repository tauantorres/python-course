python -m venv .venv
cmd.exe /k ".\.venv\Scripts\activate & python.exe -m pip install --upgrade pip & pip install -r requirements.txt & pre-commit install"