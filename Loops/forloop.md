# For Loop in Python:

---

## 🔶 What is a For Loop?

A `for` loop goes through a collection **one item at a time** and runs the body once for each item. Python handles all the tracking behind the scenes — no index variable, no manual incrementing.

## 🔶 Basic Syntax : 

```
for <variable> in <iterable>:
    <body>
```

```python
fruits = ["mango", "banana", "guava", "apple"]

for fruit in fruits:
    print(fruit)

# Output:
# mango
# banana
# guava
# apple
```

Each time through the loop, `fruit` holds the current item. When the list runs out, the loop stops automatically.

---

## 🔶 How a For Loop Works Internally ? 

Behind the scenes, a `for` loop uses Python's **iterator protocol**. It calls `iter()` on the collection to get an iterator, then keeps calling `next()` on it until there is nothing left.

```python
cities = ["Karachi", "Lahore", "Islamabad"]

# What Python does internally:
iterator = iter(cities)
print(next(iterator))   # Karachi
print(next(iterator))   # Lahore
print(next(iterator))   # Islamabad
# next(iterator)        → StopIteration — loop ends here

# What you actually write:
for city in cities:
    print(city)
```

You never have to write the `iter()` or `next()` part yourself — `for` handles all of it.

---

## 🔶 Looping Over Different Data Types

### 🔻 List
```python
scores = [88, 72, 95, 61, 79]

for score in scores:
    print(score, end=" ")

# - List with Condition:
scores = [88, 72, 95, 61, 79]

for score in scores:
    if score >= 80:
        print(f"Passed: {score}")
    else:
        print(f"Failed: {score}")


# - Nested List (2D — like a table or grid):
classroom = [
    ["Ali",   85, "A"],
    ["Sara",  72, "B"],
    ["Bilal", 91, "A"],
]

for row in classroom:
    name, marks, grade = row
    print(f"  {name:<8} Marks: {marks}  Grade: {grade}")

# - With enumerate() — Index and Value Together:
cities = ["Karachi", "Lahore", "Islamabad", "Quetta"]

# Default index starts at 0
for index, city in enumerate(cities):
    print(f"  {index}: {city}")
# Start from 1 — useful for numbered lists
for index, city in enumerate(cities, start=1):
    print(f"  {index}. {city}")

```
### 🔻 Tuple
```python
coordinates = (10.5, 24.8, -3.2)

for point in coordinates:
    print(point, end=" ")

# - Nested Tuple:
city_data = (
    ("Karachi",   16_000_000),
    ("Lahore",    13_000_000),
    ("Islamabad",  1_100_000),
)

for city, population in city_data:
    print(f"  {city:<12} Population: {population:,}")

# - With enumerate() on a Tuple
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

for index, day in enumerate(days, start=1):
    label = "Weekend soon!" if index == 5 else ""
    print(f"  Day {index}: {day}  {label}")


```
### 🔻 String — every character is an item
```python
city = "Karachi"

for letter in city:
    print(letter, end="-")

# - Loop Over a List of Strings
names = ["Ali", "Sara", "Bilal"]

for name in names:
    print(f"{name}:", end=" ")
    for char in name:
        print(char, end=".")
    print() 

```

### 🔻 Set — order is not guaranteed
```python
unique_ids = {101, 203, 305, 407}

for uid in unique_ids:
    print(uid, end=" ")
    
# - Filtering with a Set (fast membership check):
banned_users = {"spammer99", "bot123", "fake_acc"}
logins = ["ali_k", "spammer99", "sara_m", "bot123", "bilal_dev"]

for user in logins:
    if user in banned_users:
        print(f"  ❌ Blocked:  {user}")
    else:
        print(f"  ✅ Allowed:  {user}")

# - Iterating Set Operations:
python_students = {"Ali", "Sara", "Bilal", "Hina"}
java_students   = {"Sara", "Hina", "Usman", "Zara"}

print("Students in BOTH courses:")
for student in python_students & java_students:   # intersection
    print(f"  {student}")

print("Students in Python only:")
for student in python_students - java_students:   # difference
    print(f"  {student}")

```

