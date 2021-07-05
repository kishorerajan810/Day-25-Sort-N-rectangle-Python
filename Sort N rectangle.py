n=int(input("enter :"))
c,d,e,f=[],[],[],[]
for i in range(n):
    a,b=map(int,input("Enter :").split())
    c.append(a)
    d.append(b)
for j in range(n):
    x=c[j]*d[j]
    e.append(x)
    y=(c[j],d[j],e[j])
    f.append(y)
f.sort()
print(f)
