import numpy as np

grid = 9424
ma = np.zeros([300,300])
for i in range(300):
    for j in range(300):
        x = i+1
        y = j+1
        ma[i,j] = int(((x+10)*y + grid) * (x+10)/100)%10-5

max_n = -45
for m_s in range(1,301):
    for i in range(300-m_s+1):
        for j in range(300-m_s+1):
            su_n = 0
            for k in range(m_s):
                for l in range(m_s):
                    su_n = ma[i+k,j+l]+su_n

            if su_n > max_n:
                max_n = su_n
                i_r = i+1
                j_r = j+1
                m_s_r = m_s
    print(m_s)
print(i_r,j_r,m_s_r)