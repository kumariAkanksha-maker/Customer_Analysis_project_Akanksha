
import pandas as pd

# Load the CSV file
df = pd.read_csv("Customer_data.csv")

# Display the dataset
print("Customer Dataset:\n", df)

# Basic analysis
print("\nTotal Purchase Amount per Customer:")
print(df.groupby('Customer_ID')['Purchase_Amount'].sum())

print("\nNumber of Transactions per Customer:")
print(df['Customer_ID'].value_counts())

print("\nEarliest Transaction Date:")
print(df['Transaction_Date'].min())

print("\nLatest Transaction Date:")
print(df['Transaction_Date'].max())
