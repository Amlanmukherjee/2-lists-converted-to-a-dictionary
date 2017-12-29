num_1=input('enter number of elements you want to enter')
list_1=[]
list_2=[]
dict_1={}
num_2=int(num_1)
print('enter element for list 1:::')
for j in range(0,num_2):
    input_1=input('enter element')
    list_1.append(input_1)
print('enter element for list 2:::')
for k in range(0,num_2):
    input_2=input('enter element')
    list_2.append(input_2)

for i in range(0,num_2):
    
    dict_1[list_1[i]]=list_2[i]
print('your dictionary is:::',dict_1)    
