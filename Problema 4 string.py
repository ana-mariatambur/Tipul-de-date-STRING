a=str(input("primul cuvant:"))
b=str(input("al doilea cuvant:"))
c=str(input("al treilea cuvant:"))
d=str(input("al patrulea cuvant:"))
m=str(a)
l=str(b)
p=str(c)
r=str(d)
n=0
if(((len(m))>=3)and((len(l))>=3)and((len(p))>=3)):
    n=(len(p))/2
    i=int(n)
    j=m[:2]
    k=l[0]
    h=p[:3]
    g=r[:i]
    print(a,b,c,d,sep="")
    print(str(j)+str(k)+str(h)+str(g))
else:
    print("nu corespunde conditiei")