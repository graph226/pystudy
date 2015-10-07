num=[]
for i in range(2,1000):
    num.append(i)

for i in num:
    j = 2
    while i*j<1000:
        if i*j in num:
            num.remove(i*j)
        j = j+1

print num


