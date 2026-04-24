# PYTHON WHILE LOOP
# ============================================================

# A while loop continues to run a piece of code as long as its condition stays true. 
# The instant the condition changes to False, the loop stops, and the program moves on. In a while loop, the number of iterations is also not known in advance.
# A while loop is also called as an uncontrolled loop because it can run indefinitely if the condition never becomes False.

# Key mental model:
#   → for loop  = "do this FOR each item"   (iteration-driven)
#   → while loop = "do this WHILE something is true" (condition-driven)
#     Use while loop when you don't know in advance how many times to loop.

# Basic Syntax:
#   while <condition>:
#       <body>          ← runs only while condition is True

# ================================================================
# SECTION 1 — THE BASIC WHILE LOOP :
# The condition is checked BEFORE every iteration.If it's False from the start, the body never runs even once.

num = 1                                       # Output 
                                              # 1
while num <= 5:                               # 2
    print(num)                                # 3
    num += 1   # increase by 2 each time      # 4
                                              # 5
print("Done!")                                # Done!

# The loop starts from 1 and print numbers up to 5.
# Finally, "Done!" is printed after the loop ends.

## Condition false from the start :
attempts = 10

while attempts < 5:        # 10 < 5 is False immediately
    print("This never runs")

print("Skipped entirely")   # this runs right away

# ================================================================
# SECTION 2 — COUNTING UP AND DOWN :
# Counting up:
print("\n--- Counting up ---")
n = 1
while n <= 5:
    print(n, end=" ")   # end=" " keeps output on one line
    n += 1
# Output: 1 2 3 4 5

# Counting down:
print("\n--- Counting down ---")
n = 10
while n >= 1:
    print(n, end=" ")
    n -= 2
# Output: 10 8 6 4 2

# Counting by steps — same result but explicit step control
print("\n--- Every 3rd number from 0 to 30 ---")
n = 0
while n <= 30:
    print(n, end=" ")
    n += 3
# Output: 0 3 6 9 12 15 18 21 24 27 30

# ================================================================
# SECTION 3 — LOOPING OVER SEQUENCES WITH WHILE :
# for loops are cleaner for sequences, but while gives you direct index control — useful when you need to modify the list or mid-loop 

cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]

# Basic sequence traversal :
print("\n--- Cities ---")
idx = 0
while idx < len(cities):
    print(f"  [{idx}] {cities[idx]}")
    idx += 1

# Traversal with transformation :
print("\n--- Email list ---")
idx = 0
while idx < len(cities):
    slug = cities[idx].lower().replace(" ", "_")
    print(f"  city_{slug}@gov.pk")
    idx += 1
# For each city, we convert it to lowercase, replace spaces with underscores, then build an email.Like this ,city_karachi@gov.pk

# Dictionary traversal using while :
student_scores = {
    "Ayesha": 88,
    "Bilal": 72,
    "Zara": 95,
    "Omar": 61,
    "Hina": 79
}

keys = list(student_scores.keys())
idx = 0

print("\n--- Student report ---")
while idx < len(keys):
    name = keys[idx]
    score = student_scores[name]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"  {name:<10} {score:>3}   Grade: {grade}")
    idx += 1

# ================================================================
# SECTION 4 — while True + break (EVENT-DRIVEN LOOPS) : 
# Sometimes you don't know the exit condition until you're inside the loop. The pattern: start with while True, exit with break.
# This is the correct and intentional use of an infinite loop.

# Example: Input validation — keep asking until you get valid input

while True:
    user_input = input("Enter a number: ")

    if user_input.isdigit():
        print("Valid number entered!")
        break   # stops the loop when condition is met
    else:
        print("Invalid input, try again.")
        
# Example: Game loop structure
game_running = True
turn = 1
max_turns = 4

print("\n--- Game loop ---")
while True:
    print(f"  Turn {turn}")
    turn += 1

    if turn > max_turns:
        print("  Game over!")
        break

# ================================================================
# SECTION 5 — while loop with break :
# break immediately exits the innermost loop, regardless of whether the while condition is still True.
# Execution jumps to the first statement AFTER the loop.

numbers = [10, 45, 23, 67, -5, 89, 34]
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        print(f"First negative number found: {numbers[i]} at index {i}")
        break
    i += 1        # Output: First negative number found: -5 at index 4
    
# ================================================================
# SECTION 6 — while loop with continue : 
# continue skips the REST of the current iteration and jumps back to the while condition check. The loop does NOT exit.

print("\n--- Skip even numbers ---")
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue        # skip even numbers
    print(n, end=" ")
# Output: 1 3 5 7 9

# IMPORTANT: When using continue, make sure you update the loop variable BEFORE the continue, or you'll create an infinite loop.

# ================================================================
# SECTION 7 — while loop with pass : 
# pass is a null statement — it does nothing.
# Use it as a placeholder when Python syntax requires a body but you have nothing to put there yet.

# Placeholder loop body during development
data_buffer = []
position = 0

while position < 5:
    pass    # TODO: implement buffer reading logic
    position += 1

# pass allows the loop to exist without giving an error. It is useful when you plan to add logic later

# ================================================================
# SECTION 8 — while / else : 
# Python's while loop has an optional else clause.
# The else block runs ONLY IF the loop ended naturally (condition became False). It does NOT run if the loop was exited with break.
# This is the most overlooked feature of Python loops.

# Case 1: Loop completes naturally → else RUNS
n = 1                                                  # Output:
while n <= 3:                                          # Number 1
    print(f"Number {n}")                               # Number 2
    n += 1                                             # Number 3
else:                                                  # Loop finished normally — else block ran
    print("Loop finished normally — else block ran")
    

# Case 2: Loop exits via break → else does NOT run
n = 1
while n <= 5:
    if n == 3:
        break           # forced exit
    print(f"Number {n}")
    n += 1
else:
    print("This will NOT print")

# ================================================================
# SECTION 9 — DO-WHILE PATTERN :
# Python has no do-while keyword.
# In a do-while loop (from C/Java), the body runs at LEAST once before the condition is checked.We simulate it with while True + break at the end.

# Standard while — body may never run:
value = 100
while value < 10:
    print("standard while: never runs if condition is False at start")

# do-while pattern — body ALWAYS runs at least once:                 
attempt = 0
while True:
    attempt += 1
    print(f"  Attempt {attempt}")   # always runs at least once
    if attempt >= 3:
        break                       # condition checked at the END
    
# Output :  Attempt 1       Attempt 2       Attempt 3