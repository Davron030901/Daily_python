n=int(input("element sonini kiriting:"))
a=int(input("1-hadini kiriting:"))
d=int(input("ayirmasini kiriting:"))
l=[a+(i-1)*d for i in range(1,n+1)]
print(l)