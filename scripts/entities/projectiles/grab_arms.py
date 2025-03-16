import pygame
from math import sqrt
from scripts.entities.sprite import sprite

class grab_arms():
    def __init__(self, pos, direction, groups):
        
        self.buffer_right = 45
        self.direction = direction
        self.pos_offset = [-24, 16]
        self.speed =[85, 0]

        self.buffer_right = 0
        self.buffer_left = 0
        self.buffer_up = 0
        self.buffer_down = 0
        
        self.occlusion_width = 46
        self.occlusion_height = 40

        self.occlusion_pos = [0, 0]
        
        arm_image_front = pygame.image.load("assets/pictures/projectiles/arms/front/right/0.png").convert_alpha()
        arm_image_back = pygame.image.load("assets/pictures/projectiles/arms/back/right/0.png").convert_alpha()

        if self.direction == "left":
            arm_image_front = pygame.image.load("assets/pictures/projectiles/arms/front/left/0.png").convert_alpha()
            arm_image_back = pygame.image.load("assets/pictures/projectiles/arms/back/left/0.png").convert_alpha()
            self.buffer_left = 45
            self.pos_offset = [-52, 16]
            self.speed = [-85, 0]
            
        if self.direction == "right":
            arm_image_front = pygame.image.load("assets/pictures/projectiles/arms/front/right/0.png").convert_alpha()
            arm_image_back = pygame.image.load("assets/pictures/projectiles/arms/back/right/0.png").convert_alpha()
            self.buffer_right = 45
            self.pos_offset = [-24, 16]
            self.speed = [85, 0]
        
        if self.direction == "upright":
            arm_image_front = pygame.image.load("assets/pictures/projectiles/arms/front/right/0.png").convert_alpha()
            arm_image_back = pygame.image.load("assets/pictures/projectiles/arms/back/right/0.png").convert_alpha()
            self.buffer_up = 30
            self.buffer_right = 45
            self.pos_offset = [-24, 0]
            self.speed = [85/sqrt(2), -85/sqrt(2)]


        self.action = "init"
        front = groups[0]
        back = groups[1]

        self.front_arms =  sprite("Arms_Front", [pos[0] - 3 + self.pos_offset[0], pos[1] + self.pos_offset[1] + 6], [front], pos, [5, 5], arm_image_front, 
                                   buffer_leftup = [self.buffer_left, self.buffer_up], buffer_downright=[self.buffer_right, self.buffer_down])
        self.back_arms =  sprite("Arms_Back", [pos[0] + self.pos_offset[0], pos[1] + self.pos_offset[1]], [back], pos, [5, 5], arm_image_back, 
                                   buffer_leftup = [self.buffer_left, self.buffer_up], buffer_downright=[self.buffer_right, self.buffer_down])
        
        if self.direction == "left":
            self.occlusion_pos[0] = self.front_arms.size[0]
        
        self.front_occlusion = self.front_arms.create_occlusion_rect(self.occlusion_pos[0], self.occlusion_pos[1], self.occlusion_width, self.occlusion_height)
        self.back_occlusion = self.back_arms.create_occlusion_rect(self.occlusion_pos[0], self.occlusion_pos[1], self.occlusion_width, self.occlusion_height)
        
        self.front_arms.update()
        self.back_arms.update()

        #self.base_front_occlusion_pos = (self.front_occlusion[0][0], self.front_occlusion[0][1])
        #self.base_back_occlusion_pos = (self.back_occlusion[0][0], self.back_occlusion[0][1])

        self.reverse = False
        self.destroy = False

        self.duration = 0.45
        self.duration_timer = 0

    def run(self, delta_time):

        if self.reverse == False and self.destroy == False:
            frame_movement = [self.speed[0] * delta_time, self.speed[1] * delta_time]
            self.duration_timer += delta_time
            if self.duration_timer >= self.duration:
                self.duration_timer -= self.duration
                self.reverse = True
                self.occlusions_cleared = True
            else:
                self.front_arms.surface_image_position[0] += frame_movement[0]
                self.back_arms.surface_image_position[0] += frame_movement[0]
                self.front_arms.surface_image_position[1] += frame_movement[1]
                self.back_arms.surface_image_position[1] += frame_movement[1]

        elif self.reverse == True and self.destroy == False:
            frame_movement = [-1 * self.speed[0] * delta_time, -1 * self.speed[1] * delta_time]
            self.duration_timer += delta_time
            if self.duration_timer >= self.duration:
                self.destroy = True
            else:
                self.front_arms.surface_image_position[0] += frame_movement[0]
                self.back_arms.surface_image_position[0] += frame_movement[0]
                self.front_arms.surface_image_position[1] += frame_movement[1]
                self.back_arms.surface_image_position[1] += frame_movement[1]

        self.front_arms.update()
        self.back_arms.update()
    
    def update_pos(self, pos):

        self.front_arms.pos = [pos[0] - 3 + self.pos_offset[0], pos[1] + self.pos_offset[1] + 6]
        self.back_arms.pos = [pos[0] + self.pos_offset[0], pos[1] + self.pos_offset[1]]
        

    

       
 
            
             

                
                
                
         
                





                

                 