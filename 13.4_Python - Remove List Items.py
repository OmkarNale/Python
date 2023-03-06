print("--------------------------------------------------Remove Specified Item----------------------------------------------------")

print("The remove() method removes the specified item.")

#example
#Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print("Remove banana from given lsit :",thislist)

print("---------------------------------------------------Remove Specified Index--------------------------------------------------")
print("The pop() method removes the specified index.")

#Example
#Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print("remove the item at index 1 :",thislist)

print("If you do not specify the index, the pop() method removes the last item.")

#Example
#Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print("If you do not specify the index, the pop() method removes the last item :",thislist)


print("The del keyword also removes the specified index:")

#Example
#Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print("The del keyword also removes the specified index: ",thislist)


print("The del keyword can also delete the list completely.")

#Example
#Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist
#print("after deleting complete list :",thislist) #print("after deleting complete list :",thislist) NameError: name 'thislist' is not defined

print("-------------------------------------------------Clear the List-----------------------------------------------------------")
print("The clear() method empties the list.")
print("The list still remains, but it has no content.")

#Example
#Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("The list still remains, but it has no content :",thislist)