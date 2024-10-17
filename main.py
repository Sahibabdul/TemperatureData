import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file with Temperature and Humidity data
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Ensure the columns are named correctly
print(data.head())  # Optional: view the first few rows

# Convert 'Time' to datetime format for better analysis
data['Time'] = pd.to_datetime(data['Time'], unit='s')

# Calculate the Pearson correlation between Temperature and Humidity
correlation = data['Temperature'].corr(data['Humidity'])
print(f'Pearson correlation coefficient between Temperature and Humidity: {correlation}')

# Create a subplot with two graphs
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# First graph: Temperature and Humidity over Time
axs[0].plot(data['Time'], data['Temperature'], color='b', label='Temperature (°C)')
axs[0].plot(data['Time'], data['Humidity'], color='r', label='Humidity (%)', linestyle='--')

# Add labels and legends for the first graph
axs[0].set_title('Temperature and Humidity Over Time')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Value')
axs[0].legend()
axs[0].grid(True)

# Second graph: Scatter plot for Temperature vs Humidity
axs[1].scatter(data['Temperature'], data['Humidity'], color='blue', alpha=0.5, label='Data')

# Fit a linear regression line for temperature vs humidity using NumPy polyfit
coeffs = np.polyfit(data['Temperature'], data['Humidity'], 1)
fit_line = np.polyval(coeffs, data['Temperature'])
axs[1].plot(data['Temperature'], fit_line, color='red', label='Linear Fit')

# Add labels and legends for the second graph
axs[1].set_title('Scatter Plot: Temperature vs Humidity with Linear Fit')
axs[1].set_xlabel('Temperature (°C)')
axs[1].set_ylabel('Humidity (%)')
axs[1].legend()
axs[1].grid(True)

# Automatically adjust layout to prevent overlap
plt.tight_layout()
plt.show()
