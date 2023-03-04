print("-----------------------------------------Global Variables-----------------------------------------------------")

print("Variables that are created outside of a function (as in all of the examples above) are known as global variables. Global variables can be used by everyone, both inside of functions and outside.")

# Example

print("Create a variable outside of a function, and use it inside the function")

x = "Hi Im golabe variable X"

def myFuction():
    print("Hello x =", x)

myFuction()

print("--------------------------------------------------------------------------------------------------------------")

print("----------------------------------------Global Variables------------------------------------------------------")
print("If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.")
print("--------------------------------------------------------------------------------------------------------------")

x = "Hi Im outside of myFuction golabe variable !"

def myFuction():
    y = "hello im inside th myFuction local variable !"
    print("Hello x =", x)
    print("Hello y =", y)

myFuction()

print("--------------------------------------------------------------------------------------------------------------")


