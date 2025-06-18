import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt
print("Welcome to the Sitka Weather Viewer!")
print("Choose to see the high temperatures, low temperatures, or exit the program!")
print("Choose Highs, Lows, or Exit!")
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
           
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            continue
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
while True:
    print("\nMenu:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '2':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '3':
        print("Goodbye!")
        sys.exit()

    else:
        print("Invalid choice.")


