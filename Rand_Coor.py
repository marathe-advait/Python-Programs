import random

def rand_coor():
    pat_coor = [];
    loc_coor = [];
    loc_coor.append(random.uniform(-180.000, 180.000))
    loc_coor.append(random.uniform(-180.000, 180.000))
    pat_coor.append(loc_coor[0] + random.uniform(-2.500, 2.500))
    pat_coor.append(loc_coor[1] + random.uniform(-2.500, 2.500))
    return tuple(loc_coor), tuple(pat_coor)
