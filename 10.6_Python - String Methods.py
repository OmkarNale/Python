print("-------------------------------------String Methods-------------------------------------")
print("Python has a set of built-in methods that you can use on strings.")

print("Note: All string methods return new values. They do not change the original string.")
print("-----------------------------------------------------------------------------------------")
print("Method	Description")
print("-----------------------------------------------------------------------------------------")
print("capitalize()	Converts the first character to upper case")
print("-----------------------------------------------------------------------------------------")
print("casefold()	Converts string into lower case")
print("-----------------------------------------------------------------------------------------")
print("center()	Returns a centered string")
print("-----------------------------------------------------------------------------------------")
print("count()	Returns the number of times a specified value occurs in a string")
print("-----------------------------------------------------------------------------------------")
print("encode()	Returns an encoded version of the string")
print("-----------------------------------------------------------------------------------------")
print("endswith()	Returns true if the string ends with the specified value")
print("-----------------------------------------------------------------------------------------")
print("expandtabs()	Sets the tab size of the string")
print("-----------------------------------------------------------------------------------------")
print("find()	Searches the string for a specified value and returns the position of where it was found")
print("-----------------------------------------------------------------------------------------")
print("format()	Formats specified values in a string")
print("-----------------------------------------------------------------------------------------")
print("format_map()	Formats specified values in a string")
print("-----------------------------------------------------------------------------------------")
print("index()	Searches the string for a specified value and returns the position of where it was found")
print("-----------------------------------------------------------------------------------------")
print("isalnum()	Returns True if all characters in the string are alphanumeric")
print("-----------------------------------------------------------------------------------------")
print("isalpha()	Returns True if all characters in the string are in the alphabet")
print("-----------------------------------------------------------------------------------------")
print("isdecimal()	Returns True if all characters in the string are decimals")
print("-----------------------------------------------------------------------------------------")
print("isdigit()	Returns True if all characters in the string are digits")
print("-----------------------------------------------------------------------------------------")
print("isidentifier()	Returns True if the string is an identifier")
print("-----------------------------------------------------------------------------------------")
print("islower()	Returns True if all characters in the string are lower case")
print("-----------------------------------------------------------------------------------------")
print("isnumeric()	Returns True if all characters in the string are numeric")
print("-----------------------------------------------------------------------------------------")
print("isprintable()	Returns True if all characters in the string are printable")
print("-----------------------------------------------------------------------------------------")
print("isspace()	Returns True if all characters in the string are whitespaces")
print("-----------------------------------------------------------------------------------------")
print("istitle()	Returns True if the string follows the rules of a title")
print("-----------------------------------------------------------------------------------------")
print("isupper()	Returns True if all characters in the string are upper case")
print("-----------------------------------------------------------------------------------------")
print("join()	Joins the elements of an iterable to the end of the string")
print("-----------------------------------------------------------------------------------------")
print("ljust()	Returns a left justified version of the string")
print("-----------------------------------------------------------------------------------------")
print("lower()	Converts a string into lower case")
print("-----------------------------------------------------------------------------------------")
print("lstrip()	Returns a left trim version of the string")
print("-----------------------------------------------------------------------------------------")
print("maketrans()	Returns a translation table to be used in translations")
print("-----------------------------------------------------------------------------------------")
print("partition()	Returns a tuple where the string is parted into three parts")
print("-----------------------------------------------------------------------------------------")
print("replace()	Returns a string where a specified value is replaced with a specified value")
print("-----------------------------------------------------------------------------------------")
print("rfind()	Searches the string for a specified value and returns the last position of where it was found")
print("-----------------------------------------------------------------------------------------")
print("rindex()	Searches the string for a specified value and returns the last position of where it was found")
print("-----------------------------------------------------------------------------------------")
print("rjust()	Returns a right justified version of the string")
print("-----------------------------------------------------------------------------------------")
print("rpartition()	Returns a tuple where the string is parted into three parts")
print("-----------------------------------------------------------------------------------------")
print("rsplit()	Splits the string at the specified separator, and returns a list")
print("-----------------------------------------------------------------------------------------")
print("rstrip()	Returns a right trim version of the string")
print("-----------------------------------------------------------------------------------------")
print("split()	Splits the string at the specified separator, and returns a list")
print("-----------------------------------------------------------------------------------------")
print("splitlines()	Splits the string at line breaks and returns a list")
print("-----------------------------------------------------------------------------------------")
print("startswith()	Returns true if the string starts with the specified value")
print("-----------------------------------------------------------------------------------------")
print("strip()	Returns a trimmed version of the string")
print("-----------------------------------------------------------------------------------------")
print("swapcase()	Swaps cases, lower case becomes upper case and vice versa")
print("-----------------------------------------------------------------------------------------")
print("title()	Converts the first character of each word to upper case")
print("-----------------------------------------------------------------------------------------")
print("translate()	Returns a translated string")
print("-----------------------------------------------------------------------------------------")
print("upper()	Converts a string into upper case")
print("-----------------------------------------------------------------------------------------")
print("zfill()	Fills the string with a specified number of 0 values at the beginning")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------capitalize() : Converts the first character to upper case----==-------------------------------")
print("The capitalize() method returns a string where the first character is upper case, and the rest is lower case.")
print("No parameters required !")
#Example
#Upper case the first letter in this sentence:

