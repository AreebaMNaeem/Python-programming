# 🔄 Recursion in Python

---

## 🔶 What is Recursion?

Recursion happens when a **function calls itself** to solve a problem by breaking it into smaller versions of the same problem.

---

## 🔶 The Two Essential Parts:

Every recursive function **must** have:

### 1. **Base Case** — When to STOP
```python
if some_condition:
    return some_result   # Stop here, don't call the function again
```

### 2. **Recursive Case** — How to make progress toward the base case
```python
else:
    return function(modified_input)   # Call yourself with a smaller problem
```

**Without a base case**, you get infinite recursion → crash.

```python
# ❌ Missing base case — infinite recursion
def broken():
    return broken()   # calls itself forever

# broken()   # RecursionError: maximum recursion depth exceeded

# ✅ Has base case
def working(n):
    if n == 0:         # base case
        return "Done!"
    return working(n - 1)   # recursive case
```

---

## 🔶 Simple Example — Countdown

```python
def countdown(n):
    # BASE CASE
    if n == 0:
        print("🚀 Blast off!")
        return
    
    # RECURSIVE CASE
    print(n)
    countdown(n - 1)   # call yourself with n-1

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# 🚀 Blast off!
```

**Call stack visualization:**

```
countdown(5)  ← prints 5, waits for countdown(4)
  countdown(4)  ← prints 4, waits for countdown(3)
    countdown(3)  ← prints 3, waits for countdown(2)
      countdown(2)  ← prints 2, waits for countdown(1)
        countdown(1)  ← prints 1, waits for countdown(0)
          countdown(0)  ← base case, prints 🚀 Blast off!, returns
        ↑
      countdown(1) finishes
      ↑
    countdown(2) finishes
    ↑
  countdown(3) finishes
  ↑
countdown(4) finishes
↑
countdown(5) finishes
```

---

## 🔶 Real Examples

### Example 1 — Sum Numbers from 1 to N

```python
def sum_to_n(n):
    # BASE CASE: smallest possible input
    if n == 0:
        return 0
    
    # RECURSIVE CASE: break into smaller problem
    return n + sum_to_n(n - 1)

print(sum_to_n(5))   # 5 + 4 + 3 + 2 + 1 + 0 = 15
print(sum_to_n(10))  # 55
```

**How it works:**
```
sum_to_n(5)
= 5 + sum_to_n(4)
= 5 + (4 + sum_to_n(3))
= 5 + (4 + (3 + sum_to_n(2)))
= 5 + (4 + (3 + (2 + sum_to_n(1))))
= 5 + (4 + (3 + (2 + (1 + sum_to_n(0)))))
= 5 + (4 + (3 + (2 + (1 + 0))))
= 15
```

---

### Example 2 — Factorial (n!)

```python
def factorial(n):
    # BASE CASE
    if n == 0 or n == 1:
        return 1
    
    # RECURSIVE CASE
    return n * factorial(n - 1)

print(factorial(5))   # 5 × 4 × 3 × 2 × 1 = 120
print(factorial(3))   # 3 × 2 × 1 = 6
```

---

### Example 3 — String Reversal

```python
def reverse_string(s):
    # BASE CASE: empty string
    if len(s) == 0:
        return ""
    
    # RECURSIVE CASE: take last character + reverse the rest
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))    # "olleh"
print(reverse_string("Karachi"))  # "ihcaraK"
```

**How it works:**
```
reverse_string("hello")
= reverse_string("ello") + "h"
= (reverse_string("llo") + "e") + "h"
= ((reverse_string("lo") + "l") + "e") + "h"
= (((reverse_string("o") + "l") + "e") + "h")
= ((((reverse_string("") + "o") + "l") + "e") + "h")
= ((((""  + "o") + "l") + "e") + "h")
= "olleh"
```

---

### Example 4 — Check if a String is a Palindrome

```python
def is_palindrome(s):
    # BASE CASE: if string is length 0 or 1, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Check if first and last characters match
    if s[0] != s[-1]:  
        return False
    
    # RECURSIVE CASE: check the middle part
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))      # True
print(is_palindrome("hello"))      # False
print(is_palindrome("noon"))       # True
print(is_palindrome("a"))          # True
```

---

### Example 5 — Fibonacci Sequence

```python
def fibonacci(n):
    # BASE CASES
    if n <= 1:
        return n
    
    # RECURSIVE CASE: sum of previous two fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))   # 8   (sequence: 0,1,1,2,3,5,8)
print(fibonacci(10))  # 55
```

**Caution:** This is inefficient for large n because it recalculates the same values many times.

---

## 🔶 Real World Applications:

### Example 1 — File System Navigation:

```python
import os

def count_files_in_folder(folder_path):
    """
    Recursively count all files in a folder and its subfolders.
    """
    # BASE CASE: if path is a file, count it
    if os.path.isfile(folder_path):
        return 1
    
    # If it's not a directory, return 0
    if not os.path.isdir(folder_path):
        return 0
    
    # RECURSIVE CASE: count files in subfolders
    total = 0
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        total += count_files_in_folder(item_path)
    
    return total

# file_count = count_files_in_folder("/home/user/Documents")
```

---

### Example 2 — Power Calculation:

```python
def power(base, exponent):
    """
    Calculate base^exponent recursively.
    Example: 2^5 = 2 × 2 × 2 × 2 × 2 = 32
    """
    # BASE CASE: any number to power 0 is 1
    if exponent == 0:
        return 1
    
    # RECURSIVE CASE: base^n = base × base^(n-1)
    return base * power(base, exponent - 1)

print(power(2, 5))   # 32
print(power(3, 4))   # 81
print(power(10, 3))  # 1000
```

---

### Example 3 — GCD (Greatest Common Divisor) — Euclidean Algorithm

```python
def gcd(a, b):
    """
    Find Greatest Common Divisor using Euclidean algorithm.
    BASE CASE: when b is 0, a is the GCD.
    """
    # BASE CASE
    if b == 0:
        return a
    
    # RECURSIVE CASE: gcd(a, b) = gcd(b, a % b)
    return gcd(b, a % b)

print(gcd(48, 18))   # 6
print(gcd(100, 50))  # 50
print(gcd(17, 5))    # 1
```

---

### Example 4 — Generate Multiplication Table

```python
def print_table(n, multiplier=1):
    """
    Print multiplication table for n recursively.
    Example: print_table(3) prints 3×1, 3×2, ... 3×10
    """
    # BASE CASE: stop at 10
    if multiplier > 10:
        return
    
    # RECURSIVE CASE: print current, then increment
    print(f"{n} × {multiplier} = {n * multiplier}")
    print_table(n, multiplier + 1)

print_table(5)
# Output:
# 5 × 1 = 5
# 5 × 2 = 10
# ... and so on until 5 × 10 = 50
```

---

Key points:
  - Every recursion needs a base case
  - Each call must get closer to base case
  - Call stack grows with each call
  - Use recursion for trees/nested structures
  - Use iteration for simple loops

Debugging recursion:
  - Print each call to see the pattern
  - Verify base case is correct
  - Check that recursion makes progress
  - Use small inputs to trace execution
```

---
