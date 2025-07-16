# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Mutable- Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# do not allow duplicates- Dictionaries cannot have two items with the same key:
# The values in dictionary items can be of any data type:
# Indexed by keys, not by numbers
# Defined using curly braces {}
# Dictionary Methods
    # clear()	        Removes all the elements from the dictionary
    # copy()	        Returns a copy of the dictionary
    # fromkeys()	    Returns a dictionary with the specified keys and value
    # get()	            Returns the value of the specified key
    # items()	        Returns a list containing a tuple for each key value pair
    # keys()	        Returns a list containing the dictionary's keys
    # pop()	            Removes the element with the specified key
    # popitem()	        Removes the last inserted key-value pair
    # setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
    # update()	        Updates the dictionary with the specified key-value pairs
    # values()	        Returns a list of all the values in the dictionary

# Create a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# There is also a method called get() that will give you the same result:
# The keys() method will return a list of all the keys in the diction
# The values() method will return a list of all the values in the dictionary.
# The items() method will return each item in a dictionary, as tuples in a list.
print(person["name"])
print(person["age"])
print(person.get("city"))
print(person.keys())
print(person.values())
print(person.items())

# Modify Items:
# You can modify the value of a specific item by referring to its key name:
# The update() method will update the dictionary with the items from the given argument.
person["name"] = "Aman"
print(person)

person.update({"age": 25})
print(person)

# Add Items:
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
person["email"] = "aman@email.com" 
print(person)

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# The del keyword removes the item with the specified key name:
# The clear() method empties the dictionary:
    
person.pop("email")
print(person)

person.popitem()
print(person)

del person["name"]
print(person)

person.clear()
print(person)

# Looping Through a Dictionary
# You can loop through a dictionary by using a for loop:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)
  
  
# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
mydict = thisdict.copy()
print(mydict)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)