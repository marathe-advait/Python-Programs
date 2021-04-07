def cal_distance(coor):
        loc_coor = coor[0]
        pat_coor = coor[1]
        dist = ((pat_coor[0]-loc_coor[0])**2 + (pat_coor[1]-loc_coor[1])**2)**0.5;
        return dist
