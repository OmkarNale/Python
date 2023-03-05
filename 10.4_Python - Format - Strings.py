print("-----------------------------------------------String Format-------------------------------------------------------")
print("As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:")

x = 36
y = "Hi this String "

# z = x + y
# print("z =",z) #z = x + y : TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("------------------------------------------------------------------------------------------------------------------")

print("But we can combine strings and numbers by using the format() method!")
print("The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:")

# ExampleGet
#Use the format() method to insert numbers into strings:

x = 36
y = "My age is {}"
print(y.format(x))

print("------------------------------------------------------------------------------------------------------------------")

print("The format() method takes unlimited number of arguments, and are placed into the respective placeholders:")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${} dollars."
print(myorder.format(quantity, itemno, price))

print("------------------------------------------------------------------------------------------------------------------")
print("You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print("------------------------------------------------------------------------------------------------------------------")
