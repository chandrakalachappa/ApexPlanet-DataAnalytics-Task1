import pandas as pd
import numpy as np

INPUT_FILE = "ApexPlanet_DataAnalytics_Dataset (1).xlsx"
OUTPUT_FILE = "ApexPlanet_Task1_Cleaned_Dataset.csv"

df = pd.read_excel(INPUT_FILE, sheet_name="Sales_Dataset")

# Standardize column names
df.columns = (
    df.columns.astype(str).str.strip().str.replace(r"\s+", "_", regex=True)
)

# Preserve original IDs
df["Original_Order_ID"] = df["Order_ID"].astype(str)

# Trim text columns
text_cols = ["Order_ID","Customer_ID","Customer_Name","Gender","City","Product","Category"]
for col in text_cols:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Convert date and numeric fields
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
for col in ["Age","Quantity","Unit_Price","Total_Sales"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna("Unknown")

# Make Order_ID unique while preserving the source ID
n = df.groupby("Order_ID").cumcount() + 1
df["Order_ID"] = np.where(
    n.eq(1), df["Order_ID"], df["Order_ID"] + "_DUP" + n.astype(str)
)

# Feature engineering
df["Order_Year"] = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month
df["Order_Month_Name"] = df["Order_Date"].dt.strftime("%B")
df["Age_Group"] = pd.cut(
    df["Age"], bins=[0,17,25,35,50,65,200],
    labels=["<18","18-25","26-35","36-50","51-65","65+"]
)

# Validate sales calculation
df["Sales_Calculation_Check"] = np.isclose(
    df["Quantity"] * df["Unit_Price"], df["Total_Sales"], atol=0.02
)

# Flag IQR outliers (do not delete them automatically)
q1 = df["Total_Sales"].quantile(0.25)
q3 = df["Total_Sales"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
df["Total_Sales_Outlier_IQR"] = (
    (df["Total_Sales"] < lower) | (df["Total_Sales"] > upper)
)

df.to_csv(OUTPUT_FILE, index=False)
print("Cleaning complete.")
print("Rows:", len(df))
print("Missing Age:", df["Age"].isna().sum())
print("Missing City:", df["City"].isna().sum())
print("Unique Order IDs:", df["Order_ID"].nunique())
print("Sales formula mismatches:", (~df["Sales_Calculation_Check"]).sum())
print("IQR sales outliers:", df["Total_Sales_Outlier_IQR"].sum())
