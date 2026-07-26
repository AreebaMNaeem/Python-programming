# 🗄️ Database Core Concepts

---

## 1️⃣ Tables & Columns (The Foundation)

### What is a Table?

A **table** is structured data organized in rows and columns, like an Excel sheet.

**Structure:**
```
Students Table:
┌────┬─────────┬──────────────┬────────┐
│ id │  name   │   email      │  gpa   │
├────┼─────────┼──────────────┼────────┤
│ 1  │ Ali     │ ali@uni.edu  │ 3.8    │
│ 2  │ Sara    │ sara@uni.edu │ 3.9    │
│ 3  │ Bilal   │ bilal@uni.edu│ 3.5    │
└────┴─────────┴──────────────┴────────┘

Rows = Records (each student)
Columns = Attributes (id, name, email, gpa)
```

### Column Data Types

**Determines what data can be stored:**

```sql
CREATE TABLE students (
    id INTEGER,              -- Whole numbers
    name TEXT,              -- Strings
    gpa REAL,               -- Decimals
    is_active BOOLEAN,      -- True/False
    admission_date DATE,    -- Calendar date
    created_at TIMESTAMP    -- Date + time
);
```

---

## 🪪 Primary Key (PK) - Identity Card

### What is a Primary Key?

**A column that uniquely identifies each row.**

**Rules:**
- ✅ Must be UNIQUE (no two rows same value)
- ✅ Cannot be NULL (must always have value)
- ✅ Only ONE primary key per table
- ✅ Usually `id`

### Analogy: National ID Card

```
Every Pakistani citizen has UNIQUE CNIC
├── No two people share same CNIC
├── CNIC never changes
└── CNIC identifies you completely

Similarly, Every row needs unique PK
├── No two users with same id
├── PK doesn't change
└── Database knows EXACTLY which row
```

### Real Example: University System

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,  -- This is PK
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    roll_number TEXT
);

-- Valid:
INSERT INTO students VALUES (1, 'Ali', 'ali@uni.edu', 'A-2024-001');
INSERT INTO students VALUES (2, 'Sara', 'sara@uni.edu', 'A-2024-002');

-- INVALID (duplicate id):
INSERT INTO students VALUES (1, 'Bilal', 'bilal@uni.edu', 'A-2024-003');  ❌ ERROR!
```

**Why PK matters:**
```
Without PK: Which 'Ali' are you talking about? (confusing!)
With PK: You mean student id=5 named Ali (crystal clear!)
```

---

## 🔗 Foreign Key (FK) - Relationship Builder

### What is a Foreign Key?

**A column that references another table's primary key.**

Creates relationships between tables.

### Analogy: Family Tree

```
Child has: father_id, mother_id
┌─────────────────────────────────┐
│ father_id → points to Father's id│
└─────────────────────────────────┘

This LINK means:
"This child belongs to that father"
```

### Real Example: Orders & Users

```sql
Users Table:
┌────┬─────────────┐
│ id │    name     │
├────┼─────────────┤
│ 1  │ Ali         │
│ 2  │ Sara        │
│ 3  │ Bilal       │
└────┴─────────────┘

Orders Table:
┌─────┬──────────┬──────────────┐
│ id  │ user_id  │  product     │
├─────┼──────────┼──────────────┤
│ 101 │ 1        │ Laptop       │  ← Order belongs to Ali (id=1)
│ 102 │ 2        │ Phone        │  ← Order belongs to Sara (id=2)
│ 103 │ 1        │ Keyboard     │  ← Another order by Ali
└─────┴──────────┴──────────────┘

user_id is FOREIGN KEY
It REFERENCES users(id)
```

### SQL Syntax

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Why Foreign Keys Matter

✅ **Prevents invalid data:**
```sql
-- This FAILS because user_id=999 doesn't exist
INSERT INTO orders VALUES (104, 999, 'Tablet');  ❌ ERROR!

