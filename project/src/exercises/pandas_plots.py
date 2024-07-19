import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Salary': [50000, 60000, 55000, 65000, 62000]
}
df = pd.DataFrame(data)
print(df)

# Line plot
df.plot(kind='line', x='Name', y='Salary', title='Salary Over Names')
plt.xlabel('Name')
plt.ylabel('Salary')
#plt.show()

df.plot(kind='bar', x='Name', y='Salary', title='Salary over names')
plt.xlabel('Name')
plt.ylabel('Salary')
#plt.show()

# Scatter plot
df.plot(kind='scatter', x='Age', y='Salary', title='Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
#plt.show()

# Bar plot with seaborn
sns.barplot(x='Name', y='Salary', data=df)
plt.title('Salary by Employee')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()


# Scatter plot with regression line
sns.lmplot(x='Age', y='Salary', data=df)
plt.title('Age vs Salary with Regression Line')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()


# Line plot with custom color and style
df.plot(kind='line', x='Name', y='Salary', color='green', linestyle='--', marker='o', title='Salary Over Names')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()


# Adding title and labels
ax = df.plot(kind='bar', x='Name', y='Salary')
ax.set_title('Salary by Employee')
ax.set_xlabel('Employee Name')
ax.set_ylabel('Salary')
plt.show()

# Rotating axis labels
ax = df.plot(kind='bar', x='Name', y='Salary')
ax.set_xticklabels(df['Name'], rotation=45)
plt.title('Salary by Employee')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()
