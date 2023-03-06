print("---------------------------------------------------Change Item Value-------------------------------------------------------")

print("To change the value of a specific item, refer to the index number:")

#Example
#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print("Print thislist = ",thislist)
print("Print thislist[2] =",thislist[2])

print("---------------------------------------------------------------------------------------------------------------------------")

print("Change a Range of Item Values")
print("To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:")

#Example
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print("thislit =",thislist)
print("thislist[2:4] =",thislist[2:4])

print("If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:")

#Example
#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print("thislist =",thislist)
print("thislist[1:2]=",thislist[1:2])

print("---------------------------------------------------------------------------------------------------------------------------")
print("Note: The length of the list will change when the number of items inserted does not match the number of items replaced.")
print("---------------------------------------------------------------------------------------------------------------------------")

print("If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:")
#Example
#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print("thislist =",thislist)
print("thislist[1:3] =",thislist[1:3])
print("---------------------------------------------------------------------------------------------------------------------------")

print("Insert Items")

print("To insert a new list item, without replacing any of the existing values, we can use the insert() method.")
print("The insert() method inserts an item at the specified index:")

#Example
#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print("thislit =",thislist)

print("---------------------------------------------------------------------------------------------------------------------------")
print("Note: As a result of the example above, the list will now contain 4 items.")print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
