#  Sets in Python :

---
## 🔶 What is a Set?

A set is an **unordered collection of unique elements**. Python automatically removes duplicates and handles all the uniqueness rules for you.

Think of a set like a **bag of unique items** — you can throw things in, but it will never hold two of the same thing. Drop in "apple" twice and the bag still only contains one "apple".

```python
# Duplicate values are automatically removed
numbers = {1, 2, 3, 2, 1, 4, 3}
print(numbers)   # {1, 2, 3, 4}  ← only unique values kept
```

> 💡 **Three things that define a set:**  
> 🔻 **Unordered** — items have no fixed position, no index.  
> 🔻 **Unique** — duplicates are silently dropped.  
> 🔻 **Mutable** — you can add or remove items after creation.  

---

## 🔶 Creating a Set :

### Method 1 — Curly braces `{}`:
```python
skills = {"python", "sql", "excel", "git"}
print(skills)
# Output: {'git', 'python', 'sql', 'excel'}  ← order not guaranteed
```

### Method 2 — `set()` constructor:
```python
# From a list
cities = set(["Karachi", "Lahore", "Islamabad", "Karachi"])
print(cities)   # {'Karachi', 'Lahore', 'Islamabad'}  ← duplicate removed


### ⚠️ The empty set trap:
```python
empty_dict = {}      # ← this is a DICTIONARY, not a set!
empty_set  = set()   # ← this is the correct way to make an empty set

print(type(empty_dict))   # <class 'dict'>
print(type(empty_set))    # <class 'set'>
# `{}` always creates an empty **dictionary**. Always use `set()` for an empty set.
```

---

## 🔶 Key Properties :

```python
# PROPERTY 1 — No duplicates
tags = {"python", "coding", "python", "beginner", "coding"}
print(tags)   # {'python', 'coding', 'beginner'}

# PROPERTY 2 — Unordered (no indexing)
fruits = {"mango", "banana", "apple"}
# print(fruits[0])   ← TypeError: sets don't support indexing

# PROPERTY 3 — Elements must be immutable (hashable)
valid_set   = {1, "hello", (1, 2)}    # ✅ int, str, tuple — all immutable
# invalid_set = {[1, 2], [3, 4]}      # ❌ TypeError — lists are mutable

```

---

## 🔶 Adding Elements

### `.add()` — add a single item:
```python
languages = {"Python", "JavaScript", "Go"}

languages.add("HTML")
print(languages)   # {'Python', 'JavaScript', 'Go', 'HTML'}

# Adding a duplicate — silently ignored
languages.add("Python")
print(languages)   # still same — no error, no duplicate
```

### `.update()` — add multiple items at once:
```python
languages.update(["Java", "C++", "Swift"])
print(languages)


# update() accepts any iterable — list, tuple, set, even string
languages.update({"Kotlin", "Dart"})
languages.update(("Scala",))
print(languages)
```

---

## 🔶 Removing Elements : 

```python
cities = {"Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"}

# .remove() — removes item, raises KeyError if not found
cities.remove("Peshawar")
print(cities)

# .discard() — removes item, NO error if not found (safer)
cities.discard("Quetta")
cities.discard("London")    # ← no error even though London doesn't exist
print(cities)

# .pop() — removes and returns a random item (set is unordered)
removed = cities.pop()
print(f"Removed: {removed}")
print(f"Remaining: {cities}")

# .clear() — empties the entire set
cities.clear()
print(cities)   # set()
```

---

## 🔶 Checking Membership :

```python
enrolled_students = {"Ali", "Sara", "Bilal", "Hina", "Omar"}

# 'in' and 'not in' : 
print("Ali" in enrolled_students)      # True
print("Zara" in enrolled_students)     # False
print("Zara" not in enrolled_students) # True

```

---

## 🔶 Set Operations :

This is where sets truly shine. Python supports all four mathematical set operations using both **operators** and **methods**.

```python
team_a = {"Ali", "Sara", "Bilal", "Hina"}
team_b = {"Bilal", "Omar", "Hina", "Zara"}
```

### 🔹 Union — all unique members from both teams:
```python
# Operator
print(team_a | team_b)
# Output: {'Ali', 'Sara', 'Bilal', 'Hina', 'Omar', 'Zara'}

# Method — same result
print(team_a.union(team_b))
```

### 🔹 Intersection — members in BOTH teams:
```python
# Operator
print(team_a & team_b)
# Output: {'Bilal', 'Hina'}  ← only common members

# Method
print(team_a.intersection(team_b))
```

### 🔹 Difference — members in A but NOT in B:
```python
# Operator — order matters
print(team_a - team_b)   # {'Ali', 'Sara'}         ← in A only
print(team_b - team_a)   # {'Omar', 'Zara'}         ← in B only

# Method
print(team_a.difference(team_b))
```

### 🔹 Symmetric Difference — members in EITHER but NOT BOTH:
```python
# Operator
print(team_a ^ team_b)
# Output: {'Ali', 'Sara', 'Omar', 'Zara'}  ← excludes common members

