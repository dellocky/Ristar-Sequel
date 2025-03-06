from scripts.settings import settings
from scripts.library.occlusion import occlusion
#from scripts.layers import mask_layer
import scripts.library.animation_player as animation_player
import pygame

class sprite():
    def __init__(self, name, pos, groups,  hitbox_rect_pos, hitbox_rect_size, surface_image, buffer_leftup = [0, 0], buffer_downright = [0, 0]):      
    
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

        #self.mask = pygame.mask.from_surface(self.surface)
        self.occlude = False

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
            self.height_difference = self.surface_image.get_rect().height - self.height_default
            self.width_difference = self.surface_image.get_rect().width - self.width_default
            #self.hitbox_rect = self.surface_image.get_bounding_rect() #(midbottom=self.hitbox_rect.midbottom)
            #self.pos[1] = self.hitbox_rect.center[1]
            animation.animation_change = False
            #print(self.height_difference)
    
    def get_image(self, animation, index):

        animation.folder_index = index
        self.surface_image = self.current_animation.get_image()
        self.height_difference = self.surface_image.get_rect().height - self.height_default
        self.width_difference = self.surface_image.get_rect().width - self.width_default


    def reset_animations(self):

        for animations in self.animations_dict.values():
            for animation in animations.values():
                animation.reset()
        try: 
            self.surface_image = self.animations_dict[self.action][self.direction_animation].get_image()
        except:
            pass
    
    def create_occlusion_rect(self, pos_x, pos_y, width, height):
        #spirte_occlusion = occlusion(pos_x, pos_y, width, height)
        #base_surface = pygame.surface.Surface((width, height))
        spirte_occlusion = [[pos_x, pos_y], pygame.surface.Surface((width, height))]
        self.occlusion_rects.append(spirte_occlusion)
        #self.occlude = True
        return spirte_occlusion
    
    def resize_occlusion(self, index, dimensions):
        target_occlusion = self.occlusion_rects[index]
        self.occlusion_rects[index] = pygame.transform.smoothscale(target_occlusion, (dimensions[0], dimensions[1]))
        print("ahh")
        return target_occlusion
    
    def clear_occlusion_rects(self):
        self.occlusion_rects.clear()
        self.occlude = False

    def run(self, event_loop, delta_time):

        self.surface.fill((self.colorkey))
        self.surface.blit(self.surface_image, (self.width_difference + self.surface_image_position[0], -(self.height_difference) + self.surface_image_position[1]))
        for occlusion in self.occlusion_rects:
            occlusion[1].fill((self.colorkey))
            self.surface.blit(occlusion[1], occlusion[0])


    def update(self):
        self.surface.fill((self.colorkey))
        self.surface.blit(self.surface_image, (self.width_difference + self.surface_image_position[0], -(self.height_difference) + self.surface_image_position[1]))
        for occlusion in self.occlusion_rects:
            occlusion[1].fill((self.colorkey))
            self.surface.blit(occlusion[1], occlusion[0])
        #for occlusion in self.occlusion_rects:
            #pygame.draw.rect(occlusion.surface, self.colorkey, occlusion.rect)
            #self.surface.blit(occlusion.surface, occlusion.pos)

   
    