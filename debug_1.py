import numpy as np

f = open('d2.txt','r')
lines = f.readlines()
num = len(lines)

r = []
s = 0

i = 0
while i < num:
    s = s+int(lines[i])
    if s in r:
        print(s)
        break
    r.append(s)
    i += 1
    if i == num:
        i = 0
f.close()