# 🔐 FastAPI Auth — Postman Testing Guide

Testing the register → login → protected routes flow for the product API.

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
- Server: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

---

## 1️⃣ Register a New User (Public)

`POST http://127.0.0.1:8000/auth/register`

**Headers:** `Content-Type: application/json`

**Body:**
```json
{
  "username": "areeba",
  "email": "areeba@example.com",
  "password": "mypassword123"
}
```

**Expected Response (201):**
```json
{
  "id": 1,
  "username": "areeba",
  "email": "areeba@example.com"
}
```

---

## 2️⃣ Log In — Get a Token (Public)

`POST http://127.0.0.1:8000/token`

**Headers:** `Content-Type: application/x-www-form-urlencoded`

⚠️ **Not JSON** — this route reads `OAuth2PasswordRequestForm`, so in Postman: go to **Body → x-www-form-urlencoded**, add keys `username` and `password`.

**Body:**
```
username: areeba
password: mypassword123
```

**Expected Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

⚠️ Copy the `access_token` — needed for every route below.

---

## 3️⃣ Get Your Own Profile (Protected)

`GET http://127.0.0.1:8000/auth/me`

**Headers:** `Authorization: Bearer YOUR_ACCESS_TOKEN`

**Expected Response (200):**
```json
{
  "id": 1,
  "username": "areeba",
  "email": "areeba@example.com"
}
```

---

## 4️⃣ Add a Product (Protected)

`POST http://127.0.0.1:8000/product`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

**Body:**
```json
{
  "name": "laptop",
  "description": "gaming laptop",
  "price": 1000,
  "quantity": 10
}
```

**Expected Response (200):**
```json
{
  "id": 1,
  "name": "laptop",
  "description": "gaming laptop",
  "price": 1000,
  "quantity": 10,
  "owner": "areeba"
}
```

---

## 5️⃣ Get All Products (Protected)

`GET http://127.0.0.1:8000/products`

**Headers:** `Authorization: Bearer YOUR_ACCESS_TOKEN`

**Expected Response (200):** array of all products, regardless of owner.

---

## 6️⃣ Get One Product (Protected)

`GET http://127.0.0.1:8000/product/1`

**Headers:** `Authorization: Bearer YOUR_ACCESS_TOKEN`

---

## 7️⃣ Update a Product (Protected + Owner-Only)

`PUT http://127.0.0.1:8000/product?id=1`

**Headers:**
```
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

**Body:**
```json
{
  "name": "gaming laptop pro",
  "description": "RTX 4090 edition",
  "price": 1500,
  "quantity": 5
}
```

**Expected Response (200):** updated product — but only if the token belongs to the product's `owner`.

---

## 8️⃣ Delete a Product (Protected + Owner-Only)

`DELETE http://127.0.0.1:8000/product?id=1`

**Headers:** `Authorization: Bearer YOUR_ACCESS_TOKEN`

**Expected Response:** empty body, success — again, only if you're the owner.

---

## ❌ Error Responses to Expect

| Status | When |
|---|---|
| `400` | wrong username/password at login, or username already taken at registration |
| `401` | missing token, invalid token, or expired token |
| `403` | valid token, but trying to update/delete a product you don't own |
| `404` | product ID doesn't exist |

---

## 🔁 Full Testing Flow

1. Register **User A** → login → save token A
2. Create a product as User A
3. Register **User B** → login → save token B
4. Try `GET /auth/me` with token B → confirms it's a different identity
5. Try `PUT /product?id=1` with **token B** on User A's product → expect `403`
6. Repeat with **token A** → should succeed

---

## 💡 Tips

- Token expires after **30 minutes** — log in again for a fresh one
- In Postman, save the token as a **collection variable** (`{{token}}`) instead of pasting it manually each time
- `/token` is the only route expecting form data — every other body is JSON

---