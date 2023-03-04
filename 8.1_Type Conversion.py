print("------------------------------------------------Type Conversion--------------------------------------------")
print("You can convert from one type to another with the int(), float(), and complex() methods:")

# example
# Convert from one type to another:

print("--------------------------------------------------")
x = 5
y = 5.32
z = 5j
print("x =",x)
print("y =",y)
print("z =",z)
print("--------------------------------------------------")

print("convert from int to float:");
a = float(x)
print("a =",a)
print("type of a =",type(a))

print("--------------------------------------------------")

print("convert from float to int:");
b = int(x)
print("b =",b)
print("type of b =",type(b))

print("--------------------------------------------------")
print("convert from int to complex:");
c = complex(x)
print("c =",c)
print("type of c =",type(c))

print("--------------------------------------------------")
print("convert from float to complex:");
d = complex(y)
print("d =",d)
print("type of d =",type(d))

print("--------------------e = int(z) : TypeError: can't convert complex to int------------------------------")
# print("convert from complex to int:");
# e = int(z)
# print("e =",e)
# print("type of e ="type(e))

print("--------------------e = int(z) : TypeError: can't convert complex to float------------------------------")
# print("convert from complex to int:");
# f = int(z)
# print("f =",f)
# print("type of f =",type(f))
print("--------------------------------------------------")


print("Note: You cannot convert complex numbers into another number type.")