#coding: UTF-8

f = open("amimedia2nd.txt")
stlines = f.readlines()
f.close()
text = ""

for line in stlines:
    line = line.rstrip()
    text = text + line

f = open("after.txt","w")
f.write(text)
f.close()
