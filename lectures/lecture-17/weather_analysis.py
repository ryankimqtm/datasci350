import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Read the weather data
with open('weather_data.txt', 'r') as f:
    lines = f.readlines()

# Skip the header comment
data_str = ''.join(lines[1:])
df = pd.read_csv(StringIO(data_str), sep=r'\s+')

# Print basic statistics
print("Weather Data Analysis:")
print("=====================")
print(f"Number of days: {len(df)}")
print(f"Average high temperature: {df['temp_high'].mean():.1f}°F")
print(f"Average low temperature: {df['temp_low'].mean():.1f}°F")
print(f"Maximum temperature: {df['temp_high'].max():.1f}°F on {df.loc[df['temp_high'].idxmax(), 'date']}")
print(f"Minimum temperature: {df['temp_low'].min():.1f}°F on {df.loc[df['temp_low'].idxmin(), 'date']}")
print(f"Days with precipitation > 1 inch: {len(df[df['precipitation'] > 1])}")

# Create a visualisation
sns.set_style("whitegrid")
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot temperature range on the left axis
ax1.fill_between(df['date'], df['temp_low'], df['temp_high'], alpha=0.3, color='skyblue')
ax1.plot(df['date'], df['temp_high'], marker='o', color='red', label='High Temp')
ax1.plot(df['date'], df['temp_low'], marker='o', color='blue', label='Low Temp')
ax1.set_ylabel('Temperature (°F)')

# Add precipitation as bars on a second axis, on the right
ax2 = ax1.twinx()
ax2.bar(df['date'], df['precipitation'], alpha=0.3, color='navy', width=0.5, label='Precipitation')
ax2.set_ylabel('Precipitation (inches)', color='navy')
ax2.tick_params(axis='y', labelcolor='navy')
ax2.grid(False)

# One legend for both axes, and every fifth date on the x-axis
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
ax1.set_xticks(df['date'][::5])
ax1.tick_params(axis='x', labelrotation=45)
ax1.set_title('30-Day Weather Report: Temperature Range and Precipitation', fontsize=16)
fig.tight_layout()

# Save the figure
fig.savefig('weather_analysis.png')
print("Analysis complete. Results saved to 'weather_analysis.png'")
