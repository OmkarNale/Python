print("---------------------------------------Python has a set of built-in methods that you can use on strings.--------------------------")

print("-------------------------------------------------------Upper Case-----------------------------------------------------------------")

print("The upper() method returns the string in upper case:")

a = "Hello World!"
print("a in upper case = ",a.upper())

print("----------------------------------------------------------------------------------------------------------------------------------")

print("-------------------------------------------------------Lower Case-----------------------------------------------------------------")

print("The lower() method returns the string in lower case:")

a = "Hello World!"
print("a in upper case = ",a.lower())

print("----------------------------------------------------------------------------------------------------------------------------------")

print("--------------------------------------------------Remove Whitespace---------------------------------------------------------------")

print("Whitespace is the space before and/or after the actual text, and very often you want to remove this space.")
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

a = "Hello World!                  "
print("a in remove Whitespace = ",a.strip())

print("----------------------------------------------------------------------------------------------------------------------------------")

print("--------------------------------------------------Replace String---------------------------------------------------------------")

print("The replace() method replaces a string with another string:")

a = "Hello World!"
print("Replcae h with j = ",a.replace('H','J'))

print("----------------------------------------------------------------------------------------------------------------------------------")



print("--------------------------------------------------Split String--------------------------------------------------------------------")

print("The split() method returns a list where the text between the specified separator becomes the list items.")

#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello World!"
print("Split string = ",a.split())

print("----------------------------------------------------------------------------------------------------------------------------------")

