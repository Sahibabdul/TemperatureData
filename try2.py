# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have your dataset loaded into a pandas DataFrame named 'df'
df = pd.read_csv('data.csv')

# If you have Unix timestamps, we need to convert them to human-readable datetime
df['Time'] = pd.to_datetime(df['Time'], unit='s')

# Set timestamp as index for easy time-based plotting
df.set_index('Time', inplace=True)

# 1. Time Series Plot for Temperature and Humidity
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Temperature'], label='Temperature (°C)', color='r')
plt.plot(df.index, df['Humidity'], label='Humidity (%)', color='b')
plt.title('Temperature and Humidity Over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

# 2. Histogram for Temperature and Humidity
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(df['Temperature'], bins=30, color='red', alpha=0.7)
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(df['Humidity'], bins=30, color='blue', alpha=0.7)
plt.title('Humidity Distribution')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# 3. Scatter Plot of Temperature vs Humidity
plt.figure(figsize=(8, 6))
plt.scatter(df['Temperature'], df['Humidity'], color='green', alpha=0.5)
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(df[['Temperature', 'Humidity']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 5. Boxplot for Temperature and Humidity
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['Temperature'], color='orange')
plt.title('Boxplot for Temperature')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Humidity'], color='lightblue')
plt.title('Boxplot for Humidity')

plt.tight_layout()
plt.show()

