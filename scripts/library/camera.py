import pygame
from scripts.library.settings import settings

class camera:
    def __init__(self, display, player):
        self.display = display
        self.half_width = display.get_size()[0]//2
        self.half_height = display.get_size()[1]//2
        #self.offset_default = pygame.math.Vector2()
        self.player = player

        #self.offset_default.x = player.hitbox_rect.midright[0] - self.half_width - settings.TILE_SIZE/2
        #self.offset_default.y = player.hitbox_rect.midright[1] - self.half_height + settings.TILE_SIZE
    
    def draw(self, display, *sprites):
        offset = [0, 0]
        if self.player.pos[0] > self.half_width:
            offset[0] = self.player.pos[0] - self.half_width
        if self.player.pos[1] > self.half_height:
            offset[1] = self.player.pos[1] - self.half_height

        for sprite_groups in sprites:
            for sprite in sprite_groups:
                offset_pos = (sprite.pos[0] - offset[0], sprite.pos[1] - offset[1])
                display.blit(sprite.surface, offset_pos)
                #pygame.draw.rect(display, (255, 0 ,0), sprite.hitbox_rect)
    
    def draw_ui(self, display, *sprites):
        for sprite_groups in sprites:
            for sprite in sprite_groups:
                #pygame.draw.rect(display, (255, 0 ,0), sprite.hitbox_rect)
                display.blit(sprite.surface, sprite.pos)
                #pygame.draw.rect(display, (255, 0 ,0), sprite.hitbox_rect)
        
    def lighten(self, display, *sprites):

        self.offset.x = self.player.hitbox_rect.centerx - self.half_width
        self.offset.y = self.player.hitbox_rect.centery - self.half_height

        for sprite in sprites:
            offset_pos = sprite.hitbox_rect.topleft - self.offset
            display.blit(sprite.surface, offset_pos, special_flags=pygame.BLEND_RGB_ADD)
    
    def darken(self, display, *sprites):

        self.offset.x = self.player.hitbox_rect.centerx - self.half_width
        self.offset.y = self.player.hitbox_rect.centery - self.half_height

        for sprite_groups in sprites:
            for sprite in sprite_groups:
                offset_pos = sprite.hitbox_rect.topleft - self.offset
                display.blit(sprite.surface, offset_pos, special_flags=pygame.BLEND_RGB_SUB)

    
    def ordered_init(self, display, *sprites):
        #sprite[0] = sprite
        #sprite[1] = flag 
        
        for sprite in sprites:
            offset_pos = sprite[0].hitbox_rect.topleft - self.offset_default
            if sprite[1] == "add":
                display.blit(sprite[0].surface, offset_pos, special_flags=pygame.BLEND_RGB_ADD)
            if sprite[1] == "sub":
                display.blit(sprite[0].surface, offset_pos, special_flags=pygame.BLEND_RGB_SUB)



        
    