-- This WORKS because user_id=1 exists
INSERT INTO orders VALUES (104, 1, 'Tablet');    ✅ SUCCESS!
```

✅ **Ensures data integrity:**
- Can't create order for non-existent user
- Can't delete user who has orders (optional CASCADE delete)
- Relationships always valid

---

## 🔄 Relationships (1-1, 1-Many, Many-Many)

### One-to-One (1:1)

**One row in Table A matches exactly one row in Table B.**

```
Person ↔ Passport
├── One person has ONE passport
├── One passport belongs to ONE person
└── Not very common in databases

Person ↔ Driving License
├── One person can have ONE license
├── One license for ONE person
```

**Real Example:**
```sql
Users Table          |  Profiles Table
user_id              |  profile_id
    ↓                |      ↓
    1 (Ali)          |      1 (Ali's profile)
    2 (Sara)         |      2 (Sara's profile)
    3 (Bilal)        |      3 (Bilal's profile)
```

### One-to-Many (1:M) - MOST COMMON ⭐

**One row in Table A matches MANY rows in Table B.**

```
Teacher → Students (1:M)
├── One teacher has MANY students
├── Each student has ONE teacher
└── Very common pattern

User → Orders (1:M)
├── One user has MANY orders
├── Each order belongs to ONE user

Author → Books (1:M)
├── One author writes MANY books
├── Each book by ONE author
```

**Real Example: Online Shop**

```
Users Table:           Orders Table:
user_id → name         order_id → user_id
1 → Ali                101 → 1 (Ali)
2 → Sara               102 → 1 (Ali)
3 → Bilal              103 → 2 (Sara)
                       104 → 1 (Ali)

Ali (id=1) has 3 orders
Sara (id=2) has 1 order
```

### Many-to-Many (M:M)

**Many rows in Table A match MANY rows in Table B.**

**Needs JUNCTION TABLE to work!**

```
Students ↔ Courses (M:M)
├── One student takes MANY courses
├── One course has MANY students
└── Requires enrollments table

Products ↔ Suppliers (M:M)
├── One product from MANY suppliers
├── One supplier supplies MANY products
└── Requires product_suppliers table
```

**Real Example: Student Enrollments**

```
Students:          Courses:           Enrollments (Junction):
id → name          id → name          student_id → course_id
1 → Ali            101 → Math         1 → 101
2 → Sara           102 → English      1 → 102
3 → Bilal          103 → Physics      2 → 101
                                      2 → 103
                                      3 → 102
                                      3 → 103

Ali takes: Math, English
Sara takes: Math, Physics
Bilal takes: English, Physics

One student → Multiple courses
One course → Multiple students
```

---

## 🔒 Constraints - Data Protection Rules

**Rules that ensure data quality.**

```sql
NOT NULL       → name TEXT NOT NULL
UNIQUE         → email TEXT UNIQUE
PRIMARY KEY    → id INTEGER PRIMARY KEY
FOREIGN KEY    → user_id REFERENCES users(id)
CHECK          → age INTEGER CHECK (age >= 18)
DEFAULT        → status TEXT DEFAULT 'active'
```

---

## ⚠️ NULL - Unknown vs Empty

### What is NULL?

**"I don't know the value"** (not the same as 0 or empty string)

### The Difference

```
Age = NULL    → Age is unknown (not known if born)
Age = 0       → Person is newborn
Age = ""      → Invalid (age should be number, not text)

Email = NULL  → Email not provided
Email = ""    → Invalid (empty string, not NULL)

Rating = NULL → Product not yet rated
Rating = 0    → Product has zero rating (explicit)
```

### Real Example

```sql
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT
);

-- User reviewed, gave rating, no comment:
INSERT INTO reviews VALUES (1, 1, 101, 5, NULL);  ✅ Valid

-- User viewed, hasn't rated yet:
INSERT INTO reviews VALUES (2, 2, 101, NULL, NULL);  ✅ Valid

-- User gave zero rating (explicit):
INSERT INTO reviews VALUES (3, 3, 101, 0, 'Bad');  ❌ Invalid (rating must be 1-5)
```

---

## 🏗️ Normalization - Clean Database Design

### What is Normalization?

**Organizing data to eliminate redundancy and inconsistency.**

### Bad Design (Redundant Data)

```
Orders Table:
order_id | user_name | user_email | user_city | product | price
1        | Ali       | ali@gmail  | Karachi   | Laptop  | 80000
2        | Ali       | ali@gmail  | Karachi   | Mouse   | 2000
3        | Sara      | sara@gmail | Lahore    | Laptop  | 80000

❌ Problems:
- Ali's email stored 2 times
- Ali's city stored 2 times
- If Ali's email changes, must update multiple rows
- Wasting storage space
```

### Good Design (Normalized)

```
Users Table:
user_id | name  | email      | city
1       | Ali   | ali@gmail  | Karachi
2       | Sara  | sara@gmail | Lahore

Orders Table:
order_id | user_id | product | price
1        | 1       | Laptop  | 80000
2        | 1       | Mouse   | 2000
3        | 2       | Laptop  | 80000

✅ Benefits:
- Each data point stored ONCE
- Easy to update
- Less redundancy
- Efficient storage
```

---

## ⚙️ Indexes - Speed Booster

### What is an Index?

**Data structure that makes searching FAST.**

### Analogy: Book Index

```
Book without index:
├── Want to find "Database"
├── Read all 500 pages 📖📖📖
└── Finally found on page 234 (slow!)

Book with index:
├── Check index: "Database → page 234"
├── Jump directly to page 234
└── Found instantly! (fast!)
```

### Real Example: Contact Search

```sql
-- Without index (slow):
-- Scans entire users table to find by email
SELECT * FROM users WHERE email = 'ali@gmail.com';  -- Slow

-- With index (fast):
CREATE INDEX idx_users_email ON users(email);
SELECT * FROM users WHERE email = 'ali@gmail.com';  -- Fast!

-- Behind the scenes:
-- Index maintains sorted list of emails
-- Database jumps directly to 'ali@gmail.com'
```

### Trade-off

```
✅ Pros:
- Faster SELECT queries
- Faster WHERE searches
- Faster sorting

❌ Cons:
- Slower INSERT (must update index)
- Slower UPDATE (must update index)
- Extra disk space
```

### When to Index

```sql
-- Good indexes (frequently searched):
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_products_name ON products(name);

-- Bad indexes (rarely searched, or small table):
CREATE INDEX idx_small_table ON tiny_data(column);  -- Overkill
```

---

## 💳 Transactions - All or Nothing

### What is a Transaction?

**A group of SQL operations that must ALL succeed or ALL fail.**

### Analogy: Bank Transfer

```
Transfer Rs. 1000 from Account A to Account B:

GOOD OUTCOME:
1. Debit 1000 from Account A ✅
2. Credit 1000 to Account B ✅
Result: Transfer complete!

BAD OUTCOME (electricity failure):
1. Debit 1000 from Account A ✅
2. Credit 1000 to Account B ❌ (database crashed)
Result: Account A lost 1000, but Account B didn't get it!
        WITHOUT TRANSACTION → Data is corrupted!
        WITH TRANSACTION → Rollback everything!
```

### SQL Syntax

```sql
BEGIN;  -- Start transaction

UPDATE accounts SET balance = balance - 1000 WHERE id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE id = 2;

COMMIT;  -- All success, save changes

-- OR if error:
ROLLBACK;  -- Undo everything
```

### Real Example: Online Order

```sql
BEGIN;

-- Deduct from inventory
UPDATE products SET quantity = quantity - 1 WHERE id = 101;

-- Create order record
INSERT INTO orders VALUES (505, 1, 101, '2024-01-15');

-- Update user stats
UPDATE users SET total_orders = total_orders + 1 WHERE id = 1;

COMMIT;  -- All three succeed together, or all three fail together
```

---

## 🔐 ACID Properties (Interview Favorite!)

**Four properties that guarantee database reliability:**

### Atomicity (All or Nothing)

**Transaction completes fully or not at all.**

```
Transfer money: 
├── Both debit AND credit must succeed
├── OR both must fail
└── No half-transactions
```

### Consistency (Rules Enforced)

**Database moves from one valid state to another.**

```
Before: Ali has 1000, Sara has 500 (total = 1500)
Transfer: Ali → Sara, 100
After: Ali has 900, Sara has 600 (total = 1500)

✅ Total preserved (consistent)
❌ If total becomes 1200, database is inconsistent!
```

### Isolation (Safe Concurrency)

**Transactions don't interfere with each other.**

```
Transaction 1: Transfer A→B (1000)
Transaction 2: Transfer B→C (500)

❌ Without isolation:
├── T1 reads B = 5000
├── T2 reads B = 5000
├── T1 credits B = 6000
├── T2 debits B = 4500
└── Result: B = 4500 (lost 1000 credit!)

✅ With isolation:
├── T1 and T2 happen sequentially
├── Safe concurrent access
└── B is correctly 5500
```

### Durability (Permanent)

**Committed data survives system failures.**

```
Insert data:
├── Power failure happens
├── Database crashes
├── Server reboots
└── Data still there! (saved to disk)
```

---

## 🔗 JOINs - Quick Overview

**Combines rows from multiple tables using relationships.**

```sql
INNER JOIN   → Only matching rows from both tables
LEFT JOIN    → All rows from left table + matches from right
RIGHT JOIN   → All rows from right table + matches from left
FULL JOIN    → All rows from both tables
```

**Basic Example:**
```sql
SELECT users.name, orders.product
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

👉 **Detailed JOIN exploration in separate file!**

---

## 🐍 SQL vs ORM (For FastAPI)

### SQL (Pure SQL)

```python
import sqlite3

cursor.execute("SELECT * FROM users WHERE age > 18")
result = cursor.fetchall()
```

**Pros:**
- ✅ Full control
- ✅ Faster for complex queries
- ✅ Optimized queries

**Cons:**
- ❌ Not Pythonic
- ❌ SQL injection risks
- ❌ More boilerplate

### ORM (SQLAlchemy - FastAPI Standard)

```python
from sqlalchemy import select
from models import User

# Pythonic way
users = session.query(User).filter(User.age > 18).all()

# Or with select:
stmt = select(User).where(User.age > 18)
users = session.execute(stmt).scalars().all()
```

**Pros:**
- ✅ Pythonic syntax
- ✅ Safer (prevents SQL injection)
- ✅ Less boilerplate

**Cons:**
- ❌ Slight performance overhead
- ❌ Less control for complex queries

### Rule of Thumb

```
Good developers know BOTH:
├── SQL for understanding (learn fundamentals)
├── ORM for FastAPI (clean, safe code)
└── Use SQL when ORM gets too complex
```

---

## 📌 Mental Model Summary

Think of a database as a **company:**

```
📋 Tables = Departments
   ├── Users table = HR Department
   ├── Products table = Sales
   └── Orders table = Finance

🪪 Primary Key = Employee ID
   └── Each employee has unique ID

🔗 Foreign Key = Manager reference
   └── Employee references their manager

📊 Relationships = Communication
   ├── One manager → Many employees (1:M)
   └── Students ↔ Courses (M:M)

🔒 Constraints = Company rules
   ├── NOT NULL = ID is mandatory
   ├── UNIQUE = No duplicate emails
   └── CHECK = Age must be > 18

🚀 Indexes = Speed shortcuts
   └── Jump directly instead of reading all

💳 Transactions = Atomic operations
   └── All succeed or all fail together

✅ ACID = Reliability guarantee
   └── Safe, consistent, permanent data
```

---

