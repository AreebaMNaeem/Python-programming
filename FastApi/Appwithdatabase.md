# FastAPI + SQLAlchemy + MySQL — CRUD API

A simple Product CRUD API built with FastAPI and SQLAlchemy, connected to
MySQL (works with MySQL Workbench). Ported from an original PostgreSQL version.

## Project structure

```
.
├── main.py              # FastAPI app, routes, dependency injection
├── models.py             # Pydantic model (validates HTTP request/response bodies)
├── database_models.py    # SQLAlchemy ORM model (maps to the MySQL table)
├── database.py           # DB engine + session config (the only file that changes per DB)
└── requirements.txt
```

## What changed going from Postgres → MySQL

Only **`database.py`**. That's the teaching point: SQLAlchemy is an ORM, so
your route code, your ORM model, and your Pydantic model never need to know
which database engine is underneath. You only touch the connection string
and the driver.

| | Postgres | MySQL |
|---|---|---|
| Driver package | `psycopg2-binary` | `pymysql` |
| Connection string | `postgresql://user:pass@localhost:5432/dbname` | `mysql+pymysql://user:pass@localhost:3306/dbname` |

One other MySQL-specific tweak: MySQL requires a length on `VARCHAR`
columns, so `String` became `String(255)` in `database_models.py`
(Postgres allows unbounded `VARCHAR`, MySQL doesn't).

## Setup

### 1. Create the database in MySQL Workbench

Open Workbench, connect to your local server, and run:

```sql
CREATE DATABASE product_db;
```

### 2. Update your credentials

In `database.py`, replace `root` / `your_password` with your actual MySQL
Workbench login:

```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:your_password@localhost:3306/product_db"
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

## Teaching notes for students

### Dependency Injection (`get_db`)

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Every route declares `db: Session = Depends(get_db)` instead of creating
its own session. FastAPI calls `get_db()`, runs it up to `yield`, passes
`db` into the route, then — once the route returns — resumes `get_db()` to
run `db.close()`. This guarantees the session always closes, even if the
route raises an error, and it means routes don't need to know *how* a
session is built. Swap `get_db` for a fake one in tests and no route code
changes — that's the actual value of DI, not just "less typing."

### Two models, two jobs

- `models.Product` (Pydantic) — validates and parses JSON from HTTP requests.
- `database_models.Product` (SQLAlchemy) — represents an actual row in the
  MySQL `product` table.

`product.model_dump()` converts a validated Pydantic object into a plain
dict, which is then unpacked (`**`) into the SQLAlchemy model to create a
new row. This separation is deliberate: your API's public contract (what
JSON looks like) and your database schema (what columns exist) are allowed
to evolve independently.

### Bug fixed from the original code

```python
# before (bug): missing parentheses means .count is a method reference,
# which is always truthy, so the "if count == 0" seed logic never behaved
# as intended once there was data.
count = db.query(database_models.Product).count

# after (fixed):
count = db.query(database_models.Product).count()
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/products` | List all products |
| GET | `/product/{id}` | Get one product |
| POST | `/product` | Create a product |
| PUT | `/product?id={id}` | Update a product |
| DELETE | `/product?id={id}` | Delete a product |