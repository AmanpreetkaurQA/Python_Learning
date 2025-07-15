# Elif
# The elif keyword( Stands for "else if") is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.

x = 1
if x > 20:
    print("x is greater than 20")
elif x > 5:
    print("x is greater than 5 but not greater than 20")
else:
    print("x is 1 or less")

# You can also have an else without the elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

a = 200
b = 33
if a > b: print("a is greater than b")


# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

a = 2
b = 330
print("A") if a > b else print("B")

# And
# The and keyword is a logical operator, and is used to combine conditional statements:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The or keyword is a logical operator, and is used to combine conditional statements:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


# Nested If
# You can have if statements inside if statements, this is called nested if statements.

x = 41
if x > 10:
  print("Above ten")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The Python Match Statement
# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# Default Value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

# Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

# Example
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# Nested if-elif-else with for loop

students = {
    'Aman': 92,
    'Neha': 76,
    'Ravi': 59,
    'Pooja': 85,
    'Karan': 44
}

for name, score in students.items():
    print(f"\nEvaluating {name}'s performance:")

    if score >= 90:
        print("Grade: A - Excellent")
    elif score >= 75:
        print("Grade: B - Good")
    elif score >= 60:
        print("Grade: C - Average")
    elif score >= 40:
        print("Grade: D - Needs Improvement")
    else:
        print("Grade: F - Fail")



# Using while with break and continue
# Scenario: Simulate a user login system with 3 attempts.

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    
    if password == "":
        print("Empty input! Try again.")
        continue  # skip counting this as an attempt

    if password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect password.")
        attempts += 1

if attempts == max_attempts:
    print("Too many failed attempts. Account locked.")
