import pygame
from math import floor
from scripts.entities.sprite import sprite

class grab_arms():
    def __init__(self, pos, direction, groups):
        
        self.buffer = 0
        self.buffer_right = 45
        self.pos = [pos[0] - 24 - self.buffer, pos[1] + 16]
        self.direction = direction
        self.action = "init"
        front = groups[0]
        back = groups[1]


        arm_image_front = pygame.image.load("assets/pictures/projectiles/arms/front/right/0.png").convert_alpha()
        arm_image_back = pygame.image.load("assets/pictures/projectiles/arms/back/right/0.png").convert_alpha()

        self.front_arms =  sprite("Arms_Front", [self.pos[0] - 3, self.pos[1] + 6], [front], self.pos, [5, 5], arm_image_front, 
                                  buffer_leftup=[self.buffer, 0], buffer_downright=[self.buffer_right, 0])
        self.back_arms =  sprite("Arms_Back", [self.pos[0], self.pos[1]], [back], self.pos, [5, 5], arm_image_back, 
                                 buffer_leftup=[self.buffer, 0], buffer_downright=[self.buffer_right, 0])

        self.front_surf_pos = [self.front_arms.pos[0], self.front_arms.pos[1]]
        self.back_surf_pos = [self.back_arms.pos[0], self.back_arms.pos[1]]

        self.occlusion_width = 40
        self.occlusion_width_max = self.occlusion_width - 2
        self.occlusion_height = 40

        self.total_movement_x = 0
        self.total_movement_y = 0
        
        self.front_occlusion = self.front_arms.create_occlusion_rect(self.buffer, 0, self.occlusion_width, self.occlusion_height)
        self.back_occlusion = self.back_arms.create_occlusion_rect(self.buffer, 0, self.occlusion_width, self.occlusion_height)
        
        self.front_arms.update()
        self.back_arms.update()

        #self.base_front_occlusion_pos = (self.front_occlusion[0][0], self.front_occlusion[0][1])
        #self.base_back_occlusion_pos = (self.back_occlusion[0][0], self.back_occlusion[0][1])
        
        self.base_front_arms_pos = (self.front_arms.pos[0], self.front_arms.pos[1])
        self.base_back_arms_pos = (self.back_arms.pos[0], self.back_arms.pos[1])

        self.reverse = False
        self.destroy = False

    def run(self, delta_time):

        if self.reverse == False and self.destroy == False:
            frame_movement = 50 * delta_time 
            self.total_movement_x += frame_movement
            if self.total_movement_x >= 39:
                self.reverse = True
                self.occlusions_cleared = True
            else:
                self.front_arms.surface_image_position[0] += frame_movement
                self.back_arms.surface_image_position[0] += frame_movement
                self.occlusion_width -= frame_movement
                #self.front_occlusion[0][0] = round(self.base_front_occlusion_pos[0] - self.total_movement_x)
                #self.back_occlusion[0][0] = round(self.base_back_occlusion_pos[0] - self.total_movement_x)
                #self.front_arms.resize_occlusion(0, (self.occlusion_width+100, self.occlusion_height))


             
        
        elif self.reverse == True and self.destroy == False:
            frame_movement = -50 * delta_time 
            self.total_movement_x += frame_movement
            if self.total_movement_x <= 0:
                self.destroy = True
            else:
                self.front_arms.surface_image_position[0] += frame_movement
                self.back_arms.surface_image_position[0] += frame_movement
                self.occlusion_width -= frame_movement
                #self.front_occlusion[0][0] = round(self.base_front_occlusion_pos[0] - self.total_movement_x)
                #self.back_occlusion[0][0] = round(self.base_back_occlusion_pos[0] - self.total_movement_x)
                #self.front_arms.resize_occlusion(0, (self.occlusion_width+100, self.occlusion_height))
        self.front_arms.update()
        self.back_arms.update()
    

       
 
            
             

                
                
                
         
                





                

                 