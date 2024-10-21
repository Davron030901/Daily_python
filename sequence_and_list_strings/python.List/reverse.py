n=int(input("list element sonini kiriting:"))
l=[2*i-1 for i in range(n,1,-1)]
l.reverse()
print(l)
print(list(reversed(l)))
print(l[::-1])