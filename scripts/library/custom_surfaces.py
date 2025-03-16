import pygame

class circle_surface:
    def __init__(self, radius, color, surface = None):

        self.surface = pygame.Surface((radius * 2, radius * 2))
        self.radius = radius
        if surface == None:
            pygame.draw.circle(self.surface, color, (radius, radius), radius)
            self.surface.set_colorkey((0, 0, 0))

        self.hitbox_rect = pygame.Rect(0, 0, radius*2, radius*2)


        