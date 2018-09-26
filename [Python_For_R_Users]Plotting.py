#


# -*- coding: utf-8 -*-
###############################################################################
#Chapter 4 : Plotting
###############################################################################

###############################################################################
#Univariate plots in pandas
###############################################################################
# Histogram
#df['column_name'].plot(kind='hist')
#plt.show()

# Boxplot
#df['column_name'].plot(kind='box')
#plt.show()

#Bar graphs are good for categorical data. 
#Remember to first obtain the counts of values using the .value_counts() method before plotting.

## Bar plot
#counts = df['column_name'].value_counts()
#counts.plot(kind='bar')
#plt.show()

#Import 'tips' dataset
import pandas as pd
tips = pd.read_csv('tips.csv')

import matplotlib.pyplot as plt

#Create a histogram of the tip column.
tips['tip'].plot(kind = 'hist')
plt.show()

# Boxplot of the tip column
tips['tip'].plot(kind = 'box')
plt.show()

#Create a bar plot that displays the number of values present in each category of sex
cts = tips['sex'].value_counts()
cts.plot(kind = 'bar')
plt.show()

#The .plot() method is defined for both DataFrame and Series objects 
#which allows you to draw quick plots directly from pandas.

###############################################################################
#Bivariate plots in pandas
###############################################################################
#Comparing multiple variables simultaneously is also another useful way to understand your data. 
#When you have two continuous variables, a scatter plot is usually used.

# Scatter plot
#df.plot(x='x_column', y='y_column', kind='scatter')
#plt.show()

#You can use a boxplot to compare one continuous and one categorical variable. 
#However, you will be using the .boxplot() method instead of the .plot() method.

# Boxplot
#df.boxplot(column='y_column', by='x_axis')
#plt.show()


#Create a scatter plot with 'tip' on the y-axis and 'total_bill' on the x-axis.
import matplotlib.pyplot as plt
tips.plot(x = 'total_bill',y = 'tip', kind = 'scatter')
plt.show()

#Create a boxplot of the tip column grouped by the sex column.
tips.boxplot(column = 'tip',by = 'sex')
plt.show()

# Also keep in mind you need to call plt.show() from matplotlib to display your plots.

###############################################################################
#Univariate plots in seaborn
###############################################################################
#Seaborn is a popular plotting library. It embraces the concepts of "tidy data" 
#and allows for quick ways to plot multiple varibles.
#import seaborn as sns
#import matplotlib.pyplot as plt

# Bar plot
#sns.countplot(x='column_name', data=df)
#plt.show()

# Histogram
#sns.distplot(df['column_name'])
#plt.show()

#Use the seaborn countplot() function to draw a bar plot of sex.
import seaborn as sns
import matplotlib.pyplot as plt

#Bar plot
sns.countplot(x = 'sex' ,data = tips)
plt.show()

#Use the seaborn distplot() function to draw a histogram of total_bill.
# Histogram
sns.countplot(tips['total_bill'])
plt.show()

###############################################################################
#Bivariate plots in seaborn
###############################################################################
#We use boxplots when we have a numeric variable and a categorical variable. 
#Scatter plots are used when we have two numeric variables.

#For boxplots and scatter plots, we can use the boxplot() and regplot() methods.

#INSTRUCTIONS
#Use the seaborn boxplot() function to generate a boxplot of the tip column by sex
import seaborn as sns
import matplotlib.pyplot as plt

# Boxplot for tip by sex
sns.boxplot(x = 'sex', y = 'tip', data=tips)
plt.show()

# Scatter plot of total_bill and tip
sns.regplot(x = 'total_bill' ,y = 'tip' ,data = tips)
plt.show()

###############################################################################
#Facet plots in seaborn
###############################################################################
#Some plotting functions in seaborn such as distplot() and lmplot() have built-in facets.
#All you need to do is pass a col and/or row argument 

import seaborn as sns
import matplotlib.pyplot as plt

# Create a facet
#facet = sns.FacetGrid(df, col='column_a', row='column_b')

# Generate a facetted scatter plot
#facet.map(plt.scatter, 'column_x', 'column_y')
#plt.show()

#Create a scatter plot of 'total_bill' on the x-axis and 'tip' on the y-axis with lmplot().
#Facet the plot by 'smoker' and color the points by 'sex'

# Scatter plot of total_bill and tip faceted by smoker and colored by sex
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', col = 'smoker')
plt.show()

#Use the FacetGrid() function to create a facet object facetted by 'time' 
#and 'smoker', and colored by 'sex'.
#Call .map() on facet to generate a facetted scatter plot of 'total_bill' and 'tip'.

facet = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
facet.map(plt.scatter, 'total_bill', 'tip')
plt.show()

###############################################################################
#Univariate and bivariate plots in matplotlib
###############################################################################
#Matplotlib is at the core of all the plotting functions in Pandas and Seaborn. 

#In this exercise, you will generate a histogram and scatterplot:

import matplotlib.pyplot as plt

#Create a histogram of the 'total_bill' column.
plt.hist(tips['total_bill'])
plt.show()

# Bivariate scatterplot
plt.scatter(tips['tip'], tips['total_bill'])
plt.show()

###############################################################################
#Subfigures in matplotlib
###############################################################################
#Sometimes you want to combine several subplots in a single figure.

#You can do this by creating a figure and an axes simultaneously by using the plot.subplots()

# Create a figure with 1 axes
fig, ax = plt.subplots(1, 1)

# Plot a scatter plot in the axes
ax.scatter(tips['tip'], tips['total_bill'])
plt.show()

# Create a figure with scatter plot and histogram
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.scatter(tips['tip'], tips['total_bill'])
ax2.hist(tips['total_bill'])
plt.show()

###############################################################################
#Working with axes
###############################################################################    
#Create a seaborn histogram of the 'tip' column and assign it to dis
# Distplot of tip
import seaborn as sns
dis = sns.distplot(tips['tip'])

# Print the type
print(type(dis))

# a figure with 2 axes (1 row 2 columns).
#Generate a histogram in row 1 column 1 and a scatter plot in row 1 column 2.

# Figure with 2 axes: regplot and distplot
fig, (ax1, ax2) = plt.subplots(1, 2)
sns.distplot(tips['tip'], ax=ax1)
sns.regplot(x='total_bill', y='tip', data=tips, ax=ax2)
plt.show()

###############################################################################
#Polishing up a figure
############################################################################### 

import matplotlib.pyplot as plt
import seaborn as sns

# Create a figure with 1 axes
fig, ax = plt.subplots()

# Draw a displot
ax = sns.distplot(tips['total_bill'])

# Label the title and x axis
ax.set_title('Histogram')
ax.set_xlabel('Total Bill')
plt.show()


