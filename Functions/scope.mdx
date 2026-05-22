# 🌍 Scope in Python

---

## 🔶 What is Scope?
**Scope** is the region of your code where a variable exists and can be used. Different parts of your code create different "rooms" (scopes), and variables live in these rooms.

## 🔶 The Two Main Scopes:

### 1. **Global Scope** — Variables defined outside all functions

```python
# These are global — accessible from anywhere in the file
app_name = "My Python App"
version = "1.0.0"
max_users = 1000

def show_info():
    print(f"{app_name} v{version}")   # ✅ can read global variables
    print(f"Max users: {max_users}")

show_info()
print(app_name)   # ✅ accessible here too
```

**Think of global variables as:**
- Traffic lights at an intersection — all drivers can see them, and when the light changes, it affects everyone at once.
- Settings written on a whiteboard in the office — visible to all

---

### 2. **Local Scope** — Variables defined inside a function

```python
def calculate_bill():
    subtotal = 1000      # local variable
    tax = subtotal * 0.17   # local variable
    total = subtotal + tax  # local variable
    return total

result = calculate_bill()
print(result)        # ✅ 1170.0

# print(subtotal)    # ❌ NameError — subtotal doesn't exist outside the function
# print(tax)         # ❌ NameError — tax doesn't exist outside the function
```

**Think of local variables as:**
- Notes on your personal desk — only you can see them
- Ingredients you take out while cooking — exist only during that recipe

---

## 🔶 Reading vs Modifying Global Variables:

### ✅ Reading — just works:
```python
city = "Karachi"

def show_city():
    print(city)   # ✅ Reading global variable — no problem

show_city()   # Karachi
```

### ❌ Modifying — creates a NEW local variable by default:
```python
count = 0

def increment():
    count = count + 1   # ❌ UnboundLocalError
    print(count)

# increment()   # Crashes — Python sees 'count =' and makes it local,
#               # but then tries to read it before it's defined
```
---

### ✅ Modifying — use the `global` keyword:
```python
counter = 0

def increment():
    global counter       # "I want to use the global counter, not create a local one"
    counter = counter + 1
    print(f"Counter: {counter}")

increment()   # Counter: 1
increment()   # Counter: 2
increment()   # Counter: 3
print(counter)   # 3 — global variable was actually modified
> 💡 `global` tells Python: "Don't create a new local variable — use the global one."
```
 
---

## 🔶 The LEGB Rule — How Python Finds Variables:

When you use a variable name, Python searches for it in this exact order:

```
L → Local       (inside current function)
E → Enclosing   (inside outer function, if nested)
G → Global      (module level)
B → Built-in    (Python's built-in names like print, len, etc.)
```

Python stops searching the moment it finds the name.

---

### **L** — Local scope:
```python
def example():
    x = 10   # local variable
    print(x)   # Found in L (Local) → stops searching

example()   # 10
```

---

### **E** — Enclosing scope (nested functions):
```python
def outer():
    x = 20   # enclosing variable

    def inner():
        print(x)   # Not in L (Local) → checks E (Enclosing) → found!
    
    inner()

outer()   # 20
```

---

### **G** — Global scope:
```python
x = 30   # global variable

def example():
    print(x)   # Not in L or E → checks G (Global) → found!

example()   # 30
```

---

### **B** — Built-in scope:
```python
def example():
    print(len([1, 2, 3]))   # 'len' not in L, E, or G → checks B (Built-in) → found!

example()   # 3
```

---

### All four scopes together:(Nested Function)
```python
x = "Global"   # G

def outer():
    x = "Enclosing"   # E
    
    def inner():
        x = "Local"   # L
        print(x)   # Checks L first → found "Local"
    
    inner()
    print(x)   # Checks L (not found) → E (found "Enclosing")

outer()
print(x)   # Checks L, E (not found) → G (found "Global")

# Output:
# Local
# Enclosing
# Global
```

---

## 🔶 Shadowing — When Local Hides Global:

If a local variable has the same name as a global variable, the local one **shadows** (hides) the global one inside that function.

```python
name = "Global Name"

def greet():
    name = "Local Name"   # shadows the global 'name'
    print(name)   # prints "Local Name"

greet()
print(name)   # prints "Global Name" — global unchanged
```
---

## 🔶 The `nonlocal` Keyword — For Nested Functions:

`global` lets you modify global variables. `nonlocal` lets you modify variables from an **enclosing function** (not global, not local — the middle layer).

```python
def outer():
    count = 0   # enclosing variable

    def increment():
        nonlocal count   # "Use the count from outer(), not global"
        count += 1
        print(f"Count: {count}")
    
    increment()
    increment()
    increment()
    print(f"Final count: {count}")

outer()
# Output:
# Count: 1
# Count: 2
# Count: 3
# Final count: 3

# Without `nonlocal`, you'd get an error because `count += 1` would try to create a local variable.
```

---

## 🔶 Best Practices:

### ✅ DO:
- Keep global variables to a minimum (config, constants)
- Use UPPERCASE for true constants: `MAX_USERS = 100`
- Prefer passing values as arguments instead of using globals
- Use local variables whenever possible

### ❌ DON'T:
- Don't modify global variables unless absolutely necessary
- Don't shadow built-in names (`list`, `dict`, `str`, etc.)
- Don't rely on global state for function logic — pass parameters instead

---

