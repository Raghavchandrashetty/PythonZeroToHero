import pandas as pd

# create dataframe

data = {'Name' : ['Alice', 'Bob', 'Charlie', 'david', 'Eve'],
      'Age' : [24, 34, 24, 34, 37],
      'City' : ['Newyork', 'Los Abgeles','Chicago', 'detroit', 'Phoenix']}

df = pd.DataFrame(data)

print("**** " , df)

# add a new column
df['Salary'] = [50000, 125000, 180000, 87000, 140000]

print("data frame with salary\n ", df)

df.drop('City', axis=1, inplace=True)
print("data frame after deleting city \n ", df)

filtered_df = df[df['Age'] > 25]
print("data frame with age > 25 \n ", filtered_df)

selected_columns = df[['Name', 'Salary']]

print("data frame with name and salary\n ", selected_columns)

grouped_df =  df.groupby('Age').mean()

print("data frame with mean\n ", grouped_df)

# Create a DataFrame with missing data
data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, None, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', None, 'Phoenix']
}
df_nan = pd.DataFrame(data_with_nan)

print("\nDataFrame with Missing Data:\n", df_nan)

# Fill missing values
df_filled = df_nan.fillna({'Age': df_nan['Age'].mean(), 'City': 'Unknown'})

print("\nDataFrame with Filled Missing Data:\n", df_filled)

# Drop rows with missing values
df_dropped = df_nan.dropna()

print("\nDataFrame with Dropped Missing Data:\n", df_dropped)


# Create another DataFrame
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
}
df2 = pd.DataFrame(data2)

# Merge the two DataFrames
merged_df = pd.merge(df, df2, on='Name')

print("\nMerged DataFrame:\n", merged_df)

import matplotlib.pyplot as plt

# Plot a bar chart of Age vs Salary
df.plot(kind='bar', x='Name', y='Salary')
plt.title('Salary of Employees')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()