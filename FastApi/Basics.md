# ⚡ FastAPI Basics 

---

## 1️⃣ What is FastAPI, really?

FastAPI is a Python framework for building web APIs — the layer that lets an app or a phone talk to your backend over the internet.

Under the hood it leans on things you've already studied:
- **Classes and objects** (your `FastAPI()` app is itself an object)
- **Type hints** (`str`, `int`, `bool`) to validate incoming data
- **Decorators** (`@app.get(...)`) to attach a Python function to a specific URL + method

**A canteen counter analogy:** 
- You hand over your order slip → that's the request
- The counter guy checks it and passes it to the right window → that's FastAPI routing
- He brings back your food → that's the response
- FastAPI itself is just that counter guy — matching orders to windows and handing back whatever comes out
---

## 2️⃣ Your First Route

```python
from fastapi import FastAPI

# app = an object, created from the FastAPI class
app = FastAPI()

@app.get("/")          # this decorator maps GET "/" to the function below
def home():
    return {"message": "Welcome to the Campus Tuck Shop API!"}
```

Run it:
```bash
uvicorn main:app --reload
```
Then open `http://127.0.0.1:8000` in your browser.

### 🔑 What's Actually Going On Here (OOP-wise)

### 🔶 Object Instantiation :
`app` is just an object made from the `FastAPI` class.

### 🔶 Method Binding :
`@app.get("/")` looks like special syntax, but it's really just a shorter way of calling a method on `app`. Here's the breakdown:

```
app.get("/")        →  returns a decorator, waiting for a function
decorator(home)      →  your function gets passed in
```

Which is the same as writing this directly:
```python
app.add_api_route("/", endpoint=home, methods=["GET"])
```

`app` then stores this as a route:
```
app.routes:  "/"  →  home()
```

`@app.post`, `@app.put`, `@app.delete` all work the same way.


---


## 3️⃣ A Small Working Example: Tuck Shop Menu

```python
from fastapi import FastAPI

app = FastAPI()

# Stand-in for a database, for now
tuck_shop_menu = {
    1: {"item": "Samosa", "price": 30},
    2: {"item": "Chicken Roll", "price": 120},
}

@app.get("/menu")
def get_menu():
    return tuck_shop_menu

@app.get("/menu/{item_id}")
def get_menu_item(item_id: int):
    return tuck_shop_menu.get(item_id, {"error": "Item not on the menu"})
```

- `/menu` → returns the whole menu.
- `/menu/{item_id}` → returns just one item, looked up by its ID.

`item_id: int` does two jobs at once: converts the URL value to an integer, and rejects the request if it isn't one.

---

## 4️⃣ Bringing In a Real Model (Pydantic + Classes)

Right now, adding a new item means editing the dictionary by hand. Let's define a proper shape for what an "item" looks like, using a class.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# A blueprint for what a menu item should contain
class MenuItem(BaseModel):
    item: str
    price: float
    available: bool = True   # defaults to True if not provided

tuck_shop_menu = {}

@app.post("/menu/{item_id}")
def add_menu_item(item_id: int, item: MenuItem):
    tuck_shop_menu[item_id] = item
    return {"message": "Item added to the menu!", "item": item}
```

Try sending this as the request body:
```json
{
  "item": "Chai",
  "price": 40,
  "available": true
}
```

**Inheritance:** `MenuItem` inherits validation, type-checking, and JSON conversion from `BaseModel` — free, no extra code.

**Analogy:** `BaseModel` is like a printed order form — fields already laid out. Wrong data (price as text, say) gets rejected before it reaches the kitchen.

---

## 5️⃣ Full CRUD on the Menu

```python
@app.get("/menu")                              # Read all
def list_items():
    return tuck_shop_menu

@app.get("/menu/{item_id}")                     # Read one
def get_item(item_id: int):
    return tuck_shop_menu.get(item_id, {"error": "Not found"})

@app.post("/menu/{item_id}")                    # Create
def create_item(item_id: int, item: MenuItem):
    tuck_shop_menu[item_id] = item
    return {"message": "Item created", "item": item}

@app.put("/menu/{item_id}")                     # Update
def update_item(item_id: int, item: MenuItem):
    tuck_shop_menu[item_id] = item
    return {"message": "Item updated", "item": item}

@app.delete("/menu/{item_id}")                  # Delete
def delete_item(item_id: int):
    if item_id in tuck_shop_menu:
        del tuck_shop_menu[item_id]
        return {"message": "Item removed"}
    return {"error": "Not found"}
```

---

## 🔑 OOP Concepts You Just Used

| Concept | Where it showed up | What it's doing |
|---|---|---|
| **Object instantiation** | `app = FastAPI()` | Creating an object from the `FastAPI` class |
| **Inheritance** | `class MenuItem(BaseModel)` | `MenuItem` gains validation and JSON conversion from `BaseModel` |
| **Encapsulation** | `tuck_shop_menu = {}` | The dict is internal — only accessible through the routes you define |
| **Polymorphism** | `create_item` / `update_item` share the same `/menu/{item_id}` path | Behavior changes based on HTTP verb (POST vs PUT), not the path |
| **Abstraction** | `list_items()` just returns data | Caller doesn't know or care whether it's a dict, file, or real database behind it |

---

## 🛠️ Set It Up

1. Install the essentials:
   ```bash
   pip install fastapi uvicorn
   ```
2. Save the code above as `main.py`.
3. Run it:
   ```bash
   uvicorn main:app --reload
   ```
4. Explore the auto-generated docs at `http://127.0.0.1:8000/docs` — try creating, updating, and deleting a menu item right from the browser.

---