# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list=[]
# for number in numbers:
#     add_1=number+1
#     new_list.append(add_1)
#
# print(new_list)
#
# new_lists=[n+1 for n in numbers]
# print(new_lists)

# name="Angela"
# new_list=[letter for letter in name]
# print(new_list)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# squared_numbers = [num*num for num in numbers]
# print(squared_numbers)

# list_of_strings=input().split(",")
# print(list_of_strings)

# list_of_strings=input().split(",")
# numbers=[int(x) for x in list_of_strings]
# print(numbers)
# result=[num for num in numbers if num%2==0]
# print(result)

# import pandas
# import csv
#
# data=pandas.DataFrame()
# data.to_csv("file1.csv")
# data.to_csv("file2.csv")

with open("file1.csv") as file1:
    list1=file1.readlines()

with open("file2.csv") as file2:
    list2=file2.readlines()

result=[int(num) for num in list1 if num in list2]
print(result)