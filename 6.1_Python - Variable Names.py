# Variable Names : A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables: 

    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.

# Example - Legal variable names:

myvar = "John"
print("myvar =",myvar)
my_var = "John"
print("my_var =",my_var)
_my_var = "John"
print("_my_var =",_my_var)
myVar = "John"
print("myVar =",myVar)
MYVAR = "John"
print("MYVAR =",MYVAR)
myvar2 = "John"
print("myvar2 =",myvar2)

# Example - Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"

print("Remember that variable names are case-sensitive")

print("----------------------------------------------------------------------------")

print("Variable names with more than one word can be difficult to read.")
print("There are several techniques you can use to make them more readable:")

print("----------------------------------------------------------------------------")
print("Camel Case")
print("Each word, except the first, starts with a capital letter:") 

myVariableName = "John"
print("myVariableName = ", myVariableName)

print("----------------------------------------------------------------------------")
print("Pascal Case")
print("Each word starts with a capital letter:") 

MyVariableName = "John"
print("MyVariableName = ", MyVariableName)

print("----------------------------------------------------------------------------")
print("Snake Case")
print("Each word is separated by an underscore character:") 

my_variable_name = "John"
print("my_variable_name = ", my_variable_name)






