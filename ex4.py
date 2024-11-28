# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Extract the features for the scatter plot
x = df['sepal length (cm)']
y = df['sepal width (cm)']

# Create the scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', alpha=0.7, edgecolors='k')

# Add title and axis labels
plt.title('Scatter Plot of Sepal Length vs Sepal Width', fontsize=14)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Sepal Width (cm)', fontsize=12)

# Display the plot
plt.grid(True)
plt.show()
