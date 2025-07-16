# Tuples-A tuple is a collection which is ordered and unchangeable.
#  it is an object of the tuple class.
# Immutable (cannot be changed)- Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Ordered- Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allows duplicates- Since tuples are indexed, they can have items with the same value:
# Defined using parentheses ()
# Tuples are Slightly faster than lists in performance
# Often used to return multiple values from functions
# Tuple items can be of any data type:


# Creating Tuples
empty = ()
print(empty)
single = (10,)  # Single element tuple must have a comma
print(single)
mixed = (1, "hello", 3.14, True)
print
nested = (1, [2, 3], (4, 5))
print(nested)


# Access Tuples elements(Indexing and Slicing)
colors = ("red", "green", "blue")
print(colors[2])  
print(colors[-1])   
print(colors[0:2])

# Tuple Length
# To determine how many items a tuple has, use the len() function:
print(len(colors))


# Change Tuple Values- Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x= list(colors)
x[1] = "yellow"
colors = tuple(x)
print(colors)

# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

y=list(colors)
y.append("orange")
colors=tuple(y)
print(colors)

z= ("Black",)
colors += z
print(colors)

# Remove Items from Tuples:
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
# The del keyword can delete the tuple completely:
y= list(colors)
y.remove("Black")
colors=tuple(y)
print(colors)

# del colors
# print(colors)


# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking": Assign each element to a variable in one line:
person = ("Alice", 30, "New York")
name, age, city = person
print(f"{name} is {age} years old and lives in {city}")


# Loop Through a Tuple
for x in colors:
  print(x)
  

for i in range(len(colors)):
  print(colors[i])

i = 0
while i < len(colors):
  print(colors[i])
  i = i + 1
  
# Join Tuples
# To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
mytuple = colors * 2
print(mytuple)

# Tuple Methods
# Python has two built-in methods that you can use on tuples.
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

nums = (1, 2, 3, 2, 2)
print(nums.count(2))  
print(nums.index(3))   