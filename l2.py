#[-1,42,65,1,-4,6] writee a prog to find the secind smallest neg no from the list without buid in functions
l=[22,-1,42,65,1,-4,6]
a=999
b=999
for i in l:
    if a>i:
        b=a
        a=i
    elif b>i and b>a:
        b=i
print(b)
