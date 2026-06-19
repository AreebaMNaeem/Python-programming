# 📋 List Comprehension in Python

---

## 🔶 What is List Comprehension?

Imagine you have a list of numbers and want to square each one. You could write:

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)   # [1, 4, 9, 16, 25]
```

But Python has a **cleaner way** to do this in a single line:

```python
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)   # [1, 4, 9, 16, 25]
```

**List comprehension** is a compact, readable way to create new lists by applying an operation to each item in an existing list. It's just **a for loop written on one line**.

---

## 🔶 Basic Syntax:

```
new_list = [expression for item in iterable]
```

Breaking it down:  
| `expression` : What to do with each item `num * 2`  
| `for item in iterable` : Loop through a collection `for num in numbers`  
| `new_list` : The result list  `doubling = [...]`  


---

### Example 1 — Extract first letter of each word:
```python
cities = ["Karachi", "Lahore", "Islamabad", "Peshawar"]
initials = [city[0] for city in cities]
print(initials)   # ['K', 'L', 'I', 'P']
```

### Example 2 — Convert strings to integers:
```python
numbers_as_text = ["10", "25", "50", "100"]
numbers_as_int = [int(x) for x in numbers_as_text]
print(numbers_as_int)   # [10, 25, 50, 100]
```

---

## 🔶 Adding a Filter — The `if` Clause:

You can add a condition to **only include** certain items:

```
new_list = [expression for item in iterable if condition]
```

### Example 1 — Keep only even numbers:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print(evens)   # [2, 4, 6, 8, 10]
```

### Example 2 — Keep only words longer than 5 characters:
```python
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_words = [word for word in words if len(word) > 5]
print(long_words)   # ['elephant', 'butterfly']
```

### Example 3 — Keep only positive numbers:
```python
temperatures = [25, -5, 30, -10, 15, 0, 20]
above_zero = [temp for temp in temperatures if temp > 0]
print(above_zero)   # [25, 30, 15, 20]
```

---

## 🔶 If-Else Inside Comprehension:

You can transform items **differently** based on a condition:

```
new_list = [expression_if_true if condition else expression_if_false for item in iterable]
```

### Example 1 — Label numbers as odd or even:
```python
numbers = [1, 2, 3, 4, 5, 6]
labels = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(labels)   # ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
```

### Example 2 — Grade students based on marks:
```python
marks = [95, 72, 88, 65, 92, 78]
grades = ["Pass" if mark >= 70 else "Fail" for mark in marks]
print(grades)   # ['Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass']
```

### Example 3 — Price adjustment based on category:
```python
prices = [100, 500, 200, 1000, 300]
adjusted = [price * 1.10 if price < 500 else price * 0.95 for price in prices]
print(adjusted)   # [110.0, 475.0, 220.0, 950.0, 330.0]
```

---

## 🔶 Nested List Comprehension

Flatten multi-dimensional lists or create nested structures:

### Flattening a 2D list:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten: convert to single list
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**How to read it:**
- `for row in matrix` — loop through each row
- `for num in row` — loop through each number in that row
- `num` — take that number

---

### Flatten with filter:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten AND keep only even numbers
even_flat = [num for row in matrix for num in row if num % 2 == 0]
print(even_flat)   # [2, 4, 6, 8]
```

---

## 🔶 Real World Examples :

### Example 1 — Cleaning a Dataset (Remove Empty Values):
```python
raw_data = ["Ali", "", "Sara", None, "Bilal", "", "Hina"]

# Remove empty strings and None
cleaned = [name for name in raw_data if name]
print(cleaned)   # ['Ali', 'Sara', 'Bilal', 'Hina']
```

---

### Example 2 — Email Validation and Filtering:
```python
email_list = [
    "ali@gmail.com",
    "invalid-email",
    "sara@yahoo.com",
    "bilal@",
    "hina@outlook.com",
    "zara@company.pk"
]

# Keep only valid emails (contain @ and domain)
valid_emails = [email for email in email_list if "@" in email and "." in email.split("@")[1]]
print(valid_emails)
# ['ali@gmail.com', 'sara@yahoo.com', 'hina@outlook.com', 'zara@company.pk']

# Extract only Gmail users
gmail_only = [email for email in email_list if email.endswith("@gmail.com")]
print(gmail_only)   # ['ali@gmail.com']
```

---

### Example 3 — File Names Processing:
```python
files = ["document.pdf", "image.jpg", "script.py", "photo.png", "data.csv"]

# Extract only image files
images = [f for f in files if f.endswith((".jpg", ".png", ".gif"))]
print(images)   # ['image.jpg', 'photo.png']

# Remove extension
names_only = [f.split(".")[0] for f in files]
print(names_only)   # ['document', 'image', 'script', 'photo', 'data']

# Convert to uppercase
uppercase = [f.upper() for f in files]
print(uppercase)
# ['DOCUMENT.PDF', 'IMAGE.JPG', 'SCRIPT.PY', 'PHOTO.PNG', 'DATA.CSV']
```

---