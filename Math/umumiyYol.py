v=float(input('Qayiq tezligini kiriting (metr/sekun): '))
u=float(input('Oqim tezligini kiriting (metr/sekun):'))
t1=float(input('Ko\'ldagi vaqtni kiriting (sekun): '))
t2=float(input('Oqim bo\'yicha vaqtni kiriting (sekun):'))
print('Oqim bo\'yicha masofa (metr) S= ',v*t1+(v-u)*t2)
print('Oqimga qarshi masofa  (metr) S= ',v*t1+(v+u)*t2)