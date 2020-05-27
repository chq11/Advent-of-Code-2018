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
    for i in range(len(car_s)):
        for ind_r in range(len(car_s) - 1 - i):
            ind = len(car_s) - 1 - ind_r
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
    for ii in range(len(car_c)):
        k = 1
        while k < len(car_c) - 1 -ii:
            if car_c[ii][0] == car_c[ii+k][0]:
                if car_c[ii][1] == car_c[ii+k][1]:
                    return ii, ii+k
            if car_c[ii][0] != car_c[ii+k][0]:
                k = len(car_c)
            k += 1

    return

f = open('number.txt', 'r') #shape 150*150, car number:17
lines = f.readlines()

amap = np.zeros([150, 150], np.int8) #0 ,1-,2|,3/,4\,5+
car = np.zeros([17, 4], np.int16) #[y, x, direction, number of '+'], up 2,down 8,left 4,right 6
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
    i = 0
    car_number = len(car)
    while i < car_number:
        y, x, di, t_n = car_move(car_i=car[i])
        car[i] = [y, x, di, t_n]
        loc = check_car(car)
        if loc is not None:
            car = np.delete(car, loc[1], 0)
            car = np.delete(car, loc[0], 0)
            i -= 1
            car_number -= 2
            if car_number == 1:
                print('x:', car[0][1],'y:', car[0][0])
                run = 0
        i += 1
