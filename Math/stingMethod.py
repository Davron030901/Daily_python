# a="Hello"+" "+"World"
# print(a)
# ism=input("ismingizni kiriting:")
# a='Salom '
# s=a+ism
# print(f"""{ism}
#
#
#  {a}""")
# a='Salom dunyo'
# print(len(a))
# print(a[::-1])
# print(a[::-2])
# print(a[::-3])
# print(a[::1])
# print(a[::2])
# print(a[::3])
# s=input("id: ")
# if s.isdigit():
#     print("Siz keyingi etabga o'tdingiz")
# else:
#     print("Siz idga raqam kiritmadingiz:")

# print(s.sdigit())i
import datetime
day=int(input("Tug'ilgan kuningizni kiriting:"))
month=int(input("Tug'ilgan oyingizni kiriting:"))
year=int(input("Tug'ilgan yilingizni kiriting:"))
birth=datetime.datetime(year=year,month=month,day=day)

now=datetime.datetime.now()
differense=now-birth
d=differense.days
y=d//365
y1=d-y*365
m=y1//30
m1=y1-m*30
h=m1//7
h1=m1-h*7
print(f"{h} hafta {h1}kun")
print(f"{m} oy {m1}kun")


# print(differense)
# print(d)