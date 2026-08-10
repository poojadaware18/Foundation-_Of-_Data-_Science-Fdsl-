import pandas as pd
import numpy as np
from scipy import stats

# 1. Load dataset
df = pd.read_csv("Car data.csv")

print("Dataset Preview:\n", df.head())
print("\nSummary Statistics:\n", df.describe())

# 2. Manual Mean, Median, Mode function
def manual_stats(values):
    # Mean
    mean_val = sum(values) / len(values)

    # Median
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n % 2 == 0:
        median_val = (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2
    else:
        median_val = sorted_vals[n//2]

    # Mode
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    mode_val = max(counts, key=counts.get)

    return mean_val, median_val, mode_val

# 3. Apply to all numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

for col in numeric_cols:
    print(f"\nColumn: {col}")

    # Manual calculation
    manual_mean, manual_median, manual_mode = manual_stats(df[col].tolist())
    print("Manual Mean:", manual_mean)
    print("Manual Median:", manual_median)
    print("Manual Mode:", manual_mode)

    # Pandas
    print("Pandas Mean:", df[col].mean())
    print("Pandas Median:", df[col].median())
    print("Pandas Mode:", df[col].mode()[0])

    # NumPy / SciPy
    arr = df[col].to_numpy()
    print("NumPy Mean:", np.mean(arr))
    print("NumPy Median:", np.median(arr))
    print("SciPy Mode:", stats.mode(arr, keepdims=True))
    
    # Skewness check
    skewness = df[col].skew()
    print("Skewness:", skewness)
    if df[col].mean() > df[col].median():
        print("Distribution is right (positively) skewed")
    elif df[col].mean() < df[col].median():
        print("Distribution is left (negatively) skewed")
    else:
        print("Distribution is approximately symmetric")
