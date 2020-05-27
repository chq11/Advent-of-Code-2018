import numpy as np

init_state = '#.##.#.##..#.#...##...#......##..#..###..##..#.#.....##..###...#.#..#...######...#####..##....#..###'
init_s = np.zeros([len(init_state)], np.int8)
for i in range(len(init_state)):
    if init_state[i] == '#':
        init_s[i] = 1
    else:
        init_s[i] = 0

l_m = 0
r_m = 0
if np.sum(init_s[0:5]) > 0:
    new_init_s = np.zeros([np.shape(init_s)[0] + 4])
    new_init_s[4:] = init_s
    init_s = new_init_s
    l_m += 1
if np.sum(init_s[-5:]) > 0:
    new_init_s = np.zeros([np.shape(init_s)[0] + 4])
    new_init_s[:-4] = init_s
    init_s = new_init_s
    r_m += 1

f = open('d_12.txt', 'r')
lines = f.readlines()
c_d_1 = np.zeros([len(lines), 5], np.int8)
c_d_2 = np.zeros([len(lines)], np.int8)
for i in range(len(lines)):
    for j in range(5):
        if lines[i][j] == '#':
            c_d_1[i][j] = 1
        else:
            c_d_1[i][j] = 0
    if lines[i][-2] == '#':
        c_d_2[i] = 1
    else:
        c_d_2[i] = 0

same = 0
nane_o = 0
sum_o = 0
g_i = 0
while g_i < 50000000000:
    g_s = np.zeros([np.shape(init_s)[0]])
    for i in range(np.shape(init_s)[0] - 4):
        c_str = init_s[i:(i + 5)]
        j = 0
        while j < 32:
            if np.sum(c_str == c_d_1[j]) == 5:
                g_s[i + 2] = c_d_2[j]
                j = len(lines)
            j += 1
    init_s = g_s
    if np.sum(init_s[0:5]) > 0:
        new_init_s = np.zeros([np.shape(init_s)[0] + 4])
        new_init_s[4:] = init_s
        init_s = new_init_s
        l_m += 1
    if np.sum(init_s[-5:]) > 0:
        new_init_s = np.zeros([np.shape(init_s)[0] + 4])
        new_init_s[:-4] = init_s
        init_s = new_init_s
        r_m += 1

    sum_n = 0
    for i in range(len(init_state) + 4 * (r_m + l_m)):
        sum_n += init_s[i] * (i - 4 * l_m)

    nane_n = sum_n - sum_o
    if nane_o != nane_n:
        sum_o = sum_n
        nane_o = nane_n
        same = 0
    else:
        sum_o = sum_n
        same += 1
    if same == 20:
        l_sum = (50000000000 - g_i + 1)*nane_n + sum_o
        g_i = 50000000000

    g_i += 1
print(l_sum)