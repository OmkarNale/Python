print("---------------------------------------------------Python Lists------------------------------------------------------------")

print("mylist = [\"apple\", \"banana\", \"cherry\"]")

print("---------------------------------------------------------------------------------------------------------------------------")

print("List :")

print("Lists are used to store multiple items in a single variable.")

print("Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.")

print("Lists are created using square brackets:")

# Example
# Create a List:

Name_list = ["omkar","arun", "nale"]
print("Name_list =",Name_list)

print("---------------------------------------------------------------------------------------------------------------------------")

print("List Items :")

print("List items are ordered, changeable, and allow duplicate values.")
print("List items are indexed, the first item has index [0], the second item has index [1] etc.")
print("---------------------------------------------------------------------------------------------------------------------------")

print("Ordered :")
print("When we say that lists are ordered, it means that the items have a defined order, and that order will not change.")
print("If you add new items to a list, the new items will be placed at the end of the list.")

print("---------------------------------------------------------------------------------------------------------------------------")
print(":Note: There are some list methods that will change the order, but in general: the order of the items will not change.")
print("---------------------------------------------------------------------------------------------------------------------------")

print("Changeable :")
print("The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.")

print("---------------------------------------------------------------------------------------------------------------------------")

print("Allow Duplicates :")
print("Since lists are indexed, lists can have items with the same value:")

#Example
# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print("---------------------------------------------------------------------------------------------------------------------------")

print("List Length")
print("To determine how many items a list has, use the len() function:")

#Example
#Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print("lenght of thislist =",len(thislist))

print("---------------------------------------------------------------------------------------------------------------------------")


print("List Items - Data Types")
print("List items can be of any data type:")

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1,list2,list3)
print("---------------------------------------------------------------------------------------------------------------------------")

print("A list can contain different data types:")

#Example
#A list with strings, integers and boolean values:

List11 = ["apple", "banana", "cherry",1, 5, 7, 9, 3,True, False, False]

print("List11 =",List11)

print("---------------------------------------------------------------------------------------------------------------------------")

print("type()")
print("From Python's perspective, lists are defined as objects with the data type 'list':")

print("<class 'list'>")

print("What is the data type of a list?")
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print("---------------------------------------------------------------------------------------------------------------------------")

print("The list() Constructor")
print("It is also possible to use the list() constructor when creating a new list.")

#Example
#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print("thislist =",thislist)
print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")

print("Python Collections (Arrays)")
print("There are four collection data types in the Python programming language:")
print("1. List is a collection which is ordered and changeable. Allows duplicate members.")
print("2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.")
print("3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.")
print("4. Dictionary is a collection which is ordered** and changeable. No duplicate members.")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("Note : *Set items are unchangeable, but you can remove and/or add items whenever you like.")
print("Note : **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")

print("When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.")












