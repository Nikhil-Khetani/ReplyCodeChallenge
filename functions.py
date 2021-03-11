import numpy as np
import math
import random


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
    def __repr__(self):
        return "{} {} {} {}".format(self.x,self.y,self.range,self.connection_speed)
        
def printOutput():
    global A_list
    f = open("output.txt","w")
    f.write(str(len(A_list)))
    for i in range(len(A_list)):
        f.write("{} {} {}".format(i,A_list[i].x,A_list[i].y))
    return 0
  
def dist(a, b):

    return np.abs(a.x - b.x) + np.abs(b.x - b.y)

def reward():
    global B_list
    global R
   
    for b in B_list:
        if len(r(b)) == 0:
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
    global A_list
    global M
    global W
    global H
    for i in range(M):
        A_list[i].x = random.randint(0,W)
        A_list[i].y = random.randint(0,H)
    print(A_list)
    pass
        


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
    for i in range(N):
        x, y, latency, connection_weight = f.readline().rsplit()
        B_list.append(Building(int(x),int(y),float(latency), float(connection_weight) ))
    for i in range(M):
        Ar,Ac = f.readline().rsplit()
        A_list.append(Antenna(float(Ar),float(Ac)))
    optimise()
    print(score())
    printOutput()

    

        