### 🔻 Dictionary — by default gives keys
```python
student = {"name": "Ayesha", "age": 21, "gpa": 3.8}

# - Keys only (default):
for key in student:
    print(key, end=" ")
# Output: name age gpa

# - Values only:
for value in student.values():
    print(value, end=" ")
# Output: Ayesha 21 3.8

# - Both key and value:
for key, value in student.items():
    print(f"  {key}: {value}")
# Output:
#   name: Ayesha
#   age: 21
#   gpa: 3.8

# Nested Dictionary: 
hostel = {
    "Room 1": {"occupant": "Ali",   "rent": 8000},
    "Room 2": {"occupant": "Sara",  "rent": 9500},
    "Room 3": {"occupant": "Bilal", "rent": 8500},
}

total = 0
for room, info in hostel.items():
    print(f"{room} : {info['occupant']} Rs.{info['rent']}")
    total += info["rent"]

print(f"Total Rent Rs.{total}")

```
---

## 🔶 zip() — Loop Over Multiple Lists Together

`zip()` pairs items from two or more lists side by side. It stops at the **shortest** list.

```python
names  = ["Ali", "Sara", "Bilal", "Hina"]
grades = [88,    92,     75,      96    ]
cities = ["Karachi", "Lahore", "Islamabad", "Quetta"]

for name, grade, city in zip(names, grades, cities):
    print(f"  {name:<8} {grade}   {city}")
# Output:
#   Ali      88   Karachi
#   Sara     92   Lahore
#   Bilal    75   Islamabad
#   Hina     96   Quetta
```

### zip stops at the shortest list:
```python
short = [1, 2, 3]
long  = [10, 20, 30, 40, 50]

for a, b in zip(short, long):
    print(a, b, end=" | ")
# Output: 1 10 | 2 20 | 3 30   (40 and 50 ignored)
```
---

## 🔶 Loop Control — break, continue, pass

### break — exit the loop immediately:
```python
products = ["keyboard", "mouse", "monitor", "webcam"]

for product in products:
    if product == "monitor":
        print(f"Found: {product}")
        break
    print(f"Checked: {product}")
# Output:
# Checked: keyboard
# Checked: mouse
# Found: monitor
```

### continue — skip the current item, move to next:
```python
marks = [78, 45, 92, 38, 85, 55, 91]

for mark in marks:
    if mark < 60:
        continue
    print(f"  Pass: {mark}")
# Output:
#   Pass: 78
#   Pass: 92
#   Pass: 85
#   Pass: 91
```

### pass — placeholder, does nothing:
```python
categories = ["electronics", "clothing", "food"]

for category in categories:
    if category == "food":
        pass    # TODO: add food logic later
    else:
        print(f"  Processing: {category}")
```

---

## 🔶 for / else

The `else` block runs **only if the loop completed without hitting `break`**. If `break` fired, `else` is skipped entirely.

```python
# No break → else RUNS
for i in range(3):
    print(f"  item {i}")
else:
    print("  Loop completed — else ran")

# break → else SKIPPED
for i in range(5):
    if i == 3:
        break
    print(f"  item {i}")
else:
    print("  This will NOT print")
```

### Real-world use — search with result reporting:
```python
emails = ["ali@gmail.com", "sara@yahoo.com", "bilal@gmail.com"]
search = "zara@gmail.com"

for email in emails:
    if email == search:
        print(f"  Found: {email}")
        break
else:
    print(f"  '{search}' not found in the list")
# Output: 'zara@gmail.com' not found in the list
```

---

## 🔶 Nested For Loops

A loop inside a loop. For every **one** iteration of the outer loop, the inner loop runs **all** its iterations.

```python
# Pairing every student with every subject
students = ["Ali", "Sara"]
subjects = ["Math", "Physics"]

for student in students:
    for subject in subjects:
        print(f"  {student} → {subject}")
# Output:
#   Ali → Math
#   Ali → Physics
#   Sara → Math
#   Sara → Physics
```

