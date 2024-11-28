# Import libraries
import pandas as pd

# Create a DataFrame with missing values
data = {'Country': ['USA', 'UK', 'Canada', None],
        'GDP': [21.43, 2.83, 1.74, 0.3]}
df = pd.DataFrame(data)

# Clean missing values by removing rows with missing 'Country'
df_cleaned = df.dropna(subset=['Country'])

# Sort by GDP in descending order
df_sorted = df_cleaned.sort_values('GDP', ascending=False)

# Print cleaned and sorted DataFrame
print("Cleaned and Sorted DataFrame:")
print(df_sorted)

# Calculate the total GDP
total_gdp = df_cleaned['GDP'].sum()

# Print total GDP
print("\nTotal GDP:")
print(total_gdp)
