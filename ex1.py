# Import libraries
import pandas as pd

# Create a DataFrame
data = {'Product': ['A', 'B', 'C'], 'Sales': [100, 200, 300]}
df = pd.DataFrame(data)

# Add a "Profit" column
# For simplicity, let's assume Profit is 20% of Sales
df['Profit'] = df['Sales'] * 0.2

# Print DataFrame with Profit
print("DataFrame with Profit:")
print(df)

# Sort by Profit
df_sorted_by_profit = df.sort_values('Profit', ascending=False)
print("\nDataFrame Sorted by Profit:")
print(df_sorted_by_profit)
