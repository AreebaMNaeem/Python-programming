# 🛍️ FastAPI Complete CRUD App

This is a simple CRUD (Create, Read, Update, Delete) API for an online shop, built with FastAPI. It's meant as a teaching example — showing how a small set of routes, combined with a Pydantic model, can manage a product catalog end to end.

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
shop_inventory = {}

# Step 4: CRUD Routes

# Home
@app.get("/")
def home():
    return {"message": "Welcome to Online Shop! 🛒"}

# CREATE (POST) → Add product
@app.post("/products/{product_id}")
def create_product(product_id: int, product: Product):
    if product_id in shop_inventory:
        return {"error": "Product already exists"}
    shop_inventory[product_id] = product
    return {"msg": "Product added", "product": product}

# READ (GET) → Get single product
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id in shop_inventory:
        return shop_inventory[product_id]
    return {"error": "Product not found"}

# READ ALL (GET) → Get all products
@app.get("/products")
def list_products():
    return shop_inventory

# UPDATE (PUT) → Update product
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in shop_inventory:
        return {"error": "Product not found"}
    shop_inventory[product_id] = product
    return {"msg": "Product updated", "product": product}

# DELETE (DELETE) → Remove product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in shop_inventory:
        return {"error": "Product not found"}
    del shop_inventory[product_id]
    return {"msg": f"Product {product_id} deleted"}
```

---

## 🏗️ Design Concepts Behind This App

| Concept | Where it appears | Why it matters |
|---|---|---|
| **Inheritance** | `class Product(BaseModel)` | `BaseModel` gives `Product` type checking, validation, and JSON conversion automatically. |
| **Encapsulation** | `shop_inventory = {}` | The dictionary is internal state — users never touch it directly, only through the API routes. |
| **Polymorphism** | `@app.get`, `@app.post`, `@app.put`, `@app.delete` on `/products/{product_id}` | The same URL path behaves differently depending on the HTTP verb used. |
| **Abstraction** | `@app.get("/products")` → `return shop_inventory` | The client doesn't need to know *how* products are stored — dict, file, or real database — it just calls the route. |

---

## 🚀 Getting the Server Running

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

## 🧪 Trying Out the Routes

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

## 🎯 Key Points

✅ **Step 1:** Import FastAPI and BaseModel  
✅ **Step 2:** Define Pydantic model for validation  
✅ **Step 3:** Create "database" (in-memory dictionary)  
✅ **Step 4:** Create CRUD routes  
✅ **Test:** Use Swagger UI at `/docs`


---