> ⚠️ Every extra level of nesting multiplies total iterations. Two loops of 100 = 10,000 runs. Keep nesting shallow when possible.

---

## 🔶 List Comprehension — For Loop in One Line

A short, clean way to build a list using a `for` loop in a single line.

```python
# Traditional for loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)   # [1, 4, 9, 16, 25]

# Same thing as list comprehension
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# With a condition — only even squares
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)   # [4, 16, 36, 64, 100]
```

---

## 🔶 Real World Examples

### 🔻 Example 1 — Student Report Card
```python
print("=== Report Card ===")
print("-" * 30)

students = {
    "Ayesha": {"Math": 90, "Physics": 85, "Chemistry": 88},
    "Bilal":  {"Math": 75, "Physics": 80, "Chemistry": 70},
    "Zara":   {"Math": 95, "Physics": 92, "Chemistry": 97},
}

for name, subjects in students.items():
    average = sum(subjects.values()) / len(subjects)

    # Grade assignment using if/elif/else
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    else:
        grade = "C"

    print(f"\n{name}")
    for subject, score in subjects.items():
        print(f"  {subject:} {score}")
    print(f"  {'Average':} {average:.1f}  →  Grade {grade}")
```

---

### 🔻 Example 2 — Restaurant Bill Calculator
```python
print("====== Bill ======")
print("-" * 30)

menu = {
    "Biryani": 350,
    "Karahi": 550,
    "Naan": 30,
    "Lassi": 120,
}

order = ["Biryani", "Naan", "Naan", "Lassi", "Karahi"]

bill = {}
for item in order:
    bill[item] = bill.get(item, 0) + menu[item]

for item, amount in bill.items():
    print(f"  {item:} Rs.{amount}")
print("-" * 30)
print(f"  {'Total':} Rs.{sum(bill.values())}")
```

---

### 🔻 Example 3 — Filtering Employees by Department
```python

print("=== Engineering Team ===")
employees = [
    {"name": "Usman",  "dept": "Engineering", "salary": 85000},
    {"name": "Fatima", "dept": "Design",       "salary": 72000},
    {"name": "Hamza",  "dept": "Engineering",  "salary": 91000},
    {"name": "Nadia",  "dept": "Marketing",    "salary": 67000},
]
total = 0
for emp in employees:
    if emp["dept"] == "Engineering":
        print(f"  {emp['name']}: Rs.{emp['salary']:,}")
        total += emp["salary"]
print(f"{'─' * 28}")
print(f"  {'Total Payroll':} Rs.{total:,}")

```

---

### 🔻 Example 4 — Voting Results
```python
print("=== Election Results ===")
print("-" * 30)

ballot = ["Ali", "Sara", "Ali", "Bilal", "Sara", "Ali", "Sara", "Bilal", "Ali"]

votes = {}
for vote in ballot:
    votes[vote] = votes.get(vote, 0) + 1

for candidate, count in votes.items():
    bar = "█" * count
    print(f"  {candidate:<8} {bar} ({count})")

winner = max(votes, key=votes.get)
print("-" * 30)
print(f"🏆 Winner: {winner} with {votes[winner]} votes")

```

---

## 🔶 Common Mistakes

### ❌ Mistake 1 — Using range(len()) when you can iterate directly:
```python
fruits = ["mango", "banana", "guava"]

# Wrong — unnecessary complexity
for i in range(len(fruits)):
    print(fruits[i])

# Right — clean and Pythonic
for fruit in fruits:
    print(fruit)
```

### ❌ Mistake 2 — Modifying a list while looping over it:
```python
numbers = [1, 2, 3, 4, 5, 6]

# Wrong — skips items unpredictably
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

# Right — loop over a copy using [:]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)   # [1, 3, 5]
```

### ❌ Mistake 3 — Loop variable persists after the loop ends:
```python
for item in ["apple", "banana", "cherry"]:
    pass

print(item)   # cherry ← still accessible after loop ends!

# Fix — be explicit if you need the last value
last_item = None
for item in ["apple", "banana", "cherry"]:
    last_item = item

print(last_item)   # cherry ✅ — intentional and clear
```

---

