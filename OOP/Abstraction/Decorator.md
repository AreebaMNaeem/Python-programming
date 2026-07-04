# 🎁 Decorators in Python

---

## 🔶 Understanding Decorators:

A **decorator** wraps a function to add extra behavior without changing the original code.

- It uses the @ symbol in Python.
```python
@decorator_name
def my_function():
    pass
```

---

## 🎁 Real-World Analogy: Gift Wrapping

**Without Decoration:** Plain box with something inside
- You see the item as is
- No extra presentation

**With Decoration:** Same box, but now:
- Wrapped in colorful paper
- Ribbon on top
- A greeting card attached
- Still the same gift inside, just prettier outside!

**Similarly in code:**
- Original function stays unchanged
- Decorator adds features around it
- Original behavior preserved

---

## 📝 Basic Decorator Example

```python
def add_timestamp(func):
    def wrapper():
        print("⏰ Starting execution...")
        func()
        print("⏰ Execution finished!")
    return wrapper

@add_timestamp
def process_order():
    print("📦 Processing your order...")

process_order()
```

**Output:**
```
⏰ Starting execution...        ← Wrapper added this (outer layer)
📦 Processing your order...    ← Original function (the gift)
⏰ Execution finished!         ← Wrapper added this (outer layer)
```

The original function stays the same — decorator just wraps extra behavior around it! 🎁

---

## 💡 Why Use Decorators?

- **Logging:** Track function calls
- **Validation:** Check inputs
- **Authentication:** Verify access
- **Timing:** Measure execution speed
- **Retry Logic:** Repeat on failure

---

## 📋 Real-World Example 1: Student Exam Logger

```python
def exam_logger(func):
    def wrapper(student_name, marks):
        print(f"📋 Logging exam for {student_name}")
        result = func(student_name, marks)
        print(f"✅ Exam logged successfully")
        return result
    return wrapper

@exam_logger
def record_exam(student_name, marks):
    return f"{student_name} scored {marks}/100"

print(record_exam("Ali", 85))
```

**Output:**
```
📋 Logging exam for Ali
✅ Exam logged successfully
Ali scored 85/100
```

---

## 🏦 Real-World Example 2: Bank Transaction Validator

```python
def validate_transaction(func):
    def wrapper(amount):
        if amount <= 0:
            print("❌ Transaction failed: Amount must be positive!")
            return None
        if amount > 100000:
            print("❌ Transaction failed: Amount exceeds limit!")
            return None
        result = func(amount)
        return result
    return wrapper

@validate_transaction
def withdraw_money(amount):
    print(f"💰 Withdrew Rs.{amount}")
    return amount

withdraw_money(5000)    # ✅ Works
withdraw_money(-100)    # ❌ Fails
withdraw_money(200000)  # ❌ Fails
```

**Output:**
```
💰 Withdrew Rs.5000
❌ Transaction failed: Amount must be positive!
❌ Transaction failed: Amount exceeds limit!
```
---

## 🎯 Decorators with Parameters


```python
def repeat_action(times):
    def decorator(func):
        def wrapper(message):
            for _ in range(times):
                func(message)
        return wrapper
    return decorator

@repeat_action(3)
def send_notification(message):
    print(f"📢 {message}")

send_notification("Assignment due tomorrow!")
```

**Output:**
```
📢 Assignment due tomorrow!
📢 Assignment due tomorrow!
📢 Assignment due tomorrow!
```

---

## 🏛️ Decorators on Class Methods

### Role-Based Access Control (RBAC) Example : 

```python
def admin_only(func):
    def wrapper(self, action):
        if self.role != "admin":
            print(f"❌ Access denied for {self.role}")
            return
        return func(self, action)
    return wrapper

class System:
    def __init__(self, role):
        self.role = role
    
    @admin_only
    def delete_user(self, action):
        print(f"✅ {action} - User deleted")

admin = System("admin")
user = System("user")

admin.delete_user("Delete user Ali")
user.delete_user("Delete user Sara")
```

**Output:**
```
✅ Delete user Ali - User deleted
❌ Access denied for user
```

---

## 🎂 Stacking Multiple Decorators

```python
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def add_exclamation(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper

@uppercase
@add_exclamation
def welcome():
    return "welcome to pakistan"

print(welcome())
```

**Output:**
```
WELCOME TO PAKISTAN!
```

**Note:** Bottom decorator applies first!

---

## 🔧 Built-in Decorators

### @property

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance

acc = BankAccount(5000)
print(acc.balance)  # Access like attribute, not method
```

### @staticmethod

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 10))  # Call without instance
```

### @classmethod

```python
class Student:
    school = "ABC School"
    
    @classmethod
    def from_string(cls, student_str):
        name, roll = student_str.split("-")
        return cls(name, roll)
    
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

student = Student.from_string("Ali-101")
print(f"{student.name} - {student.school}")
```

---
