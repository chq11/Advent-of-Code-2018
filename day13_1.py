import numpy as np

def crossroad(car_n):
    if car_n[2] == 2:
        if car_n[3] == 1:
            return car_n[0], car_n[1] - 1, 4, 2
        elif car_n[3] == 2:
            return car_n[0] - 1, car_n[1], 2, 3
        elif car_n[3] == 3:
            return car_n[0], car_n[1] + 1, 6, 1
        else:
            print('crossroad error2')
    elif car_n[2] == 8:
        if car_n[3] == 1:
            return car_n[0], car_n[1] + 1, 6, 2
        elif car_n[3] == 2:
            return car_n[0] + 1, car_n[1], 8, 3
        elif car_n[3] == 3:
            return car_n[0], car_n[1] - 1, 4, 1
        else:
            print('crossroad error8')
    elif car_n[2] == 4:
        if car_n[3] == 1:
            return car_n[0] + 1, car_n[1], 8, 2
        elif car_n[3] == 2:
            return car_n[0], car_n[1] - 1, 4, 3
        elif car_n[3] == 3:
            return car_n[0] - 1, car_n[1], 2, 1
        else:
            print('crossroad error4')
    elif car_n[2] == 6:
        if car_n[3] == 1:
            return car_n[0] - 1, car_n[1], 2, 2
        elif car_n[3] == 2:
            return car_n[0], car_n[1] + 1, 6, 3
        elif car_n[3] == 3:
            return car_n[0] + 1, car_n[1], 8, 1
        else:
            print('crossroad error6')
    else:
        print('crossroad error')

def car_move(car_i):
    if amap[car_i[0], car_i[1]] == 1:
        if car_i[2] == 4:
            return car_i[0], car_i[1] - 1, 4, car_i[3]
        elif car_i[2] == 6:
            return car_i[0], car_i[1] + 1, 6, car_i[3]
        else:
            print('car move error1')
    elif amap[car_i[0], car_i[1]] == 2:
        if car_i[2] == 2:
            return car_i[0] - 1, car_i[1], 2, car_i[3]
        elif car_i[2] == 8:
            return car_i[0] + 1, car_i[1], 8, car_i[3]
        else:
            print('car move error2')
    elif amap[car_i[0], car_i[1]] == 3:
        if car_i[2] == 2:
            return car_i[0], car_i[1] + 1, 6, car_i[3]
        elif car_i[2] == 8:
            return car_i[0], car_i[1] - 1, 4, car_i[3]
        elif car_i[2] == 4:
            return car_i[0] + 1, car_i[1], 8, car_i[3]
        elif car_i[2] == 6:
            return car_i[0] - 1, car_i[1], 2, car_i[3]
        else:
            print('car move error3')
    elif amap[car_i[0], car_i[1]] == 4:
        if car_i[2] == 2:
            return car_i[0], car_i[1] - 1, 4, car_i[3]
        elif car_i[2] == 8:
            return car_i[0], car_i[1] + 1, 6, car_i[3]
        elif car_i[2] == 4:
            return car_i[0] - 1, car_i[1], 2, car_i[3]
        elif car_i[2] == 6:
            return car_i[0] + 1, car_i[1], 8, car_i[3]
        else:
            print('car move error4')
    elif amap[car_i[0], car_i[1]] == 5:
        return crossroad(car_i)
    else:
        print('car move error')

def sort_car(car_s):
    sav = np.zeros([1, 4], np.int16)
    for i in range(17):
        for ind_r in range(16 - i):
            ind = 16 - ind_r
            if car_s[ind][0] < car_s[ind - 1][0]:
                sav[0] = car_s[ind - 1]
                car_s[ind - 1] = car_s[ind]
                car_s[ind] = sav[0]
            elif car_s[ind][0] > car_s[ind - 1][0]:
                pass
            else:
                if car_s[ind][1] < car_s[ind - 1][1]:
                    sav[0] = car_s[ind - 1]
                    car_s[ind - 1] = car_s[ind]
                    car_s[ind] = sav[0]
                else:
                    pass
    return car_s

def check_car(car_c):
    run = 1
    for ii in range(17):
        k = 1
        while k < 16-ii:
            if car_c[ii][0] == car_c[ii+k][0]:
                if car_c[ii][1] == car_c[ii+k][1]:
                    return 0
            if car_c[ii][0] != car_c[ii+k][0]:
                k = 17
            k += 1

    return run

f = open('d_13.txt', 'r') #shape 150*150, car number:17
lines = f.readlines()

amap = np.zeros([150, 150], np.int8) #0 ,1-,2|,3/,4\,5+
car = np.zeros([17, 4], np.int16) #[y,x,direction,number of '+'], up 2,down 8,left 4,right 6
car[:, 3] = 1
c_i = 0
for y in range(150):
    for x in range(150):
        if lines[y][x] == ' ':
            amap[y, x] = 0
        if lines[y][x] == '-':
            amap[y, x] = 1
        if lines[y][x] == '|':
            amap[y, x] = 2
        if lines[y][x] == '/':
            amap[y, x] = 3
        if lines[y][x] == '\\':
            amap[y, x] = 4
        if lines[y][x] == '+':
            amap[y, x] = 5
        if lines[y][x] == 'v':
            car[c_i] = [y, x, 8, 1]
            amap[y, x] = 2
            c_i += 1
        if lines[y][x] == '>':
            car[c_i] = [y, x, 6, 1]
            amap[y, x] = 1
            c_i += 1
        if lines[y][x] == '^':
            car[c_i] = [y, x, 2, 1]
            amap[y, x] = 2
            c_i += 1
        if lines[y][x] == '<':
            car[c_i] = [y, x, 4, 1]
            amap[y, x] = 1
            c_i += 1

run = 1
while run:
    car = sort_car(car)
    for i in range(17):
        y, x, di, t_n = car_move(car_i=car[i])
        car[i] = [y, x, di, t_n]
        run = check_car(car)
        if run == 0:
            print(x, y)
            break

# car = np.array([
#  [ 87,  69,   6],
#  [ 24,  45,  6],
#  [ 140,  95,  6],
#  [ 45,  36,  8],
#  [ 55,  70,  2],
#  [ 56,  89, 2],
#  [ 61, 124, 2],
#  [ 84,   7, 2],
#  [ 87,  38,  4],
#  [ 87, 134,  8],
#  [ 95, 130,  6],
#  [109,  86, 8],
#  [114, 49,  8],
#  [135, 136,  2],
#  [87, 71,  6],
#  [140, 62, 4],
#  [142,  14,  6]])
# # print(np.argsort(car[:,1]))

# sav = np.zeros([1, 4], np.int16)
# for i in range(17):
#     for ind_r in range(16 - i):
#         ind = 16 - ind_r
#         if car[ind][0] < car[ind - 1][0]:
#             sav[0] = car[ind - 1]
#             car[ind - 1] = car[ind]
#             car[ind] = sav[0]
#         elif car[ind][0] > car[ind - 1][0]:
#             pass
#         else:
#             if car[ind][1] < car[ind - 1][1]:
#                 sav[0] = car[ind - 1]
#                 car[ind - 1] = car[ind]
#                 car[ind] = sav[0]
#             else:
#                 pass