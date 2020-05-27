import numpy as np
from collections import Counter

f = open('d_3.txt', 'r')
lines = f.readlines()
claim = np.zeros([len(lines), 5], np.int16)
for i in range(len(lines)):
    line = lines[i].strip().split()
    claim[i][0] = int(line[0].strip('#'))
    claim[i][1] = int(line[2].strip(':').split(',')[0])
    claim[i][2] = int(line[2].strip(':').split(',')[1])
    claim[i][3] = int(line[3].split('x')[0])
    claim[i][4] = int(line[3].split('x')[1])

print(np.max(claim[:,1] + claim[:,3]), np.min(claim[:,1] + claim[:,3])) # 16<colum<999
print(np.max(claim[:,2] + claim[:,4]), np.min(claim[:,2] + claim[:,4])) # 14<row<999

area = np.zeros([1000, 1000])

for i in range(len(lines)):
    for row in range(claim[i][4]):
        for col in range(claim[i][3]):
            area[claim[i][2] + row][claim[i][1] + col] += 1

print(np.sum(area))
area[area < 2] = 0
area[area > 0] = 1
print(np.sum(area))