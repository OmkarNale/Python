print("---------------------------------Many Values to Multiple Variables--------------------------------------------------")
print("Python allows you to assign values to multiple variables in one line:")

x, y,z = "omkar", "Raj", "Rajan"
print("x =",x)
print("y =",y)
print("z =",z)

print("-------------------------------------------------------------------------------------------------------------------")
print("Note: Make sure the number of variables matches the number of values, or else you will get an error.")
# x, y, z = "Orange"
# print("x =",x)         #error - x, y, z = "Orange" ValueError: too many values to unpack
# print("y =",y)
# print("z =",z)
print("--------------------------------------------------------------------------------------------------------------------")

print("-----------------------------------One Value to Multiple Variables--------------------------------------------------")
print("And you can assign the same value to multiple variables in one line:")

x = y = z = "Orange"
print("x =",x)
print("y =",y)
print("z =",z)

print("--------------------------------------------------------------------------------------------------------------------")

print("-----------------------------------Unpack a Collection--------------------------------------------------")
print("If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.")

name = ["omkar","aniket","Rajan"]
print("name =", name)
x, y, z = name
print("x =",x)
print("y =",y)
print("z =",z)

