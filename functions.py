import numpy as np
import math

def reward(b):
    global A_list
    global N
    global R
    

    if (np.abs(len(r(b,A_list) != 0) == N):
        return R
    else():
        return 0
        

def score():
    global B_list
    global N

    sum = 0

    for i in range(0,N):
       sum += s(B_list[i])

    return sum + reward

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


class Building():
    def __init__(self, x, y, latency, connection_weight):
        self.x= x
        self.y = y
        self.latency = latency
        self.connection_weight = connection_weight

class Antenna():
    def __init__(self, range, connection_speed):
        self.range = range
        self.connection_speed = connection_speed
        self.x = None
        self.y = None


def readInput(filename):
    f = open(filename, "r")
    H, W= f.readline().rsplit()
    N, M, R = f.readline().rsplit()
    H = int(H)
    W = int(W)
    N = int(N)
    M = int(M)
    R = int(R)
    building_list = []
    antenna_list = []
    for i in range(N):
        x, y, latency, connection_weight = f.readline().rsplit()
        building_list.append(Building(x,y,latency, connection_weight))
    for i in range(M):
        Ar,Ac = f.readline().rsplit()
        antenna_list.append(Antenna(Ar,Ac))
    return H,W,N,M,R,building_list,antenna_list



#H,W,N,M,R,building_list,antenna_list = readinput("data_scenarios_a_example_in.txt")
#print([i.latency for i in building_list ])


