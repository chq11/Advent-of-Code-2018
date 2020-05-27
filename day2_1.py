import numpy as np

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

f = open('d2.txt','r')
lines = f.readlines()
num = len(lines)
f.close()
all_c = np.zeros([num,2])

for k in range(num):
    resu = all_list(lines[k])
    k_l = len(resu)
    for i in range(k_l):
        if resu[list(resu.keys())[i]] == 2:
            all_c[k, 0] = 1
        if resu[list(resu.keys())[i]] == 3:
            all_c[k, 1] = 1

qq = np.sum(all_c, 0)
print(qq)
en = qq[0]*qq[1]
print(en)
    # print(list(resu.keys())[1])