# 🔐 Encapsulation in Python

---

## 🔶 What is Encapsulation?

Encapsulation means **bundling data and functions together** inside a class, and **controlling how they are accessed from outside**.

Instead of letting anyone access and mess with your class's internal data, you decide who gets to see what and who gets to change what.

```python
# Without encapsulation — anyone can change anything
class Student:
    def __init__(self, name):
        self.marks = 0

s = Student("Ali")
s.marks = 999  # ❌ Anyone can set invalid marks!
s.marks = -50   # ❌ Negative marks?!
```

```python
# With encapsulation — control access
class Student:
    def __init__(self, name):
        self.__marks = 0  # Private - only accessible through methods
    
    def set_marks(self, marks):
        if 0 <= marks <= 100:  # ✅ Validation before storing
            self.__marks = marks
        else:
            print("Invalid marks!")
    
    def get_marks(self):
        return self.__marks

s = Student("Ali")
s.set_marks(85)   # ✅ Valid
s.set_marks(999)  # ❌ Invalid - rejected!
```

---

## 🔶 Real-World Analogy: Hospital Patient Records

Imagine a hospital:

**Without Encapsulation:**
- Anyone walks in, sees patient files on the desk
- Anyone can change the medical records
- A cleaner accidentally deletes important data
- Records become unreliable

**With Encapsulation:**
- Records are locked in a cabinet
- Only doctors/nurses can access them
- Changes are documented and validated
- System is trustworthy

---

## 🔶 Access Specifiers

**Access Specifiers** define how class members (variables and methods) can be accessed from outside the class.

They help implement encapsulation by controlling the **visibility** of data.

Python has **three types of access specifiers:**

```
┌─────────────────────────┐
│  Access Specifiers      │
├─────────────────────────┤
│  1. Public              │
│  2. Protected           │
│  3. Private             │
└─────────────────────────┘
```

---

## 🔶 Public, Protected, and Private Members

Python uses **naming conventions** to indicate access levels:

### 1️⃣ Public Members (No prefix)

Accessible from **anywhere**:

```python
class Shop:
    def __init__(self, name, owner):
        self.name = name        # Public
        self.owner = owner      # Public

shop = Shop("Ali's Biryani", "Ali")
print(shop.name)      # ✅ Accessible
shop.name = "Sara's"  # ✅ Can be changed
```

---

### 2️⃣ Protected Members (Single underscore `_`)

Meant for **internal use and subclasses**. Should not be accessed directly from outside, but Python doesn't prevent it.

```python
class Bank:
    def __init__(self, name):
        self._bank_code = "PK123"  # Protected
    
    def show_info(self):
        print(self._bank_code)

bank = Bank("HBL")
print(bank._bank_code)  # ⚠️ Works, but not recommended
```

---

### 3️⃣ Private Members (Double underscore `__`)

Hidden from outside access. Python uses **name mangling** to make it harder to access.

```python
class CreditCard:
    def __init__(self, cardnumber):
        self.__cardnumber = cardnumber  # Private

card = CreditCard("1234-5678-9012-3456")
print(card.__cardnumber)  # ❌ AttributeError!

# Name mangling (possible but not recommended)
print(card._CreditCard__cardnumber)  # ⚠️ Works, but ugly
```

---

## 🔶 Getters and Setters

Instead of directly accessing private data, we use methods to control access.

**Getter** = Method to read a private variable
**Setter** = Method to modify a private variable (with validation)

```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    # Getter
    def get_salary(self):
        return self.__salary
    
    # Setter with validation
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be positive!")
    
    def get_name(self):
        return self.__name

emp = Employee("Ali", 50000)
print(emp.get_salary())    # ✅ 50000

emp.set_salary(60000)      # ✅ Valid
print(emp.get_salary())    # 60000

emp.set_salary(-5000)      # ❌ Invalid - rejected!
print(emp.get_salary())    # Still 60000
```

---
## 🔶 Why not allow direct modification of data?

In Python, object attributes can be changed directly:
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BankAccount(5000)
print(account.balance)   # ✅ Valid balance
account.balance = -2000  # ❌ Invalid balance
print(account.balance)   # -2000

⚠️ Problem: The balance became `-2000`, which may not be allowed in a bank account. There is no validation to prevent incorrect values.
```

## 🔶 Pythonic Way: @property Decorator

Instead of writing `get_` and `set_` methods, Python provides `@property` for cleaner syntax:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative!")
    
    def deposit(self, amount):
        self.balance = self.__balance + amount

account = BankAccount("Sara", 10000)
print(account.balance)     # ✅ Calls Getter - looks like attribute access
account.balance = 15000    # ✅ Calls Setter - looks like assignment
print(account.balance)     # 15000

account.balance = -1000    # ❌ Invalid - rejected!
print(account.balance)     # Still 15000
```

---



## 🔶 Encapsulation with Inheritance

### Protected Members in Subclasses

Protected members (`_`) **can be accessed** in child classes:

```python
class Vehicle:
    def __init__(self, brand):
        self._brand = brand  # Protected

class Car(Vehicle):
    def show_brand(self):
        print(f"Brand: {self._brand}")  # ✅ Accessible in subclass

car = Car("Toyota")
car.show_brand()      # ✅ Brand: Toyota
print(car._brand)     # ⚠️ Works but not recommended
```

### Private Members in Subclasses

Private members (`__`) are **NOT accessible** in child classes:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

class SavingsAccount(BankAccount):
    def show_balance(self):
        try:
            print(self.__balance)  # ❌ AttributeError
        except AttributeError:
            print("Cannot access private member in subclass!")

savings = SavingsAccount(5000)
savings.show_balance()  # ❌ Cannot access private member in subclass!
```

---


## 🔶 Why Use Encapsulation?

| Benefit | Example |
|---------|---------|
| **Validation** | Age can't be negative |
| **Security** | Password hidden from view |
| **Control** | Balance only changes via deposit/withdraw |
| **Flexibility** | Can change internals without breaking code |
| **Abstraction** | Users don't need to know implementation |

---

## 🔶 Quick Comparison

| Type | Prefix | Access | Use Case |
|------|--------|--------|----------|
| Public | None | Anywhere | General data |
| Protected | `_` | Class + Subclasses | Family data |
| Private | `__` | Only inside class | Sensitive data |

---