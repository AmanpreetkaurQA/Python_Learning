#  Lists- Lists are used to store multiple items in a single variable.
#  it is an object of the List class.
# Mutable (can be changed)- The list is changeable, meaning that we can change, add, and remove items in a list after it has bee
# Ordered- When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# Allows duplicates- Since lists are indexed, lists can have items with the same value:
# Defined using square brackets []
# List items can be of any data type:
# List Methods
    # append()	Adds an element at the end of the list
    # clear()	Removes all the elements from the list
    # copy()	Returns a copy of the list
    # count()	Returns the number of elements with the specified value
    # extend()	Add the elements of a list (or any iterable), to the end of the current list
    # index()	Returns the index of the first element with the specified value
    # insert()	Adds an element at the specified position
    # pop()	Removes the element at the specified position
    # remove()	Removes the item with the specified value
    # reverse()	Reverses the order of the list
    # sort()	Sorts the list

thislist = ["apple", "banana", "cherry", "papaya"]
print(thislist[1])           

thislist.append("orange")    # Add to list  To add an item to the end of the list
print(thislist)             

thislist[0] = "mango"        # Modify element
print(thislist)              

# Insert Items
# The insert() method inserts an item at the specified index:
thislist.insert(2, "watermelon")
print(thislist)



# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")


# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1])                                     

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# The search will start at index 1 (included) and end at index 2 (not included).
print(thislist[1:2])       


# Extend List
# To append elements from another list to the current list, use the extend() method.
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item
# The remove() method removes the specified item.   If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index:  The del keyword can also delete the list completely.
del thislist[0]
print(thislist)
# del thislist

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# thislist.clear()
# print(thislist)

# Copy a List
# You can use the built-in List method copy() to copy a list.
# You can also make a copy of a list by using the : (slice) operator.
# # Another way to make a copy is to use the built-in method list().
mylist = thislist.copy()
print(mylist)

mylist = list(thislist)
print(mylist)

mylist = thislist[:]
print(mylist)

# Sort List
# The sort() method sorts the list in ascending order, by default:
# To sort descending, use the keyword argument reverse = True:
# The reverse() method reverses the current sorting order of the elements.
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

thislist.reverse()
print(thislist)

# Loop Through a List
# You can loop through the list items by using a for loop:
for x in thislist:
  print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
for i in range(len(thislist)):
  print(thislist[i])

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
freshlist = [x for x in thislist if "a" in x]
print(freshlist)