print("---------------------------------------------------Loop Through a List-----------------------------------------------------")

print("You can loop through the list items by using a for loop:")

#Example 
#Print all items in the list, one by one:

x = ["orange","banana","mango","kiwi","apple"]
for i in x:
    print(i)

print("Learn more about for loops in our Python For Loops Chapter.")
print("-----------------------------------------------Loop Through the Index Numbers----------------------------------------------")

print("You can also loop through the list items by referring to their index number.")
print("Use the range() and len() functions to create a suitable iterable.")

#Example
#Print all items by referring to their index number:

x = ["orange","banana","mango","kiwi","apple"]
for i in range(len(x)):
    print(i)

print("The iterable created in the example above is [0, 1, 2].")

print("-------------------------------------------------Using a While Loop--------------------------------------------------------")

print("You can loop through the list items by using a while loop.")

print("Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.")

print("Remember to increase the index by 1 after each iteration.")

#Example
#Print all items, using a while loop to go through all the index numbers

x = ["orange","banana","mango","kiwi","apple"]
i = 0
print("x =",x)
while i < len(x):
    print("i =",i,":",x[i])
    i = i+1

print("Learn more about while loops in our Python While Loops Chapter.")

print("---------------------------------------------Looping Using List Comprehension----------------------------------------------")

print("List Comprehension offers the shortest syntax for looping through lists:")

#Example
#A short hand for loop that will print all items in a list:

x = ["orange","banana","mango","kiwi","apple"]
[print(i) for i in x]

print("Learn more about list comprehension in the next chapter: List Comprehension.")

print("---------------------------------------------------------------------------------------------------------------------------")













