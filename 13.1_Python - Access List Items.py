print("---------------------------------------------------Access Items------------------------------------------------------------")

print("List items are indexed and you can access them by referring to the index number:")

#Example
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print("thislist[1] =",thislist[1])

print("--------------------------------------------------------------------------------------------------------------------------")
print("Note:Note: The first item has index 0.")
print("--------------------------------------------------------------------------------------------------------------------------")

print("Negative Indexing")
print("Negative indexing means start from the end")
print("-1 refers to the last item, -2 refers to the second last item etc.")
#Example
#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print("thislist[-1] =",thislist[-1])
print("thislist[-2] =",thislist[-2])
print("--------------------------------------------------------------------------------------------------------------------------")

print("Range of Indexes")

print("You can specify a range of indexes by specifying where to start and where to end the range.")
print("When specifying a range, the return value will be a new list with the specified items.")

#example
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("print item in between 2 to 5 not include =",thislist[2:5])

print("--------------------------------------------------------------------------------------------------------------------------")
print("Note: The search will start at index 2 (included) and end at index 5 (not included).")
print("Note: Remember that the first item has index 0.")
print("--------------------------------------------------------------------------------------------------------------------------")
print("By leaving out the start value, the range will start at the first item:")

#example
# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("returns the items from the beginning to, but NOT including, \"kiwi\" ",thislist[:4])

print("--------------------------------------------------------------------------------------------------------------------------")
print("By leaving out the end value, the range will go on to the end of the list:")

#Example
# This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("returns the items from \"cherry\" to the end =",thislist[2:])
print("--------------------------------------------------------------------------------------------------------------------------")

print("Range of Negative Indexes")
print("Specify negative indexes if you want to start the search from the end of the list:")

#Example
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("returns the items from \"orange\" (-4) to, but NOT including \"mango\" (-1) =",thislist[-4:-1])
print("--------------------------------------------------------------------------------------------------------------------------")

print("Check if Item Exists")
print("To determine if a specified item is present in a list use the in keyword:")

#Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print("--------------------------------------------------------------------------------------------------------------------------")
