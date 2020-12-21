


l1=[]
x1=36
while x1:
    char1=chr(randint(33,126))
    while l1.count(char1)!=2:
        l1.insert(randint(0,36),char1)
    x1-=1
print(l1)
l2=[]
j=36
while j:
    for i in range(0,6):
        l3=[]
        for k in range(0,6):
            i
            l3[k].append(l1[j])
            j-=1
        l2[i].append(l3)
print(l2)