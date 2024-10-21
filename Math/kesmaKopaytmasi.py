import math

A=int(input("A="))
B=int(input("B="))
C=int(input("C="))
AC=abs(C-A)
BC=abs(C-B)
AB=abs(A-B)
if(AB==BC+AC):
    print("AC=", AC)
    print("BC=", BC)
    print("AC*BC=", AC * BC)
else:
    print("C nuqta orasida joylashmagan")