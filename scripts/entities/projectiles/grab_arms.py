import pygame
from math import sqrt
from scripts.entities.sprite import sprite

class grab_arms():
    # Direction configurations
    speed = 100
    DIRECTION_CONFIG = {
        "left": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/left/0.png",
                "back": "assets/pictures/projectiles/arms/back/left/0.png"
            },
            "buffers": {"left": 45, "right": 0, "up": 0, "down": 0},
            "pos_offset": [-52, 16],
            "speed": [-speed, 0],
            "arm_stagger": [4, 6],
            "occlusion_offset": [82, 0] 
        },
        "right": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/right/0.png",
                "back": "assets/pictures/projectiles/arms/back/right/0.png"
            },
            "buffers": {"left": 0, "right": 45, "up": 0, "down": 0},
            "pos_offset": [-24, 16],
            "speed": [speed, 0],
            "arm_stagger": [-3, 6],
            "occlusion_offset": [-2, 0]
        },
        "upright": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upright/0.png",
                "back": "assets/pictures/projectiles/arms/back/upright/0.png"
            },
            "buffers": {"left": 0, "right": 30, "up": 30, "down": 0},
            "pos_offset": [0, -43],
            "speed": [speed/sqrt(2), -speed/sqrt(2)],
            "arm_stagger": [-5, 5],
            "occlusion_offset": [0, 67]
        },
        "upleft": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upleft/0.png",
                "back": "assets/pictures/projectiles/arms/back/upleft/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 30, "down": 0},
            "pos_offset": [-36, -43],
            "speed": [-speed/sqrt(2), -speed/sqrt(2)],
            "arm_stagger": [5, 5],
            "occlusion_offset": [0, 67]
        }
    }

    def __init__(self, pos, direction, groups):
        if direction not in self.DIRECTION_CONFIG:
            raise ValueError(f"Invalid direction: {direction}")
            
        config = self.DIRECTION_CONFIG[direction]

        arm_image_front = pygame.image.load(config["image_paths"]["front"]).convert_alpha()
        arm_image_back = pygame.image.load(config["image_paths"]["back"]).convert_alpha()
        
        self.direction = direction
        self.buffer_right = config["buffers"]["right"]
        self.buffer_left = config["buffers"]["left"]
        self.buffer_up = config["buffers"]["up"]
        self.buffer_down = config["buffers"]["down"]
        self.pos_offset = config["pos_offset"]
        self.speed = config["speed"]
        self.arm_stagger = config["arm_stagger"]
        
        self.occlusion_width = 48
        self.occlusion_height = 40
        self.occlusion_pos = [0, 0]
        
        self.action = "init"
        front, back = groups[0], groups[1]

        front_pos = [pos[0] + self.pos_offset[0] + self.arm_stagger[0], 
                    pos[1] + self.pos_offset[1] + self.arm_stagger[1]]
        back_pos = [pos[0] + self.pos_offset[0], 
                   pos[1] + self.pos_offset[1]]
        
        # Create sprites
        self.front_arms = sprite(
            "Arms_Front", 
            front_pos, 
            [front], 
            pos, 
            [5, 5], 
            arm_image_front,
            buffer_leftup=[self.buffer_left, self.buffer_up],
            buffer_downright=[self.buffer_right, self.buffer_down]
        )
        
        self.back_arms = sprite(
            "Arms_Back", 
            back_pos, 
            [back], 
            pos, 
            [5, 5], 
            arm_image_back,
            buffer_leftup=[self.buffer_left, self.buffer_up],
            buffer_downright=[self.buffer_right, self.buffer_down]
        )
        
        # Set occlusion position based on direction (using addition)
        self.occlusion_pos = config["occlusion_offset"]

        # Create occlusion rectangles
        self.front_occlusion = self.front_arms.create_occlusion_rect(
            self.occlusion_pos[0], 
            self.occlusion_pos[1], 
            self.occlusion_width, 
            self.occlusion_height
        )
        self.back_occlusion = self.back_arms.create_occlusion_rect(
            self.occlusion_pos[0], 
            self.occlusion_pos[1], 
            self.occlusion_width, 
            self.occlusion_height
        )
        
        # Initialize state
        self.front_arms.update()
        self.back_arms.update()
        self.reverse = False
        self.destroy = False
        self.duration = 0.3
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

        self.front_arms.pos = [pos[0] + self.arm_stagger[0] + self.pos_offset[0], pos[1] + self.pos_offset[1] + self.arm_stagger[1]]
        self.back_arms.pos = [pos[0] + self.pos_offset[0], pos[1] + self.pos_offset[1]]
        

    

       
 
            
             

                
                
                
         
                





                

                 