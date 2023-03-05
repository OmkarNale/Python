print("-----------------------------------------Slicing---------------------------------------")

print("You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.")

# Example
# Get the characters from position 2 to position 5 (not included):

x = "Hello World"

print("x = ",x)
print("Get the characters from position 2 to position 7 (not included):",x[2:7])

print("----------------------------------------------------------------------------------------")
print("Note: The first character has index 0.")
print("----------------------------------------------------------------------------------------")

print("------------------------------------------------------Slice From the Start-------------------------------------------------")

print("Get the characters from the start to position 5 (not included):")

#Exaple
#Get the characters from the start to position 5 (not included):

y = "Hello World!"
print("y =",y)
print("Get the characters from the start to position 7 (not included):",y[:7])

print("---------------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------Slice From the end-------------------------------------------------")

print("By leaving out the end index, the range will go to the end:")

#Exaple
#By leaving out the end index, the range will go to the end:

z = "Hello World!"
print("z =",z)
print("Get the characters from the start to position 7 (not included):",z[2:])

print("---------------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------------Negative Indexing----------------------------------------------------")

print("Use negative indexes to start the slice from the end of the string:")

#Exaple
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

p = "Hello World!"
print("p =",p)
print("Get the characters: From: o in World! (position -5) To, but not included: d in World! (position -2)::",p[-5:-2])

print("---------------------------------------------------------------------------------------------------------------------------")