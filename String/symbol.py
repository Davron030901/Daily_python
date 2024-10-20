str1=input("Enter first text:")
str=input("Enter second text:")
num1=input("Enter symbol: ")
text=""
for i in  str1:
    text+=i;
    if num1==i:
        text += str
print(text)