# Method
print(team_a.symmetric_difference(team_b))
```
---

## 🔶 Set Comparison Methods :

```python
permissions_viewer = {"read"}
permissions_editor = {"read", "write"}
permissions_admin  = {"read", "write", "delete", "manage"}

# issubset() — is every element of A also in B?
print(permissions_viewer.issubset(permissions_editor))    # True
print(permissions_editor.issubset(permissions_viewer))    # False

# issuperset() — does A contain all elements of B?
print(permissions_admin.issuperset(permissions_editor))   # True
print(permissions_editor.issuperset(permissions_admin))   # False

# isdisjoint() — do A and B share NO elements at all?
backend_skills  = {"python", "django", "postgresql"}
frontend_skills = {"react", "css", "javascript"}
print(backend_skills.isdisjoint(frontend_skills))   # True — nothing in common
```

---

## 🔶 Looping Over a Set :

```python
programming_languages = {"Python", "JavaScript", "Go", "Rust", "Java"}

# Basic loop
for language in programming_languages:
    print(f"  → {language}")
# Output: (all languages, order not guaranteed)

# Loop with a condition
for language in programming_languages:
    if len(language) <= 3:
        print(f"  Short name: {language}")
# Output: Go

# Sorted loop — if you need consistent order
for language in sorted(programming_languages):
    print(f"  {language}")
# Output: Go, Java, JavaScript, Python, Rust  (alphabetical)

> 💡 Sets are **unordered** — if you need consistent order while looping, wrap with `sorted()`.
```

---

## 🔶 Set Comprehension :

Build a set in one clean line — same idea as list comprehension, but with `{}` and guaranteed uniqueness.

```python
# Basic set comprehension
squares = {x ** 2 for x in range(1, 8)}
print(squares)   # {1, 4, 9, 16, 25, 36, 49}

# With a condition
even_squares = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)   # {4, 16, 36, 64, 100}

# Extract unique first letters from a list of names
names = ["Ali", "Ayesha", "Bilal", "Bashir", "Sara", "Sana"]
first_letters = {name[0] for name in names}
print(first_letters)   # {'A', 'B', 'S'}

```
---

## 🔶 Real World Examples :

### 🔻 Example 1 — Removing Duplicate Emails
```python
raw_emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "ali@gmail.com",
    "bilal@gmail.com",
    "sara@yahoo.com",
    "haneef@outlook.com",
]

unique_emails = set(raw_emails)

print(f"Original count : {len(raw_emails)}")
print(f"After dedup    : {len(unique_emails)}")
print(f"Duplicates removed: {len(raw_emails) - len(unique_emails)}")

for email in sorted(unique_emails):
    print(f"  {email}")

```

---

### 🔻 Example 2 — Online Store Order vs Stock
```python
customer_order = {"laptop", "mouse", "keyboard", "webcam", "headphones"}
in_stock       = {"mouse", "keyboard", "monitor", "webcam", "charger"}
out_of_stock   = {"laptop", "headphones", "usb_hub"}

can_ship = customer_order & in_stock
print(f"Can ship now     : {can_ship}")

cannot_ship = customer_order - in_stock
print(f"Cannot ship      : {cannot_ship}")

not_ordered = in_stock - customer_order
print(f"In stock but not ordered: {not_ordered}")

fully_available = customer_order.issubset(in_stock)
print(f"\nOrder fully available? : {fully_available}")
```
---

### 🔻 Example 3 — Restaurant Menu vs Customer Allergies
```python
dish_ingredients = {
    "biryani":  {"rice", "chicken", "spices", "oil", "onion"},
    "pasta":    {"pasta", "cheese", "milk", "cream", "garlic"},
    "salad":    {"lettuce", "tomato", "cucumber", "olive_oil"},
    "burger":   {"bun", "beef", "cheese", "lettuce", "mayo"},
}

customer_allergies = {"milk", "cheese", "cream"}

print("=== Menu Safety Check ===")
for dish, ingredients in dish_ingredients.items():
    allergens_in_dish = ingredients & customer_allergies

    if allergens_in_dish:
        print(f"  ❌ {dish:<10} — contains: {allergens_in_dish}")
    else:
        print(f"  ✅ {dish:<10} — safe to eat")
```

---

### 🔻 Example 4 — Attendance Tracker
```python
registered = {"Ali", "Sara", "Bilal", "Hina", "Omar", "Zara"}
attended   = {"Ali", "Bilal", "Omar", "Zara"}

absent     = registered - attended
extra      = attended - registered   # attended but not registered

print(f"  Registered : {len(registered)}")
print(f"  Attended   : {len(attended)}")
print(f"  Absent     : {absent}")
print(f"  Attendance : {len(attended)/len(registered)*100:.0f}%")

if extra:
    print(f"  Unregistered attendees: {extra}")
else:
    print(f"  No unregistered attendees")

```
---
