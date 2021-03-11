
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