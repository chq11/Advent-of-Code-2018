import numpy as np
from scipy.special import comb

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

f = open('d2.txt','r')
lines = f.readlines()
num = len(lines)
f.close()

comb_list = np.zeros([int(comb(num,2)),2], np.int16)
k = 0
for i in range(num-1):
    j = i+1
    while j < num:
        comb_list[k,:] = [i,j]
        j += 1
        k += 1

for i in range(int(comb(num,2))):
    line_1 = lines[comb_list[i, 0]]
    line_2 = lines[comb_list[i, 1]]
    c = 0
    for j in range(26):
        if line_1[j] != line_2[j]:
            c += 1
    if c == 1:
        print(line_1)
        print(line_2)


# ed_comb = np.zeros(int(comb(num,2)))
# print(ed_comb)
    # print(list(resu.keys())[1])