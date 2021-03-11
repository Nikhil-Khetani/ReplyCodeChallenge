import numpy as np
import math

class Grid(object):
    def __init__(self, H, W, A_list, B_list):
        self.H = H
        self.W = W
        self.A_list = A_list 
        self.B_list = B_list
        self.Space = {}
        for j in range(1, H+1):
            for i in range(1, W+1):
                self.Space[str(i) + ',' + str(j)] = {}
    
    def get_spot(self, i, j):
        return self.Space[str(i) + ',' + str(j)]
    
    def set_spot(self, i, j, a=None, b=None):
        if a==None and b==None:
            pass
        elif b==None:
            self.Space[str(i) + ',' + str(j)]['a'] = a
        else:
            self.Space[str(i) + ',' + str(j)]['b'] = b


class Building(object):
    

    def __init__(self, x, y, latency, connection_weight, City):
        self.x= x
        self.y = y
        self.City = City
        self.City.set_spot(x, y, b=self)
        self.latency = latency
        self.connection_weight = connection_weight

class Antenna(object):
    
    def __init__(self, range, connection_speed, City):
        self.range = range
        self.connection_speed = connection_speed
        self.x = None
        self.y = None
        self.City = City
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
        self.City.set_spot(x, y, a=self)
        
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

def s(b, a=None):
    
    global A_list
    
    if a == None:
        if len(r(b)) == 0:
            return 0
        else:
            return s(b, c(b))
    else:
        return b.connection_weight*a.connection_speed - b.latency*dist(a, b)
    
def c(b):
    array = r(b)
    a_max = array[0]
    s_max = s(b, a_max)
    for a in array:
        s_temp = s(b, a)
        if s_temp > s_max:
            s_max = s_temp
            a_max = a
    
    return a_max

def optimise():
    return

if __name__ == "__main__":

    f = open("data_scenarios_a_example_in.txt", "r")
    tempH, tempW= f.readline().rsplit()
    tempN, tempM, tempR = f.readline().rsplit()
    H = int(tempH)
    W = int(tempW)
    N = int(tempN)
    M = int(tempM)
    R = int(tempR)
    B_list = []
    A_list = []
    City = Grid(H, W, A_list, B_list)
    for i in range(N):
        x, y, latency, connection_weight = f.readline().rsplit()
        B_list.append(Building(x,y,latency, connection_weight, City))
    for i in range(M):
        Ar,Ac = f.readline().rsplit()
        A_list.append(Antenna(Ar,Ac, City))
        
    

    

        
