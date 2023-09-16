import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assuming trade_data.csv is your dataset file)
df = pd.read_csv('trade_data.csv')

# Calculate mean for specific columns
mean_export = df['Export (US$ Thousand)'].mean()
mean_import = df['Import (US$ Thousand)'].mean()

# Calculate median for specific columns
median_export = df['Export (US$ Thousand)'].median()
median_import = df['Import (US$ Thousand)'].median()

# Calculate standard deviation for specific columns
std_export = df['Export (US$ Thousand)'].std()
std_import = df['Import (US$ Thousand)'].std()

# Display the results
print("Statistics for Export (US$ Thousand):")
print(f"Mean: {mean_export}")
print(f"Median: {median_export}")
print(f"Standard Deviation: {std_export}")

print("\nStatistics for Import (US$ Thousand):")
print(f"Mean: {mean_import}")
print(f"Median: {median_import}")
print(f"Standard Deviation: {std_import}")

# Create a histogram for export values
plt.hist(df['Export (US$ Thousand)'], bins=20, edgecolor='k')
plt.title('Export Values Distribution')
plt.xlabel('Export (US$ Thousand)')
plt.ylabel('Frequency')
plt.show()

# Create a histogram for import values
plt.hist(df['Import (US$ Thousand)'], bins=20, edgecolor='k')
plt.title('Import Values Distribution')
plt.xlabel('Import (US$ Thousand)')
plt.ylabel('Frequency')
plt.show()

# Calculate the correlation between "Export (US$ Thousand)" and "Import (US$ Thousand)" columns
correlation = df['Export (US$ Thousand)'].corr(df['Import (US$ Thousand)'])

# Display the correlation coefficient
print(f"Correlation between Export and Import: {correlation}")

# Create a scatter plot to visualize the relationship
plt.scatter(df['Export (US$ Thousand)'], df['Import (US$ Thousand)'])
plt.title('Scatter Plot: Export vs. Import')
plt.xlabel('Export (US$ Thousand)')
plt.ylabel('Import (US$ Thousand)')
plt.show()