x = "hello world!"
print("x =",x)
print("x with capitalize() =",x.capitalize())
("-------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------casefold()	Converts string into lower case--------------------------------------------------")
print("The casefold() method returns a string where all the characters are lower case.")
print("This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.")
print("No parameters required !")

#Example
#Make the string lower case:

x = "HELLO WORLD!"
print("x =",x)
print("x with capitalize() =",x.casefold())
("-------------------------------------------------------------------------------------------------------------------------------")

print("----------------------------------------center()	Returns a centered string----------------------------------------------")
print("The center() method will center align the string, using a specified character (space is default) as the fill character.")
print("parameters required !")
print("length :	Required. The length of the returned string")
print("character:Optional. The character to fill the missing space on each side. Default is " " (space)")
#Example
#Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

x = "HELLO  WORLD!"
print("x =",x)
print("x with center() =",x.center(20,'x'))
print("x with center() =",x.center(20,))
("-------------------------------------------------------------------------------------------------------------------------------")

print("---------------------------count()	Returns the number of times a specified value occurs in a string----------------------")
print("The count() method returns the number of times a specified value appears in the string.")
print("parameters required !")
print("value:Required. A String. The string to value to search for ")
print("start:Optional. An Integer. The position to start the search. Default is end")	
print("Optional. An Integer. The position to end the search. Default is the end of the string")
#Example
#Return the number of times the value "apple" appears in the string:

x = "HELLO  WORLD!WORLD WORLDWORLD WORLD"
print("x =",x)
print("x with count()) =",x.count("WORLD"))
print("find WORLD count in index range of 10 to 24 :",x.count("WORLD", 10, 24))

print("--------------------------------------------------------------------------------------------------------------------------")

print("-------------------------------encode()	Returns an encoded version of the string-----------------------------------------")
print("The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.")
print("parameters required !")
print("encoding	: Optional. A String specifying the encoding to use. Default is UTF-8 ")
print("errors:	Optional. A String specifying the error method. Legal values are:")	
print("-------------------------------------------------------------------------------------------------")
print("Legal values are:")
print("--------------------------------------------------------------------------------------------------")
print("\'backslashreplace\'	- uses a backslash instead of the character that could not be encoded")
print("\'ignore\'	- ignores the characters that cannot be encoded")
print("\'namereplace\'	- replaces the character with a text explaining the character")
print("\'strict\'	- Default, raises an error on failure")
print("\'replace\'	- replaces the character with a questionmark")
print("\'xmlcharrefreplace\'	- replaces the character with an xml character")
print("-------------------------------------------------------------------------------------------------")

#Example
#UTF-8 encode the string:

x = "HELLO  WORLD!WORLD WORLD WORLD"
print("x =",x)
print("x with count() =",x.encode())

