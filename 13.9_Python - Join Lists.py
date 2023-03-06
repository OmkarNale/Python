print("------------------------------------------------Python - Join Lists--------------------------------------------------------")

print("-----------------------------------------------Join Two Lists--------------------------------------------------------------")

print("There are several ways to join, or concatenate, two or more lists in Python.")
print("One of the easiest ways are by using the + operator.")

#Example
#Join two list using + operator:

list1 = ["orange","mango","kiwi","apple"]
list2 = ["xyz", "pqr","xyz"]

final_list = list1 + list2
print("final_list = ", final_list)

print("--------------------------------------------")

print("Another way to join two lists is by appending all the items from list2 into list1, one by one:")

for x in list2:
    list1.append(x)

print("lsit1 =",list1)

print("----------------------------------------------")

print("Or you can use the extend() method, which purpose is to add elements from one list to another list:")

# Example
# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print("Use the extend() method to add list2 at the end of list1 :",list1)

print("---------------------------------------------------------------------------------------------------------------------------")




























