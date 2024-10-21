n = int(input("element sonini kiriting:"))
a = int(input("1-hadini kiriting:"))
b = int(input("2-hadini kiriting:"))
l = [a, b]
[l.append(sum(l)) for _ in range(2, n)]
print(l)