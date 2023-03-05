print("---------------------------------------------Python - Booleans--------------------------------------------------------")

print("Booleans represent one of two values: True or False.")

print("----------------------------------------------------------------------------------------------------------------------")

print("Boolean Values")

print("In programming you often need to know if an expression is True or False.")
print("You can evaluate any expression in Python, and get one of two answers, True or False.")
print("When you compare two values, the expression is evaluated and Python returns the Boolean answer:")

# Example
print("10 > 9 :",10 > 9)
print("10 == 9 :",10 == 9)
print("10 < 9 :",10 < 9)

print("----------------------------------------------------------------------------------------------------------------------")

print("When you run a condition in an if statement, Python returns True or False:")

# Example
# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print(b," is greater than ",a)
else:
  print(b," is not greater than ",a)
print("----------------------------------------------------------------------------------------------------------------------")

print("Evaluate Values and Variables")
print("The bool() function allows you to evaluate any value, and give you True or False in return,")

#Example
#Evaluate a string and a number:

print("bool(\'hello\') = ",bool('hello'))
print("bool(123) = ",bool(123))
print("bool(1) = ",bool(1))
print("bool(0) = ",bool(0))

# Evaluate two variables:
x = 12
y = "jokm"
print("x =",x)
print("y =",y)
print("bool(x) =",bool(x))
print("bool(y) =",bool(y))
print("----------------------------------------------------------------------------------------------------------------------")

print("Most Values are True")

print("Almost any value is evaluated to True if it has some sort of content.")

print("Any string is True, except empty strings.")
print("Any number is True, except 0.")
print("Any list, tuple, set, and dictionary are True, except empty ones.")

# Example
# The following will return True:

print("bool(\"abc\") =",bool("abc"))
print("bool(123) =",bool(123))
print("bool([\"apple\", \"cherry\", \"banana\"]) =",bool(["apple", "cherry", "banana"]))
print("----------------------------------------------------------------------------------------------------------------------")

print("Some Values are False")
print("In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.")

#Example
#The following will return False:

print("bool(False) =",bool(False))
print("bool(None) =",bool(None))
print("bool(0)",bool(0))
print("bool("")",bool(""))
print("bool(())",bool(()))
print("bool([])",bool([]))
print("bool({})",bool({}))

print("----------------------------------------------------------------------------------------------------------------------")

print("One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:")

#Example

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print("bool(myobj) =",bool(myobj))

print("----------------------------------------------------------------------------------------------------------------------")

print("Functions can Return a Boolean")
print("You can create functions that returns a Boolean Value:")

#Example 
#Print the answer of a function:

def myFunction() :
  return True

print("myFunction returns the = ",myFunction())

print("You can execute code based on the Boolean answer of a function:")

#Example
#Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


print("Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:")

# Example
# Check if an object is an integer or not:

x = 200
print("isinstance(x, int) =",isinstance(x, int))

print("----------------------------------------------------------------------------------------------------------------------")















