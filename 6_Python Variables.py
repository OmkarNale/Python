# Variables - Variables are containers for storing data values.

print("Creating Variables - Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.")
x = 5
y = "John"
print("x =",x)
print("y =",y)
print("-------------------------------------------------------------------------------")

print(" Variables do not need to be declared with any particular type, and can even change type after they have been set.")
x = 4  # x is of type int
print("x =",x)     
x = "Sally" # x is now of type str
print("x = ",x)
print("-------------------------------------------------------------------------------")

print("Casting - If you want to specify the data type of a variable, this can be done with casting.")
x = 3
x = str(3)    # x will be '3'
print("Casting to string",3)
y = int(3)    # y will be 3
print("Casting to int",3)
z = float(3)  # z will be 3.0
print("Casting to float",3)
print("-------------------------------------------------------------------------------")

print("Get the Type - You can get the data type of a variable with the type() function.")

x = 5
y = "john"

print("Type of x =",type(x))
print("Type of x =",type(y))
print("-------------------------------------------------------------------------------")


print("Single or Double Quotes? - String variables can be declared either by using single or double quotes:")

x = "John"
print("x =",x)
# is the same as
x = 'John'
print("x =",x)
print("-------------------------------------------------------------------------------")


print(" Case-Sensitive - Variable names are case-sensitive.")

a = 4
A = 978
#A will not overwrite a
print("a =",a)
print("A =",A)
if(a == A):
    print("same")
else:
    print("Not Same")
print("-------------------------------------------------------------------------------")





