### to implement


def general_backtracking(list_of_items, dict_items_to_vals, index,
                    set_of_assignments, legal_assignment_func,
                    *args):

    if index == len(list_of_items):
        return True

    for value in set_of_assignments:
        dict_items_to_vals[ list_of_items[index] ] = value
        if legal_assignment_func( dict_items_to_vals , list_of_items[index], *args) and \
         general_backtracking(list_of_items , dict_items_to_vals, index+1, set_of_assignments, legal_assignment_func, *args):
            return True
    dict_items_to_vals[ list_of_items[index] ] = 0
    return False
