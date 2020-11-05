a=0
s=0
ori=0
n=int(input("dati numarul: "))
while ori<n:
    ori+=1
    s=ori+a
    a=s
print("suma este",s)

b=1
p=0
ori=0
while ori<n:
    ori+=1
    p=ori*b
    b=p
print("produsul este",p)
print("media este",s/n)