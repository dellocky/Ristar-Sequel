import pygame
from scripts.library.objects.settings import settings

class camera:
    def __init__(self, display, player):
        self.display = display
        half_width = display.get_size()[0]//2
        half_height = display.get_size()[1]//2
        invert_point = 2
        screen_ratio = 7/8

        self.camera_scroll_x_min = half_width * screen_ratio
        self.camera_scroll_x_max = half_width * (invert_point - screen_ratio)

        self.camera_scroll_x_min_pos = self.camera_scroll_x_min
        self.camera_scroll_x_max_pos = self.camera_scroll_x_max

        self.camera_scroll_y_min = half_height * screen_ratio
        self.camera_scroll_y_max = half_height * (invert_point - screen_ratio)

        self.camera_scroll_y_min_pos = self.camera_scroll_y_min
        self.camera_scroll_y_max_pos = self.camera_scroll_y_max


        self.offset = [0, 0]
        self.player = player
    
    def update(self):
        player_midpoint = [self.player.pos[0] + (self.player.size[0]/2), self.player.pos[1] + (self.player.size[1]/2)]

        if player_midpoint[0] > self.camera_scroll_x_max_pos: #inital camera movement
            self.offset[0] = player_midpoint[0] - self.camera_scroll_x_max
            self.camera_scroll_x_max_pos = self.camera_scroll_x_max + self.offset[0]
            self.camera_scroll_x_min_pos = self.camera_scroll_x_min + self.offset[0]   
        
        if player_midpoint[0] < self.camera_scroll_x_min_pos and player_midpoint[0] > self.camera_scroll_x_max:
            self.offset[0] = player_midpoint[0] - self.camera_scroll_x_min
            self.camera_scroll_x_max_pos = self.camera_scroll_x_max + self.offset[0]
            self.camera_scroll_x_min_pos = self.camera_scroll_x_min + self.offset[0]

        if player_midpoint[1] > self.camera_scroll_y_max_pos: #inital camera movement
            self.offset[1] = player_midpoint[1] - self.camera_scroll_y_max
            self.camera_scroll_y_max_pos = self.camera_scroll_y_max + self.offset[1]
            self.camera_scroll_y_min_pos = self.camera_scroll_y_min + self.offset[1]   
        
        if player_midpoint[1] < self.camera_scroll_y_min_pos and player_midpoint[1] > self.camera_scroll_y_max:
            self.offset[1] = player_midpoint[1] - self.camera_scroll_y_min
            self.camera_scroll_y_max_pos = self.camera_scroll_y_max + self.offset[1]
            self.camera_scroll_y_min_pos = self.camera_scroll_y_min + self.offset[1]      

   
    def draw(self, display, *sprites):
        for sprite_groups in sprites:
            for sprite in sprite_groups:
                if sprite.visible:
                    offset_pos = (sprite.pos[0] - self.offset[0], sprite.pos[1] - self.offset[1])
                    display.blit(sprite.surface, offset_pos)
                    if sprite.draw_hitbox_rect == True:
                        pygame.draw.rect(sprite.hitbox_surf, (0, 0, 255), sprite.hitbox_rect)
                        display.blit(sprite.hitbox_surf, (sprite.hitbox_rect.left - self.offset[0], sprite.hitbox_rect.top - self.offset[1]))
    
    def draw_ui(self, display, *sprites):
        for sprite_groups in sprites:
            for sprite in sprite_groups:
                display.blit(sprite.surface, sprite.pos)
             
        
    """
    #if sprite.occlude: keep this, its fun!!!
                    #for occlusion in sprite.occlusion_rects:
                        #display.blit(occlusion[1].to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(0, 0, 255, 255)), occlusion[0])
                        #display.blit(sprite.mask.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(255, 0, 0, 255)), sprite.pos)
                        #overlap_mask = sprite.mask.overlap_mask(occlusion[1], (occlusion[0][0] - sprite.pos[0], occlusion[0][1] - sprite.pos[1]))
                        #overlap_surface = overlap_mask.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=(0, 0, 0, 255))
                        #overlap_surface.set_colorkey((0, 0, 1))
                        #display.blit(overlap_surface, sprite.pos)
 

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
    
    """



        
    

