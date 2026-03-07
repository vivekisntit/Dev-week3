# Importing pandas
import pandas as pd
import numpy as np

# Loading data from csv file
df=pd.read_csv("sales_data.csv")

# Printing shape & size of dataset
print(f"Number of rows in the DataFrame: {df.shape[0]}")
print(f"Number of columns in the DataFrame: {df.shape[1]}")

# Printing other information
print("Column names in the DataFrame:")
for col in df.columns:
    print(col)
print("\nDataFrame Info:")
print(df.info())

print("Data types of each columns:\n")
print(df.dtypes)

# Finding if any values are missing
print(df.isnull().sum())
print(df.duplicated(subset=["Product"]).sum())

# Quantity analysis

avg_quantity=df.iloc[:,2].mean()
print(f"Average amount of quantity sold: {avg_quantity}")

med_quantity=df.iloc[:,2].median()
print(f"Median amount of quantity sold: {med_quantity}\n")

# Price analysis
avg_sold_items=df.iloc[:,3].mean()
print(f"Average price of sold items: ₹{avg_sold_items:.2f}")

med_sold_items=df.iloc[:,3].median()
print(f"Median price of sold items: ₹{med_sold_items:.2f}\n")

std_dev_sold_items=df.iloc[:,3].std()
print(f"Standard deviation of price of sold items: ₹{std_dev_sold_items:.3f}\n")

# Sales analysis
print(f"Data type of Total_Sales: {df['Total_Sales'].dtype}")

df["Total_Sales"]=pd.to_numeric(df["Total_Sales"], errors='coerce')
print(f"Data type of Total_Sales after conversion: {df['Total_Sales'].dtype}\n")

avg_price=df["Total_Sales"].mean()
print(f"Average sales: ₹{avg_price:.2f}")

med_price=df["Total_Sales"].median()
print(f"Median sales: ₹{med_price:.2f}")

std_dev_total_sales=df["Total_Sales"].std()
print(f"Standard deviation of sales: ₹{std_dev_total_sales:.3f}\n")

# Overall analysis
price_per_item=avg_sold_items/avg_quantity
print(f"Average price per sold item: ₹{price_per_item:.3f}\n")

med_per_item=med_sold_items/med_quantity
print(f"Median price per sold item: ₹{med_per_item:.3f}\n")

std_dev_per_item=std_dev_sold_items/avg_quantity
print(f"Standard deviation of price per sold item: ₹{std_dev_per_item:.3f}\n")

total_revenue=df['Total_Sales'].sum()
print(f'Total Revenue: ₹{total_revenue:.2f}')

# Regional Sale insights
max_value=df["Total_Sales"].max()
print(f"Maximum sales: ₹{max_value:.2f}")

result=df.groupby("Region")["Total_Sales"].sum()
print(f"Region-wise total sales:{result}\n")
print(f"Maximum region-wise sales: ₹{result.max():.2f}")

s=pd.Series(result)
idx=s.idxmax()
print(f"{idx} has the highest sales of ₹{s.max():.2f}")

# Pie chart for region-wise sales
import matplotlib.pyplot as plt
result.plot(kind='pie', title='Total Sales by Region', xlabel='Region', ylabel='Total Sales (₹)', figsize=(10, 6))
plt.show()