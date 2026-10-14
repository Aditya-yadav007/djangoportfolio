# Aditya's Portfolio

A personal portfolio website built with Django. The site displays project cards from the database and exposes a Django REST Framework API for managing those projects.

## Features

- Portfolio page at `/Aditya/`
- Project API at `/api/projects/`
- Public read access to projects; only authenticated staff users can create, update, or delete them
- Django admin for managing project entries
- Sample portfolio projects in `fixtures/projects.json`

## Requirements

- Python 3.10 or later
- Dependencies listed in `requirements.txt`

## Setup

From the repository root, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Set a development secret key in the current PowerShell session:

```powershell
$env:DJANGO_SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Apply database migrations and load the sample projects:

```powershell
python manage.py migrate
python manage.py loaddata fixtures/projects.json
```

Create a staff account to manage projects, then start the development server:

```powershell
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/Aditya/> for the portfolio, <http://127.0.0.1:8000/api/projects/> for the API, or <http://127.0.0.1:8000/admin/> to manage projects.

## Project API

The API is registered with a Django REST Framework router at `/api/projects/`. It supports the standard list, detail, create, update, and delete operations. Anyone can read project data; write operations require a signed-in staff account.

## Configuration note

The Django settings read `DJANGO_SECRET_KEY` from the environment and use `DEBUG = True` for local development. Before deploying, set a private production secret key, turn off debug mode, and configure `ALLOWED_HOSTS` for the deployment environment.
