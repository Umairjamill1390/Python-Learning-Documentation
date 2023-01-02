# Job Ready Programmer

#######################################################################
#                  SECTION 1 : Python Basics
#######################################################################


#======================================================================
#===================DATA TYPES AND METHODS=============================

# There are 4 main data types in python
number = 123          # int
decimal = 123.456     # float
name = "Andrew"       # str
decision = True       # bool

#______________________________________________________________________
# Variables of the same data type can be added/merged (except for bool)

# Example 1 (int)
num1 = 22
num2 = 33 
sum = num1 + num2  
print(sum)            # prints -> 55

# Example 2 (float)
num1 = 11.11
num2 = 22.22
sum = num1 + num2 
print(sum)            # prints -> 33.33

# Example 3 (str)
first_name = "Andrew"
last_name = " Garfield"
full_name = first_name + last_name 
print(full_name)      # prints -> Andrew Garfield

# Example 4 (using str() method)
actor_name = "Andrew Garfield"
movie_rank = 3 
movie_name = "The Amazing Spider-Man (2012)"
print("Movie: " + movie_name + "\nRanking at #" + str(movie_rank) + "\nStarring " + actor_name )

# Exaplme 5 (using str() method in variable declaration)
name = "Andrew Garfield"
num = 3
sentence = name + " has made a total of " + str(num) + " movies."
print(sentence)      # prints -> Andrew Garfield has made a total of 3 movies

# Exmaple 6 (Using type() method)
print("Testing data type")
number = 123          # int
decimal = 123.456     # float
name = "Andrew"       # str
decision = True       # bool
data_type = type(decimal)
print(data_type).     # prints -> float

#======================================================================
#============================== Slicing ===============================

#______________________________________________________________________
# Used to extract parts of a sequence as a whole or in a pattern
# Try these examples yourself

# Example 1 (int)
sentence = "This is a sentence"
print(sentence)
print("Slice = " + 
      str(sentence[0:4])) 

# Example 2
sentence = "This is a sentence"
print("Slice = " + 
      str(sentence[0: ])) 

# Example 3
sentence = "This is a sentence"
print(sentence)
print("Slice = " + 
      str(sentence[ :7]))  

# Example 4
sentence = "This is a sentence"
print(sentence)
print("Slice = " + 
      str(sentence[ :-5])) 
# Example 5
sentence = "This is a sentence"
print(sentence)
print("Slice = " + 
      str(sentence[-8: ])) 

# Example 6
sentence = "This is a sentence"
print(sentence)
print("Slice = " + 
      str(sentence[0:18:1])) 

# Example 7
sentence = "This is a sentence"
print(sentence)
print("Slice = " + 
      str(sentence[-8: :2]))

#======================================================================
#===================== String Practice Problems =======================

#______________________________________________________________________
# Below are some basic string methods


# NAME           REPRESENTATION             EXPLANATION
#---------------------------------------------------------------------------------------------------------------------------
# Print          print()                    # Prints out data on console
# String         str()                      # Converts integer data to string data type
# Type           type()                     # Used to figure out the data's type
# Slice          string[_:_:_]              # Slice is used to Extract data from a string
# Format         "num = {0}".format(10)     # Formats the specified value(s) and insert them inside the string's placeholder


#______________________________________________________________________
# Please practice the following problems for testing string methods
#
# What will be the outcome for the folloing problems?

# Problem 1
sentance = "abcdefghijklmnopqrstuvwxyz"
print(sentance.startswith("abcd"))

# Problem 2
sentance = "abcdefghijklmnopqrstuvwxyz"
print(sentance.endswith("abcd"))

# Problem 3 
sentance = "abcdefghijklmnopqrstuvwxyz"
print(sentance.endswith("vwxyz"))

# Problem 4 
sentance = "abcdefghijklmnopqrstuvwxyz"
print(sentance.startswith("efgh",4))

# Problem 55
sentance = "This is a sentence"
print(sentance.endswith("sentence",-8))

# Problem 6
sentance = "This is a sentence"
print(sentance.endswith("ence",-7))

# _____________ # _____________ # _____________ #

# Problem 7
sentance = "12345+67890"
print(sentance.isdigit())

# Problem 8
sentance = "1234567890"
print(sentance.isdigit())

# Problem 9
sentance = "12345 67890"
print(sentance.isdigit())

# Problem 10
sentance = "12345xx67890"
print(sentance.isalnum())

# Problem 11
sentance = "1234567890"
print(sentance.isalnum())

# Problem 12
sentance = "12345 67890"
print(sentance.isalnum())

# Problem 13
sentance = "12345*67890"
print(sentance.isalnum())







