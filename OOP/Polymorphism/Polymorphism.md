# 🎭 Polymorphism in Python

---

## 🎯 What is Polymorphism?

Polymorphism means **"Many Forms"** — the same method behaves **differently** depending on the object or context.

It allows you to write flexible code that works with multiple types without changing the logic.

```python
# Same method name, different behaviors
obj1.process()  # Does one thing
obj2.process()  # Does something else
```

---

## 🎬 Real-World Analogy: Actor in Different Roles

An actor plays different characters in different movies:

- In a **drama** → Acts emotionally, serious dialogue
- In a **comedy** → Acts funny, makes jokes
- In an **action movie** → Performs stunts, fights

Same person (interface), different behaviors (implementations).

**In code:** Same method `act()`, different behaviors depending on the character! 🎭

---

## 1️⃣ Polymorphism with Classes (Method Overriding)
```python
class Employee:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class ContractEmployee(Employee):
    def __init__(self, contract_amount):
        self.contract_amount = contract_amount
    
    def calculate_salary(self):
        return self.contract_amount * 0.9  # 10% tax deduction

# Same method, different results
def process_payroll(employees):
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"Salary: Rs.{salary}")

# Works with any employee type
payroll = [
    FullTimeEmployee(50000),
    PartTimeEmployee(500, 40),
    ContractEmployee(100000)
]

process_payroll(payroll)
```

**Output:**
```
Salary: Rs.50000
Salary: Rs.20000
Salary: Rs.90000.0
```

**Key:** Function doesn't know employee type — it just calls `calculate_salary()`! ✅

---

## 2️⃣ Polymorphism with Operators (Operator Overloading)

```python
# Same operator, different behavior

print(10 + 5)              # Integer addition
print("Hello" + " World")  # String concatenation
print([1, 2] + [3, 4])     # List concatenation
```

👉 Same operator `+`, but behaves differently depending on data type.

### Customizing Operators in Classes :

We can even create our own operator behavior:
```python
class StudentMarks:
    def __init__(self, semester_name, marks):
        self.semester_name = semester_name
        self.marks = marks
    
    def __add__(self, other):
        # Combining marks from two semesters
        total = self.marks + other.marks
        return StudentMarks("Combined", total)
    
    def __str__(self):
        return f"{self.semester_name}: {self.marks} marks"

semester1 = StudentMarks("Semester 1", 85)
semester2 = StudentMarks("Semester 2", 90)

result = semester1 + semester2  # Uses __add__
print(result)
```

**Output:**
```
Combined: 175 marks
```

---

## ✅ Types of Polymorphism

| Type | Example |
|------|---------|
| **Method Overriding** | Same method, different implementations in subclasses |
| **Operator Overloading** | Same operator `+`, different behaviors for different types |
| **Duck Typing** | Objects with same methods work interchangeably |

---

## 💡 Why Use Polymorphism?

✅ **Flexibility** — Code works with multiple types
✅ **Reusability** — Write once, use with many objects
✅ **Scalability** — Add new types without changing existing code
✅ **Maintainability** — Cleaner, more organized code

---

