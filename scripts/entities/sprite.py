from scripts.library.objects.settings import settings
from scripts.library.classes.occlusion import occlusion
import scripts.library.classes.animation_player as animation_player
import pygame

class sprite():
    def __init__(self, name, pos, groups,  hitbox_rect_pos, hitbox_rect_size, surface_image, buffer_leftup = [0, 0], buffer_downright = [0, 0], anchor = "bottom_left"):      
    
        self.name = name
        self.groups = groups
        self.occlusion_rects = []
        #self.rgb = (255, 255, 255)
        self.surface_image = surface_image
        self.surface_image_position = [0, 0]
        self.pos = pos
        self.hitbox_rect_pos = hitbox_rect_pos
        self.hitbox_surf = pygame.surface.Surface((hitbox_rect_size[0], hitbox_rect_size[1]))
        self.hitbox_rect = pygame.rect.Rect(hitbox_rect_pos[0], hitbox_rect_pos[1], hitbox_rect_size[0], hitbox_rect_size[1])
        self.hitbox_offset = (hitbox_rect_pos[0] - pos[0], hitbox_rect_pos[1] - pos[1])

        self.size = [self.surface_image.get_rect().width, self.surface_image.get_rect().height]

        self.height_default = self.size[1] + buffer_leftup[1]
        self.height_difference = buffer_leftup[1]
        self.width_default = self.size[0] + buffer_leftup[0]
        self.width_difference = buffer_leftup[0]
 
        self.surface = pygame.surface.Surface((self.size[0] + buffer_leftup[0] + buffer_downright[0], self.size[1] + buffer_leftup[1] + buffer_downright[1]))
        self.colorkey = (0, 0, 1)
        self.fill_color_1 = self.colorkey
        self.fill_color_2 = self.colorkey
        self.anchor = anchor

        #self.mask = pygame.mask.from_surface(self.surface)

        self.surface.set_colorkey((self.colorkey))

        #Debugging Tools<----------------------------------------------------------------> 
        #self.fill_color_1 = (20, 20, 20)
        #self.fill_color_2 = (20, 20, 255)
        self.visible = True
        self.draw_hitbox_rect = False
        
        for I in groups:
            I.append(self)
        
    def update_image_offset(self):
        self.height_difference = self.surface_image.get_rect().height - self.height_default
        self.width_difference = self.surface_image.get_rect().width - self.width_default
    
    def create_occlusion_rect(self, pos_x, pos_y, width, height):

        spirte_occlusion = [[pos_x, pos_y], pygame.surface.Surface((width, height))]
        self.occlusion_rects.append(spirte_occlusion)
        return spirte_occlusion
    
    def clear_occlusion_rects(self):
        self.occlusion_rects.clear()

    def run(self, event_loop, delta_time):

        self.surface.fill(self.fill_color_1)
        self.custom_blit()
        for occlusion in self.occlusion_rects:
            occlusion[1].fill(self.fill_color_2)
            self.surface.blit(occlusion[1], occlusion[0])


    def update(self):
        self.surface.fill(self.fill_color_1)
        self.custom_blit()
        for occlusion in self.occlusion_rects:
            occlusion[1].fill(self.fill_color_2)
            self.surface.blit(occlusion[1], occlusion[0])
    
    def custom_blit(self):
        if self.anchor == "top_left":
            self.surface.blit(self.surface_image, (0, 0))
        if self.anchor == "top_right":
            self.surface.blit(self.surface_image, (-self.width_difference, 0))
        if self.anchor == "bottom_left":
            self.surface.blit(self.surface_image, (0, -self.height_difference))
        if self.anchor == "bottom_right":
            self.surface.blit(self.surface_image, (-self.width_difference, -self.height_difference))


    def animate_movement(self):
        self.current_animation = self.animation_controller[self.movement][self.direction_movement]
        
    def animate_action(self):
        self.current_animation = self.animation_controller[self.action][self.direction_action]
    