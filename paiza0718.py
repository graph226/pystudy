# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
number = int(raw_input())
list_raw=[raw_input() for _ in range(number)]
list_spl=[]

for n in list_raw:
    n = n.rstrip('X')
    list_spl.append([int(x) for x in list(str(n))])


list_ans=[]
for each in list_spl:
    bar = 0
    for i in range(len(each)):
        if i%2==0 :
            tmp = each[i]*2
            tmp = tmp/10 + tmp%10
            bar = bar + tmp
        else:
            bar = bar + each[i]
    list_ans.append(bar)

for i in range(number):
    list_ans[i] = 10 - list_ans[i]%10

for n in list_ans:
    n = n%10
    print n
