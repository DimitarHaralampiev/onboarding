import csv
from datetime import datetime

from matplotlib import pyplot as plt


# Get high temperatures from file.
filename = 'sitka_weather_07-2014.csv'

try:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing_date')
            else:
                dates.append(current_date)
                highs.append(row)
                lows.append(low)

        print(highs)
except FileNotFoundError:
    print(f'File {filename} does not exist')

fig = plt.figure(dpi=128, figsize=(10, 6))

# Plot data.
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = 'Daily high temperature, juli 2014'
plt.title(title, fonsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()