# -*- coding: utf-8 -*-
###############################################################################
#Control flow
###############################################################################
#Conditional statements work similarly in R and Python
x = 1

if x > 0:
    print('Positive')
elif x < 0:
    print('Negative')
else:
    print('Zero!')

# In this exercise, you will write a bunch of conditional statements 
#to determine the status of a person who had 5 drinks.

# Assign 5 to a variable
num_drinks = 5

# if statement
if num_drinks < 0:
    print('error')
# elif statement
elif num_drinks <= 4:
    print('non-binge')
# else statement
else :
    print('binge')

#The main differences in conditional statements between Python and R 
#are the lack of curly brackets

# and the else if statement is elif in Python

###############################################################################
#Loops
###############################################################################
int_list = [1, 2, 3, 4]

for value in int_list:
    print(value)

num_drinks = [5, 4, 3, 3, 3, 5, 6, 10]

# Write a for loop
for drink in num_drinks:
    # if/else statement
    if drink <= 4:
        print('non-binge')
    else:
        print('binge')
###############################################################################
#Individual binge drinking function
###############################################################################
#can create a function using the def keyword, followed by the name of the function.
#If your function has parameters, you place them within the round brackets
#and end the line with a colon        

#Everything in the body of the function will be indented

#The return statement of the function determines what the function returns
#In Python, the return statment is mandatory, 
def square(x):
    return(x**2)
square(2)
        
#Remember, 'binge' drinking happens
#men consume 5 or more drinks 
#or women consume 4 
#or more drinks in about 2 hours.        

#Write a function binge_male() that accepts a single argument, num_drinks
#, and returns the binge status for males.
 
# Binge status for males
def binge_male(num_drinks):
    if num_drinks <= 5:
        return('non-binge')
    else:
        return('binge')
        
# Check
print(binge_male(6))

#Write a function binge_female() that accepts a single argument, 
#num_drinks and returns the binge status for females.
# Binge status for females
def binge_female(num_drinks):
    if num_drinks <= 4:
        return('non-binge')
    else:
        return('binge')

# Check
print(binge_female(2))

#Function definitions are a little different in Python than in R, 
#but the one thing that has been consistenly different are 
#the indentations in Python.
       
###############################################################################
#General binge drinking function
###############################################################################        
#You have two binge status functions - one for males and the other for females. 

#n this exercise you will write a function that accepts two arguments: 
#sex and num_drinks

#you will make use of the functions binge_male() and binge_female()

#INSTRUCTION
#Write a binge_status() function that takes 2 arguments: sex and num_drinks
#Using binge_male() and binge_female() functions, 
#return the correct num_drinks for the relevant sex

# A function that returns a binge status
def binge_status(sex, num_drinks):
    if sex == 'male':
        return binge_male(num_drinks)
    else:
        return binge_female(num_drinks)
#Test your function by looking at the results for:
#A 'male' who had 5 drinks, and
#A 'female' who had 5 drinks.
print(binge_status('male', 5))
print(binge_status('female', 5))

#As you saw, just like in R, you can have functions return other functions in Python.

###############################################################################
#Lambda functions
############################################################################### 
#If you have ever used the *apply family of functions 
#(such as sapply() and lapply()) in R
#there's a good chance you might have used anonymous functions
#Anonymous functions in Python are known as lambda functions.

#The keyword in a lambda function is lambda instead of def
#These functions are typically used for functions that are 'one-line' long.

#For example, a function that returns the cube of a number can be written as:
cube_lambda = lambda x: x**3
print(cube_lambda(3))
#27

#Instruction
#Convert the sq_func() regular function 
#into a lambda function and call it sq_lambda.

#Use the lambda function to print the results when 3 is passed into the function.

# A function that takes a value and returns its square
def sq_func(x):
    return(x**2)
    
# A lambda function that takes a value and returns its square
sq_lambda = lambda x: x**2

# Use the lambda function
print(sq_lambda(3))

#Did you notice that unlike R, you can actually 
#save a lambda function in Python so that you can resuse it later?

###############################################################################
#Mapping functions
###############################################################################
#R has the *apply family of functions that can take a function 
#and apply it to several or all elements of a list/data.frame/matrix.
#The Python equivalent is the built-in map() function. 

#map() takes the name of the function as its first argument, 
#and then a list of values as the second argument

#Recall that you need to wrap the output of map() 
#inside list() to get the desired results.

#Map the binge_male function across the num_drinks list.
# map the binge_male function to num_drinks
print(list(map(binge_male, num_drinks)))
# map the binge_female function to num_drinks
print(list(map(binge_female, num_drinks)))

#Remember that you need wrap the results of map() 
#inside list() to get the desired results!

###############################################################################
#List comprehension
###############################################################################
#List comprehensions are a concise 
#and convenient way to address a common programming task
# 1- iterating though a list, 
# 2- making a calculation, 
# 3- and saving the calculation into a new list

# While this can be performed using a for loop, 
#a list comprehension preforms the same task with fewer number of lines.

#The following list comprehension squares all values in a list:
x = [1, 2, 3, 4]
print([i**2 for i in x])

#A list of file names has been provided to you in the inflam_files list
#Your task is to write a list comprehension that imports 
#these files as pandas DataFrames in a single list
inflam_files = ['inflammation-03.csv', 'inflammation-02.csv', 'inflammation-01.csv']
#Re-write the provided for loop as a list comprehension: dfs_comp.

import pandas as pd

# Append dataframes into list with for loop
dfs_list = []
for f in inflam_files:
    dat = pd.read_csv(f)
    dfs_list.append(dat)

# Re-write the provided for loop as a list comprehension: dfs_comp
dfs_comp = [pd.read_csv(f) for f in inflam_files]
print(dfs_comp)

#List comprehensions in Python are a convenient way 
#to create a new list from an existing list! 

###############################################################################
#Dictionary comprehension
###############################################################################
#A dictionary comprehension is very similar to a list comprehension.
#The difference is that the final result is a dictionary instead of a list

#ecall that each element in a dictionary has 2 parts, a key and a value
#separated by a colon

#The following dictionary comprehension squares all values in a list:
x = [['a', 1], ['b', 2], ['c', 3], ['d', 4]]

print({key:(value**2) for (key, value) in x})
#When you print a dictionary, the order of elements is not guaranteed.
#Dictionary comprehensions are wrapped inside { }.

twitter_followers = [['jonathan', 458], ['daniel', 660], ['hugo', 3509], ['datacamp', 26400]]
# Write a dict comprehension
tf_dict = {key:value for (key,value) in twitter_followers}

# Print tf_dict
print(tf_dict)







