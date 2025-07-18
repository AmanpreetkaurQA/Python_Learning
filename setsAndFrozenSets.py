# A frozenset is:
# An immutable version of a set
# Cannot be changed once created
# Can be used as keys in dictionaries or added to sets (unlike normal sets)


# A set is: A set is a collection which is unordered, unchangeable*, and unindexed.
# A collection of unordered, unique elements
# Mutable (you can add/remove elements)
# Cannot contain duplicate items
# Defined using curly braces {} or the set() constructor
# Set Methods
    # add()	 	            Adds an element to the set
    # clear()	 	            Removes all the elements from the set
    # copy()	 	            Returns a copy of the set
    # difference()	        -	Returns a set containing the difference between two or more sets
    # difference_update()	    -=	Removes the items in this set that are also included in another, specified set
    # discard()	 	        Remove the specified item
    # intersection()	        &	Returns a set, that is the intersection of two other sets
    # intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
    # isdisjoint()	 	    Returns whether two sets have a intersection or not
    # issubset()	            <=	Returns whether another set contains this set or not
 	#                         <	Returns whether all items in this set is present in other, specified set(s)
    # issuperset()	        >=	Returns whether this set contains another set or not
 	#                         >	Returns whether all items in other, specified set(s) is present in this set
    # pop()	 	            Removes an element from the set
    # remove()	 	        Removes the specified element
    # symmetric_difference()	^	Returns a set with the symmetric differences of two sets
    # symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
    # union()	|	Return a set containing the union of sets
    # update()	|=	Update the set with the union of this set and others

# Creating a Set
# Using {}:
# Using set() constructor:
my_set = {1, 2, 3, 4}
print(my_set)  

# Duplicates automatically removed
s = set([1, 2, 2, 3])  
print(s)       

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in my_set:
  print(x)
  
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
my_set.add(10)
print(my_set)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# The remove() method raises an error if the specified item does not exist, and the discard() method does not raise an error.
# Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
# The clear() method empties the set:
# The del keyword will delete the set completely:

my_set.remove(2)
print(my_set)

my_set.discard(10)
print(my_set)

my_set.pop()
print(my_set)


# Loop Items
colors = {"red", "green", "blue"}
for color in colors:
    print(color)

# Join Sets
# The union() method returns a new set with all items from both sets.
# You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)

# frozenSet 
fs = frozenset([1, 2, 3, 2])
print(fs) 

fs2 = frozenset([3, 4])
print(fs.union(fs2))               # frozenset({1, 2, 3, 4})
print(fs.intersection(fs2))        # frozenset({3})
