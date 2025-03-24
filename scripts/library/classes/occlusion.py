import pygame

class occlusion:
    def __init__(self, pos_x, pos_y, width, height, buffer = [0, 0]):
        self.colorkey = (0, 0, 0)
        self.pos = [pos_x, pos_y]
        self.surface = pygame.surface.Surface([width, height])
        self.surface.set_colorkey((0, 0, 1))
        
        




    

