# 🧩 Pydantic — Data Validation for FastAPI


---

## 🔍 What Pydantic Does

- **Data Parsing** and **Data Validation** at its core — takes raw input (JSON) and turns it into a validated Python object
- Uses Python **type hints** to check shape and type as part of that parsing
- Powers FastAPI's request/response models under the hood
- Auto-generates clear error messages when parsing fails

---

## ⚙️ Without Pydantic

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/add-student/")
def add_student(name: str, roll_no: int):
    return {"name": name, "roll_no": roll_no}
```

No type checking → wrong data can slip through silently.

---

## ⚙️ With Pydantic

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    roll_no: int
    is_enrolled: bool = True   # default value

@app.post("/add-student/")
def add_student(student: Student):
    return {"message": "Student added", "data": student}
```

Send this:
```json
{
  "name": "Bilal",
  "roll_no": "not-a-number"
}
```

→ Rejected automatically, zero manual checks:

```json
{
  "detail": [
    {
      "loc": ["body", "roll_no"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

---

## 🎫 Like a Fee Voucher Counter

A voucher has fixed fields:
- Name → text
- Roll number → digits
- Amount → digits

Write the amount in words? Bounced back, no exceptions.

👉 `BaseModel` = that same fixed form. Wrong shape → rejected before it reaches your logic.

---

## 🔑 OOP Concepts, Quickly

| Concept | Where |
|---|---|
| **Inheritance** | `class Student(BaseModel)` — `Student` inherits validation & parsing from `BaseModel` |
| **Encapsulation** | Validation logic lives inside `BaseModel` — you never write it yourself |
| **Polymorphism** | Every model (`Student`, `Product`, whatever you define) shares the same `BaseModel` interface, but validates different fields |

---

## 🎁 Type Coercion — Part of Parsing

```json
{
  "name": "Sara",
  "roll_no": "204"
}
```
`"204"` is a string, but safely convertible → auto-converted to `204` ✅. This is **type coercion**, one piece of what "data parsing" means.

---

⚡ **In short:** 👉 Pydantic = Type checking + Parsing + Auto-conversion. That's the "magic" behind FastAPI.