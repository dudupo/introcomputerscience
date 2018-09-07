from ex11_map_coloring import read_adj_file, COLORS, check_map
from copy import deepcopy
import heapq

class BackTrack:
    def __init__ (self, adj_dict, colors):
        self.heap = adj_dict.keys()
        self.colors = { **{ 0  : deepcopy(colors)   } ,
        **{key : deepcopy(colors) for key in adj_dict.keys() }}
        self.state = { key : None for key in adj_dict.keys() }
        self.adj_dict = adj_dict
    #abs
    def pop(self):
        return self.heap.pop()

    def settingAll(self):
        return len(self.heap) == 0

    def opthions(self , country):
        return self.colors[country]

    def setColor(self, country, color):
        self.state[country] = color
    def undoColor(self, country, color):
        self.state[country] = None

    def checkMap(self, country):
        return check_map(self.state, country, self.adj_dict)

    def backTrack(self):
        if self.settingAll():
            return True

        country = self.pop()
        for color in self.opthions(country):
            self.setColor(country, color)
            if self.checkMap(country) and self.backTrack():
                return True
            self.undoColor(country, color)
        return False

    def getAdjCountrys(self, country):
        for adj in self.adj_dict[country]:
            yield adj

    def getAdjNotSeted(self, country):
        for adj in self.getAdjCountrys(country):
            if self.state[adj] is None:
                yield adj

class BackTrackDH(BackTrack):
    def __init__(self, adj_dict, colors):
        super().__init__(adj_dict, colors)
        self.heap = [( -len(adj_countrys) , country) for country , adj_countrys
          in self.adj_dict.items() ]
        heapq.heapify(self.heap)

    def pop(self):
        _, country = heapq.heappop(self.heap)
        return country

class BackTrackMRV(BackTrackDH):
    def __init__(self, adj_dict, colors):
        super().__init__(adj_dict, colors)
        self.heap = [( len(self.colors[country]) , country) for country
          in self.adj_dict.keys() ]
        heapq.heapify(self.heap)
        self.undo = {}


    def isOpthion(self, country, color):
        return color in self.colors[country]

    def push(self, country):
        heapq.heappush(self.heap, (len(self.colors[country]), country))

    def removeColorOpthion(self, country, color):
        self.colors[country].remove( color )
        self.push( country )

    def addColorOpthion(self, country, color):
        self.colors[country].append( color )
        self.push( country )

    def setColor(self, country, color):
        self.state[country] = color
        for adj in self.getAdjNotSeted(country):
            if self.isOpthion(adj, color):
                self.removeColorOpthion( adj , color )
                self.undo[ (country, adj) ] = color

    def undoColor(self, country, color):
        for adj in self.getAdjNotSeted(country):
            if (country, adj) in self.undo:
                self.addColorOpthion(adj , self.undo[(country, adj)])

        self.state[country] = None

class BackTrackFC(BackTrackMRV):
    def __init__(self, adj_dict, colors):
        super().__init__(adj_dict, colors)
        self.map_check_flag = True

    def checkMap(self, country):
        return self.map_check_flag and super().checkMap(country)

    def removeColorOpthion(self, country, color):
        self.map_check_flag = len(self.colors[country]) > 1
        super().removeColorOpthion(country, color)
    def undoColor(self, country, color):
        self.map_check_flag = True
        super().undoColor(country, color)

class BackTrackLCV():
    def __init__(self, adj_dict, colors, backTrackType):
        self.back_track_obj = backTrackType(adj_dict, colors)
        self.state = self.back_track_obj.state
        self.back_track_obj.opthions = self.opthions
        self.tempcolors =  { color : 0 for color in colors }
    def backTrack(self):
        self.back_track_obj.backTrack()

    def opthions(self, country):
        tempcolors = deepcopy(self.tempcolors)
        obj = self.back_track_obj
        for adj in obj.getAdjNotSeted(country):
            for color in obj.colors[adj]:
                tempcolors[color] += 1
        return sorted( [ color for color ,count in tempcolors.items()],
         key = lambda color : tempcolors[color] )

def back_track_degree_heuristic( adj_dict, colors ):
    back_track_obj = BackTrackDH( adj_dict, colors )
    back_track_obj.backTrack()
    print(back_track_obj.state)
def back_track_MRV( adj_dict, colors ):
    back_track_obj = BackTrackMRV( adj_dict, colors )
    back_track_obj.backTrack()
    print(back_track_obj.state)
def back_track_FC( adj_dict, colors ):
    back_track_obj = BackTrackFC( adj_dict, colors )
    back_track_obj.backTrack()
    print(back_track_obj.state)
def back_track_LCV( adj_dict, colors ):
    back_track_obj = BackTrackLCV( adj_dict, colors, BackTrackFC)
    back_track_obj.backTrack()
    print(back_track_obj.state)

import os
import threading
if __name__ == '__main__' :
    limit = 3000
    os.sys.setrecursionlimit(limit)
    graph = read_adj_file( os.sys.argv[1] )
    back_track_degree_heuristic( graph , COLORS  )
    back_track_MRV( graph , COLORS )
    back_track_FC( graph , COLORS )
    def callable():
         back_track_LCV( graph , COLORS)
    thread = threading.Thread(target=callable)
    thread.start()
