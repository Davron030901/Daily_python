str=input("Enter text:")
num=int(input("Enter number: "))

alnum=True
if len(str)>=num:
    print(str[0:num])
else:
    while alnum:
        str=str+"."
        if len(str)==num:
            alnum=False
    print(str)