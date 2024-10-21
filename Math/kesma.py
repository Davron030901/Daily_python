import math

A=int(input("A="))
B=int(input("B="))
C=int(input("C="))
AC=math.fabs(C-A)
BC=math.fabs(C-B)
print("AC=",AC)
print("BC=",BC)
print("AC-BC=",AC+BC)