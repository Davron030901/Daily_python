
'''Berilgan k butun musbat sondagi raqamlar miqdorini aniqlovchi butun tipli Digit Count(k)
funksiyasi tasvirlansin. Bu funksiyadan foydalanib berilgan 5 ta musbat butun sonning har biri
uchun raqamlari soni aniqlansin.
12 1 36 121 5-----2 1 2 3 1'''
def Digit_Count(k):
    count=0
    while k!=0:
        k=k//10
        count+=1
    return count
for i in range(5):
    print(Digit_Count(int(input(f'Natural {i+1}sonni kiriting k>0 :'))))