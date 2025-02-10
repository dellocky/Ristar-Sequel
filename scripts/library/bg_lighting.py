import pygame
from library.settings import settings

class bg_lighting:

    
    def __init__(self, brightness, player, groups):

        self.brightness = brightness
        color = (self.brightness, round(self.brightness*.8), self.brightness)
        self.hitbox_rect = pygame.Rect(0, 0, settings.TOTAL_WIDTH*1.1, settings.TOTAL_HEIGHT*1.1)
        self.surface = pygame.Surface((settings.TOTAL_WIDTH*1.1, settings.TOTAL_HEIGHT*1.1))
        self.light_rect = pygame.draw.rect(self.surface, color, self.hitbox_rect)
        self.timer_color = 0
        self.player = player
        for I in groups:
            I.append(self)

    def tick(self):
        
        self.timer_color +=1 
        if self.timer_color == 50:
            if self.brightness < 250:
                self.brightness +=1
                color = (self.brightness, round(self.brightness*.1), self.brightness)
                self.light_rect = pygame.draw.rect(self.surface, color, self.rect)
            self.timer_color = 0

    def update(self):

        #self.tick()
        self.hitbox_rect.centerx = self.player.hitbox_rect.centerx
        self.hitbox_rect.centery = self.player.hitbox_rect.centery

        

