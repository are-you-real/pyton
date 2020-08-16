def miss_el(incomplete_list, n):
    full_list = set(list(range(1,n+1)))
    incomplete_set = set(incomplete_list)
    return full_list.difference(incomplete_set)
