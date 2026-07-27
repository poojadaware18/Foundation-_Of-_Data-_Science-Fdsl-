import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\DELL\OneDrive\Documents\Desktop\machine learning(lab)\ass1_data.csv")
#head function
print(df.head())
#tail function
print(df.tail())
#info function
print(df.info())
#describe function
print(df.describe())
#type function
print("Type:", type(df))
#columns function
print("Columns:", list(df.columns))
#index function
print("Index:", df.index.tolist())
print("loc example (rows 0-2, specific columns):")
print(df.loc[0:2,['tahun','tingkat_sekolah']])

print("\niloc example (first 3 rows, first 3 columns):")
print(df.iloc[0:3, 0:3])


