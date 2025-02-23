from scripts.library.settings import settings
import scripts.library.animation_player as animation_player
import pygame

class sprite():
    def __init__(self, name, pos, groups,  hitbox_rect_pos, hitbox_rect_size, surface_image, buffer = 0):      
    
        self.name = name
        self.groups = groups
        self.occlusion_rects = []
        #self.rgb = (255, 255, 255)
        self.surface_image = surface_image
        self.pos = pos
        self.hitbox_rect_pos = hitbox_rect_pos
        self.hitbox_surf = pygame.surface.Surface((hitbox_rect_size[0], hitbox_rect_size[1]))
        self.hitbox_rect = pygame.rect.Rect(hitbox_rect_pos[0], hitbox_rect_pos[1], hitbox_rect_size[0], hitbox_rect_size[1])
        self.hitbox_offset = (hitbox_rect_pos[0] - pos[0], hitbox_rect_pos[1] - pos[1])

        self.size = [self.surface_image.get_rect().width, self.surface_image.get_rect().height]
        self.default_height = self.size[1] + buffer
        self.height_difference = buffer
 
        self.surface = pygame.surface.Surface((self.size[0], self.size[1] + buffer), pygame.SRCALPHA)
        self.colorkey = (0, 0 ,1)
        self.surface.set_colorkey((self.colorkey))

        #Debugging Tools<----------------------------------------------------------------> 
        self.draw_hitbox_rect = False
        for I in groups:
            I.append(self)
        
            
    def create_animation(self, animation, dictionary, direction, looping = True):

        animation = animation_player.animation_player(animation, looping)
        dictionary[direction] = animation

    def animate(self, animation, delta_time):
        
        animation.tic(delta_time)
        if  animation.animation_change == True:
            self.surface_image = animation.current_image
            self.height_difference = self.surface_image.get_rect().height - self.default_height
            #self.hitbox_rect = self.surface_image.get_bounding_rect() #(midbottom=self.hitbox_rect.midbottom)
            #self.pos[1] = self.hitbox_rect.center[1]
            animation.animation_change = False
            #print(self.height_difference)
    
    def get_image(self, animation, index):

        animation.folder_index = index
        self.surface_image = self.current_animation.get_image()
        self.height_difference = self.surface_image.get_rect().height - self.default_height


    def reset_animations(self):

        for animations in self.animations_dict.values():
            for animation in animations.values():
                animation.reset()
        try: 
            self.surface_image = self.animations_dict[self.action][self.direction_animation].get_image()
        except:
            pass
    
    def create_occlusion_rect(self, pos_x, pos_y, width, height):
        self.occlusion_rects.append([[pos_x, pos_y], pygame.surface.Surface((width, height)), pygame.rect.Rect(pos_x, pos_y, width, height), [self.pos[0] - pos_x, self.pos[1] - pos_y]])
    
    def clear_occlusion_rects(self):
        self.occlusiuon_rects.clear()

    def run(self, event_loop, delta_time):
        self.surface.fill(self.colorkey)
        self.surface.blit(self.surface_image, (0, -(self.height_difference)))
        for occlusion in self.occlusion_rects:
            pygame.draw.rect(occlusion[1], self.colorkey, occlusion[2])
            self.surface.blit(occlusion[1], occlusion[0])

    def init(self):
        self.surface.fill(self.colorkey)
        self.surface.blit(self.surface_image, (0, -(self.height_difference)))
        for occlusion in self.occlusion_rects:
            pygame.draw.rect(occlusion[1], self.colorkey, occlusion[2])
            self.surface.blit(occlusion[1], occlusion[0])

   
    