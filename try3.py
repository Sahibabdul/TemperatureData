import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Load the CSV file with Temperature, Humidity, and Unix Time data
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Convert 'Time' from Unix timestamp to datetime format
data['Time'] = pd.to_datetime(data['Time'], unit='s')

# Normalize the 'Time' column to use as color in the scatter plot
norm = plt.Normalize(data['Time'].min().timestamp(), data['Time'].max().timestamp())

# Calculate the Pearson correlation between Temperature and Humidity
correlation = data['Temperature'].corr(data['Humidity'])
print(f'Pearson correlation coefficient between Temperature and Humidity: {correlation}')

# Create a subplot with two graphs
fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# First graph: Temperature and Humidity over Time
axs[0].plot(data['Time'], data['Temperature'], color='b', label='Temperature (°C)')
axs[0].plot(data['Time'], data['Humidity'], color='r', label='Humidity (%)', linestyle='--')

# Add labels and legends for the first graph
axs[0].set_title('Temperature and Humidity Over Time')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Value')
axs[0].legend()
axs[0].grid(True)

# Sort the data by time for proper line plotting
sorted_data = data.sort_values('Time')

# Second graph: Scatter plot for Temperature vs Humidity, colored by Time
scatter = axs[1].scatter(sorted_data['Temperature'], sorted_data['Humidity'], 
                        c=sorted_data['Time'].apply(lambda x: x.timestamp()), cmap='viridis', alpha=0.7)

# Connect the dots by time with a line plot
axs[1].plot(sorted_data['Temperature'], sorted_data['Humidity'], color='gray', linestyle='-', alpha=0.5)



# Add labels and legends for the second graph
axs[1].set_title('Scatter Plot: Temperature vs Humidity with Color by Time and Connected Line')
axs[1].set_xlabel('Temperature (°C)')
axs[1].set_ylabel('Humidity (%)')
axs[1].legend()
axs[1].grid(True)

# Add colorbar to indicate the time
cbar = plt.colorbar(scatter, ax=axs[1], orientation='vertical', label='Timestamp (Time)')
cbar.set_label('Time', rotation=270, labelpad=15)

# Automatically adjust layout to prevent overlap
plt.tight_layout()
plt.show()
