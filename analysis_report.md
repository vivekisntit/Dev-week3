# Sales Analysis Report
## Introduction
This report presents an analysis of a sales dataset using Python and the pandas library. The goal of the analysis is to understand sales patterns, examine product performance and extract key statistical insights from the dataset.

The dataset was imported from a CSV file and analyzed to evaluate quantities sold, product price and overall sales performance.

## Dataset Overview
The dataset contains 100 rows and 7 columns representing all the sales.
Columns in the dataset
- Date – Date of the sale
- Product – Name of the product
- Quantity – Number of units sold
- Price – Price of each item
- Customer_ID – Special id for each customer
- Region – Geographic region of the sales
- Total_Sales – Total sales amount for each customer

All columns contain **100 non-null values**, meaning the dataset has no missing values.

The dataset showed 95 duplicate product entries, indicating that the same products appear multiple times across different transactions.

## Quantity Analysis
The quantity is analysis is as follows.
Key Statistics
- Average quantity sold: 4.78 units
- Median quantity sold: 5 units

## Price Analysis
The price analysis is as follows.
Key Statistics
- Average sale per transaction: ₹23,598.51
- Median sale per transaction: ₹24,192
- Standard deviation of sale per transaction: ₹13,917.63

## Sales Analysis
The sales analysis is as follows.
Key Statistic
- Average sales: ₹1,23,650.48
- Median sales: ₹97,955.50
- Standard deviation of sales: ₹1,00,161.085

## Overall analysis
- Average price of each product that is sold : ₹5,399.270
- Median price of each product that is sold : ₹4,838.400
- Standard Deviation of price of each product that is sold : ₹2,911.638

Total Revenue from the sales is ₹1,23,65,048.00

## Regional Sale Insights
Region-wise total sales:
- North:    ₹39,83,635
- South:    ₹37,37,852
- East:     ₹25,19,639
- West:     ₹21,23,922

North region has the highest sales of ₹39,83,635.00
![Region-wise sale]("revenue.png")

## Best Product
Dataset includes the following products:
- Headphones    
- Laptop        
- Monitor       
- Phone         
- Tablet  

Products with their total sale:
- Headphones   ₹13,84,033
- Laptop       ₹38,89,210
- Monitor      ₹13,48,071
- Phone        ₹28,59,394
- Tablet       ₹28,84,340

**Laptops** have the highest sale of ₹38,89,210.00
![Product-wise sale]("revenue3.png")