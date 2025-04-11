# Blinkit-Analysis

1 - Import Libraries:

pandas is imported as pd for data manipulation.

numpy is imported as np (though it's not directly used in the final version of the code, it's often used with pandas).

there are few more libraries that we usually import for the advanced analysis seaborn, numpy and matplotlib

2 - Load Data:

The script reads the grocery data from an Excel file ("D:\Downloads\BlinkIT Grocery Data.xlsx") into a pandas DataFrame.  A DataFrame is like a table in Python.

3 - Inspect Data:
I inspected the data in the excel file and i saw there were some issues with that data with more that 500 rows had 0 in them and many values were missing.

I printed the names of the columns in the DataFrame using print(df.columns). This helps you understand the structure of the data.

I identified rows where 'Item Weight', 'Sales', and 'Rating' are all missing (NaN) using df[df[['Item Weight', 'Sales', 'Rating']].isnull().all(axis=1)] and prints these rows. This helps in understanding the extent of missing data.

4 - Handle Missing Values:

The script fills missing values (NaNs) in the 'Item Weight', 'Sales', and 'Rating' columns with the mean value of each column.  This is a common way to handle missing numerical data.

5 - Remove Duplicates:

The script removes any duplicate rows from the DataFrame using df.drop_duplicates(inplace=True). The inplace=True argument means that the changes are made directly to the original DataFrame.

6 - Handle Zero Values in 'Item Visibility':

The script replaces any zero values in the 'Item Visibility' column with the mean value of that column.  This assumes that zeros in this column represent missing or incorrect data.

7 - Save Cleaned Data:

Finally, I saved the cleaned DataFrame to a new CSV file ("D:\Downloads\cleaned_data.csv") using df.to_csv(). The index=False argument prevents pandas from writing the row index to the CSV file.
