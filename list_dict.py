num=input('enter number of elements you want to enter')
a=[]
b=[]
c={}
d=int(num)
print('enter element for list 1:::')
for j in range(0,d):
    e=input('enter element')
    a.append(e)
print('enter element for list 2:::')
for k in range(0,d):
    f=input('enter element')
    b.append(f)

for i in range(0,d):
    
    c[a[i]]=b[i]
print('your dictionary is:::',c)    
