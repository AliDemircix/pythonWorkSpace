import pandas as pd

# Read the first Excel sheet
df1 = pd.read_excel("excel/first_sheet.xlsx")

# Read the second Excel sheet
df2 = pd.read_excel('excel/second_sheet.xlsx')

# Merge the two DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', suffixes=['_first', '_second'])
print(merged_df)

# Create a new column to check for differences in prices
merged_df['Price_Difference'] = merged_df['PRICES_first'] - merged_df['PRICES_second']

# Filter rows with price differences
price_diff_df = merged_df[merged_df['Price_Difference'] != 0]
print(price_diff_df)

# Update the second Excel sheet with the updated prices
for index, row in price_diff_df.iterrows():
    df2.loc[df2['ID'] == row['ID'], 'PRICES'] = row['PRICES_first']

# Save the updated second Excel sheet
df2.to_excel('excel/updated_second_sheet.xlsx', index=False)

