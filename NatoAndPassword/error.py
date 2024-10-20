# # FileNotFound
# # with open('a_file.text') as file:
# #     file.read()
#
# #KeyError
# # a_dictionary={"key":"value"}
# # value=a_dictionary["non_existent_key"]
#
# # IndexError
# # fruit_list = ["apple", "banana", "pear"]
# # fruit=fruit_list[3]
#
# # TypeError
# # text="abc"
# # print(text+5)
#
# try:
#     file=open('a_file.text')
#     a_dictionary={"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file=open('a_file.text','w')
#     file.write('Something')
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist.')
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")
#     # file.close()
#     # print('File was closed')

# height=float(input("Enter height: "))
# weight=float(input("Enter weight: "))
#
# if height>3:
#     raise ValueError("Height is greater than or equal to 3")
# bmi=weight/height**2
# print(bmi)

# # IndexError
# fruits=eval(input("Enter the fruits: "))
# # ["apple","pear","orange"]
# def make_pie(index):
#     try:
#         fruit=fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit+"pie")

# make_pie(1)5

# KeyError
#eval() function will create a list of dictionaries using th
facebook_posts=eval(input("Enter the facebook: "))

total_likes=0
# TODO:Catch the KeyError exception
for post in facebook_posts:
    total_likes=total_likes+post["Likes"]
# [{'Likes':21,'Comments':2},{'share':13,'Comments':2},{'Likes':21,'Comments':1,"share":1}]
print(total_likes)
