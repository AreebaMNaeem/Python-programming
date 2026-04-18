# PYTHON VARIABLES
# ============================================================

# WHAT IS A VARIABLE?
# A variable is just a name that stores data so you can use it later in your program.
# Think of it like a box with a label:
# - The box holds the value (like a number, text, or list).
# - The label is the variable name you use to refer to that value.

city = "Karachi"
temperature = 38
is_sunny = True
# Python figured out the types on its own — that's dynamic typing.

# ----------------------------------------------------------------
# NAMING RULES (what Python allows or rejects)
# RULE 1 — Must start with a letter or underscore.
# RULE 2 — Can only contain letters, digits, and underscores.
# RULE 3 — Variable names in Python are Case-sensitive (This means age,Age,AGE are different variables).
# RULE 4 — Cannot be a Python keyword (e.g.,while,if,else etc.).
# RULE 5 — Variable names cannot contain spaces or special characters, except for underscores (_).

# VALID names
user_name = "Ali"
_private = 42
totalMarks2024 = 95

# INVALID — these cause SyntaxError or logical problems
# 2fast = "error"          → cannot start with a digit
# user-name = "Ali"        → hyphen is an operator, not allowed
# class = 10               → 'class' is a reserved keyword
# my var = 5               → spaces not allowed

# ----------------------------------------------------------------
# NAMING CONVENTIONS (what good Python looks like)
# Use snake_case for regular variables (PEP 8 standard)
# Use UPPER_CASE for constants
# Use _leading_underscore for "private" or internal variables
# Avoid single letters except in loops (i, j, k) or math (x, y)

student_name = "Sara"          # good
PASSING_MARKS = 50             # constant
_config_path = "/etc/app.cfg"  # private/internal

# ----------------------------------------------------------------
# ASSIGNMENT — THE BASICS
# Single assignment
age = 21
height = 5.9
country = "Pakistan"

# Re-assignment — variables can change value and even type
score = 100        # int
score = 99.5       # now a float — Python allows this
score = "pending"  # now a string — still valid

# ----------------------------------------------------------------
# MULTIPLE ASSIGNMENT
# Assign the same value to many variables at once
x = y = z = 0

# Assign different values to different variables in one line
name, roll_no, gpa = "Ahmed", 101, 3.8
print(name, roll_no, gpa)   # Ahmed 101 3.8

# ----------------------------------------------------------------
# CONSTANTS
# Constants in Python are variables that should remain unchanged throughout execution, but Python trusts the programmer to follow the rule — it doesn’t enforce it.
# Python has no built-in constant enforcement.The convention is ALL_CAPS(that means constant names are written in uppercase) — it signals "don't change this."

MAX_RETRIES = 3
BASE_URL = "https://api.example.com"
PI = 3.14159265358979

# If you want real enforcement, Python 3.8+ introduced a Final type hint in the typing module you can use that.

from typing import Final

SPEED_OF_LIGHT: Final = 299_792_458   # If you try to reassign SPEED_OF_LIGHT, Python itself won’t stop you.However, type checkers like mypy will raise a warning.