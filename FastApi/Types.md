# 🏷️ Types in FastAPI

FastAPI's "type system" isn't one thing — it's four layers stacked on top of each other. Here's what each one actually does.

---

## 1️⃣ Python Type Hints — The Foundation

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/books/{book_id}")
def get_book(book_id: int, author: str | None = None):
    return {"book_id": book_id, "author": author}
```

- `book_id: int` → must be a whole number, or FastAPI rejects the request
- `author: str | None = None` → optional query param

🔑 **OOP angle:** type hints are a contract — they tell FastAPI/Pydantic exactly what shape to expect, before your function body even runs.

---

## 2️⃣ Pydantic Models — Structured Request Bodies

```python
from pydantic import BaseModel

class CourseEnrollment(BaseModel):
    student_name: str
    course_code: str
    credit_hours: int
    is_paid: bool = False

@app.post("/enroll/")
def enroll_student(enrollment: CourseEnrollment):
    return enrollment
```

| Send this | Result |
|---|---|
| `{"student_name": "Ali", "course_code": "CS201", "credit_hours": 3}` | ✅ accepted — `is_paid` defaults to `false` |
| `{"student_name": "Ali", "credit_hours": "three"}` | ❌ rejected — `credit_hours` must be a number, `course_code` missing |

🔑 **OOP angle:** you're defining a class that *is* the shape of your data — not just checking types, but modeling structure.

---

## 3️⃣ FastAPI's Own Types — HTTP-Specific Helpers

Type hints alone (`int`, `str`) only say *what type* data must be. These extra types say *where the data comes from* in the HTTP request, and let you add rules on top.

**a) `Path` — for values inside the URL itself**
```python
from fastapi import Path

@app.get("/books/{book_id}")
def read_book(book_id: int = Path(..., gt=0)):
    return {"book_id": book_id}
```
`book_id` comes from the URL (`/books/5`). `Path(..., gt=0)` adds a rule on top of `int`: the number must be greater than 0. The `...` means this field is required — there's no default.

**b) `Query` — for values after the `?` in a URL**
```python
from fastapi import Query

@app.get("/search")
def search(keyword: str = Query(None, min_length=3, max_length=50)):
    return {"keyword": keyword}
```
Called as `/search?keyword=fastapi`. `Query(None, min_length=3, max_length=50)` says: optional (defaults to `None`), but if provided, must be 3–50 characters.

---

### 📦 Request Body Types

Path and Query pull data *out of the URL*. These pull from elsewhere:

- `Form` → traditional HTML form submissions (not JSON)
- `File`, `UploadFile` → file uploads
- `Header` → reads HTTP headers from the request
- `Cookie` → reads cookies from the request

#### Example:

**`Form` — for traditional HTML form submissions (not JSON)**
```python
from fastapi import Form

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
```
Used when data arrives as `application/x-www-form-urlencoded` (a normal HTML `<form>` submit) instead of JSON.

**`File` / `UploadFile` — for uploaded files**
```python
from fastapi import File, UploadFile

@app.post("/upload-cover")
def upload_cover(file: UploadFile = File(...)):
    return {"filename": file.filename}
```
`UploadFile` gives you the file as an object (name, content type, and a way to read its bytes) rather than raw binary data.

---

### 📦 Response types — for controlling what you send *back*

- `Response` → raw, low-level response
- `JSONResponse` → JSON explicitly (the default anyway)
- `HTMLResponse` → raw HTML string
- `StreamingResponse` → sends data in chunks — for large files, avoids loading it all into memory first

```python
from fastapi.responses import HTMLResponse

@app.get("/welcome", response_class=HTMLResponse)
def welcome():
    return "<h1>Welcome to the Library API</h1>"
```
By default FastAPI sends JSON. `response_class=HTMLResponse` overrides that for this one route, so the string comes back as actual HTML instead of a JSON string.


---

## 4️⃣ The `typing` Module — Advanced Hints

Python's basic types (`int`, `str`, `bool`) can't express things like "a list of numbers" or "this or that type" on their own. The `typing` module fills that gap.

**`Optional[X]` — this field can be `X`, or it can be missing entirely**
```python
from typing import Optional

@app.get("/books/{book_id}")
def get_book(book_id: int, note: Optional[str] = None):
    return {"book_id": book_id, "note": note}
```
`Optional[str]` is just shorthand for `str | None` — the field is a string if provided, otherwise `None`.

| Hint | Means |
|---|---|
| `List[int]` | a list of integers |
| `Dict[str, float]` | key-value pairs, str → float |
| `Union[str, int]` | either type allowed |

---

## 🏛️ Think of It Like a Library Portal

- **Basic types** → `book_id: int`, `title: str` — the raw fields
- **Pydantic model** → the full "add a new book" form, structured
- **FastAPI types** → *how* the request arrives — search bar (query), login form, cover image upload
- **Response types** → *how* you hand data back — JSON for the app, HTML for a browser page

---
