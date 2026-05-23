# 🎯 *args and **kwargs in Python

---

## 🔶 The Problem They Solve

Imagine you're building a calculator app. You start with a simple `add()` function:

```python
def add(a, b):
    return a + b

print(add(10, 5))   # 15
```

Works great — until someone wants to add **three** numbers. Now you need a new function:

```python
def add_three(a, b, c):
    return a + b + c
```

Then someone wants to add **ten** numbers. Do you write `add_ten()`? What about 50 numbers? 100?

This is where `*args` and `**kwargs` come in. They let your function accept **any number** of arguments without knowing in advance how many there will be.

```python
def add(*args):
    return sum(args)

print(add(1, 2))                # 3
print(add(1, 2, 3, 4, 5))       # 15
print(add(10, 20, 30, 40, 50, 60, 70))   # 280
```
---

## 🔶 What Are `*args` and `**kwargs`?

### `*args` — collect extra **positional** arguments into a **tuple**
### `**kwargs` — collect extra **keyword** arguments into a **dictionary**

> 💡 The magic is in the **asterisks** (`*` and `**`), not the names. You could write `*numbers` or `**options` — but `args` and `kwargs` are the universal convention everyone uses.

---

## 🔶 Understanding `*args`:

The single asterisk `*` tells Python: "collect all extra positional arguments into a tuple called `args`".

```python
def greet(*args):
    print(f"args is a {type(args)}")
    print(f"args contains: {args}")

greet("Ali", "Sara", "Bilal")
# Output:
# args is a <class 'tuple'>
# args contains: ('Ali', 'Sara', 'Bilal')
```

---

### Real example — Sum unlimited numbers:
```python
def calculate_total(*prices):
    total = 0
    for price in prices:
        total += price
    return total

print(calculate_total(100, 200))   # 300

print(calculate_total(50, 75, 120, 200, 350))   # 795

print(calculate_total(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))   # 550
# Same function handles any number of arguments.

```

---

### Mixing regular parameters with `*args`:
```python
def introduce(name, *hobbies):
    print(f"My name is {name}")
    print(f"My hobbies are:")
    for hobby in hobbies:
        print(f"  - {hobby}")

introduce("Ayesha", "reading", "coding", "photography")
```
Output:
```python
My name is Ayesha
My hobbies are:
 - reading
 - coding
 - photography
# `name` gets the first argument. Everything else goes into `hobbies` as a tuple.
```

---

## 🔶 Understanding `**kwargs`:

The double asterisk `**` tells Python: "collect all extra keyword arguments into a dictionary called `kwargs`".

```python
def show_info(**kwargs):
    print(f"kwargs is a {type(kwargs)}")
    print(f"kwargs contains: {kwargs}")

show_info(name="Ali", age=22, city="Karachi")
# Output:
# kwargs is a <class 'dict'>
# kwargs contains: {'name': 'Ali', 'age': 22, 'city': 'Karachi'}
```

---

### Real example — Build a user profile:
```python
def create_profile(**user_data):
    print("=== User Profile ===")
    for key, value in user_data.items():
        print(f"  {key.capitalize()}: {value}")

create_profile(username="ali123", email="ali@gmail.com", age=25, city="Karachi")
```

```python
Output:
=== User Profile ===
    Username: ali123
    Email: ali@gmail.com
    Age: 25
    City: Karachi
# The function doesn't need to know which fields you'll send — it handles whatever you give it.
```

---

### Mixing regular parameters with `**kwargs`:
```python
def book_ticket(passenger, **details):
    print(f"Booking ticket for: {passenger}")
    print("Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

book_ticket("Sara", 
            destination="Lahore",
            seat_class="Economy",
            meal="Vegetarian",
            luggage="20kg")
# Output:
Booking ticket for: Sara
Details:
    destination: Lahore
    seat_class: Economy
    meal: Vegetarian
    luggage: 20kg
```

---

## 🔶 Using `*args` and `**kwargs` Together:

You can combine both in the same function.

```python
def process_order(order_id, *items, **options):
    print(f"Order ID: {order_id}")
    print(f"Items: {items}")
    print(f"Options: {options}")

process_order(
    12345,
    "Laptop", "Mouse", "Keyboard",
    gift_wrap=True,
    express_delivery=True,
    note="Fragile"
)
# Output:
Order ID: 12345
Items: ('Laptop', 'Mouse', 'Keyboard')
Options: {'gift_wrap': True, 'express_delivery': True, 'note': 'Fragile'}
```

---

## 🔶 Parameter Order Rules:

When you combine different parameter types, Python enforces this **exact** order:

```
1. Regular positional parameters
2. *args
3. Keyword-only parameters (after *args)
4. **kwargs
```

```python
def complete_example(a, b, *args, c, d=100, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}, d={d}")
    print(f"kwargs={kwargs}")

complete_example(1, 2, 3, 4, 5, c=99, d=200, x=10, y=20)
# Output:
# a=1, b=2
# args=(3, 4, 5)
# c=99, d=200
# kwargs={'x': 10, 'y': 20}
```

> ⚠️ **Breaking this order causes a SyntaxError.**

```python
# ❌ Wrong — kwargs before args
def bad(a, **kwargs, *args):   # SyntaxError
    pass

# ✅ Correct
def good(a, *args, **kwargs):
    pass
```
---
## 🔶 Unpacking — The Reverse Operation:

`*` and `**` also work in **function calls** to unpack collections.

### Unpacking a list/tuple with `*`:
```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]
result = add(*numbers)   # unpacks to add(10, 20, 30)
print(result)   # 60
```

### Unpacking a dictionary with `**`:
```python
def register(username, email, age):
    print(f"User: {username}, Email: {email}, Age: {age}")

user_data = {
    "username": "ali123",
    "email": "ali@gmail.com",
    "age": 25
}

register(**user_data)   # unpacks to register(username="ali123", email=..., age=25)
# Output: User: ali123, Email: ali@gmail.com, Age: 25
```

---

