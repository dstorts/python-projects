# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)

import pandas
#
# data = pandas.read_csv("weather_data.csv") #create a table object from csv
# #print(data)
# data_dict = data.to_dict() #separate the data object into dictionaries based on columns
# #print(data_dict)
# temp_list = data["temp"].to_list()
# # print(temp_list)
# #temp_avg = sum(temp_list) / len(temp_list)
# #print(temp_avg)
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# #get data in rows
# #print(data[data.day == "Monday"]) #grab row where day is Monday
# #notice how there is a day attribute. pandas creates attributes on the fly, named after the column names from your csv
#
# print(data[data.temp == data.temp.max()])
#
# def convert_c_to_f(c):
#     return (c*(1.8))+32
#
# monday = data[data.day == "Monday"]
# print(convert_c_to_f(int(monday.temp)))
#
# #create dataframe from scratch
#
# internal_data = {
#     'students': ['Alice', 'Kirito', 'Eugeo'],
#     'scores':[91, 79, 88]
# }
#
# my_dataframe = pandas.DataFrame(internal_data)
# my_dataframe.to_csv("new_data.csv")


#grey, cinnamon, black count
squirrel_data = pandas.read_csv("SquirrelConsensus_2018_CentralPark.csv")
fur_grey = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
fur_cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
fur_black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

fur_counts_tuple = {
    'Fur Color': ['Grey', 'Cinnamon', 'Black'],
    'Num of Squirrels': [fur_grey, fur_cinnamon, fur_black]
}

squirrel_furs = pandas.DataFrame(fur_counts_tuple)
squirrel_furs.to_csv("SqirrelColors.csv")