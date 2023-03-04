print("---------------------------------------------------Output Variables-----------------------------------------------")
print("The Python print() function is often used to output variables.")

x = "Python is awesome"
print("x =",x)

print("------------------------------------------------------------------------------------------------------------------")

print("In the print() function, you output multiple variables, separated by a comma:")
# Example
x,y,z = "omkar", "aniket", "rajan"
print(x,y,z)
print("---------------------------")
# Example
x = "omkar"
y = "aniket"
z = "rajan"
print(x,y,z)
print("---------------------------")
# Example - concanat
x = "omkar "
y = "aniket "
z = "rajan "
print(x + y + z)

print("------------------------------------------------------------------------------------------------------------------")
print("Notice the space character after  Omkar and Aniket , without them the result would be omkaraniketrajan.")
print("if wwe used + with string then it will concanat strings or if it is number then it will Add those nmber")
print("------------------------------------------------------------------------------------------------------------------")

print("For numbers, the + character works as a mathematical operator:")
x = 6
y = 4

print("x + y =", x+y)
print("------------------------------------------------------------------------------------------------------------------")
print("In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:")
print("------------------------------------------------------------------------------------------------------------------")

x = 5
y = "John"
# print(x + y) #  print(x + y) : TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:")

x = 5
y = "John"
print(x , y)

print("------------------------------------------------------------------------------------------------------------------")

