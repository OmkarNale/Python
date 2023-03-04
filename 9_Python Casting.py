print("---------------------------------------------Specify a Variable Type--------------------------------------------")

print("There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.")
print("----------------------------------------------------------------------------------------------------------------")
print("Casting in python is therefore done using constructor functions:")
print("----------------------------------------------------------------------------------------------------------------")
print("int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string lite(providing the string represents a whole number)")
print("----------------------------------------------------------------------------------------------------------------")
print("float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)")
print("----------------------------------------------------------------------------------------------------------------")
print("str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals")
print("----------------------------------------------------------------------------------------------------------------")

x = 5

y = 20.34

z = "4"

print("Convert into Integers:")

a = int(x)
print("x =",x)
print("a type is",type(a))

b = int(y)
print("y =",y)
print("b type is",type(b))

c = int(z)
print("z =",z)
print("c type is ", type(z))

print("--------------------------------------------")
print("Convert into float:")

e = float(x)
print("x =",x)
print("e type is",type(e))

f = float(y)
print("y =",y)
print("f type is",type(f))

g = float(z)
print("z =",z)
print("g type is ", type(g))

print("--------------------------------------------")
print("Convert into string:")

p = str(x)
print("x =",x)
print("p type is",type(p))

q = str(y)
print("y =",y)
print("q type is",type(q))

r = str(z)
print("z =",z)
print("r type is ", type(r))