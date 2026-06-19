# ⚙️ Functions in Python — The Basics

---

## 🔶 What is a Function?

A **function** is a reusable block of code with a name. You write it once, then call it by name whenever you need it. No copying and pasting the same code everywhere.

---

## 🔶 Why Use Functions?

1. **Reusability** — write once, use many times(DRY principle)

2. **Organization** — break big problems into small pieces

3. **Readability** — good names make code self-explaining

4. **Testing** — test small pieces one at a time

---

## 🔶 Defining a Function:

### Basic syntax:
```python
def function_name():
    # code block (indented)
    print("This is inside the function")
```

- `def` — keyword that starts a function definition
- `function_name` — the name you give it (snake_case by convention)
- `()` — parentheses (parameters go inside if needed)
- `:` — colon starts the function body
- **Indented block** — everything indented below is part of the function

### Simple example:
```python
def greet():
    print("Assalam o Alaikum!")
    print("Welcome to Python functions")

# Function is defined but NOT running yet
```
---

## 🔶 Calling a Function:

Defining a function doesn't run it — you have to **call** it by name.

```python
def say_hello():
    print("Hello, World!")

# Function defined but nothing happens yet

say_hello()   # ← NOW it runs
# Output: Hello, World!
> 💡 **Calling = function_name + parentheses `()`**
```
---

## 🔶 Parameters vs Arguments:

### Parameters — placeholders in the function definition
```python
def greet_person(name):   # 'name' is a PARAMETER
    print(f"Hello, {name}!")
```

### Arguments — actual values when calling that function
```python
greet_person("Ayesha")   # "Ayesha" is an ARGUMENT
# Output: Hello, Ayesha!
> **Simple rule:** Parameters are in the **definition**. Arguments are in the **call**.

```
---

### Multiple parameters:
```python
def introduce(name, age, city):
    print(f"My name is {name}")
    print(f"I am {age} years old")
    print(f"I live in {city}")

introduce("Hassan", 22, "Karachi")
# Output:
# My name is Hassan
# I am 22 years old
# I live in Karachi
```
---

## 🔶 Different types of Arguments:
1.Positional arguments → Values are passed in the correct order.  
2.Default arguments → Pre-set values are used if none are given.  
3.Keyword arguments → Values are matched by name.  
4.Variable-length arguments: *args and **kwargs



🔻**Positional arguments:** These must be given in the same order as defined in the function.
```python
def calculate_rectangle(length, width):
    area = length * width
    print(f"Area: {area}")

calculate_rectangle(10, 5)    # length=10, width=5  ✅
calculate_rectangle(5, 10)    # length=5, width=10  ✅ (different result)
```

🔻**Default arguments:** Have default values

You can give parameters default values. If the caller doesn't provide an argument, the default is used.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ali")                    # Hello, Ali!  (uses default)
greet("Sara", "Assalam o Alaikum")  # Assalam o Alaikum, Sara!  (overrides default)
```

Rules for default parameters:
1. Default parameters must come **after** non-default parameters
2. Once you use a default, all parameters after it must also have defaults

```python
# ✅ Correct
def example(a, b, c=10, d=20):
    pass

# ❌ Wrong — non-default after default
def example(a, b=10, c):
    pass
```

🔻**Keyword Arguments:**
Instead of relying on position, you can specify which parameter gets which value by **name**.

```python
def book_ticket(passenger, destination, seat_class):
    print(f"Passenger: {passenger}")
    print(f"Destination: {destination}")
    print(f"Class: {seat_class}")

# Positional (order matters)
book_ticket("Ali", "Lahore", "Economy")

# Keyword (order doesn't matter)
book_ticket(destination="Lahore", seat_class="Economy", passenger="Ali")
book_ticket(seat_class="Business", passenger="Sara", destination="Islamabad")
```

When to use: When a function has many parameters and you want to be explicit about which is which.

🔻**Required vs Optional Parameters:**
```python
def make_sandwich(bread, filling, sauce=None, drink=None):
    """
    bread, filling → REQUIRED (no defaults)
    sauce, drink → OPTIONAL (have defaults)
    """
    print(f"Sandwich made with {bread} and {filling}")
    if sauce:
        print(f"  Sauce: {sauce}")
    if drink:
        print(f"  Drink: {drink}")

# Minimum required arguments
make_sandwich("White Bread", "Chicken")

# With optional arguments
make_sandwich("Brown Bread", "Egg", sauce="Mayo")
make_sandwich("Whole Wheat", "Veggies", sauce="Ketchup", drink="Juice")
```

---

## 🔶 Return Values:

A function can **send a value back** to wherever it was called using `return`.

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)   # 15
```

Without `return`, the function does work but gives you nothing back:
```python
def add_no_return(a, b):
    sum = a + b
    # no return statement

result = add_no_return(10, 5)
print(result)   # None  ← function returned nothing
```

---

### `return` vs `print` :
1. return: Gives a value back to the function’s caller and stops the function.
2. print: Shows text or results on the console while the function keeps running.

```python
# Using print
def calculate_with_print(a, b):
    result = a + b
    print(result)   # shows output but doesn't give back a value

# Using return
def calculate_with_return(a, b):
    result = a + b
    return result   # gives back a value you can use

# Compare:
x = calculate_with_print(10, 5)    # prints 15, but x = None
y = calculate_with_return(10, 5)   # y = 15 (you can use this value)

# You can't use x in calculations
# z = x * 2   ← TypeError: None × 2 doesn't work

# But you can use y
z = y * 2   # z = 30 ✅
> 💡 **Rule:** Use `print` to **show** something. Use `return` to **give back** something.
```

---

### Returning multiple values (Python packs them into a tuple):
```python
def get_user_info():
    name = "Ayesha"
    age = 21
    city = "Karachi"
    return name, age, city   # returns a tuple

# Unpack the tuple
user_name, user_age, user_city = get_user_info()
print(user_name)   # Ayesha
print(user_age)    # 21
print(user_city)   # Karachi
```
---

### Early return — exit the function before the end:
```python
def check_eligibility(age):
    if age < 18:
        return "Not eligible"   # function stops here
    
    # This only runs if age >= 18
    return "Eligible"

print(check_eligibility(15))   # Not eligible
print(check_eligibility(25))   # Eligible
```

---

## 🔶 Functions Without Return :

If a function doesn't have a `return` statement, Python automatically returns `None`.

```python
def without_return():
    x = 5 + 3

def explicit_none():
    return None


# Both functions return None
# func1 = no_return()      # None
# func2 = explicit_none()  # None
```

---

## 🔶 Docstrings — Documenting Your Functions

A **docstring** is a string right after the function definition that explains what the function does. Use triple quotes `"""..."""`.

```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    """
    return weight / (height ** 2)

# Access the docstring
print(calculate_bmi.__doc__)
```

**Why write docstrings?**
- Other developers (or future you) understand the function faster
- Tools like `help()` can display them
- Professional codebases require them

---

