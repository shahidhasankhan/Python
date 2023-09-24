# weather_data = []
# with open("weather_data.csv", mode="r") as weather_data_file:
#     data = weather_data_file.readlines()
# for each_data in data:
#     weather_data.append(each_data.strip())

# import csv
# with open("weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperature = []
#     for each_row in data:
#         if each_row[1] != "temp":
#             temperature.append(int(each_row[1]))
# print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["temp"])
# print(data.temp)
# data.info()
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(sum(temp_list)/round(len(temp_list)))
# print(data["temp"].mean())

# print(data["temp"].max())

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
print(data[data.temp == data.temp.max()].day)

# monday_data = data[data.day == "Monday"]
# print(monday_data)
# monday_temp = int(monday_data.temp.get(0))
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# import pandas
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
