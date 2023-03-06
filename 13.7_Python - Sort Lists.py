print("----------------------------------------------------Python - Sort Lists----------------------------------------------------")

print("Sort List Alphanumerically :")
print("List objects have a sort() method that will sort the list alphanumerically, ascending, by default:")

#Example
# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("list after alphanumerically sorted in ascending order: ",thislist)

#Example
#Sort the list numerically:

numlist = [10,20,4,788,333,6,994,2000]
numlist.sort()
print("Sort the list numerically:",numlist)

print("-----------------------------------------------Sort Descending-------------------------------------------------------------")

print("To sort descending, use the keyword argument reverse = True:")

#Example
# Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print("Sort the list descending: ",thislist)

#Example
#Sort the list descending:

numlist = [10,20,4,788,333,6,994,2000]
numlist.sort(reverse = True)
print("Sort the list numerically descending order:",numlist)


print("--------------------------------------------Customize Sort Function--------------------------------------------------------")

print("You can also customize your own function by using the keyword argument key = function.")

print("The function will return a number that will be used to sort the list (the lowest number first):")

#Example
# Sort the list based on how close the number is to 50:

def myfunc(n):
    print(abs(n - 50))
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print("Sort the list based on how close the number is to 50 :",thislist)

print("-----------------------------------------------------Case Insensitive Sort-------------------------------------------------")

print("By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:")

#Example
#Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("Case sensitive sorting can give an unexpected result:",thislist)

print("Luckily we can use built-in functions as key functions when sorting a list.")
print("So if you want a case-insensitive sort function, use str.lower as a key function:")

#Example
#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print("Perform a case-insensitive sort of the list:",thislist)


print("--------------------------------------------------------Reverse Order------------------------------------------------------")

print("What if you want to reverse the order of a list, regardless of the alphabet?")
print("The reverse() method reverses the current sorting order of the elements.")

# Example
# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print("Reverse the order of the list items:",thislist)

print("---------------------------------------------------------------------------------------------------------------------------")































