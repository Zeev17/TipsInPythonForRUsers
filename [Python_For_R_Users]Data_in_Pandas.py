# -*- coding: utf-8 -*-
###############################################################################
#Selecting columns
###############################################################################
#Unlike R, Python doesn't have a built-in data structure similar to data frames. 
#The library pandas gives you access to DataFrames in Python

import pandas as pd

#in pandas, you can either use the dot (.) notation
#or the square bracket notation ([ ]) to select columns.

#However, if your column name has a space in it, 
#or if the name clashes with a DataFrame attribute,
#then the convenient dot notation won't work.

df = pd.DataFrame({
        'A' : [1, 2, 3],
        'B' : [4, 5, 6],
        'C' : [7, 8, 9]},
        index = ['x', 'y', 'z'])

print(df)
#Subsetting columns
df['A']
df.A
df[['A', 'B']]
#Subsetting rows
#Row-label	(loc)	vs	row-index	(iloc) 
#Python	starts	counting	from	0
df.iloc[0]
df.iloc[[0,1]]

df.iloc[0, :]
df.iloc[[0,1], :]

#Print the tip column of tips using dot notation.

# Load the tips.csv dataset
tips = pd.read_csv('tips.csv')

# Look at the first 5 rows
print(tips.head(5))

# Print the tip column using dot notation
print(tips.tip)
# Print the sex column using square bracket notation
print(tips['sex'])
# Print the tip and sex columns
print(tips[['tip','sex']])

#The tips DataFrame also has a column named size
#Since size is also an attribute, 
#which returns the number of elements in a DataFrame, you can't use the tips.size
#to access the 'size' column. You will need to use tips['size']

###############################################################################
#Selecting rows
###############################################################################
#You can subset rows either
#using the row name (.loc accessor) 
#or the row index (.iloc accessor).

#To perform conditional subsetting, you pass .loc a boolean expression
#When using multiple conditions, you can use the & or |

#Remember, you need to surround each conditional statement inside parentheses.

# Print the first row of tips using iloc
print(tips.iloc[0])

# Print all the rows where sex is Female
print(tips[tips.sex == 'Female'])

# Print all the rows where sex is Female and total_bill is greater than 15
print(tips[(tips.sex == 'Female') & (tips.total_bill > 15)])

#You now know how to subset rows and columns individually
#Now you'll subset both rows and columns.

###############################################################################
#Selecting rows and columns
###############################################################################
#The syntax for subsetting both rows and columns in Pandas is similar to R
#The rows and columns are specified to the left and right of the comma, respectively

#To subset rows and columns using boolean expressions or labels, you can use:
#df.loc[row_labels, column_labels]
#
#To subset rows and columns using indices, you can use:
#df.iloc[row_indices, column_indices]

#Instruction
#Subset all the rows where sex is 'Female' while retaining only the total_bill, 
#tip, and sex columns, in that order.
print(tips.loc[(tips.sex == 'Female'),['total_bill','tip','sex']])

#All the rows including the following variables :total_bill, tip, and sex
#print(tips.iloc[:,[0,1,2]])

# first 3 rows and first 3 columns with iloc
print(tips.iloc[[0,1,2],[0,1,2]])

###############################################################################
#Integers and floats
###############################################################################
print(type(tips))
#However, this information is insufficient when working with DataFrames
#, since the result will be:
#class 'pandas.core.frame.DataFrame'>

#f you want to find out the data type of each column in the DataFrame
#, you can either use the .info()
tips.info()

#Now, if you want to change the data type of a column, 
#you can call the .astype() method
#df['column_a'] = df['column_a'].astype(int)

#INSTRUCTIONS
#Inspect the output of tips.dtypes in the shell.
tips.dtypes
#Convert the size column to int type.
tips['size'] = tips['size'].astype(int)
#Convert the tip columns to float type.
tips['tip'] = tips['tip'].astype(float)
# Look at the types
print(tips.dtypes)

#Great! Did you notice that data types of 'size' and 'tip'? They are now int64 and float64

###############################################################################
#Strings
###############################################################################
#Columns containing strings are represented as the object type in Pandas.

#Since a lot of data you will encounter involve strings, 
#it is important that you know how to manipulate them

#Python allows you to use its built-in string manipulation methods with the str accessor
#methods, some of which are .upper() and .lower(). 
#They convert strings to upper and lower case, respectively.

# Converts 'col_a' to lower case
#df['col_a'].str.lower()

# Converts 'col_b' to upper case
#df['col_b'].str.upper()


#INSTRUCTIONS
#Inspect the 'sex' and 'smoker' columns in the shell.
print(tips.iloc[:,[2,3]])
print(tips[['sex','smoker']])
#Convert the 'sex' column into lower case.
tips['sex'] = tips['sex'].str.lower()
#Convert the 'smoker' column into upper case.
tips['smoker'] = tips['smoker'].str.upper()
#Inspect the 'sex' and 'smoker' columns to ensure that case conversion worked.
print(tips[['sex', 'smoker']])
#Python has several other powerful string manipulation methods.

###############################################################################
#Category
###############################################################################
#Pandas provides the category data type, which is analogous to the R factor.
#You can convert a column into a categorical data type 
#by passing 'category' to the .astype() method

#you can see the various categories (known as levels in R)
#by using the .cat accessor and calling the .categories attribute.

