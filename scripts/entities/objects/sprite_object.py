import pygame 
from scripts.entities.sprite import sprite
from scripts.library.settings import settings

    
class sprite_object(sprite):

    def __init__(self, name, pos, groups, hitbox_rect_size, surf):
        super().__init__(name, pos, pos, groups, [settings.TILE_SIZE, settings.TILE_SIZE])
        self.surface = surf
        #self.surface.set_alpha(255)

   
        

    
        
   



