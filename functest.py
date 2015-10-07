#coding:utf-8

a = [1,2,3,4]
b = []
c = []

def func(a,b,c):
    b.append(a.pop())
    return

print a
print b
func(a,b,c)
print a
print b
func(a,b,c)
print a
print b
