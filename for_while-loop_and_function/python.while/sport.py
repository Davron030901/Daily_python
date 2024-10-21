'''Sportchi mashg‘ulotni boshladi. U 1-kun 10 km masofani bosib o‘tdi. Keyingi har kun bosib
o‘tilgan yo‘l uzunligi oldingi kun bosib o‘tilgan yo‘ldan p foiz oshirildi. (p haqiqiy son. 0<p<50)
p berilgan bo‘lsa, necha kundan keyin jami bosib o‘tilgan masofa 40 kmdan oshishi aniqlansin va
o‘tgan kunlar soni k hamda jami bosib o‘tilgan masofa S hisoblansin.
40.0 3 43.6'''
s=10
p=float(input('Qo\'yilma foizini kiriting: '))
k,S=0,0
while S<40:
    S+=s
    s+=s*p/100
    k+=1
print(k,' ',S)