# 🚨 Error Handling in Python

---

## 🔶 Python: An Interpreted Language:

Python is **interpreted**, not compiled like C/C++.

**What does this mean?**
- Code runs line by line
- Errors are found **while the program is running**
- You get more **runtime errors** than compile-time errors

**Error distribution in Python:**
- Very few compile-time errors (only syntax)
- Lots of runtime errors (logic, type mismatches, missing files, etc.)

```python
# Python finds this error while running, not before
name = "Ali"
print(name[10])  # IndexError happens HERE, not when file loads
```

---

## 🔶 Compile Time vs Runtime:

### ➡️ Compile Time Errors

Errors caught **before your program runs**.

**Examples:**

```python
# ❌ Missing colon
if True
    print("Hello")
# Error: SyntaxError: invalid syntax

# ❌ Wrong indentation
def greet():
print("Hi")
# Error: IndentationError: expected an indented block

# ❌ Invalid syntax
x = 5 +* 3
# Error: SyntaxError: invalid syntax
```

### ➡️ Runtime Errors

Errors that happen **while your program is running**.

**Examples:**

```python
# ❌ Dividing by zero
print(10 / 0)
# Error: ZeroDivisionError: division by zero

# ❌ Converting wrong type
age = int("twenty")
# Error: ValueError: invalid literal for int() with base 10: 'twenty'

# ❌ Accessing missing file
file = open("student_data.txt")
# Error: FileNotFoundError: [Errno 2] No such file or directory

# ❌ Accessing wrong index
scores = [85, 90, 78]
print(scores[10])
# Error: IndexError: list index out of range

# ❌ Accessing missing key
student = {"name": "Ali", "age": 20}
print(student["grade"])
# Error: KeyError: 'grade'
```

---

## 🌍 Real-World Analogy:

### ➡️ School Exam System

**Compile Time = Teacher checking exam paper before printing**
- Are all questions clearly written?
- Is the format correct?
- Are there grammar mistakes?

**Runtime = Student taking the exam**
- Student doesn't understand a question
- Time runs out
- Student makes a calculation mistake
- Student can't find the answer

---

## 🔶 What is an Exception?

An **exception** is an error that occurs **while your program is running**.

Instead of letting your program crash, you can **catch** the exception and handle it gracefully.

### Common Exceptions:

| Exception | Happens When |
|-----------|--------------|
| `ZeroDivisionError` | Dividing by zero: `10 / 0` |
| `ValueError` | Wrong value: `int("abc")` |
| `TypeError` | Wrong data type: `"hello" + 5` |
| `IndexError` | Index doesn't exist: `list[100]` |
| `KeyError` | Dictionary key doesn't exist: `dict["missing_key"]` |
| `FileNotFoundError` | File doesn't exist: `open("missing.txt")` |
| `NameError` | Variable doesn't exist: `print(undefined_var)` |

---

## 1️⃣ Basic try-except Block : 

The **simplest** way to handle errors:

```python
try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except:
    print("Something went wrong!")
```

**How it works:**
1. Python tries to run code in `try` block
2. If an error happens, it **jumps** to `except` block
3. Program continues instead of crashing

---

## 2️⃣ Catching Specific Errors (BEST PRACTICE):

Its Better to catch specific errors:

```python
try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

## 3️⃣ else Block :

`else` runs **only if no error occurred**:

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a number!")
else:
    print(f"You are {age} years old")
```

**Test cases:**
```
Input: 25
Output: You are 25 years old

Input: abc
Output: Please enter a number!
```

---

### 4️⃣ Add `finally` Block (Always runs) :

`finally` runs **no matter what** — error or no error.

Used for **cleanup** (closing files, closing connections):

```python
try:
    file = open("marks.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("File operation complete")
```

**Output if file exists:**
```
[file content]
File operation complete
```

**Output if file doesn't exist:**
```
File not found!
File operation complete
```

**Better way using `with` (auto cleanup):**

```python
try:
    with open("marks.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Done!")
```

---

### 5️⃣ Handling Multiple Exceptions Together :

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except (ValueError, ZeroDivisionError):
    print("Invalid input or cannot divide by zero!")

```
### 6️⃣ Using `raise` (Create your own errors) :

`raise` lets you **throw** an error when something doesn't make sense:

```python
def check_password(password):
    if len(password) < 6:
        raise ValueError("Password must be 6+ characters!")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain a number!")
    return "Password is strong!"

try:
    pwd = input("Enter password: ")
    print(check_password(pwd))
except ValueError as e:
    print(f"Error: {e}")
```

**Test cases:**
```
Input: abc
Output: Error: Password must be 6+ characters!

Input: abcdef
Output: Error: Password must contain a number!

Input: pass123
Output: Password is strong!
```

---

## 🌍 REAL-WORLD USE CASES : 

### ✅ Use Case 1: Online Shopping Checkout
```python
try:
    cart_total = int(input("Enter cart total: "))
    if cart_total < 0:
        raise ValueError("Total cannot be negative!")
    print(f"Proceeding to payment: Rs.{cart_total}")
except ValueError as e:
    print(f"Payment failed: {e}")
```

### ✅ Use Case 2: School Attendance System
```python
attendance = {"Ali": 85, "Sara": 90, "Bilal": 60}

try:
    student = input("Enter student name: ").title()
    percentage = attendance[student]
    if percentage < 75:
        raise ValueError("Attendance below 75%!")
    print(f"✅ {student} is eligible!")
except KeyError:
    print("❌ Student not found in system!")
except ValueError as e:
    print(f"❌ {e}")
```

### ✅ Use Case 3: Food Delivery App Rating
```python
try:
    rating = int(input("Rate delivery (1-5): "))
    if rating < 1 or rating > 5:
        raise ValueError("Rating must be 1-5!")
    print(f"✅ Rating {rating} submitted!")
except ValueError as e:
    print(f"❌ Invalid: {e}")
```
### ✅ Use Case 4: ATM PIN Verification
```python
try:
    pin = input("Enter PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        raise ValueError("PIN must be 4 digits!")
    print("✅ PIN verified!")
except ValueError as e:
    print(f"❌ {e}")
```
### ✅ Use Case 5: Job Application Form

```python
try:
    experience = int(input("Years of experience: "))
    if experience < 2:
        raise ValueError("Minimum 2 years required!")
    print("✅ Application accepted!")
except ValueError as e:
    print(f"❌ {e}")
```

## 🔶 Summary

**Try-Except Flow:**
1. `try` — Code that might fail
2. `except` — Handle specific errors
3. `else` — Runs if NO error (optional)
4. `finally` — Always runs (optional)
5. `raise` — Create your own errors

**Key Points:**
- Python has **more runtime errors** than compile-time errors
- Always catch **specific** exceptions
- Use `finally` for cleanup (files, connections)
- Use `raise` to validate user input
- Write **clear error messages**

---

