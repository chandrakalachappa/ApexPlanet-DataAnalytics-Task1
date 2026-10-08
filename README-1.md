# ApexPlanet Data Analytics - Task 1

## Data Immersion & Wrangling

This repository contains the deliverables for **Task 1: Data Immersion & Wrangling** of the ApexPlanet Data Analytics internship.

### Objective
Prepare the provided sales/customer dataset for analysis by profiling, cleaning, transforming, validating, and saving an analysis-ready dataset.

## Files

- `data_cleaning.py` - Python/Pandas script used for data cleaning and transformation.
- `data_dictionary.xlsx` - Data dictionary describing the variables, data types, and business relevance.
- `ApexPlanet_Task1_Cleaned_Dataset.csv` - Final cleaned dataset.
- `README.md` - Project documentation.

## Cleaning and Transformation Steps

1. Removed completely empty rows and columns.
2. Removed duplicate records.
3. Standardized column names and trimmed text values.
4. Converted `Order_Date` to a date format.
5. Created `Order_Year`, `Order_Month`, and `Order_Month_Name`.
6. Converted numeric fields such as `Age`, `Quantity`, `Unit_Price`, and `Total_Sales`.
7. Handled missing categorical values using `Unknown`.
8. Handled missing numeric values using the column median for applicable numeric fields.
9. Recalculated/validated sales using `Quantity × Unit_Price`.
10. Created `Age_Group` from `Age`.
11. Detected `Total_Sales` outliers using the IQR method.
12. Exported the final analysis-ready dataset as CSV.

## Dataset Summary

The cleaned dataset contains **1,000 records** and **19 columns**.

## Tools Used

- Python
- Pandas
- Excel/CSV

## Deliverables

The GitHub repository should contain the data dictionary, cleaning script, and cleaned dataset as requested in the Task 1 instructions.

## Author

Chandrakala Chappa
