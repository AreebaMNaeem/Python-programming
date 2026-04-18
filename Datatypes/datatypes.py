# PYTHON DATA TYPES — The Basic Four
# ============================================================

# Python is a dynamically typed language, which means every value you store has a type — but you never have to declare it yourself.
# Python reads the value and figures it out.

# SECTION 1 — INTEGER (int)
# An integer is any whole number — positive, negative, or zero.No decimal point, no fractions. Just a clean whole number.
# How big can an int get? Unlike many languages, Python integers have no fixed size limit.They grow as large as your memory allows.

students_in_class = 42
salary = 50_000       # Use underscores as a visual separator (like commas in writing).Python ignores them — they're just for readability.

print(type(students_in_class))   # <class 'int'>
print(f"My Salary is: {salary}")

# ================================================================
# SECTION 2 — FLOAT (float)
# A float is any number with a decimal point.

item_price = 49.99
absolute_zero = -273.15

print(type(item_price))   # <class 'float'>
print(f"The Price is : {item_price}")

# ================================================================
# SECTION 3 — STRING (str)
# A string is an ordered sequence of characters.
# Strings are immutable — once created, they cannot be changed in place.

username = "ali_codes"
paragraph = """This is a
multi-line string.
It preserves newlines."""

print(type(username))   # <class 'str'>
print(f"The Username is: {username}")

## Escape characters:
# Use backslash to insert special characters inside strings.

print("She said \"wow\"")      # She said "wow"
print('It\'s working')         # It's working
print("Line 1\nLine 2")        # newline
print("Col1\tCol2")            # tab
print("back\\slash")           # backslash

## String formatting (To add the variables in a string):
name = "Hassan"
age = 22
gpa = 3.856
result = f"Student: {name} has Age: {age} and GPA: {gpa:.2f}"
print(result)
# Output: Student: Hassan has Age: 22 and GPA: 3.86

## .format() — older but still widely used
print("Name: {}, Score: {:.1f}".format("Sara", 94.678))

## String Operations
### 1. Indexing:
# Strings are sequences — every character has an index.To access a single character square brackets '[]' can be used.
# Positive index: left to right starting at 0
# Negative index: right to left starting at -1

course = "Python"
#        P  y  t  h  o  n
# index  0  1  2  3  4  5
# neg   -6 -5 -4 -3 -2 -1

print(course[0])      # P
print(course[-1])     # n

### 2. Slicing (To extract a portion of a string):

print(course[1:4])    # yth   → start:stop (stop is excluded)
print(course[:3])     # Pyt   → from beginning to index 2
print(course[3:])     # hon   → from index 3 to end
print(course[::2])    # Pto   → every 2nd character

### 3. String Concatenation (Joining strings together):
first_name = "Areeba"
last_name = "Naeem"

full_name = first_name + " " + last_name
print(full_name)   # Output: Areeba Naeem


## Common string methods:
city = "  karachi  "
print(len(city))             # 11             → length of the string
print(city.strip())          # "karachi"      → remove surrounding whitespace
print(city.strip().upper())  # "KARACHI"      → change the case
print(city.strip().lower())  # "karachi"
print(city.strip().title())  # "Karachi"      → capitalize first letter

sentence = "python is powerful and python is popular"
print(sentence.count("python"))          # 2
print(sentence.replace("python", "Go"))  # replaces all occurrences of the part of string

### split(separator) : This splits the string into a list based on the separator:
print(sentence.split())   # ['python', 'is', 'powerful', 'and', 'python', 'is', 'popular']

line = "Ali,25,Karachi,Engineer"
print(line.split(","))    # ['Ali', '25', 'Karachi', 'Engineer']

### join : to combine a list (or any iterable) of strings into one single string:
words = ["Python", "is", "great"]
print(" ".join(words))       # Python is great

# ================================================================
# SECTION 4 — BOOLEAN (bool)
# A boolean has exactly two possible values: True or False.
# True == 1 and False == 0 — this has real consequences.

is_logged_in = True
has_errors = False

print(type(is_logged_in))   # <class 'bool'>
print(f"Is the User logged In: {is_logged_in}")
