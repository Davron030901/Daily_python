new=["A","B","C","D","E"]
for m in new:
    print(m,end="")


l=["geeks",'for','geeks']
for i in l:
    print(i)

t=("geeks",'for','geeks')
for j in t:
    print(j)

s={1,2,3,4,5,6,}
for k in s:
    print(k)

d=dict()
d["xyz"]=123
d['abs']=345
for z in d:
    print("%s  %d" % (z,d[z]))
for q,w in d.items():
    print(f"{q}:{w}")