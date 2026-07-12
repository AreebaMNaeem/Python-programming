# 🚀 FastAPI Prerequisites

---

## 🔧 Understanding the Foundation

Before building with FastAPI, you need to understand some core concepts. Think of it like building a house — you need proper tools, materials, and a clean workspace before construction!

---

## 💻 Virtual Environment (venv)

### What is it?

A **virtual environment** is an isolated Python workspace for your project.

**Real-world analogy:** 
Each restaurant has its own pantry. One restaurant doesn't use another's spices, right? Same with Python projects!

- **Without venv:** All projects share packages → conflicts and chaos
- **With venv:** Each project gets its own package setup → clean and safe

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate It

**Windows (PowerShell):**
```bash
venv\Scripts\activate
```

**Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

**You'll see `(venv)` in terminal = Success!** ✅

### Deactivate When Done

```bash
deactivate
```

---

## 📦 FastAPI and Its Ecosystem

FastAPI doesn't work alone. It needs supporting packages:

| Package | Purpose |
|---------|---------|
| **fastapi** | Main framework |
| **uvicorn** | Web server (runs your app) |
| **pydantic** | Data validation |
| **sqlalchemy** | Database work |
| **python-multipart** | Handle forms & file uploads |

### Install FastAPI Stack

```bash
pip install fastapi uvicorn[standard] sqlalchemy pydantic
```

---

## 📋 requirements.txt - Your Recipe Book

Instead of telling someone "install these 50 packages," you create a list.

### Create `requirements.txt`

```bash
pip freeze > requirements.txt
```

**It looks like:**
```
fastapi==0.115.0
uvicorn==0.30.0
pydantic==2.9.0
sqlalchemy==2.0.0
```

### Others Can Install Exact Same Setup

```bash
pip install -r requirements.txt
```

**Why?** Your friend can reproduce your environment exactly! No "it works on my machine" excuses. ✅

---

## 🏗️ Imports & Project Structure

**Package** = A folder with `__init__.py` file that groups related code.

### Good Project Structure

```
my_shop/
├── main.py              # Entry point
├── __init__.py
├── models/              # Database models
│   ├── __init__.py
│   └── product.py
├── routes/              # API endpoints
│   ├── __init__.py
│   ├── products.py
│   └── orders.py
├── database.py          # DB connection
└── requirements.txt
```

### How to Use

**models/product.py:**
```python
class Product:
    id: int
    name: str
    price: float
```

**routes/products.py:**
```python
from fastapi import APIRouter
from models.product import Product

router = APIRouter()

@router.get("/products")
def get_products():
    return {"msg": "All products"}
```

**main.py:**
```python
from fastapi import FastAPI
from routes import products

app = FastAPI()
app.include_router(products.router, prefix="/api")
```

**Why?** Breaks large apps into manageable pieces (like departments in a company). 🏢

---

## ⚡ ASGI vs WSGI 

FastAPI uses ASGI(Asynchronous Server Gateway Interface), which is why it's fast! 🚀

**WSGI (Old Way - Flask, Django):**
- Handles one request at a time
- Wait for response → then handle next request
- One waiter per table

**ASGI (New Way - FastAPI):**
- Handles multiple requests simultaneously
- Doesn't wait if client is slow
- One waiter serving many tables at once

---

## 📖 Automatic Documentation

FastAPI generates docs automatically using type hints and Pydantic.

### Access Documentation

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello(name: str):
    return {"message": f"Hello {name}"}
```

**Visit:**
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

You didn't write a single doc line, but FastAPI created complete interactive docs! ✨

---

## 🔐 Environment Variables (.env)

### Never Hardcode Secrets!

**❌ Bad:**
```python
DATABASE_URL = "postgresql://user:password@localhost/db"
SECRET_KEY = "my-super-secret-key"
```

**✅ Good:**
```
# .env file
DATABASE_URL=postgresql://user:password@localhost/db
SECRET_KEY=my-super-secret-key
```

### Use Environment Variables

**Install package:**
```bash
pip install python-dotenv
```

**In your code:**
```python
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")
secret = os.getenv("SECRET_KEY")
```

**Why?** Secrets stay safe, configs stay flexible! 🔒

### .gitignore (Don't commit secrets!)

```
.env
venv/
__pycache__/
*.pyc
```

---

## 🎯 Running Your FastAPI App

### Basic Start

```bash
uvicorn main:app --reload
```

- `main` = your Python file name
- `app` = your FastAPI instance variable
- `--reload` = auto-restart on code change

### Custom Host & Port

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

### Production Mode

```bash
# Don't use --reload in production!
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 📝 Complete Minimal Setup

### Step 1: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### Step 2: Create main.py

```python
from fastapi import FastAPI

app = FastAPI(title="My Shop API")

@app.get("/")
def root():
    return {"message": "Welcome to my shop!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "Product"}
```

### Step 3: Install Dependencies

```bash
pip install fastapi uvicorn[standard]
```

### Step 4: Create requirements.txt

```bash
pip freeze > requirements.txt
```

### Step 5: Run App

```bash
uvicorn main:app --reload
```

**Visit:** http://localhost:8000 ✅

---


