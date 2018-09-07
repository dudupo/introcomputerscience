from ex11_map_coloring import read_adj_file, COLORS, check_map












import heapq

from copy import deepcopy , copy

def initilaize(adj_dict, colors):
    heap = [( 0 , key ) for key , value in adj_dict.items() ]
    heapq.heapify(heap)
    state = { key : None for key in adj_dict.keys() }
    colors = { **{ 0  : deepcopy(colors)   } ,
    **{key : deepcopy(colors) for key in adj_dict.keys() }}
    return heap, state, colors

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
    heap, state, colors = initilaize(adj_dict, colors)
    def back_track_mrv(heap , state, adj_dict, colors):
        def decrease_keys(country):
            ret =  True
            for adj_country in adj_dict[country]:
                if state[adj_country] is None:
                    if state[country] in colors[adj_country]:
                        colors[adj_country].remove( state[country]  )
                        heapq.heappush(heap, ( - len(colors[adj_country])  , adj_country))
            return ret
        def increase_keys(country):
            for adj_country in adj_dict[country]:
                if state[adj_country] is None:
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



    #//   state.color() <--- color
    #//   for v in state.edges() :
    #//       if color in v.options:
    #//           v.options -= color
    #//   heapify and then continue back_track
    #//   if is impassible to fill with that colors
    #//   then for v in state.edges() :
    #//       if color not in v.opthions:
    #//           v.opthions += color
    #//   heapify and try other color / the heapify can white
    back_track_mrv( heap , state, adj_dict, colors)
    print (state)

def back_track_FC(adj_dict, colors):
    heap, state, colors = initilaize(adj_dict, colors)

    def back_track_fc(heap , state, adj_dict, colors):
        def decrease_keys(country):
            ret =  True
            for adj_country in adj_dict[country]:
                if state[adj_country] is None:
                    if state[country] in colors[adj_country]:
                        colors[adj_country].remove( state[country]  )
                        if len(colors[adj_country]) == 0 :
                            return False
                        heapq.heappush(heap, ( - len(colors[adj_country])  , adj_country))
            return ret
        def increase_keys(country):
            for adj_country in adj_dict[country]:
                if state[adj_country] is None:
                    if state[country] not in colors[adj_country]:
                        colors[adj_country].append( state[country]  )
                        heapq.heappush(heap, ( - len(colors[adj_country])  , adj_country))
        if len(heap) == 0 :
            return True
        negdegree , country = heapq.heappop(heap)
        for color in colors[country] :
            state[country] = color
            if decrease_keys(country):
                if check_map(state, country, adj_dict) and \
                 back_track_fc(heap, state, adj_dict, colors):
                    return True
            increase_keys(country)
        state[country] = None
        heapq.heappush(heap , (- len(colors[country]), country) )
        return False
    back_track_fc( heap , state, adj_dict, colors)
    print (state)

def back_track_LCV(adj_dict, colors):
    heap, state, colors = initilaize(adj_dict, colors)

    def back_track_lcv(heap , state, adj_dict, colors):
        def decrease_keys(country):
            ret =  0
            for adj_country in adj_dict[country]:
                if state[adj_country] is None:
                    if state[country] in colors[adj_country]:
                        colors[adj_country].remove( state[country]  )
                        heapq.heappush(heap, ( - len(colors[adj_country])  , adj_country))
                        ret += len(colors[adj_country])
            return ret
        def increase_keys(country):
            for adj_country in adj_dict[country]:
                if state[adj_country] is None:
                    if state[country] not in colors[adj_country]:
                        colors[adj_country].append( state[country]  )
                        heapq.heappush(heap, ( - len(colors[adj_country])  , adj_country))

        def colorvalue(country , color):
            state[country] = color
            ret = decrease_keys(country)
            increase_keys(country)
            return ret
        if len(heap) == 0 :
            return True
        negdegree , country = heapq.heappop(heap)
        for color in sorted(colors[country], key = lambda color : - colorvalue(country , color)):
            state[country] = color
            decrease_keys(country)
            if check_map(state, country, adj_dict) and \
             back_track_lcv(heap, state, adj_dict, colors):
                return True
            increase_keys(country)
        state[country] = None
        heapq.heappush(heap , (- len(colors[country]), country) )
        return False
    back_track_lcv( heap , state, adj_dict, colors)
    print (state)

def fast_back_track(adj_dict, colors):
    pass


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
