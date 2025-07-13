#importing necessary libraries
import pandas as pd
import numpy as np


#loading the dataset with a raw string to avoid escape sequence issues
df = pd.read_csv(r'E:\Python-numpy\learning_numpy\Project\data.csv')
# print(df.head())

#checking missing values
# print('Missing values in each column')
# print(df.isnull().sum())


# Convert 'Salary' column to numeric, coercing errors to NaN
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

df.replace([np.inf,-np.inf],np.nan,inplace=True)


# Fill missing values only in numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean(numeric_only=True))

#removing duplicate records
df.drop_duplicates(inplace=True)

#replace negative age
df['Age'] = np.where(df['Age']<0, df['Age'].mean(),df['Age'])

salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

#remove rows where salary is too high or too low
df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

df.to_csv('cleaned_data.csv',index = False)
print('Data cleaning completed ! Saved as "cleaned_data.csv"')
