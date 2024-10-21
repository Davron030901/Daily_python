'''n o‘lchamli butun tipli massiv berilgan, hamma elementlari(o‘sish yoki kamayish bo‘yicha)
tartiblangan. Faqat toq indeksdagi elementlari chop etilsin. '''
n=int(input('element sonini kiriting:'))
g=[i for i in range(n)]
for j in range(0,len(g),2):
    print(j,end=' ')