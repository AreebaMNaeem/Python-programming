# PYTHON OPERATORS
# Arithmetic | Assignment | Comparison | Logical
# ============================================================

# An operator is a symbol that tells Python to perform a specificoperation on one or more values (called operands).
# This file covers four essential operator categories:
#   → Arithmetic   (math operations)
#   → Assignment   (store and update values)
#   → Comparison   (compare values, always return bool)
#   → Logical      (combine conditions)

# ================================================================
# SECTION 1 — ARITHMETIC OPERATORS :
# These perform mathematical calculations.Result type depends on the operands.
a = 17
b = 5

print(a + b)     # 22  → addition
print(a - b)     # 12  → subtraction
print(a * b)     # 85  → multiplication
print(a / b)     # 3.4 → true division — ALWAYS returns float

## Floor Division : Floor Division meaning the result is the integer value "discarding any fractional part"

a = 20
b = 3
c = a // b # 20 ÷ 3 = 6.66… but floor division keeps only 6.
print(c)   # Output: 6 - This performs floor division of a by b.


## Modulo : Returns the remainder after division.This matters for negative numbers.

a = 20
b = 3
c = a % b
print(c)  # Output: 2

## Exponentiation : Raises a number to the power of another number.
print(2 ** 10)    # 1024
a = 2
b = 3
c = a ** b
print(c)  # Output: 8

## Operator precedence :
# Python follows PEMDAS / BODMAS — same as standard math. Use parentheses when in doubt — they always win.

print(2 + 3 * 4)        # 14  → multiplication first
print((2 + 3) * 4)      # 20  → parentheses override
print(2 ** 3 ** 2)      # 512 → ** is right-associative: 2**(3**2) = 2**9
print(-2 ** 2)           # -4  → -(2**2), not (-2)**2

# ================================================================
# SECTION 2 — ASSIGNMENT OPERATORS :
# The basic assignment operator ""=" stores a value in a variable.

score = 100

## Augmented assignment operators : These combine an operation with assignment. 
# Instead of writing long expressions, you can update the variable in a shorter way.

score += 10     # score = score + 10  → 110
score -= 5      # score = score - 5   → 105
score *= 2      # score = score * 2   → 210
score //= 4     # score = score // 4  → 52
score %= 50     # score = score % 50  → 2
score **= 3     # score = score ** 3  → 8
score /= 4      # score = score / 4   → 2.0

print(score)    # 2.0

# ------ All augmented operators in one place -------------------
#
#  Operator  |  Meaning               |  Example      | Equivalent
#  ----------|------------------------|---------------|------------
#  +=        |  add and assign        |  x += 3       | x = x + 3
#  -=        |  subtract and assign   |  x -= 3       | x = x - 3
#  *=        |  multiply and assign   |  x *= 3       | x = x * 3
#  /=        |  divide and assign     |  x /= 3       | x = x / 3
#  //=       |  floor div and assign  |  x //= 3      | x = x // 3
#  %=        |  modulo and assign     |  x %= 3       | x = x % 3
#  **=       |  power and assign      |  x **= 3      | x = x ** 3

# ================================================================
# SECTION 3 — COMPARISON OPERATORS :
# Comparison operators compare two values and ALWAYS return a bool.They are the building blocks of every condition in your code.
# = is assignment. == is comparison. Mixing them is a classic bug.

x = 42
y = 100

print(x == y)    # False → equal to
print(x != y)    # True  → not equal to
print(x < y)     # True  → less than
print(x > y)     # False → greater than
print(x <= y)    # True  → less than or equal to
print(x >= y)    # False → greater than or equal to

print(5 == 5.0)    # True   → same value, different types

## Strings: compare lexicographically (character by character by Unicode value)
print("apple" < "banana")    # True  → 'a' < 'b'
print("apple" < "Apple")     # False → lowercase 'a' (97) > uppercase 'A' (65)
print("abc" == "abc")        # True

## Booleans compared to integers:
print(True == 1)     # True
print(False == 0)    # True
print(True > False)  # True

# ================================================================
# SECTION 4 — LOGICAL OPERATORS :
# Logical operators combine or modify boolean expressions.They are: and, or, not.
# Result: bool in most cases, but Python returns actual operand value 

## 1. and :
# Returns True only if BOTH operands are truthy.
# Returns the first falsy value found, or the last value if all truthy.

print(True and True)     # True
print(True and False)    # False
print(False and True)    # False
print(False and False)   # False

age = 20
has_id = True
print(age >= 18 and has_id)   # True  → both conditions met

## 2. or :
# Returns True if AT LEAST ONE operand is truthy.
# Returns the first truthy value found, or the last value if all falsy.

print(True or False)     # True
print(False or True)     # True
print(False or False)    # False
print(True or True)      # True

is_admin = False
is_owner = True
print(is_admin or is_owner)   # True  → one condition is enough

## 3. not :
# Flips the boolean value of its operand.Always returns True or False (actual bool).

print(not True)    # False
print(not False)   # True
print(not 0)       # True   → 0 is falsy, not falsy = True
print(not 42)      # False  → 42 is truthy, not truthy = False
print(not "")      # True   → empty string is falsy
print(not "hi")    # False  → non-empty string is truthy

## Short-circuit evaluation :
# Python is lazy — it stops evaluating as soon as the result is certain.
# - With 'and': if the first operand is falsy, the second is NEVER evaluated
# - With 'or':  if the first operand is truthy, the second is NEVER evaluated
# This is not just an optimization — it prevents errors and enables patterns.


## 'and' and 'or' return operand values, not just bools :
# This is the key insight that enables the patterns above. Python returns the actual deciding operand, not True/False.

print(0 and "hello")     # 0       → first is falsy, returned immediately
print(5 and "hello")     # "hello" → first is truthy, second decides
print(0 or "hello")      # "hello" → first is falsy, second decides
print(5 or "hello")      # 5       → first is truthy, returned immediately
print(0 or "" or None)   # None    → all falsy, last one returned

## 'not' always returns an actual bool regardless of input type:
print(not 0)       # True  (not an int)
print(not "")      # True  (not a string)

# ================================================================
# Operator precedence for logical operators :
# Order: not → and → or
# Use parentheses to make complex conditions readable.

a, b, c = True, False, True

print(a or b and c)          # True  → 'and' first: b and c = False, then a or False = True
print((a or b) and c)        # True  → parentheses: a or b = True, True and c = True
print(not a or b)            # False → not first: not a = False, False or b = False
print(not (a or b))          # False → parentheses: a or b = True, not True = False

# ================================================================
