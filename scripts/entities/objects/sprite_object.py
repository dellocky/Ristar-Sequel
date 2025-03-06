import pygame 
from scripts.entities.sprite import sprite
from scripts.settings import settings

    
class sprite_object(sprite):

    def __init__(self, name, pos, groups, hitbox_rect_size, surf):
        self.hitbox_rects = []
        super().__init__(name, pos, groups, pos, [settings.TILE_SIZE, settings.TILE_SIZE], surf)
        self.hitbox_rects.append(self.hitbox_rect)
        #self.surface.set_alpha(255)

   
        

    
        
   



