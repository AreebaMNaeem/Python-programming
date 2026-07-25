# 💾 Introduction to Databases

## 🤔 Why Do We Need Databases?

### The Problem: Storing Data in Python Lists

```python
users = [
    {"id": 1, "name": "Ali", "email": "ali@gmail.com"},
    {"id": 2, "name": "Sara", "email": "sara@gmail.com"},
    {"id": 3, "name": "Bilal", "email": "bilal@gmail.com"}
]
```

**Issues:**
- ❌ Data disappears when program closes
- ❌ Searching/filtering is slow
- ❌ Can't handle large data (100,000+ users)
- ❌ No security or user isolation
- ❌ Hard to connect related data (users → orders → products)
- ❌ Multiple users can't access simultaneously

**Database solves ALL these problems!** ✅

---

## 📋 What is a Database?

A **database** is:
- **Organized** storage system with structure
- **Persistent** (data survives program shutdown)
- **Efficient** (fast searching, filtering, updates)
- **Secure** (controlled access, encryption)
- **Relational** (data connected together)

```python
# Before: Data in lists (lost when program ends)
users = [{"id": 1, "name": "Ali"}]

# After: Data in database (survives forever)
# Database stores it permanently on disk
```

---

## 🔧 Three Important Concepts

### 1️⃣ Database

The **actual data** stored organized in tables.

```
Students Database
├── Students Table (id, name, roll_number, gpa)
├── Courses Table (id, name, credits, instructor)
├── Enrollments Table (student_id, course_id, grade)
└── Grades Table (enrollment_id, exam_score, assignment_score)
```

### 2️⃣ DBMS (Database Management System)

**Software** that manages the database. Think of it as the "waiter" between your app and data.

**Popular DBMS:**
- **PostgreSQL** ⭐ (Best for FastAPI - powerful, reliable)
- **MySQL** (Popular, easy to learn)
- **SQLite** (Perfect for beginners, no setup)
- **MongoDB** (Different approach - NoSQL)

### 3️⃣ SQL (Structured Query Language)

**Language** to talk to the DBMS. Like English, but for databases.

```sql
-- SQL queries
SELECT * FROM users WHERE city = 'Karachi';
INSERT INTO orders VALUES (1, 'Laptop', 80000);
UPDATE users SET email = 'new@gmail.com' WHERE id = 5;
```

---

## 📊 Relational Databases (Most Important!)

**"Relational"** means data is stored in **tables** that **relate to each other**.

### Table Structure

Think of it like an Excel spreadsheet:

```
Students Table:
┌────┬─────────┬──────────────────┐
│ id │  name   │      email       │
├────┼─────────┼──────────────────┤
│ 1  │ Ali     │ ali@uni.edu.pk   │
│ 2  │ Sara    │ sara@uni.edu.pk  │
│ 3  │ Bilal   │ bilal@uni.edu.pk │
└────┴─────────┴──────────────────┘

Rows = Records (actual data)
Columns = Attributes (properties)
```

---

## 🔑 Primary Key & Foreign Key (Critical!)

## 1. Primary Key (PK)

**Uniquely identifies each row.**

Requirements:
- ✅ Every row must have one
- ✅ Cannot be NULL
- ✅ Cannot repeat
- ✅ Usually `id`

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,  -- This is PK
    name TEXT,
    email TEXT
);
```

## 2. Foreign Key (FK)

**Connects to another table's primary key.**

Creates relationships between tables.

**Example: Students & Course Enrollments**

```
Students Table:          Enrollments Table:
┌────┬───────────┐      ┌──────────┬────────────┐
│ id │   name    │      │student_id│ course_id  │
├────┼───────────┤      ├──────────┼────────────┤
│ 1  │ Ali       │  ←───│ 1        │ CS101      │
│ 2  │ Sara      │  ←───│ 2        │ CS101      │
│ 3  │ Bilal     │      │ 1        │ MATH201    │
└────┴───────────┘      └──────────┴────────────┘

student_id is a FOREIGN KEY
It points to Students.id
Creates a link between tables!
```
```sql
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id)  -- This is FK
);
```


---

## 🔄 CRUD Operations (The Foundation)

Every app does CRUD (Create, Read, Update, Delete):

| Operation | SQL Keyword | Example |
|-----------|-------------|---------|
| **Create** | INSERT | Add new user |
| **Read** | SELECT | Get user data |
| **Update** | UPDATE | Change email |
| **Delete** | DELETE | Remove user |

---

## 💡 Real-World Example: Online Shop Database

**What tables do you need?**

```
Online Shop Database:
├── Products Table (id, name, price, stock)
├── Users Table (id, email, password, city)
├── Orders Table (id, user_id, order_date)
├── OrderItems Table (id, order_id, product_id, quantity)
└── Reviews Table (id, user_id, product_id, rating, comment)
```

**Relationships:**
- Users → Orders (one user has many orders)
- Orders → OrderItems (one order has many items)
- Products → OrderItems (one product in many orders)
- Users → Reviews (one user writes many reviews)


---

## 📈 Data Types in SQL

| Type | Meaning | Example |
|------|---------|---------|
| INTEGER | Whole numbers | 25, 1000 |
| TEXT | Strings | "Ali", "ali@gmail.com" |
| REAL | Decimal numbers | 19.99, 3.14 |
| BOOLEAN | True/False | true, false |
| DATE | Calendar date | 2024-01-15 |
| TIMESTAMP | Date + time | 2024-01-15 14:30:00 |

---

## ✅ Constraints (Data Protection)

**Rules that protect your data:**

| Constraint | Purpose | Example |
|-----------|---------|---------|
| NOT NULL | Field must have value | name TEXT NOT NULL |
| UNIQUE | No duplicates | email TEXT UNIQUE |
| PRIMARY KEY | Unique identifier | id INTEGER PRIMARY KEY |
| FOREIGN KEY | Links to other table | user_id REFERENCES users(id) |
| CHECK | Custom validation | age INTEGER CHECK (age >= 18) |
| DEFAULT | Default value | status TEXT DEFAULT 'active' |

---

## 🏗️ How This Fits into FastAPI

```
User Request (FastAPI)
    ↓
FastAPI Route Handler
    ↓
SQLAlchemy ORM (Python ↔ Database bridge)
    ↓
SQL Query (SELECT, INSERT, UPDATE, DELETE)
    ↓
PostgreSQL/MySQL (Database)
    ↓
Response sent back to user
```

**Why learn SQL for FastAPI?**
- ✅ Design better database schemas
- ✅ Write efficient queries
- ✅ Debug slow APIs
- ✅ Understand relationships
- ✅ Handle complex data

---



