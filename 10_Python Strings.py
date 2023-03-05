print("---------------------------------------------------Strings-----------------------------------------------------")

print("Strings in python are surrounded by either single quotation marks, or double quotation marks.")

print("single qutes hello is the same as dubble qutes hello.")

print("You can display a string literal with the print() function:")

print("--------------------------------------------------------------------------------------------------------------")
# Example

x = 'hello'
y = "hello"

print("x =",x)
print("y =",y)
print("--------------------------------------------------------------------------------------------------------------")

print("-------------------------------------------Assign String to a Variable----------------------------------------")
print("Assigning a string to a variable is done with the variable name followed by an equal sign and the string:")

x = "Hi i'm Omkar Nale !"
print("x =",x)
print("--------------------------------------------------------------------------------------------------------------")



print("-------------------------------------------Multiline Strings-------------------------------------------------")
print("You can assign a multiline string to a variable by using three quotes:")

print("Three single quotes:")
x = '''
Hi im omkar nale !
working at expleo india as software developer !
'''
print("x =",x)

print("Or You can use three double quotes:")

z = """
Hi im omkar nale !
working at expleo india as software developer !
"""
print("z =",z)


print("--------------------------------------------------------------------------------------------------------------")

print("Note: in the result, the line breaks are inserted at the same position as in the code.")

print("--------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------Strings are Arrays--------------------------------------")

print("Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.")
print("However, Python does not have a character data type, a single character is simply a string with a length of 1.")
print("Square brackets can be used to access elements of the string.")

print("Get the character at position 1 (remember that the first character has the position 0):")
a = "Hello, World!"
print("a = ",a)
print("a[1] =",a[1])

print("--------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------Looping Through a String------------------------------------------")

print("Since strings are arrays, we can loop through the characters in a string, with a for loop.")

#Loop through the letters in the word "Hello World !":

a = "Hello, World!"
for x in a:
    print("x =",x)

print("--------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------String Length------------------------------------------")

print("To get the length of a string, use the len() function.")

#The len() function returns the length of a string:

a = "Hello, World!"
print("Print length of a string = ", len(a))

print("--------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------Check in String------------------------------------------")

print("To check if a certain phrase or character is present in a string, we can use the keyword in.")

#Check if "free" is present in the following text:
print("------------------------------use in keyword--------------------------------------")

txt = "The best things in life are free!"
print("free" in txt)

print("-------------------Use it in an if statement:------------------------")

txt = "The best things in life are free!"
if("free" in txt):
    print("Yes, free is present in text string !")


print("--------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------Check Not in String------------------------------------------")

print("To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.")

#Check if "zzz" is NOT present in the following text:
print("------------------------------use  Not in keyword--------------------------------------")

txt = "The best things in life are free!"
print("free" not in txt)

print("-------------------Use it in an if statement:------------------------")

txt = "The best things in life are free!"
if("zzz" not in txt):
    print("No, zzz is not present in text string !")


print("--------------------------------------------------------------------------------------------------------------")
