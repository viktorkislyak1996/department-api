<h1 align="center">Department API</h1>

<p align="center">
DRF API for working with employee and department data.
</p>

## Built With
![](https://img.shields.io/badge/python-3.11-blue)
![](https://img.shields.io/badge/djangorestframework-3.14-blue)
![](https://img.shields.io/badge/swagger-2.2-blue)
![](https://img.shields.io/badge/black-23.3-blue)
![](https://img.shields.io/badge/isort-5.12.0-blue)
<br>

![](https://img.shields.io/badge/mypy-1.3-blue)
![](https://img.shields.io/badge/flake8-6.0-blue)

# Getting Started
### Prerequisites
What kind of things you need to install on your workstation to start:
* Docker 24.0.2
* Docker-compose 1.29.2

### Installing
1. Clone the repo.
   ```sh
   $ git clone git@github.com:viktorkislyak1996/department-api.git
   ```
2. Install requirements and activate virtual environment.
    ```sh
   $ cd department-api
   $ poetry install
   $ poetry shell
   ```
3. Define environment variables
    ```sh
    (project-api-department-py3.11) $ vim .env
    ```
    ```env
    DEBUG=1
    DJANGO_SECRET_KEY = ...
    DJANGO_ALLOWED_HOSTS = localhost 127.0.0.1
    DB_ENGINE = django.db.backends.postgresql_psycopg2
    POSTGRES_USER = user_department
    POSTGRES_PASSWORD = password_department
    POSTGRES_DB = department
    DB_HOST = 127.0.0.1
    DB_PORT = 5433
    ```
4. Migrate and run docker compose by predefined `make` command.
    ```sh
    (project-api-department-py3.11) $ make app
    ```

### Run API server
To run API server use the command as follows:
   ```sh
   $ (project-api-department-py3.11) $ make server
   ```

### Run tests
To run unit tests use the command as follows:
   ```sh
   $ (project-api-department-py3.11) $ make test
   ```
