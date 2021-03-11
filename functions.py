import numpy as np
import math
import random
import copy
'''
class Grid(object):
    def __init__(self, H, W, A_list, B_list):
        self.H = H
        self.W = W
        self.A_list = A_list 
        self.B_list = B_list
        self.Space = {}
        for j in range(0, H):
            for i in range(0, W):
                self.Space[str(i) + ',' + str(j)] = {'a':None,
                                                     'b':None}
    
    def get_spot(self, i, j):
        return self.Space[str(i) + ',' + str(j)]
    
    def set_spot(self, i, j, a=None, b=None):
        print(self.Space.keys())
        if a==None and b==None:
            pass
        elif b==None:
            self.Space[str(i) + ',' + str(j)]['a'] = a
        else:
            self.Space[str(i) + ',' + str(j)]['b'] = b
'''

class Building(object):
    

    def __init__(self, x, y, latency, connection_weight):
        self.x= x
        self.y = y
        self.latency = latency
        self.connection_weight = connection_weight
        self.r = None

class Antenna(object):
    
    def __init__(self, a_range, connection_speed):
        self.range = a_range
        self.connection_speed = connection_speed
        self.x = None
        self.y = None
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{} {} {} {}".format(self.x,self.y,self.range,self.connection_speed)

        
def printOutput():
    global A_list
    f = open("output.txt","w")
    f.write(str(len(A_list))+"\n")
    for i in range(len(A_list)):
        f.write("{} {} {}\n".format(i,A_list[i].x,A_list[i].y))
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

    if b.r == None:
        global A_list
        
        array = []
        for a in A_list:
            if dist(a, b) <= a.range:
                array.append(a)

        b.r = array
        
        return array
    else:
        return b.r

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

    


    old_score = 0
    oldpositions = []
    for k in range(1000):
        i=0
        positions = []
        while i<M:
            
            xpos = random.randint(0,W)
            ypos = random.randint(0,H)
            print("position {} {}".format(xpos,ypos))
            if ((xpos,ypos) not in positions):
                A_list[i].set_coords(xpos,ypos)
                positions.append([xpos,ypos])
                i+=1
        print("score to be calc")
        new_score = score()
        print(new_score)
        if (new_score>=old_score):
            old_score = new_score
            oldpositions = positions
        
    for i in range(len(oldpositions)):
        A_list[i].set_coords(oldpositions[i][0],oldpositions[i][1])
    positions = oldpositions



        
    




    print(A_list)
    pass
        


if __name__ == "__main__":

    f = open("data_scenarios_a_example_in.txt", "r")
    tempW, tempH= f.readline().rsplit()
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
        B_list.append(Building(int(x),int(y),float(latency), float(connection_weight)))
    for i in range(M):
        Ar,Ac = f.readline().rsplit()
        A_list.append(Antenna(float(Ar),float(Ac)))
    optimise()
    print(score())
    printOutput()

    

        
