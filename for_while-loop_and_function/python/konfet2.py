'''1 kg konfetning narxi berilgan. 0,1, 0,2, …, 1 kg konfetning bahosi chiqarilsin.
10 ----1 2 3 4 5 6 7 8 9 10'''
a=float(input('1kg konfet bahosini kiriting kiriting:'))
for i in range(1,11):
    print(f'{i/10}kg konfet {i*a/10}')