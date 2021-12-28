# ManiFoods

[TOC]

## I. Getting started

### 1. Install dependencies

Create file .env in api folder, copy from .env.example

```bash
$ docker-compose build
$ docker-compose run --rm api poetry install
```

### 2. Create database

Migrate database schema to latest:

```bash
$ docker-compose run --rm api alembic upgrade head
```

Downgrade database schema:

```bash
$ docker-compose run --rm api alembic downgrade -1
```

### 3. PGAdmin - DB connection

http://localhost:5050

user: pgadmin4@pgadmin.org 

password: admin