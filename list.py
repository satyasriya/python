#[12,42,23,96,7,18,10,133]
#add min and max
l=[12,42,23,96,7,18,10,133]
list=[]
for i in l:
    if l[i]<l[i+1]:
        list = l[i]
    else:
        list = l[i+1]
print(list)
