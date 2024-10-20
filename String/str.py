str1=input("Enter first text:")
num1=int(input("Enter first number: "))
str2=input("Enter second text:")
num2=int(input("Enter second number: "))
str=""
# Enter a string. The first n1 characters of the string should be s1 from the beginning of the line, and the last n2 characters should be s2 from the end of the line.
if len(str1)>num1 and len(str2)>num2:
    str=str1[0:num1]+str2[(len(str2)-num2):len(str2)]
    print(str)
else:
    print("The value was entered incorrectly! (the length of the text should be greater than the number)")