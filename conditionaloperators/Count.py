numer1=int(input("Enter number1: "))
numer2=int(input("Enter number2: "))
numer3=int(input("Enter number3: "))
count_p=0
count_m=0
if numer1>0:
    count_p+=1
elif numer1<0:
    count_m+=1
if numer2>0:
    count_p+=1
elif numer2<0:
    count_m+=1
if numer3>0:
    count_p+=1
elif numer3<0:
    count_m+=1
print(f"Plus: {count_p}, Minus: {count_m}")
