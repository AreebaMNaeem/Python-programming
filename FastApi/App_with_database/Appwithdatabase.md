# 🗄️ FastAPI + SQLAlchemy + MySQL — CRUD API

This version connects to a real MySQL database, so nothing gets lost, and introduces a few new ideas along the way: SQLAlchemy, sessions, and dependency injection.

---

## 🐘 What is SQLAlchemy?

- MySQL only understands SQL (`INSERT`, `SELECT`, `WHERE`, etc.)
- SQLAlchemy = bridge between Python and SQL — write classes/objects, it generates the SQL
- Two pieces you'll meet below:
  - **Core** → the connection layer (`engine`, `Session`)
  - **ORM** → maps a Python class (`Product`) to a real MySQL table, so `db.add(product)` = an `INSERT`

---

## 📁 File Structure

```
fastapi-mysql-app/
├── .env                  → DB credentials
├── database.py           → connects to MySQL
├── database_models.py    → defines the product table
├── models.py             → validates API request/response data
└── main.py               → routes
```

---

## ⚙️ database.py — Making the Connection

```python
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

db_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=int(DB_PORT),
    database=DB_NAME,
)

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

- **`engine`** → the connection info to MySQL (host, port, credentials) — knows *how* to reach the server, not a live connection itself
- **`Session`** → one actual conversation with the DB — opened per request, used for queries/inserts, then closed
- **`SessionLocal`** → a factory that hands out a fresh `Session` whenever called

---

## 🏗️ database_models.py — The Actual Table

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)
```

- **ORM** in action: write a Python class → SQLAlchemy turns it into a real MySQL table
- No manual `CREATE TABLE` needed
- Every `Product` object created in Python = one row in the table

---

## 📦 models.py — A Second `Product`, Different Job

```python
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
```

Two classes named `Product` exist in this project on purpose:

| | `database_models.Product` | `models.Product` |
|---|---|---|
| Built with | SQLAlchemy | Pydantic |
| Job | Defines the MySQL table | Validates incoming JSON from the client |
| Talks to | The database | The API request/response |

Flow: JSON in → validated by `models.Product` → converted → handed to `database_models.Product` → reaches MySQL.

---

## 🔌 main.py — Dependency Injection in Action

```python
from fastapi import FastAPI, Depends
from models import Product
from database import SessionLocal, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()
```

`db: Session = Depends(get_db)` → **dependency injection**: mechanism where FastAPI automatically creates or retrieves the resources a route needs and injects them into the route before it executes.

What happens on every request to `/products`:
1. FastAPI calls `get_db()` first
2. `get_db()` opens a session, `yield`s it → route receives it
3. Route runs the query using that session
4. After the route returns → execution resumes after `yield` → `db.close()` runs

No manual `get_db()` calls anywhere — FastAPI handles it, and `try/finally` guarantees the session closes even if the route errors out.

---

## 🔑 CRUD, Now Backed by a Real Database

```python
@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
```

- `db.add(...)` → stages a new row (not saved yet)
- `db.commit()` → actually writes it to MySQL
- `db.query(...).filter(...).first()` → SQL's `SELECT ... WHERE ... LIMIT 1`, written in Python
- `db.delete(...)` + `db.commit()` → removes the row for real

Every one of these = a real round trip to `fastapitest_db`, not in-memory anymore.

---

## 🛠️ Setup

**1. Create the database in MySQL Workbench**

Open Workbench, connect to your local server, and run:
```sql
CREATE DATABASE fastapitest_db;
```

**2. Add your credentials to `.env`**

Create a `.env` file in the project root with your actual MySQL login:
```
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fastapitest_db
```
`database.py` reads these automatically — no credentials are ever hardcoded in the code itself.

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI, and check MySQL Workbench (`SELECT * FROM product;`) to see your data land for real.

---