print("--------------------------------------------------------------------------------------------------------------------------")
print("--------------------------endswith()	Returns true if the string ends with the specified value-----------------------------")
print("The endswith() method returns True if the string ends with the specified value, otherwise False.")
print("parameters required !")
print("value:Required. The value to check if the string ends with")
print("start:Optional. An Integer specifying at which position to start the search")	
print("end:Optional. An Integer specifying at which position to end the search")
#Example
#Check if the string ends with a punctuation sign (.):

x = "HELLO  WORLD!WORLD WORLD WORLD."
print("x =",x)
print("x with endswith(value,start,end) =",x.endswith("."))
print("x with endswith(\"World.\", 5, 11) =",x.endswith("World.", 5, 11))

print("--------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------expandtabs():Sets the tab size of the string--------------------------------------")
print("The expandtabs() method sets the tab size to the specified number of whitespaces.")
print("parameters required !")
print("tabsize	Optional. A number specifying the tabsize. Default tabsize is 8")
#Example
#Set the tab size to 2 whitespaces:

x = "HELLO  WORLD!WORLD\t WORLD WORLD."
print("x =",x)
print("x with expandtabs(number) =",x.expandtabs(4))

print("--------------------------------------------------------------------------------------------------------------------------")
print("--------------find()	Searches the string for a specified value and returns the position of where it was found-------------")
print("The find() method finds the first occurrence of the specified value.")
print("The find() method returns -1 if the value is not found.")
print("The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)")
print("parameters required !")
print("value:Required. The value to search for")
print("start:Optional. Where to start the search. Default is 0")
print("end:Optional. Where to end the search. Default is to the end of the string")

#Example
#Where in the text is the word "welcome"?

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print("where the welcome is present (index)=",x)

# Example
# Where in the text is the first occurrence of the letter "e"?
x = txt.find("e", 5, 10)
print("where the e is present (index)=",x)
print("If the value is not found, the find() method returns -1, but the index() method will raise an exception:")

# Example
# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
print("if there that string is not there then it will print:",txt.find('q'))

#example
#Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
print("find e in between index 5 to 10 :",txt.find("e", 5, 10))
print("------------------------------------------------------------------------------------------------------------------------")


print("--------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------format()	Formats specified values in a string---------------------------------------")
print("The format() method formats the specified value(s) and insert them inside the string's placeholder.")
print("The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.")
print("The format() method returns the formatted string.")
print("parameters required !")
print("value:Required. The value to search for")
print("value1, value2... : Required. One or more values that should be formatted and inserted in the string. The values are either a list of values separated by commas, a key=value list, or a combination of both. The values can be of any data type.")

#Example
#Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:

x = "Hello, {} to my world."
print("result before format :",x)
x = x.format("welcome")
print("result after format :",x)

#Example
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#example
# Using different placeholder values:

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print("txt1 =",txt1)
txt2 = "My name is {0}, I'm {1}".format("John",36)
print("txt2 =",txt2)
txt3 = "My name is {}, I'm {}".format("John",36)
print("txt3 =",txt3)

print("------------------------------------------------------------------------------------------------------------------------")

print("-----------------------------format_map()	Formats specified values in a string----------------------------------------")
print("Python String format_map() method is an inbuilt function in Python, which is used to return a dictionary key’s value.")
print("--------------------------------------------------")

print("Parameters : Here z is a variable in which the input dictionary is stored and string is the key of the input dictionary. input_dict: Takes a single parameter which is the input dictionary.")
print("--------------------------------------------------")

# input stored in variable a.
a = {'x':'John', 'y':'Wick'}
  
# Use of format_map() function
print("{x}'s last name is {y}".format_map(a))
print("------------------------------------------------------------------------------------------------------------------------")

print("-------------index()	Searches the string for a specified value and returns the position of where it was found-----------")

