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
## Slicing 

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
Adding one more index after the end index with a colon will provide the answer and move the number of steps ahead. 

```
string = "1234567890"
print(string[0:10:3])
```
