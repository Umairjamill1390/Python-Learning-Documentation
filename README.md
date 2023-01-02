# Python-Learning-Documentation
This documentation is for learning purposes. Intended to be uses as a recap for any basic python concepts. I hope this document is found useful. Please do let me know if you find any issues. 

### Comments in Python (#)
Comments are text notes added to the program to provide explanatory information about the source code. Python ignores comments and understands that its used to explain the code to future programmers. 

` # is the representation for a comment in python.`

## Data Types
- `int` stores numeric data
- `float` stores decinal values
- `str` stores alphabetic data / strings
- `bool` stores either True or False

Here is a small pyhton code representation for data types

```
any_number = 123          # int
any_decimal = 123.456     # float
any_name = "Andrew"       # str
any_decision = True       # bool
```
## Slicing 1.5

You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.

```
string = "Hello World"
print(string[1:5])        # prints -> ello Wo
```
By leaving out the end index, the range will go to the end:

```
string = "Hello World"
print(string[1:])        # prints -> ello World
```
Extract a sub-string is common with the slicing syntax of string[start:stop:step]. This syntax allows you to extract a sub-string from string by specifying the starting index (start), ending index (stop), and the number of characters to skip between indices (step -1).

```
string = "1234567890"
print(string[0:10:3])    # prints ->1470
```
## Basic String Methods 1.6

When thinking about methods in general think of them as [attributes / functions] that are associated with the type of data. A method is a function that “belongs to” an object. String methods are mainly used to validate or convert the string partially or entirely. String method representation is a dot/period after the object name Ex: **type_Object.method_name**

Here are some common methods associated with strings. 
```
sentence = "This is a SENTENCE"
print(sentence)                    # prints -> This is a SENTENCE
sentence = sentence.upper()
print(sentence)                    # prints -> THIS IS A SENTENCE
sentence = sentence.lower()
print(sentence)                    # prints -> this is a sentence
sentence = sentence.capitalize()
print(sentence)                    # prints -> This is a sentence
sentence = sentence.isdigit()
print(sentence)                    # prints -> False
```
### Some practice examples are in the [python-code-practice-problems.py](https://github.com/Umairjamill1390/Python-Learning-Documentation/blob/main/python-code-practice-problems.py) file. 

> ### Please take a look and try to undersatand the other unique types of string methods.
* string.startswith("abc")
* string.endswith("zyx")
* string.isdigit("abc")
* string.isalpha("abc")
* string.isalnum("abc")

## Format 1.7

The ` .format() ` method formats the specified value(s) and insert them inside the string's placeholder. The placeholder is defined using curly brackets: ` {} `. 

Here is a good representation of ` .format() ` method.

```
item_1 = 50
item_2 = 40
tax = 10
total = item_1 + item_2 + tax
print(total)
print("Explanation: {0} + {1} + {2} = {3}".format(item_1, item_2, tax, total))
```

