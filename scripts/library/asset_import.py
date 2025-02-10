from csv import reader
from os import walk
import pygame
from scripts.library.settings import settings

def csv_layout(path):
    map = []
    with open(path) as level_map:
        layout = reader (level_map, delimiter = ',')
        for row in layout:
            map.append(list(row))
        return map

def import_folder(path, scale=(-1,-1)):
    surface_list = []
    count = 0
    for __,__,img_files  in walk(path):
        for image in img_files:
            full_path = f"{path}/{count}.png"
            count += 1
            image_surf = pygame.image.load(full_path).convert_alpha()
            if scale[0] and scale[1] > -1:
                pass
                #image_surf = pygame.transform.smoothscale(image_surf, scale)
            else:
                pass
                #image_surf = pygame.transform.smoothscale(image_surf, (settings.SCALE*settings.TILE_SIZE, settings.SCALE*settings.TILE_SIZE))
            surface_list.append(image_surf)
        return surface_list
    
    

def get_folder_names(path):
    for __,folders,__  in walk(path):
        
        return folders
    


def import_folder_with_time(path, scale=(-1,-1)):
    surface_list = []
    count = 0   
    for __,__,img_files  in walk(path):
        for image in img_files:
            full_path = f"{path}/{count}.png"
            count += 1
            image_surf = pygame.image.load(full_path).convert_alpha()
            if scale[0] and scale[1] > -1:
                pass
                #image_surf = pygame.transform.smoothscale(image_surf, scale)
            else:
                pass
                #image_surf = pygame.transform.smoothscale(image_surf, (settings.SCALE*settings.TILE_SIZE, settings.SCALE*settings.TILE_SIZE))
            surface_list.append([image_surf, 0])
        return surface_list
    



def import_folder_dict(path, scale=(-1,-1)):
    surface_list = {}
    for __,__,img_files  in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            if scale[0] and scale[1] > -1:
                image_surf = pygame.transform.smoothscale(image_surf, scale)
            surface_list[image.split(".")[0]] = image_surf
        return surface_list
    
    

def import_folder_list_dict(path, scale=(-1,-1)):
    surface_list = []
    for __,__,img_files  in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            if scale[0] and scale[1] > -1:
                image_surf = pygame.transform.smoothscale(image_surf, scale)
            image_name = image.split(".")[0]
            image_surf = (image_surf, image_name)
            surface_list.append(image_surf)
        
        return surface_list
