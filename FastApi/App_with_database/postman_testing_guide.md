# 📮 Testing the Product API with Postman

A walkthrough for testing every CRUD route using Postman instead of Swagger — useful once you want to test outside the browser, or share a collection with someone else.

---

## ⚙️ Setup

1. Make sure your server is running:
   ```bash
   uvicorn main:app --reload
   ```
2. Open Postman → **New → HTTP Request**
3. Base URL for every request below: `http://127.0.0.1:8000`

---

## 1️⃣ GET all products

- Method: **GET**
- URL: `http://127.0.0.1:8000/products`
- Body: none
- Click **Send** → you should get back a JSON array of products currently in `fastapitest_db`.

---

## 2️⃣ GET a single product

- Method: **GET**
- URL: `http://127.0.0.1:8000/product/1`
- Body: none
- Returns that one product, or `"Product not found"` if the ID doesn't exist.

---

## 3️⃣ POST — add a new product

- Method: **POST**
- URL: `http://127.0.0.1:8000/product`
- Go to the **Body** tab → select **raw** → set the dropdown on the right to **JSON**
- Paste:
```json
{
  "id": 1,
  "name": "laptop",
  "description": "gaming laptop",
  "price": 1000,
  "quantity": 10
}
```
- Click **Send** → expect a `200` status.
- **Verify it worked:** run the GET all products request again — the new product should now appear. Or check MySQL Workbench directly with `SELECT * FROM product;`.

---

## 4️⃣ PUT — update an existing product

- Method: **PUT**
- URL: `http://127.0.0.1:8000/product?id=1` (the `id` goes in the query string, not the body)
- Body → raw → JSON:
```json
{
  "id": 1,
  "name": "gaming laptop pro",
  "description": "RTX 4090 edition",
  "price": 1500,
  "quantity": 5
}
```
- Send → expect `"Product updated"` back.
- Verify with a GET on `/product/1` — fields should reflect the update.

---

## 5️⃣ DELETE — remove a product

- Method: **DELETE**
- URL: `http://127.0.0.1:8000/product?id=1`
- Body: none
- Send → check Workbench with `SELECT * FROM product;` to confirm the row is really gone, not just hidden from the API response.

---

## 🧾 Quick Reference Table

| Action | Method | URL | Needs Body? |
|---|---|---|---|
| Get all products | GET | `/products` | No |
| Get one product | GET | `/product/{id}` | No |
| Add a product | POST | `/product` | Yes (JSON) |
| Update a product | PUT | `/product?id={id}` | Yes (JSON) |
| Delete a product | DELETE | `/product?id={id}` | No |

---

## 💡 Saving Time: Build a Postman Collection

Instead of retyping the URL every time:
1. Click **New → Collection**, name it something like `Product API`.
2. Save each request above into that collection (the **Save** button next to Send).
3. Next time, just open the collection and click through your saved requests instead of rebuilding them.

---