#Another use case for categorical values is 
#when you want to preserve ordering in your data.

#For example, intuitively it makes sense that 'low' comes before 'high'. 
#You can use reorder_categories() to provide an order to a column

# Reorder categorical levels
#df['column_name'].cat.reorder_categories(['low', 'high'], ordered=True)

#INSTRUCTIONS
#Convert the type of 'time' column into category 
tips['time'] = tips['time'].astype('category')
#and print the categories in this column.
print(tips['time'].cat.categories)
# Order the time category so lunch is before dinner
tips['time2'] = tips['time'].cat.reorder_categories(['Lunch', 'Dinner'], ordered=True)
# Use the cat accessor to print the categories in the time2 column
print(tips['time2'].cat.categories)

#Categorical types have some performance benefits, 
#and can also be used with libraries other than pandas.

###############################################################################
#Dates (I)
###############################################################################
#You will often come across timeseries data during your Data Science journey.
#is important you know how to parse them correctly 
#and Pandas provides convenient function

#easily convert it to a datetime format using the pd.to_datetime()
#pd.to_datetime(df['date_column_as_string'], format='%m/%d/%Y')

#INSTRUCTIONS
import pandas as pd
#Import the country_timeseries.csv dataset and assign it to ebola 
ebola = pd.read_csv('country_timeseries.csv')
#and inspect the type of 'Date' column.
print(ebola['Date'].dtypes)

#Convert the type of 'Date' column into datetime using the given format 
#and inspect the type of 'Date' column.

# Convert the type of Date column into datetime
ebola['Date'] = pd.to_datetime(ebola['Date'], format='%m/%d/%Y')

# Inspect the Date column
print(ebola['Date'].dtype)

###############################################################################
#Dates (II)
###############################################################################
#Instead of converting the type of a column after importing the data,
# you can import the data while parsing the dates correctly.

#To do this, you can pass the parse_dates argument of pd.read_csv()
#Once the date column is imported as the correct type (datetime64
#you can make use of the .dt accessor along with the .year, .month, and .day
# Access year
#df['Date'].dt.year

# Access month
#df['Date'].dt.month

# Access day
#df['Date'].dt.day

#Import the dataset and ensure that the 'Date' column is imported as datetime type. 
#After importing, inspect the type of 'Date' column.
import pandas as pd

# Load the dataset and ensure Date column is imported as datetime
ebola = pd.read_csv('country_timeseries.csv', parse_dates=['Date'])

# Inspect the Date column
print(ebola['Date'].dtype)

# Create a year, month, day column using the dt accessor
ebola['year'] = ebola.Date.dt.year
ebola['month'] = ebola.Date.dt.month
ebola['day'] = ebola.Date.dt.day

# Inspect the newly created columns
print(ebola[['year', 'month', 'day']].head())


###############################################################################
#Missing Values
###############################################################################
#It is very rare to find a dataset that doesn't contain any missing values.

#You can use the isnull() pandas function to check for missing values. 
#pd.isnull(df['column']) will return True if the value is missing, or False

#You can also recode missing values with the .fillna()

# Print the rows where 'Cases_Guinea' is missing
print(ebola.loc[pd.isnull(ebola['Cases_Guinea'])])

# Mean of the Cases_Guinea column
tCases_Guinea_mean = ebola['Cases_Guinea'].mean()

## Fill in missing Cases_Guinea
print(ebola['Cases_Guinea'].fillna(tCases_Guinea_mean))

ebola['Cases_Guinea'] = ebola['Cases_Guinea'].fillna(tCases_Guinea_mean)
ebola['Cases_Guinea'].head(20)

#You can also drop missing values using the .dropna() method.

#Drop missing value for 'Cases_Liberia"
#Normally 39
ebola_dropna_Liberia = ebola.dropna(subset = ['Cases_Liberia'])

###############################################################################
#Groupby
###############################################################################
#Groupbys are an incredibly powerful and fast way to perform calculations, 

#Calculate the mean 'Cases_SierraLeone' for each unique value of 'year'
print(ebola.groupby('year')['Cases_SierraLeone'].mean())

# Mean Cases_SierraLeone by year and month
print(ebola.groupby(['year', 'month'])['Cases_SierraLeone'].mean())

#In addition to calculating the mean, you can use other methods 
#such as .agg() and .filter() on grouped DataFrames.

###############################################################################
#Tidy data
###############################################################################
#Tidy data paper by Hadley Wickham.

#In this exercise you will use melt() and .pivot_table() from pandas 
#to reshape your data from one shape to another

#Remember that when you call .pivot_table() on your data
#you also need to call the .reset_index() method to get your original DataFrame back.

import pandas as pd

#Dowload df
airquality = pd.read_csv('airquality.csv')
airquality.info()
# Print the rows where 'Solar.R' is missing
print(airquality.loc[pd.isnull(airquality['Solar.R'])])

# Melt the airquality DataFrame
airquality_melted = pd.melt(airquality, id_vars=['Day', 'Month'])
print(airquality_melted)

# Pivot the molten DataFrame
airquality_pivoted = pd.pivot_table(airquality_melted, index=['Month', 'Day'], columns='variable', values='value')
print(airquality_pivoted)

# Reset the index
airquality_melted = airquality_pivoted.reset_index()
