p=0
n=0
sp=0
sn=0
t=0
xp=0
xn=0
x=1
while x<=12:
    t=eval(input("dati temperatura:"))
    if t>=0:
        sp+=t
        xp+=1
    else:
        sn+=t
        xn+=1
    x+=1
a=sp/xp
a=float('{:.2f}'.format(a))
b=sn/xn
b=float('{:.2f}'.format(b))
print ("temperatura medie pozitiva este",a)
print ("temperatura medie negativa este",b)

