neighbor_offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def get_neighbors(coordinate):
    neightbor_list = []
    for offset in neighbor_offsets:
        new_coordinate = (coordinate[0] + offset[0], coordinate[1] + offset[1])
        neightbor_list.append(new_coordinate)
    return neightbor_list

        

