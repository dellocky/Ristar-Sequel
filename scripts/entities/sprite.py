from scripts.library.settings import settings
import scripts.library.animation_player as animation_player
import pygame

class sprite():
    def __init__(self, name, pos, hitbox_rect_pos, groups, hitbox_rect_size, buffer = 0) -> None:      
    
        self.name = name
        self.groups = groups
        self.rgb = (255, 255, 255)
        self.image_rect = None


        self.pos = pos
        self.hitbox_rect = pygame.rect.Rect(hitbox_rect_pos[0], hitbox_rect_pos[1], hitbox_rect_size[0], hitbox_rect_size[1])
        self.hitbox_offset = (hitbox_rect_pos[0] - pos[0], hitbox_rect_pos[1] - pos[1])
        try:
            self.default_height = self.surface_image.get_rect().height + buffer
            self.height_difference = 5
        except:
            pass
        #self.pos = self.hitbox_rect.midbottom

        #self.speed = .575

        for I in groups:
            I.append(self)
            
    def create_animation(self, animation, dictionary, direction, looping = True):

        animation = animation_player.animation_player(animation, looping)
        dictionary[direction] = animation

    def animate(self, animation, delta_time):
        
        animation.tic(delta_time)
        if  animation.animation_change == True:
            self.surface_image = animation.current_image
            self.height_difference = self.surface_image.get_rect().height - self.default_height# - 1
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
    


   
    