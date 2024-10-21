a,b=int(input("Enter box width number: ")),int(input('Enter box height number: '))
print(a>0 and a<9 and b>0 and b<9 and ((a%2==1 and b%2==1) or (a%2==0 and b%2==0)))