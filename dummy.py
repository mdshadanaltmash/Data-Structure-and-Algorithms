import numpy as np
import pandas as pd

# Sample DataFrame
data = {
    'date_column1': [20190130.0, 20190131.0, np.nan, 20190201.0],
    'date_column2': [20190202.0, np.nan, 20190203.0, 20190204.0]
}

df = pd.DataFrame(data)
print(df.dtypes)
# Convert each date column to datetime format
for col in df.columns:
    # Convert float values to strings, remove the decimal point, and convert to datetime
    df[col] = pd.to_datetime(df[col].astype(str).str.split('.').str[0], format='%Y%m%d', errors='coerce')

print(df)
