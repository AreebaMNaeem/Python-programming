# 🛍️ FastAPI Complete CRUD App

---

## 📝 Full CRUD Application (FastAPI)

```python
from fastapi import FastAPI
from pydantic import BaseModel

# Step 1: Create app instance
app = FastAPI(title="Online Shop API")

# Step 2: Define a Pydantic model (blueprint for products)
class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    in_stock: bool = True

# Step 3: In-memory "database"
products_db = {}

# Step 4: CRUD Routes

# Home
@app.get("/")
def home():
    return {"message": "Welcome to Online Shop! 🛒"}

# CREATE (POST) → Add product
@app.post("/products/{product_id}")
def create_product(product_id: int, product: Product):
    if product_id in products_db:
        return {"error": "Product already exists"}
    products_db[product_id] = product
    return {"msg": "Product added", "product": product}

# READ (GET) → Get single product
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id in products_db:
        return products_db[product_id]
    return {"error": "Product not found"}

# READ ALL (GET) → Get all products
@app.get("/products")
def list_products():
    return products_db

# UPDATE (PUT) → Update product
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in products_db:
        return {"error": "Product not found"}
    products_db[product_id] = product
    return {"msg": "Product updated", "product": product}

# DELETE (DELETE) → Remove product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products_db:
        return {"error": "Product not found"}
    del products_db[product_id]
    return {"msg": f"Product {product_id} deleted"}
```

---

## ⚡ How to Run

```bash
uvicorn main:app --reload
```

**Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

**Swagger Docs:** 👉 http://127.0.0.1:8000/docs (FastAPI gives you interactive playground automatically! 🎉)

**ReDoc Docs:** 👉 http://127.0.0.1:8000/redoc (Alternative documentation)

---

## 📦 Example Workflows

### ✅ 1. CREATE (POST)

**URL:** `/products/1`

**Request Method:** POST

**Payload:**
```json
{
  "name": "Samsung Galaxy S24",
  "description": "5G smartphone with amazing camera",
  "price": 120000,
  "quantity": 10,
  "in_stock": true
}
```

**Response:**
```json
{
  "msg": "Product added",
  "product": {
    "name": "Samsung Galaxy S24",
    "description": "5G smartphone with amazing camera",
    "price": 120000,
    "quantity": 10,
    "in_stock": true
  }
}
```

---

### ✅ 2. READ ALL (GET)

**URL:** `/products`

**Request Method:** GET

**Response:**
```json
{
  "1": {
    "name": "Samsung Galaxy S24",
    "description": "5G smartphone with amazing camera",
    "price": 120000,
    "quantity": 10,
    "in_stock": true
  },
  "2": {
    "name": "Dell XPS 15",
    "description": "Gaming laptop with RTX 4090",
    "price": 250000,
    "quantity": 5,
    "in_stock": true
  }
}
```

---

### ✅ 3. READ SINGLE (GET)

**URL:** `/products/1`

**Request Method:** GET

**Response:**
```json
{
  "name": "Samsung Galaxy S24",
  "description": "5G smartphone with amazing camera",
  "price": 120000,
  "quantity": 10,
  "in_stock": true
}
```

---

### ✅ 4. UPDATE (PUT)

**URL:** `/products/1`

**Request Method:** PUT

**Payload:**
```json
{
  "name": "Samsung Galaxy S24 Ultra",
  "description": "5G smartphone with upgraded features",
  "price": 140000,
  "quantity": 8,
  "in_stock": true
}
```

**Response:**
```json
{
  "msg": "Product updated",
  "product": {
    "name": "Samsung Galaxy S24 Ultra",
    "description": "5G smartphone with upgraded features",
    "price": 140000,
    "quantity": 8,
    "in_stock": true
  }
}
```

---

### ✅ 5. DELETE (DELETE)

**URL:** `/products/1`

**Request Method:** DELETE

**Response:**
```json
{
  "msg": "Product 1 deleted"
}
```

---

## 🔑 OOP Concepts Inside

### 1️⃣ Inheritance
```python
class Product(BaseModel):  # Inherits from BaseModel
    # Validation, serialization comes from BaseModel
    name: str
    price: float
```

**Why:** `BaseModel` provides type checking, validation, JSON conversion automatically.

---

### 2️⃣ Encapsulation
```python
products_db = {}  # Internal state (hidden from users)
```

**Why:** Users don't access database directly. They use API routes which control access.

---

### 3️⃣ Polymorphism
```python
@app.get("/products/{product_id}")   # Same URL path
def get_product(product_id: int):
    ...

@app.post("/products/{product_id}")  # Same URL path
def create_product(product_id: int, product: Product):
    ...

@app.put("/products/{product_id}")   # Same URL path
def update_product(product_id: int, product: Product):
    ...
```

**Why:** Same path behaves differently based on HTTP verb (GET, POST, PUT, DELETE).

---

### 4️⃣ Abstraction
```python
@app.get("/products")
def list_products():
    return products_db
```

**Why:** Client doesn't care HOW we store products (dict, database, file). They just call the route and get data.

---

## 🧠 Understanding the Flow

```
1. Client sends HTTP request
   ↓
2. FastAPI matches route and HTTP method
   ↓
3. Request body validated by Pydantic model
   ↓
4. Function executes
   ↓
5. Response returned as JSON
   ↓
6. Client receives data
```

---

## 📊 HTTP Methods & Operations

| Method | Path | Operation | Example |
|--------|------|-----------|---------|
| **POST** | `/products/{id}` | CREATE | Add new product |
| **GET** | `/products` | READ ALL | List all products |
| **GET** | `/products/{id}` | READ ONE | Get product by ID |
| **PUT** | `/products/{id}` | UPDATE | Modify product |
| **DELETE** | `/products/{id}` | DELETE | Remove product |

---

## 💾 Testing with cURL

### Create
```bash
curl -X POST "http://localhost:8000/products/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 80000,
    "quantity": 5
  }'
```

### Read All
```bash
curl "http://localhost:8000/products"
```

### Read One
```bash
curl "http://localhost:8000/products/1"
```

### Update
```bash
curl -X PUT "http://localhost:8000/products/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gaming Laptop Pro",
    "description": "RTX 4090",
    "price": 120000,
    "quantity": 3
  }'
```

### Delete
```bash
curl -X DELETE "http://localhost:8000/products/1"
```

---

## 🎯 Key Points

✅ **Step 1:** Import FastAPI and BaseModel
✅ **Step 2:** Define Pydantic model for validation
✅ **Step 3:** Create "database" (in-memory dictionary)
✅ **Step 4:** Create CRUD routes
✅ **Run:** Use uvicorn to start server
✅ **Test:** Use Swagger UI at `/docs`

---


