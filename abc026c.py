# coding: utf-8

N = int(raw_input())

salary = {}
sub = {}

for i in range(N):
    sub[i+1] = []   //社員番号は1から始まる

for i in range(1,N):
    sub[int(raw_input())].append(i+1)

for i in range(N):
    if len(sub[i+1])==0:
        salary[i+1] = 1
    else:
        salary[i+1] = 0

for i in range(N, 1, -1):
    if salary[i] == 0:
        salary[i] = max(salary[j] for j in sub[i]) + 
