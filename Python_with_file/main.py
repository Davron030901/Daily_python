with open("my_file.txt") as file:
    contents=file.read()
    print(contents)

with open("my_file.txt",mode="a") as file:
    file.write("\nNew text")
#
with open("../../OneDrive/Рабочий стол/C#/new_file.txt") as file:
    print(file.read())

