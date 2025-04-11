# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 01:22:28 2025

@author: harsh
"""

import pandas as pd
import numpy as np

df = pd.read_excel("D:\\Downloads\\BlinkIT Grocery Data.xlsx")

print(df.columns)

x = df[df[['Item Weight', 'Sales', 'Rating']].isnull().all(axis=1)]  # Rows where all the specified columns have NaN.
print(x)

# Fill NaN values with the mean for specific columns

df['Item Weight'] = df['Item Weight'].fillna(df['Item Weight'].mean())
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Rating'] = df['Rating'].fillna(df['Rating'].mean()) 

# Removing Duplicates

df.duplicated()  # Identifies duplicates
df.drop_duplicates(inplace=True)  # Removes duplicates

#removing the zeros from the data to make our analysis more accurate

df['Item Visibility'] = df['Item Visibility'].replace(0, df['Item Visibility'].mean())

df.to_csv('D:\\Downloads\\cleaned_data.csv', index=False)  


