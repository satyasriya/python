l = [12, 42, 23, 96, 7, 18, 10, 133]
maximum = l[0]  
minimum = l[0]
for i in range(1, len(l)):
    if l[i] > maximum:
        maximum = l[i]
        maxi=i

    if l[i] < minimum:
        minimum=l[i]
        mini=i

print(maximum)  
print(minimum)
s=minimum+maximum
d=maximum-minimum
maxi=s
min=d
print(l)
