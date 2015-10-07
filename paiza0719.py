# coding: utf-8

def hanoi(m,a,b,c,t):
    tmp = 0
    if m>0:
        hanoi(m-1,a,c,b)
        c.append(a.pop())
        tmp = tmp +1
        if tmp == t:
            return
        hanoi(m-1,b,a,c)
    else:
        return

if __name__ == "__main__":
    n,t = map(int,raw_input().split())
    a = range(n,0,-1)
    b = []
    c = []
    tmp = 0

    hanoi(n,a,b,c,t)
    for row in a,b,c:
        for each in row:
            print each,
