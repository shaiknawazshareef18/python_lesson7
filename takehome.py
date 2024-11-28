import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Define dataset size
data_size = 100  # Adjust as needed

# Generate a sample dataset
data = pd.DataFrame({
    'Variable_A': np.random.randn(data_size),        # Normally distributed data
    'Variable_B': np.random.rand(data_size) * 100,   # Uniformly distributed data scaled to 0-100
    'Variable_C': np.random.randint(1, 50, data_size),  # Random integers between 1 and 50
    'Variable_D': np.random.randn(data_size) * 10 + 50, # Normally distributed data with mean 50 and std 10
})

# Display the first few rows of the dataset
print("Sample Dataset:")
print(data.head())

# Create a pairplot of the dataset
sns.pairplot(data, diag_kind='kde', corner=True, plot_kws={'alpha': 0.7})

# Show the plot
plt.show()

# Optionally, save the plot as a PNG file
plt.savefig('pairplot_output.png')
