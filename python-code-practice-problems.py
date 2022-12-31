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
sentence = "This is a sentence"
print(sentence)
print("Slice = " + str(sentence[-10:]))



# _______________________Basic Methods______________________

print()               # Prints out data on console
str()                 # Converts integer data to string data type
type()                # Used to figure out the data's type
