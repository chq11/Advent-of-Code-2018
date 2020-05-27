import numpy as np

f = open('number.txt', 'r')
lines = f.readlines()
time_list = np.zeros([len(lines), 5], np.int16)
ID = []

for i in range(len(lines)):
    time_list[i][0] = int(lines[i].split()[0].strip('[').split('-')[1])
    time_list[i][1] = int(lines[i].split()[0].strip('[').split('-')[2])
    time_list[i][2] = int(lines[i].split()[1].strip(']').split(':')[0])
    time_list[i][3] = int(lines[i].split()[1].strip(']').split(':')[1])
    if lines[i].split()[3][0] == '#':
        time_list[i][4] = int(lines[i].split()[3].strip('#'))
        if int(lines[i].split()[3].strip('#')) not in ID:
            ID.append(int(lines[i].split()[3].strip('#')))
    elif lines[i].split()[3][0] == 'a':
        time_list[i][4] = 0
    elif lines[i].split()[3][0] == 'u':
        time_list[i][4] = 1
    else:
        print('error!')

sav = np.zeros([1, 5], np.int16)
for i in range(len(lines)):
    for ind_r in range(len(lines) - 1 - i):
        ind = len(lines) - 1 - ind_r
        if time_list[ind][0] < time_list[ind - 1][0]:
            sav[0] = time_list[ind - 1]
            time_list[ind - 1] = time_list[ind]
            time_list[ind] = sav[0]
        elif time_list[ind][0] == time_list[ind - 1][0]:
            if time_list[ind][1] < time_list[ind - 1][1]:
                sav[0] = time_list[ind - 1]
                time_list[ind - 1] = time_list[ind]
                time_list[ind] = sav[0]
            elif time_list[ind][1] == time_list[ind - 1][1]:
                if time_list[ind][2] < time_list[ind - 1][2]:
                    sav[0] = time_list[ind - 1]
                    time_list[ind - 1] = time_list[ind]
                    time_list[ind] = sav[0]
                elif time_list[ind][2] == time_list[ind - 1][2]:
                    if time_list[ind][3] < time_list[ind - 1][3]:
                        sav[0] = time_list[ind - 1]
                        time_list[ind - 1] = time_list[ind]
                        time_list[ind] = sav[0]
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass

records = np.zeros([int(len(ID)), 60])
i = 0
guard_id = 0
while i < len(lines):
    if time_list[i][4] > 1:
        guard_id = time_list[i][4]
    elif time_list[i][4] == 0:
        id_index = 0
        while id_index < int(len(ID)):
            if ID[id_index] == guard_id:
                for j in range(time_list[i][3], time_list[i + 1][3]):
                    records[id_index][j] += 1
                id_index = int(len(ID))
            id_index += 1
        i += 1
    else:
        print('error')
    i += 1

print(ID[int(np.argmax(np.max(records, 1)))] * np.argmax(records[int(np.argmax(np.max(records, 1)))]))

