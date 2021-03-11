import numpy as np

def r(b):
    
    global A_list
    
    array = []
    for a in A_list:
        if dist(a, b) <= a.range:
            array.append(a)
    
    return array

def s(a=None, b):
    
    global A_list
    
    if a == None:
        if len(r(b)) == 0:
            return 0
        else:
            return s(c(b), b)
    else:
        return b.connection_weight*a.connection_speed - b.latency*dist(a, b)
    
def c(b):
    array = r(b)
    a_max = array[0]
    s_max = s(a_max, b)
    for a in array:
        s_temp = s(a, b)
        if s_temp > s_max:
            s_max = s_temp
            a_max = a
    
    return a_max


def dist(a, b):
    
    return np.abs(a.x - b.x) + np.abs(b.x - b.y)