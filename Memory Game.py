


l1=[]
l2=[]
x1=18
count=0
while x1 and len(l1)!=30:
    char1=chr(randint(33,126))
    while l1.count(char1)!=2:
        l1.insert(randint(0,36),char1)
        count+=1
    x1-=1

print(count)
l2=[]
i=0
while i<len(l1):
    l2.append(l1[i:i+6])
    i+=6

for k in l2:
    print(*k)
