# 🔐 FastAPI Authentication & Authorization — JWT

Adds login-protected routes to the product API — users register, log in, get a token, and can only edit/delete products they created.

---

## 🆚 Authentication vs Authorization

- **Authentication** → *who are you?* (login, proving identity)
- **Authorization** → *what are you allowed to do?* (can you edit someone else's product?)

This app does both: JWT handles authentication, ownership checks handle authorization.

---

## 📁 File Structure

```
fastapi-auth-app/
├── models.py    → data shapes (Pydantic)
├── auth.py       → security logic + user store
├── main.py        → routes
└── requirements.txt
```

---

## 🧰 Libraries Used — Authentication & Authorization

| Library | Role | Why it's needed |
|---|---|---|
| `fastapi.security.OAuth2PasswordBearer` | Reads the token from the `Authorization: Bearer <token>` header on every request | Built into FastAPI — the standard way to declare "this route needs a bearer token" |
| `fastapi.security.OAuth2PasswordRequestForm` | Reads `username`/`password` as form fields on the login request | The OAuth2 spec requires login data as form data, not JSON |
| `python-jose[cryptography]` | Encodes and decodes JWTs (`jwt.encode`, `jwt.decode`) | Builds the actual signed token, and verifies its signature + expiry on every protected request |
| `passlib[bcrypt]` | Hashes and verifies passwords (`CryptContext`) | Passwords must never be stored as plain text — bcrypt is a slow, salted, one-way hash |
| `python-multipart` | Lets FastAPI parse form data at all | Required behind the scenes for `OAuth2PasswordRequestForm` to work — without it, `/token` fails |
| `email-validator` | Validates email format | Powers Pydantic's `EmailStr` type in `UserRegister` |

- **Authentication** → handled by `OAuth2PasswordBearer` + `python-jose` + `passlib`
- **Authorization** → handled by plain Python — the `if existing["owner"] != current_user["username"]` checks in `main.py`
- No special library needed for authorization — it's just a comparison once you know who the user is

---

## 📦 models.py — Full File

```python
from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
```

- No logic here — just what each request/response must look like
- `UserOut` deliberately has no password field — never send that back to a client
- `Token` shape (`access_token` + `token_type`) is fixed by the OAuth2 spec, not optional

---

## 🔑 auth.py — Full File

```python
from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "change-this-to-a-random-long-string"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory user store: username -> {id, username, email, hashed_password}
users_db = {}
next_user_id = 1


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = users_db.get(username)
    if user is None:
        raise credentials_exception
    return user
```

**Walkthrough:**

- `oauth2_scheme` → tells FastAPI where to expect the token from, and which endpoint (`token`) issues it
- `pwd_context` → the hashing engine, configured to use bcrypt
- `users_db` / `next_user_id` → in-memory user store, no real database
- `hash_password` → scrambles a password one-way before saving — used only at registration
- `verify_password` → re-hashes a login attempt and compares — the original password is never recovered, only re-checked
- `create_access_token` → builds a JWT: `{"sub": username, "exp": expiry}`, signed with `SECRET_KEY` so tampering breaks the signature
- `get_current_user` → runs before every protected route: decodes the token, checks signature + expiry, looks up the user. Fails → `401`, route body never executes.

---

## 🔌 main.py — Full File

```python
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from models import UserRegister, UserOut, Token, Product
from auth import (
    users_db,
    hash_password,
    verify_password,
    create_access_token,
    get_current_user,
)
import auth

app = FastAPI()

# In-memory product store: id -> {id, name, description, price, quantity, owner}
products_db = {}
next_product_id = 1


# ---------- Auth routes ----------

@app.post("/auth/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user: UserRegister):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = {
        "id": auth.next_user_id,
        "username": user.username,
        "email": user.email,
        "hashed_password": hash_password(user.password),
    }
    users_db[user.username] = new_user
    auth.next_user_id += 1
    return new_user


@app.post("/token", response_model=Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/auth/me", response_model=UserOut)
def get_me(current_user: dict = Depends(get_current_user)):
    return current_user


# ---------- Product routes (all protected) ----------

@app.get("/products")
def get_all_products(current_user: dict = Depends(get_current_user)):
    return list(products_db.values())


@app.get("/product/{id}")
def get_product_by_id(id: int, current_user: dict = Depends(get_current_user)):
    product = products_db.get(id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/product")
def add_product(product: Product, current_user: dict = Depends(get_current_user)):
    global next_product_id
    new_product = {
        "id": next_product_id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "quantity": product.quantity,
        "owner": current_user["username"],
    }
    products_db[next_product_id] = new_product
    next_product_id += 1
    return new_product


@app.put("/product")
def update_product(id: int, product: Product, current_user: dict = Depends(get_current_user)):
    existing = products_db.get(id)
    if not existing:
        raise HTTPException(status_code=404, detail="No product found")

    if existing["owner"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not authorized to update this product")

    existing.update({
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "quantity": product.quantity,
    })
    return existing


@app.delete("/product")
def delete_product(id: int, current_user: dict = Depends(get_current_user)):
    existing = products_db.get(id)
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found")

    if existing["owner"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this product")

    del products_db[id]
```

**Walkthrough:**

| Route | Public or Protected? | Job |
|---|---|---|
| `POST /auth/register` | 🌐 Public | hash password, save to `users_db` |
| `POST /token` | 🌐 Public | verify credentials, issue a JWT |
| `GET /auth/me` | 🔒 Protected | return the logged-in user |
| `GET /products`, `GET /product/{id}` | 🔒 Protected | need *any* valid logged-in user |
| `POST /product` | 🔒 Protected | creates a product, stamps `owner` with the current user |
| `PUT /product`, `DELETE /product` | 🔒 Protected + ownership | need the current user to *also* be the owner, or `403` |

**Public** → no `Depends(get_current_user)` needed. `/auth/register` and `/token` must stay reachable before anyone has a token.

**Protected** → has `current_user: dict = Depends(get_current_user)` in the signature.

- `Depends(get_current_user)` on protected routes → **dependency injection**: FastAPI runs `get_current_user()` first and hands the result into the route, same pattern as `Depends(get_db)` in the database version
- The `if existing["owner"] != current_user["username"]` checks → this is the whole **authorization** layer, plain Python, no library needed

---

## 📄 requirements.txt

```
fastapi
uvicorn
python-multipart
python-jose[cryptography]
passlib[bcrypt]
email-validator
```

---

## 🛠️ Setup

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the app**
```bash
uvicorn main:app --reload
```

**3. Test in order** — `http://127.0.0.1:8000/docs`
1. `POST /auth/register` — create a user
2. `POST /token` — log in, get a JWT
3. Click **Authorize** 🔒, log in with the same credentials
4. Try `GET /products`, `POST /product` — should work
5. Try updating/deleting a product created by a *different* user → expect `403`

---