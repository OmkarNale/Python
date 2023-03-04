print("----------------------------------------------------The global Keyword--------------------------------------------------")

print("Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.")
print("To create a global variable inside a function, you can use the global keyword.")

# Example
# If you use the global keyword, the variable belongs to the global scope:


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print("---------------------------------------------------------------------------------------------------------------------")

print("Also, use the global keyword if you want to change a global variable inside a function.")

# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "fantastic"

def isFnction():
    global x
    x = "Awesome"
isFnction()
print("Python is ",x)