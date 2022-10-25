import csv
import pandas

data = pandas.read_csv("weather_data.csv")

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temp = int(row[1])
#         temperatures.append(temp)
#    print(temperatures)