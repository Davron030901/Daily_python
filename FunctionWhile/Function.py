def summa(a):
    sum=0
    b=0
    while b<=a:
        sum+=b
        b+=1
    print(f"Sum {sum}")
num=int(input("Sum all numbers from 0 to given number:"))
summa(num)