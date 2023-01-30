# Naming conventions to import is as pd
import pandas as pd

"""
Pandas is a package for handling data
To do so, data is put into a DataFrame, which looks similar to an excel file
On this excel file we can do similar things as excel, but also much more complicated things in more complicated ways
- reading and outputting data
- exploring data (summery statistics)
- slicing (taking parts of the data based on more complicated conditions)
- calculations (based on multiple criteria)
- merges and joins

in addition, the pandas dataframe format is used by ~90% of libraries in python, under which:
- virtually all algorithms, under which Neural Networks (tensorflow), decision trees (Scikit-Learn)
    and extreme gradient boosters (xgboost)
- visualization packages (matplotlib.pyplot, seaborn)
- pandas is very fast
    - It used the numpy package as a dependency which is mostly implemented in C
    - vectorized: by using pandas well, an operation can be done on an entire set of values at the same time
        instead of one value at a time

"""


############################### reading in files #####################################

# here we use pandas to read in the famous iris dataset in csv version
df = pd.read_csv('iris.csv')

# but we can also read in excel files (but then we also need to install openpyxl)
df_excel = pd.read_excel('iris.xlsx')

# or ods files (but then we also need to install odfpy
df_ods = pd.read_excel('iris.ods')

# show they are the same
print(f'the csv and excel dataframes are the same: {df.equals(df_excel)}')
print(f'the csv and ods dataframes are the same: {df.equals(df_ods)}')


# we can also make our own files.
df_self_created = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
print(df_self_created)






################################## exploring files ##############################################

# we can see what columns there are
print(df.columns)

# and we can se the entire shape
print(df.shape)
print(f'df has {df.shape[0]} rows and {df.shape[1]} columns')

# we can also see the types
print(df.dtypes)

# see some statistics
print(df.describe())
print(df.info())

# look at a single column, or multiple specific columns
print(df['species'])
# here we give a list of columns. It will print in that order. This is useful for reordering the columns of a dataframe
print(df[['species', 'sepal_length']])





################################# slicing ##########################################
# some of pandas greatest functionality is found in slicing

# maybe we are only interested in the setosa species
# this will only tell us whether its a setosa or not. it will do so in a pandas series
    # you can think of a series as a single column of data
print(df['species'] == 'setosa')

# if we give that series of true's and false's to the df in the form of df[series], we get a filtered version of the df
# this way we get a df with only the setosa's. this is called slicing
print(df[df['species'] == 'setosa'])

# we can also slice on multiple conditions, putting each slice conditoin (series) nicely between "(" and ")" brackets
print(df[(df['species'] == 'setosa') & (df['petal_width'] == 0.2)])

# maybe we are not interested in all columns of that slice. by adding a column between [] behind it, we get only that
    # column of the sliced dataframe
print(df[(df['species'] == 'setosa') & (df['petal_width'] == 0.2)]['sepal_length'])





####################### manipulating values ###########################
# we can also add a new column:
df['new column'] = 0
print(df)

# or add to it
df['new column'] = df['new column'] + 1
print(df['new column'])
df['new column'] = df['new column'] + df['sepal_length']
print(df['new column'])

# we can also combine slicing and calculations
df['new column'] = 0

# here we change the value of 'new column' to 1 only for setosa's
# but this will give an error. while the code will work, it will not change df because we are working on a copy of df!
df[df['species'] == 'setosa']['new column'] = 1

# while working on a copy is faster, so it can be helpful for doing calculations.
    # but here we want to change the original df. so we do the following df.loc[condition, column_to_change] = value
df.loc[df['species'] == 'setosa', 'new column'] = 1
print(df)

# .loc can pick values based on (row index OR condition) AND column name
    # in the format df.loc[row index OR condition, column_to_change]
# .iloc instead picks values based on row number and column number
print(df.iloc[0, 0]) # this gives the value of the first row on the first column




####################### speed comparison slicing vs looping #######################

# the above way uses a vectorized way for its operation, which is very fast. we could instead also use a for-loop
# lets compare the two
import time
import numpy as np
# for this we make a new dataframe that is a lot larger. the column A gets a random value between 0 and 100.
    # if the value is above 50, we will assign it a value
df_test_speed = df_test_speed = pd.DataFrame(np.random.randint(0, 100, size=(100000, 1)), columns=['A'])
df_test_speed['for_loop_column'] = None
df_test_speed['vectorized_loop_column'] = None
# this will iterate over all rows and assign a value for each row in the for_loop_column

# for loop
now = time.time()
for value in range(len(df_test_speed['for_loop_column'])):
    if df_test_speed.loc[value, 'A'] > 50:
        df_test_speed.loc[value, 'for_loop_column'] = 10**5

difference_loop = time.time() - now
print(f'this took {difference_loop} seconds')

# vectorized
now = time.time()
df_test_speed.loc[df_test_speed['A'] > 50, 'vectorized_loop_column'] = 10**5
difference_vectorized = time.time() - now
print(f'this took {difference_vectorized} seconds')

print(f'vectorized is {round((difference_loop/difference_vectorized)*100)}% faster than looping!')




############################ Counting values and Grouping ##############################

# here we have our initial dataframe
print(df)

# we can count how many times each row occurs sort it by most occurring first.
# our first row occurs 3 times in our df
print(df.value_counts(ascending=False))

# we can also do this for specific columns
# each flower occurs exactly 50 times.
print(df['species'].value_counts(ascending=False))
# it sets species as index, because of that we have only 1 column which shows the number.
    # we can change that by resetting the index
print(df['species'].value_counts(ascending=False).reset_index())

# we can group on species
print(df.groupby(['species']))
# but we get an object, this is because we have not chosen what to do with the values in other columns, lets choose max
print(df.groupby(['species']).max()) # this gives us the largest value of each column, split by species

# we can also groupby on multiple columns
print(df.groupby(['species', 'petal_width']).max())






######################### making a frequency analysis ###########################
# we can use the earlier learnt stuff to create a frequency analysis!
# first we define a new dataframe with the same columns, but no rows
df_freq_analysis = pd.DataFrame(columns=df.columns)

# then we iterate over the columns and count the values
for column in df.columns:
    print(column)
    temp_series = df[column].value_counts(ascending=False).reset_index()
    # here we add the two columns together as a string. for that we do need to turn them into strings with .astype(str)
    temp_series = temp_series['index'].astype(str) + ' (' + temp_series[column].astype(str) + ')'

    # now we assign this to a column
    df_freq_analysis.loc[:, column] = temp_series

# and here is our frequency analysis
print(df_freq_analysis)

print('end')