import pygame
from scripts.entities.sprite import sprite

class grab_arms(sprite):
    def __init__(self, pos, direction, groups):
        
        self.pos = pos
        self.direction = direction
        front = groups[0]
        back = groups[1]

        self.surface = pygame.surface(100, 100)
        self.surface.set_colorkey((0, 0, 1))

        self.front_arms =  super().__init__("Arms_Front", pos, [pos[0] - 16, pos[1] - 15], front, [16, 30], buffer = 9)
        self.back_arms =  super().__init__("Arms_Back", pos, [pos[0] - 16, pos[1] - 15], back, [16, 30], buffer = 9)
    
    def run(self):
        
        self.surface.fill((0, 0, 1))
        self.surface.blit(self.front_arms)
        self.surface.blit(self.back_arms)
    
        