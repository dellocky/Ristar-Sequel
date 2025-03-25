import pygame
neighbor_offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def get_neighbors(coordinate):
    neightbor_list = []
    for offset in neighbor_offsets:
        new_coordinate = (coordinate[0] + offset[0], coordinate[1] + offset[1])
        neightbor_list.append(new_coordinate)
    return neightbor_list

def get_direction(keys):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            return "upleft"
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            return "downleft"
        else:
            return "left"
        
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            return "upright"
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            return "downright"
        else:
            return "right"
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        return "up"
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        return "down"
    
    else: return False


    

