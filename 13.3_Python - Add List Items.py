print("------------------------------------------------Append Items---------------------------------------------------------------")

print("To add an item to the end of the list, use the append() method:")

#Example
#Using the append() method to append an item:

x = ["orange","apple","mango"]
print("x =",x)
x.append("KiWi")
print("after append of kiwi =",x)

print("---------------------------------------------------------------------------------------------------------------------------")
print("Insert Items")
print("To insert a list item at a specified index, use the insert() method.")
print("The insert() method inserts an item at the specified index:")

#Exxample
#Insert an item as the second position:

x = ["orange","Mango","banana"]
print("x =",x)
x.insert(1,"kiwi")
print("x after inserting kiwi at 1 index =",x)
print("---------------------------------------------------------------------------------------------------------------------------")

print("Extend List")
print("To append elements from another list to the current list, use the extend() method.")

#Example
#Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("thislist after extending =",thislist)

print("-----------------------------------------------------")
print("The elements will be added to the end of the list.")
print("---------------------------------------------------------------------------------------------------------------------------")

print("Add Any Iterable")
print("The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).")

#Example
#Add elements of a tuple to a list:

thislist =["apple", "banana", "cherry"]
thistuple = ("mango", "pineapple", "papaya")
thislist.extend(thistuple)
print("#Add elements of a tuple to a list:",thislist)

#Example
#Add elements of a set to a list:

thislist =["apple", "banana", "cherry"]
thisset = {"mango", "pineapple", "papaya"}
thislist.extend(thisset)
print("#Add elements of a set to a list:",thislist)

#Example
#Add elements of a dict to a list:

thislist =["apple", "banana", "cherry"]
thisdict = {"namr":"omkar", "id":123, "Age":23}
thislist.extend(thisdict)
print("#Add elements of a dict to a list:",thislist)

print("---------------------------------------------------------------------------------------------------------------------------")





