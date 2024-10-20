# import pandas
# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] !="temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#
import pandas

# data=pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(type(data))
# print(data["temp"])
# data_dict=data.to_dict()
# print(data_dict)  # column dictionary

# temp_list=data["temp"].to_list()   #temp list
# print(len(temp_list))
# sum=0
# for i in temp_list:
#     sum=sum+i
# print(sum)
# average=sum(data["temp"])/len(data["temp"])
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in columns
# print(data["condition"])
# print(data.condition)
#
# #Get Data in Row
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])
#
# monday = data[data.day=='Monday']
# monday_temp=monday.temp[0]
# monday_temp_F=monday_temp*9/5+32
# print(monday_temp_F) #Fahrenheit


#Create a dataframe from scratch
# data_dict={
#     "students":["Amy","James","Angela"],
#     "scores":[76,56,65]
# }
# data=pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("nev_data.csv")  #csv Write
# data.to_csv("new_txt_data.txt") #txt Writeite
# data_way={
#     "Fur":[0,1,2],
#     "Color":["grey","red","black"],
#     "Count":[2473,392,103]
# }
# data=pandas.DataFrame(data_way)
# data.to_csv("squirrel_count.csv")

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240308.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count],
}
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")