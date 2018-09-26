# -*- coding: utf-8 -*-
###############################################################################
#Assignment and data types
###############################################################################
#A quick refresher of the data types in Python:

#int (integers): numbers without a decimal
#float (floating point numbers): numbers with a decimal
#bool (booleans): True or False values
#str (strings): usually to represent text. However, 
#anything that is wrapped in quotes (single or double) is treated as a string.

# Assign an integer (42) to w
w = 42

# Assign a float (3.14) to x
x = 3.14

# Assign a boolean (True) to y
y = True

# Assign a string ('python') to z
z = 'python'

# Print the data types of y and z
print(type(y))
print(type(z))

#As you saw, Python has only one way to assign values, the equal = sign

###############################################################################
#Arithmetic with strings
###############################################################################
#However, unlike R, Python allows you to use 
#certain mathematical operators on non-numeric values

#When you use + on strings, it will concatenate them together:
print('hello' + 'world')

#'helloworld'

#When you multiply a string by an integer, n, the string will be repeated n times:
print('hello' * 3)

#'hellohellohello'

#Finally, if you place two strings next to each other, they will also be concatenated:
print('hello' 'world')
print('hello'' ''world')
#'helloworld'

# Add 'the quick' to 'brown fox'
print('the quick' + 'brown fox')

# Assign 'jump' to the variable x
x = 'jump'

# Multiply x by 3
print(x * 3)

# Have the string 'lazy' next to the string 'dog'
print('lazy' 'dog')

###############################################################################
#Lists
###############################################################################
#Lists are generic containers that can store heterogeneous data in Python
#Recall that you can use square brackets to extract values out of a list. 

#Python is a 0-indexed language, the first element has an index of 0
#want to extract multiple consecutive values, you can use the colon (:)

###############################################################################
#IMPORTANT : Python is a left-inclusive, right-exclusive language
###############################################################################
#meaning when specifying a range,
#starting value will be included, but the ending value will not be included.

x = [1, 2, 3, 4, 5]
print(x[0:4])
#[1, 2, 3, 4]


#You can also specify negative indices to subset elements
print(x[-1])
#5

# Assign the values to the list
person_list = ['Jonathan', 'Cornelissen', 'male', True, 458]

# Get the first name from the list
print(person_list[-5])

# Get the first and last name from the list
print(person_list[0:2])

# Get the employment status
print(person_list[-2])

#Python starts counting from 0

###############################################################################
#Dictionaries
###############################################################################
#Dictionaries are similar to named vectors and lists in R
#In Python, dictionaries are created using a pair of curly brackets, { }
#and passed in key-value pairs. Keys and values are separated with a colon.

#For example
#create a dictionary with the key, 'a' and a value of 1
d = {'a': 1}

#Multiple key-value pairs are separated by a comma
#To access a value by the key, you can use square brackets
#but instead of passing in an index, you pass in the key

d = {'a': 1, 'b': 2}
d['a']
#1

# Create a dictionary from of the employee information list
person_dict = {
    'fname': 'Jonathan',
    'lname': 'Cornelissen',
    'sex': 'male',
    'employed': True,
    'twitter_followers': 458
}

# Get the first and last names from the dict
print(person_dict['fname'])
print(person_dict['lname'])

#Lists and Dictionaries are two of the more common data types 
#you will be using in Python

###############################################################################
#Methods
###############################################################################
#There will be times when you need to add values into a list
#or update values in a dictionary.

#Here we will see some of the object-oriented nature of Python
# which is different from R.
    
#Everything in Python is an object (e.g., list object, dictionary object, etc). 

#Objects can all perform certain tasks (e.g., add values to a list, 
#update values in a dictionary)

#Instead of calling functions on the object you want to manipulate
#you use dot notation to have the object perform an action on itself 
#by calling a method.

# Append values to a list
person_list.append(2018)

# Print person_list
print(person_list)

# Print the last element of person_list
print(person_list[-1])
print(person_list[5])

# Update the person_dict dictionary
person_dict.update({'date' : '2018-06', 'twitter_followers' : 458})

# Print the person_dict dictionary
print(person_dict)
###############################################################################
# IMPORTANT : Remember the difference between functions and methods! 
#You pass objects to functions, whereas you call methods on objects!
###############################################################################

###############################################################################
#NumPy array
###############################################################################
#Vectors and matrices are not available in core Python
#In order to use them, you will have to import the NumPy library
#import package as pk

#Within the numpy library
#loadtxt() function to import files
#For example, you can load a file named data.csv using numpy 
#with numpy.loadtxt('data.csv')

# Import the numpy library with an alias: np
import numpy as np

# Load the boston dataset
boston = np.loadtxt('boston_data.csv', delimiter=',')

# Get the first row of data
first = boston[0]

# Calculate its mean
print(first.mean())

#The numpy library gives Python the ability to work with matricies and arrays.
#We'll work with DataFrames in the next exercise.

###############################################################################
#Pandas DataFrames
###############################################################################
#Numpy is great if your data contains homogeneous data
# In many statistical datasets, data will be heterogeneous,
#i.e., having columns of varying data types

#if that's the case, you can use a different library, pandas
#to deal with these spreadsheet-like datasets

#This gives python the DataFrame object, similar to the one in R

# Import the pandas library
import pandas as pd

# Load the tips.csv dataset
tips = pd.read_csv('tips.csv')

# Look at the first 5 rows
print(tips.head(5))

#This is analogous to the data frames in R
#You will learn more about Pandas DataFrames in chapter 3.
