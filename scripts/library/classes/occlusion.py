import pygame

class occlusion:
    def __init__(self, pos_x, pos_y, width, height, buffer = None, anchor = "bottom_left"):
        
        self.width = width
        self.height = height
        self.pos = [pos_x, pos_y]
        self.surface = pygame.surface.Surface((width, height))
        self.anchor = anchor
        
    def custom_blit(self, surface):
        if self.anchor == "top_left":
            surface.blit(self.surface (self.image_offset[0], self.image_offset[1]))
        if self.anchor == "top_right":
            surface.blit(self.surface, (self.width_difference + self.image_offset[0], self.image_offset[1]))
        if self.anchor == "bottom_left":
            surface.blit(self.surface, (self.image_offset[0], -self.height_difference + self.image_offset[1]))
        if self.anchor == "bottom_right":
            surface.blit(self.surface, (-self.width_difference - self.image_offset[0], -self.height_difference - self.image_offset[1]))
        




    

