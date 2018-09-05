from ex11_map_coloring import read_adj_file, COLORS, check_map
# from map_coloring_gui import color_map #uncomment if you installed the required libraries


### to implement
import heapq
from copy import deepcopy , copy

def back_track(heap , state, adj_dict, colors, hooking=False):

    if len(heap) == 0 :
        return True
    negdegree , country = heapq.heappop(heap)

    for color in colors :
        state[country] = color
        if check_map(state, country, adj_dict) and \
         back_track(heap, state, adj_dict, colors):
            return True
    state[country] = None
    heapq.heappush(heap , (negdegree , country) )
    return False


def back_track_degree_heuristic(adj_dict, colors):

    heap = [( -len(value), key ) for key , value in adj_dict.items() ]
    heapq.heapify(heap)
    state = { key : None for key in adj_dict.keys() }
    back_track( heap , state, adj_dict, colors)
    print (state)

def back_track_MRV(adj_dict, colors):
    heap = [( 0 , key ) for key , value in adj_dict.items() ]
    heapq.heapify(heap)

    state = { key : None for key in adj_dict.keys() }
    colors = { **{ 0  : deepcopy(colors)   } ,
    **{key : deepcopy(colors) for key in adj_dict.keys() }}


    def back_track_mrv(heap , state, adj_dict, colors):

        def foradj(country, notbeenset = True):
            for adj_country in adj_dict[country]:
                if (notbeenset and state[adj_country] is None) or not notbeenset:
                    yield adj_country

        def decrease_keys(country):
            for adj_country in foradj(country):
                if state[country] in colors[adj_country]:
                    colors[adj_country].remove( state[country]  )
                    heapq.heappush(heap, ( - len(colors[adj_country])  , adj_country))
        def increase_keys(country):
            for adj_country in foradj(country):
                if state[country] not in colors[adj_country]:
                    colors[adj_country].append( state[country]  )
                    heapq.heappush(heap, ( - len(colors[adj_country])  , adj_country))

        if len(heap) == 0 :
            return True
        negdegree , country = heapq.heappop(heap)

        for color in colors[country] :
            state[country] = color
            decrease_keys(country)
            if check_map(state, country, adj_dict) and \
             back_track_mrv(heap, state, adj_dict, colors):
                return True
            increase_keys(country)
        state[country] = None
        heapq.heappush(heap , (- len(colors[country]), country) )
        return False

    #decrease_keys()

    #print("DEBUG : i was here")

    back_track_mrv( heap , state, adj_dict, colors)

    #   state.color() <--- color
    #   for v in state.edges() :
    #       if color in v.options:
    #           v.options -= color
    #   heapify and then continue back_track
    #   if is impassible to fill with that colors
    #   then for v in state.edges() :
    #       if color not in v.opthions:
    #           v.opthions += color
    #   heapify and try other color / the heapify can white

    print (state)

def back_track_FC(adj_dict, colors):
    pass

def back_track_LCV(adj_dict, colors):
    pass

def fast_back_track(adj_dict, colors):
    pass


import os
if __name__ == '__main__' :
    graph = read_adj_file( os.sys.argv[1] )
    back_track_degree_heuristic( graph , COLORS  )
    back_track_MRV( graph , COLORS )
