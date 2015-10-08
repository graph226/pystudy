#encoding: utf-8
import math
N =int(raw_input())

cir = []
for i in range(N):
    cir.append(int(raw_input()))

cir.sort()
cir.reverse()


i = 0
tmp = 0
while i<N:
    if i%2==0:
        tmp = tmp + cir[i]**2
    else:
        tmp = tmp - cir[i]**2
    i = i + 1

print tmp*math.pi
