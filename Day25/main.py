# install pandas sudo apt-get install python3-pandas
# pandas link https://pandas.pydata.org


# with open("Day25/weather_data.csv") as data_file:
#     data= data_file.readlines()
#     print(data)

# import csv

# with open("Day25/weather_data.csv") as data_file:

#     data = csv.reader(data_file) #read csv
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)  # it shows all temperatures in the csv data

import pandas as pd

data = pd.read_csv("Day25/weather_data.csv")

print(type(data))  # get data type

# print(data) # print all data
# print(data["temp"]) # print  temp column
# print(data["day"]) # print day column

# convert data to dictionary {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list() #convert dict to list[12,14,15,14,21,22,24]
print(temp_list)

# avarage = sum(temp_list) / len(temp_list)  get avarage 17.428571428571427
# print(avarage)
print(data["temp"].mean()) # mean also gets avarage 17.428571428571427
print(data["temp"].max()) # max value 24

# Get Columns 
print(data["temp"]) 
print(data.temp) # both of them has same result gets temp column

# Get data in Row
print(data[data.day=="Monday"])

# Get max temp day row
print(data[data.temp==data.temp.max()]) # get max temp row 

#Create a dataframe from scratch
data_dict= {
    "students":["Ali","John","Angela"],
    "ages":[35,24,22]
}

data = pd.DataFrame(data_dict) # create new dataframe
data.to_csv("Day25/created_csv.csv") # to create a csv file use this
print(data)
