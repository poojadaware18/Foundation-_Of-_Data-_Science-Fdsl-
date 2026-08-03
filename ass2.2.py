import pandas as pd
import numpy as np

df = pd.read_excel("c:\fds(lab)\Car data.csv")

print("Display data Using Groupby Function")
print(df.groupby("Name")["Year"].sum())
print("-------------------------------------------------------------------------------------------------------------------------")
print()
print(df.groupby("Name")["Year"].mean())
print("-------------------------------------------------------------------------------------------------------------------------")

print("\nMultiple Aggregations")
print(df.groupby("Name").agg(
    Total_Cars=("Name", "count"),
    Avg_Price=("Price", "mean"),
    Avg_Year=("Year", "mean"),
    Avg_Seats=("Seats", "mean")
))
print("-------------------------------------------------------------------------------------------------------------------------")

print("\nPivot Table")
pivot = pd.pivot_table(
    df,
    values="Price",
    index="Fuel_Type",
    columns="Year",
    aggfunc="mean",
    fill_value=0
)
print(pivot)
print("-------------------------------------------------------------------------------------------------------------------------")

print("\nMissing values per column")
print(df.isnull().sum())
print("-------------------------------------------------------------------------------------------------------------------------")

print("\nRows with missing values")
print(df[df.isnull().any(axis=1)])
print("-------------------------------------------------------------------------------------------------------------------------")

print("\nDropping rows with missing values")
print(df.dropna())
print("-------------------------------------------------------------------------------------------------------------------------")

print("\nFilling missing Year with mean")
df_filled = df.copy()
df_filled["Year"] = df_filled["Year"].fillna(df_filled["Year"].mean())
print(df_filled)
print("-------------------------------------------------------------------------------------------------------------------------")
