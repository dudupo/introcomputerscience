from ex11_backtrack import general_backtracking

#from map_coloring_gui import color_map #uncomment if you installed the required libraries

COLORS = ['red','blue','green','magenta','yellow','cyan']

### to implement
def read_adj_file(adjacency_file):
    state = {}
    with open(adjacency_file) as _file :
        for line in  _file.readlines():
            country , adjacencys = line.rstrip("\n").split(":")
            state[country] = adjacencys.split(",") if adjacencys != '' else []
    return state


def check_map( _map, country, *args ):
    graph = args[0]
    for adjacency in graph[country] :
        if _map[adjacency] == _map[country] and adjacency != country :
            return False
    return True

def run_map_coloring(adjacency_file, num_colors = 4, map_type = None):
    graph = read_adj_file(adjacency_file)
    State = { key : None for key in graph.keys() }
    general_backtracking( [key for key in graph.keys()] , State  , 0 ,
                        COLORS[:num_colors] , check_map , graph)

    #from map_coloring_gui import color_map
    #color_map("USA" , State )


import os
if __name__ == "__main__":
    run_map_coloring( os.sys.argv[1])
