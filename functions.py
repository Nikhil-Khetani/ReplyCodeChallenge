import numpy as np
import math

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
        
def printOutput(antenna_list):
    f = open("output.txt","w")
    f.write(len(antenna_list))
    for i in range(len(antenna_list)):
        f.write("{} {} {}".format(i,antenna_list[i].x,antenna_list[i].y))
    return 0
  
def dist(a, b):
    return np.abs(a.x - b.x) + np.abs(b.x - b.y)

def reward():
    global B_list
    global R
   
    for b in B_list:
        if len(r(b) == 0):
            return 0
    return R


def score():
    global B_list

    result = 0

    for b in B_list:
       result += s(b)

    return result + reward()

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


if __name__ == "__main__":

    f = open("data_scenarios_a_example_in.txt", "r")
    H, W= f.readline().rsplit()
    N, M, R = f.readline().rsplit()
    global H = int(H)
    global W = int(W)
    global N = int(N)
    global M = int(M)
    global R = int(R)
    global B_list = []
    global A_list = []
    for i in range(N):
        x, y, latency, connection_weight = f.readline().rsplit()
        B_list.append(Building(x,y,latency, connection_weight))
    for i in range(M):
        Ar,Ac = f.readline().rsplit()
        A_list.append(Antenna(Ar,Ac))

        