print("The index() method finds the first occurrence of the specified value.")
print("The index() method raises an exception if the value is not found.")
print("The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)")
print("--------------------------------------------------")
print("Parameters :")
print("value:Required. The value to search for")
print("start:Optional. Where to start the search. Default is 0")
print("end:Optional. Where to end the search. Default is to the end of the string")
print("--------------------------------------------------")

# Where in the text is the word "welcome"?:

text = "Hello World My hello World my world !"
x = text.index("hello")
print("Where the hello present in string text (index) :",x)
print("------------------------------------------------------------------------------------------------------------------------")

# Where in the text is the first occurrence of the letter "e"?:

text = "Hello World My hello World my world !"
x = text.index("e")
print("Where the e present in string text (index) :",x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:

text = "Hello World My hello World my world !"
x = text.index("hello",5,20)
print("Where the e present in string text within range of 5 to 10 index (index) :",x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:

text = "Hello World My hello World my world !"
# x = text.index('q')
# print("if nothing is found then it returns index (index) :",x) #   x = text.index("q") ValueError: substring not found

print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------isalnum()	Returns True if all characters in the string are alphanumeric-------------------------")
print("The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).")
print("Example of characters that are not alphanumeric: (space)!#%&? etc.")
print("No parameters.")

#Example

text = "hello world HELLO WORLD Hello World !"
print(" text Is alphanumeric or not=",text.isalnum())

print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------isalpha()	Returns True if all characters in the string are in the alphabet----------------------")
print("The isalpha() method returns True if all the characters are alphabet letters (a-z).")
print("Example of characters that are not alphabet letters: (space)!#%&? etc.")
print("No parameters.")

#Example
#Check if all the characters in the text are letters:
text = "helloWORLD"
print("text Is alphabet or not=",text.isalpha())

print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------isascii()	Returns True if all characters in the string are ascii characters---------------------")
print("The isascii() method returns True if all the characters are ascii characters  (a-z).")
print("Example of characters that are not alphabet letters: (space)!#%&? etc.")
print("No parameters.")

#Example
#Check if all the characters in the text are letters:
text = "hello WORLD123"
print("text Is isascii or not=",text.isascii())

print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------isdecimal()	Returns True if all characters in the string are decimals-------------------------")
print("The isdecimal() method returns True if all the characters are decimals (0-9).")
print("This method is used on unicode objects.")
print("No parameters.")

#Example
#Check if all the characters in the text are letters:
text = "123"
print("text Is isdecimal or not=",text.isdecimal())

print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------isdigit()	Returns True if all characters in the string are digits-------------------------------")
print("The isdigit() method returns True if all the characters are digits, otherwise False.")
print("Exponents, like ², are also considered to be a digit.")
print("No parameters.")

#Example
#Check if all the characters in the text are letters:
text = "123"
print("text Is isdigit or not=",text.isdigit())

print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------isidentifier()	Returns True if the string is an identifiercl---------------------------------")
print("The isidentifier() method returns True if the string is a valid identifier, otherwise False.")
print("A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.")
print("No parameters.")

#Example
#Check if all the characters in the text are letters:
text = "test012"
print("text Is isidentifier or not=",text.isidentifier())

print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------islower()	Returns True if all characters in the string are lower case---------------------------")
print("The islower() method returns True if all the characters are in lower case, otherwise False.")
print("A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.")
print("No parameters.")

#Example
#Check if all the characters in the text are letters:
text = "test012"
print("text Is alphabet or not=",text.islower())

print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------isnumeric()	Returns True if all characters in the string are numeric--------------------------")
print("The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.")
print("Exponents, like ² and ¾ are also considered to be numeric values.")
print("\"-1\" and \"1.5\" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.")
print("No parameters.")

#Example
#Check if all the characters in the text are letters:
text = "012"
print("text Is isnumeric or not=",text.isnumeric())

print("---------------------------------------------------------------------------------------------------------------------------")

print("---------------------------isprintable()	Returns True if all characters in the string are printable------------------------")
print("The isprintable() method returns True if all the characters are printable, otherwise False.")
print("Exponents, like ² and ¾ are also considered to be numeric values.")
print("Example of none printable character can be carriage return and line feed.")
print("No parameters.")

#Example
#Check if all the characters in the text are printable:

text = "Hello World #1?"
print("text Is isprintable or not=",text.isprintable())

print("---------------------------------------------------------------------------------------------------------------------------")
 
print("--------------------------isspace()	Returns True if all characters in the string are whitespaces--------------------------")
print("The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.")

print("No parameters.")

#Example
#Check if all the characters in the text are whitespaces:

text = "  "
print("text Is isspace or not=",text.isspace())

print("---------------------------------------------------------------------------------------------------------------------------")
 
print("--------------------------istitle()	Returns True if the string follows the rules of a title-------------------------------")
print("The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.")
print("Symbols and numbers are ignored.")
print("No parameters.")

#Example
#Check if each word start with an upper case letter:

text = "Hello World!"
print("text Is istitle or not=",text.istitle())
text = "hello World!"
print("text Is istitle or not=",text.istitle())
print("---------------------------------------------------------------------------------------------------------------------------")

print("--------------------------isupper()	Returns True if all characters in the string are upper case---------------------------")
print("The isupper() method returns True if all the characters are in upper case, otherwise False.")
print("Numbers, symbols and spaces are not checked, only alphabet characters.")
print("No parameters.")

#Example
#Check if all the characters in the text are in upper case:

text = "Hello World!"
print("text Is istitle or not=",text.isupper())
text = "HELLOWORLD"
print("text Is istitle or not=",text.isupper())
print("---------------------------------------------------------------------------------------------------------------------------")
  
print("--------------------------join()	Converts the elements of an iterable into a string----------------------------------------")
print("The join() method takes all items in an iterable and joins them into one string.")
print("A string must be specified as the separator.")
print("parameters.")
print("iterable:Required. Any iterable object where all the returned values are strings")
#Example
#Check if all the characters in the text are in upper case:

myTuple = ("John", "Peter", "Vicky")
x = "-".join(myTuple)
print(x)

myTuple = ("John", "Peter", "Vicky")
myspearator = " check;"
x = myspearator.join(myTuple)
print(x)
print("---------------------------------------------------------------------------------------------------------------------------")

print("--------------------------ljust()	Returns a left justified version of the string----------------------------------------")
print("The ljust() method will left align the string, using a specified character (space is default) as the fill character.")
print("Note: In the result, there are actually 14 whitespaces to the right of the word banana.")
print("parameters.")
print("length:Required. The length of the returned string")
print("character:Optional. A character to fill the missing space (to the right of the string). Default is " " (space).")
#Example
#Return a 20 characters long, left justified version of the word "banana":

txt = "banana"
x = txt.ljust(20)
print(x,"is my favorite fruit.")

#Example
#Using the letter "O" as the padding character:

txt = "banana"
x = txt.ljust(20, "O")
print(x)

print("---------------------------------------------------------------------------------------------------------------------------")
print("--------------------------lower()	Converts a string into lower case-----------------------------------------------------")
print("The lower() method returns a string where all characters are lower case.")
print("Symbols and Numbers are ignored.")
print(" NO parameters.")

#Example
#Lower case the string:
txt = "HELLO WORLD"
x = txt.lower()
print("my favorite fruit :",x)

print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------lstrip()	Returns a left trim version of the string--------------------------------------")
print("The lstrip() method removes any leading characters (space is the default leading character to remove)")
print("parameters.")
print("characters:Optional. A set of characters to remove as leading characters")
#Example
#Remove spaces to the left of the string:

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#Example
#Remove the leading characters:

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

print("---------------------------------------------------------------------------------------------------------------------------")
print("--------------------------------lstrip()	Returns a left trim version of the string--------------------------------------")
print("The lstrip() method removes any leading characters (space is the default leading character to remove)")
print("parameters.")
print("characters:Optional. A set of characters to remove as leading characters")
#Example
#Remove spaces to the left of the string:

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#Example
#Remove the leading characters:

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

print("---------------------------------------------------------------------------------------------------------------------------")

 
# 
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

