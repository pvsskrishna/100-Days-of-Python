# Method_1 to clean data
'''with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    cleaned_data = []

    for row in data:
        new_row = row.rstrip("\n")
        cleaned_data.append(new_row)

    print(cleaned_data)'''
import pandas

# Method_2 to clean data using csv module
'''import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
        print(row)
    print(temperature)'''

# Method_3 to clean data using Pandas library
'''import pandas as pd
data = pd.read_csv('weather_data.csv')

print(data['temp'])
print(data['temp'].max())  # Extracting the Maximum temparature from the column or series
print(data[data.temp == data.temp.max() ]) # Getting data from a row whose temp is max
print(m_temp_f) # turing the temparature from celcious to Fahrenheit'''


# converting dictionary to dataframe
'''
data_dict = {
    "students":["ram","sita","krishna"],
    "marks":[23,34,56]
             }

new_data = pandas.DataFrame(data_dict)
print(new_data)
print(new_data.to_csv("new_data.csv"))'''

# Cleaning the data from the csv file to get the data of count of suerrels.
# and to generate a csv file from dataframe that we made using pandas.

import pandas
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

primary_color = data["Primary Fur Color"]
gray_squirrels_count = len(data[primary_color == "Gray"])
black_squirrels_count = len(data[primary_color == "Black"])
cinnamon_squirrels_count = len(data[primary_color == "Cinnamon"])

data_dict = {
    "Fur color":["Gray","Black","Cinnamon"],
    "Count": [gray_squirrels_count,black_squirrels_count,cinnamon_squirrels_count]
}

fur_color_dataframe = pandas.DataFrame(data_dict)
print(fur_color_dataframe)
fur_color_dataframe.to_csv("squirrels_count.csv")
