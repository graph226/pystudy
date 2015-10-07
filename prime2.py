num=[]
for i in range(2,1000):
    num.append(i)

for i in num:
    for j in num:
        if i*j in num:
            num.remove(i*j)

print num
