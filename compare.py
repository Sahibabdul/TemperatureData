# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have your datasets loaded into pandas DataFrames named 'df1' and 'df2'
df1 = pd.read_csv('data (3).csv')
df2 = pd.read_csv('data.csv')  # The second, shorter dataset

# If you have Unix timestamps, we need to convert them to human-readable datetime
df1['Time'] = pd.to_datetime(df1['Time'], unit='s')
df2['Time'] = pd.to_datetime(df2['Time'], unit='s')

# Set timestamp as index for easy time-based plotting
df1.set_index('Time', inplace=True)
df2.set_index('Time', inplace=True)

# 1. Time Series Plot for Temperature and Humidity (Comparison)
plt.figure(figsize=(12, 6))

# Plot original dataset (df1)
plt.plot(df1.index, df1['Temperature'], label='Temperature (Original) (°C)', color='r')
plt.plot(df1.index, df1['Humidity'], label='Humidity (Original) (%)', color='b')

# Plot shorter dataset (df2)
plt.plot(df2.index, df2['Temperature'], label='Temperature (Short) (°C)', color='orange', linestyle='--')
plt.plot(df2.index, df2['Humidity'], label='Humidity (Short) (%)', color='green', linestyle='--')

plt.title('Temperature and Humidity Over Time (Comparison)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

# 2. Histogram for Temperature and Humidity (Comparison)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(df1['Temperature'], bins=30, color='red', alpha=0.5, label='Original')
plt.hist(df2['Temperature'], bins=30, color='orange', alpha=0.5, label='Short')
plt.title('Temperature Distribution (Comparison)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(df1['Humidity'], bins=30, color='blue', alpha=0.5, label='Original')
plt.hist(df2['Humidity'], bins=30, color='lightblue', alpha=0.5, label='Short')
plt.title('Humidity Distribution (Comparison)')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()

# 3. Scatter Plot of Temperature vs Humidity (Comparison)
plt.figure(figsize=(8, 6))

plt.scatter(df1['Temperature'], df1['Humidity'], color='green', alpha=0.5, label='Original')
plt.scatter(df2['Temperature'], df2['Humidity'], color='purple', alpha=0.5, label='Short', marker='x')
plt.title('Temperature vs Humidity (Comparison)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.legend()
plt.show()

# 4. Correlation Heatmap (Comparison)
plt.figure(figsize=(12, 5))

# Correlation heatmap for original dataset (df1)
plt.subplot(1, 2, 1)
sns.heatmap(df1[['Temperature', 'Humidity']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap (Original)')

# Correlation heatmap for shorter dataset (df2)
plt.subplot(1, 2, 2)
sns.heatmap(df2[['Temperature', 'Humidity']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap (Short)')

plt.tight_layout()
plt.show()

# 5. Boxplot for Temperature and Humidity (Comparison)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data=[df1['Temperature'], df2['Temperature']], palette=['orange', 'purple'])
plt.xticks([0, 1], ['Original', 'Short'])
plt.title('Boxplot for Temperature (Comparison)')

plt.subplot(1, 2, 2)
sns.boxplot(data=[df1['Humidity'], df2['Humidity']], palette=['lightblue', 'lightgreen'])
plt.xticks([0, 1], ['Original', 'Short'])
plt.title('Boxplot for Humidity (Comparison)')

plt.tight_layout()
plt.show()
