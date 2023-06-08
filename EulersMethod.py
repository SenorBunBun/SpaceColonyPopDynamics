import numpy as np

def euler_method(f, S_0, t0, tf, h):

    n = int((tf - t0) / h) + 1
    t = np.linspace(t0, tf, n)
    y = np.zeros((n, len(S_0)))
    y[0] = S_0

    for i in range(1, n):
        y[i] = np.add(y[i-1], np.multiply( f(t[i-1], y[i-1]), h) )

    return t, y

def euler_method_table_gen(f, S_0, t0, tf, h, interval):

    n = int((tf - t0) / h) + 1
    t = np.linspace(t0, tf, n)
    y = np.zeros((n, len(S_0)))
    y[0] = S_0
    i_list = []
    n_list = []
    p_list = []
    dn_list = []
    dp_list = []
    for i in range(1, n):
        y[i] = np.add(y[i-1], np.multiply( f(t[i-1], y[i-1]), h) )
        if i % interval == 0:
            i_list.append(i)
            n_list.append(y[i][0])
            dn_list.append(f(t[i-1], y[i-1])[0])
            p_list.append(y[i][1])
            dp_list.append( f(t[i-1], y[i-1])[1])

    return {'Time' : i_list, 'N' : n_list, 'dN/dt' : dn_list, 'P' : p_list, 'dP/dt' : dp_list}

def dSdx(t, S):
    n, p = S
    return []

def dyDt(t, S):
    y = S
    return t

def twosystem(x, S):
    y1, y2 = S
    return [x*y1 - 3*y2, 3*y1 - x**2 * y2]


S_0 = [2, 1]
x0 = 0

#print(euler_method(twosystem, S_0, x0, 5, 1))