import pygame
from math import sqrt
from scripts.entities.sprite import sprite

class grab_arms():
    # Direction configurations
    BASE_SPEED = 250
    DIRECTION_CONFIG = {
        "ground":{
        "left": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/left/0.png",
                "back": "assets/pictures/projectiles/arms/back/left/0.png"
            },
            "buffers": {"left": 45, "right": 0, "up": 0, "down": 0},
            "pos_offset": [-63, 19],
            "speed": [BASE_SPEED, 0],
            "arm_stagger": [4, 6],
            "occlusion_size": [48, 40],
            "anchor": "bottom_right"
     
        },
        "right": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/right/0.png",
                "back": "assets/pictures/projectiles/arms/back/right/0.png"
            },
            "buffers": {"left": 45, "right": 0, "up": 0, "down": 0},
            "pos_offset": [-16, 19],
            "speed": [BASE_SPEED, 0],
            "arm_stagger": [-3, 6],
            "occlusion_size": [48, 40],
            "anchor": "bottom_left"
        },
        "up": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/left/0.png",
                "back": "assets/pictures/projectiles/arms/back/left/0.png"
            },
            "buffers": {"left": 0, "right": 0, "up": 45, "down": 0},
            "pos_offset": [-52, 61],
            "speed": [0, BASE_SPEED],
            "arm_stagger": [4, 6],
            "occlusion_size": [46, 40],
            "anchor": "bottom_left" 
        },
        "down": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/right/0.png",
                "back": "assets/pictures/projectiles/arms/back/right/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 0, "down": 0},
            "pos_offset": [-24, 16],
            "speed": [BASE_SPEED, 0],
            "arm_stagger": [-3, 6],
            "occlusion_size": [46, 40],
            "anchor": "bottom_left" 
        },
        "upright": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upright/0.png",
                "back": "assets/pictures/projectiles/arms/back/upright/0.png"
            },
            "buffers": {"left": 31, "right": 0, "up": 31, "down": 0},
            "pos_offset": [-6, -22],
            "speed": [round(BASE_SPEED/sqrt(2)), round(BASE_SPEED/sqrt(2))],
            "arm_stagger": [-5, 5],
            "occlusion_size": [46, 40],
            "anchor": "bottom_left" 
        },
        "upleft": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upleft/0.png",
                "back": "assets/pictures/projectiles/arms/back/upleft/0.png"
            },
            "buffers": {"left": 31, "right": 0, "up": 31, "down": 0},
            "pos_offset": [-31, -22],
            "speed": [round(BASE_SPEED/sqrt(2)), round(BASE_SPEED/sqrt(2))],
            "arm_stagger": [5, 5],
            "occlusion_size": [46, 40],
            "anchor": "bottom_right" 
        },
        "downright": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upright/0.png",
                "back": "assets/pictures/projectiles/arms/back/upright/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 30, "down": 0},
            "pos_offset": [0, -43],
            "speed": [BASE_SPEED/sqrt(2), -BASE_SPEED/sqrt(2)],
            "arm_stagger": [-5, 5],
            "occlusion_size": [46, 40],
            "anchor": "bottom_left" 
        },
        "downleft": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upleft/0.png",
                "back": "assets/pictures/projectiles/arms/back/upleft/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 30, "down": 0},
            "pos_offset": [-36, -43],
            "speed": [-BASE_SPEED/sqrt(2), -BASE_SPEED/sqrt(2)],
            "arm_stagger": [5, 5],
            "occlusion_size": [46, 40],
            "anchor": "bottom_right" 
        }
    },
        "air":{
        "left": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/left/0.png",
                "back": "assets/pictures/projectiles/arms/back/left/0.png"
            },
            "buffers": {"left": 45, "right": 0, "up": 0, "down": 0},
            "pos_offset": [-61, 10],
            "speed": [BASE_SPEED, 0],
            "arm_stagger": [4, 6],
            "occlusion_size": [48, 40],
            "anchor": "bottom_right"
     
        },
        "right": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/right/0.png",
                "back": "assets/pictures/projectiles/arms/back/right/0.png"
            },
            "buffers": {"left": 45, "right": 0, "up": 0, "down": 0},
            "pos_offset": [-20, 10],
            "speed": [BASE_SPEED, 0],
            "arm_stagger": [-3, 6],
            "occlusion_size": [48, 40],
            "anchor": "bottom_left"
        },
        "up": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/left/0.png",
                "back": "assets/pictures/projectiles/arms/back/left/0.png"
            },
            "buffers": {"left": 45, "right": 0, "up": 0, "down": 0},
            "pos_offset": [-52, 16],
            "speed": [-BASE_SPEED, 0],
            "arm_stagger": [4, 6],
            "occlusion_size": [46, 40],
            "anchor": "bottom_left" 
        },
        "down": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/right/0.png",
                "back": "assets/pictures/projectiles/arms/back/right/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 0, "down": 0},
            "pos_offset": [-24, 16],
            "speed": [BASE_SPEED, 0],
            "arm_stagger": [-3, 6],
            "occlusion_size": [46, 40],
            "anchor": "bottom_left" 
        },
        "upright": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upright/0.png",
                "back": "assets/pictures/projectiles/arms/back/upright/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 30, "down": 0},
            "pos_offset": [-6, -28],
            "speed": [round(BASE_SPEED/sqrt(2)), round(BASE_SPEED/sqrt(2))],
            "arm_stagger": [-5, 5],
            "occlusion_size": [46, 40],
            "anchor": "bottom_left" 
        },
        "upleft": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upleft/0.png",
                "back": "assets/pictures/projectiles/arms/back/upleft/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 30, "down": 0},
            "pos_offset": [-31, -28],
            "speed": [round(BASE_SPEED/sqrt(2)), round(BASE_SPEED/sqrt(2))],
            "arm_stagger": [5, 5],
            "occlusion_size": [46, 40],
            "anchor": "bottom_right" 
        },
        "downright": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upright/0.png",
                "back": "assets/pictures/projectiles/arms/back/upright/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 30, "down": 0},
            "pos_offset": [0, -43],
            "speed": [BASE_SPEED/sqrt(2), -BASE_SPEED/sqrt(2)],
            "arm_stagger": [-5, 5],
            "occlusion_size": [46, 40],
            "anchor": "bottom_left" 
        },
        "downleft": {
            "image_paths": {
                "front": "assets/pictures/projectiles/arms/front/upleft/0.png",
                "back": "assets/pictures/projectiles/arms/back/upleft/0.png"
            },
            "buffers": {"left": 30, "right": 0, "up": 30, "down": 0},
            "pos_offset": [-36, -43],
            "speed": [-BASE_SPEED/sqrt(2), -BASE_SPEED/sqrt(2)],
            "arm_stagger": [5, 5],
            "occlusion_size": [46, 40],
            "anchor": "bottom_right" 
        }   
    }
    }

    def __init__(self, pos, state, direction, groups):
        if direction not in self.DIRECTION_CONFIG[state]:
            raise ValueError(f"Invalid direction: {direction}")
            
        config = self.DIRECTION_CONFIG[state][direction]

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
        self.anchor = config["anchor"]
        self.occlusion_width = config["occlusion_size"][0]
        self.occlusion_height = config["occlusion_size"][1]

        self.reverse = False
        self.destroy = False
        pixels = 44
        self.duration = pixels/self.BASE_SPEED
        self.duration_timer = 0
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
            [10, 10],  # Small hitbox for intersection point
            arm_image_front,
            buffer_leftup=[self.buffer_left, self.buffer_up],
            buffer_downright=[self.buffer_right, self.buffer_down],
            anchor = self.anchor
        )
        self.front_arms.draw_hitbox_rect = True
        self.hitbox_rect = self.front_arms.hitbox_rect  # Store reference to hitbox for easy access
        
        self.back_arms = sprite(
            "Arms_Back", 
            back_pos, 
            [back], 
            pos, 
            [0, 0], 
            arm_image_back,
            buffer_leftup=[self.buffer_left, self.buffer_up],
            buffer_downright=[self.buffer_right, self.buffer_down],
            anchor = self.anchor)
        
        if self.anchor == "top_left":
            front_occ_x = 0
            back_occ_x = 0
            front_occ_y = 0
            back_occ_y = 0

        elif self.anchor == "top_right":
            front_occ_x = self.front_arms.surface.get_width() - self.occlusion_width
            back_occ_x = self.back_arms.surface.get_width() - self.occlusion_width
            front_occ_y = 0
            back_occ_y = 0

        
        elif self.anchor == "bottom_left":
            front_occ_x = 0
            back_occ_x = 0
            front_occ_y = self.front_arms.surface.get_height() - self.occlusion_height
            back_occ_y = self.back_arms.surface.get_height() - self.occlusion_height
        
        elif self.anchor == "bottom_right":
            front_occ_x = self.front_arms.surface.get_width() - self.occlusion_width
            back_occ_x = self.back_arms.surface.get_width() - self.occlusion_width
            front_occ_y = self.front_arms.surface.get_height() - self.occlusion_height
            back_occ_y = self.back_arms.surface.get_height() - self.occlusion_height

        self.front_occlusion = self.front_arms.create_occlusion_rect(
            front_occ_x,
            front_occ_y,
            self.occlusion_width, 
            self.occlusion_height,
        )   
        self.back_occlusion = self.back_arms.create_occlusion_rect(
            back_occ_x,
            back_occ_y,
            self.occlusion_width, 
            self.occlusion_height,
        )
        #self.front_arms.visible = False
        #self.back_arms.visible = False
        # Initialize state
        self.front_arms.update_difference()
        self.back_arms.update_difference()
        self.front_arms.update()
        self.back_arms.update()

    def run(self, delta_time):
        

        if self.reverse == False and self.destroy == False:
            frame_movement = [self.speed[0] * delta_time, self.speed[1] * delta_time]
            self.duration_timer += delta_time
            if self.duration_timer >= self.duration:
                self.duration_timer -= self.duration
                self.reverse = True
                self.occlusions_cleared = True
            else:
                self.front_arms.image_offset[0] += frame_movement[0]
                self.back_arms.image_offset[0] += frame_movement[0]
                self.front_arms.image_offset[1] += frame_movement[1]
                self.back_arms.image_offset[1] += frame_movement[1]

        elif self.reverse == True and self.destroy == False:
            frame_movement = [-1 * self.speed[0] * delta_time, -1 * self.speed[1] * delta_time] 
            self.duration_timer += delta_time
            if self.duration_timer >= self.duration:
                self.destroy = True
            else:
                self.front_arms.image_offset[0] += frame_movement[0]
                self.back_arms.image_offset[0] += frame_movement[0]
                self.front_arms.image_offset[1] += frame_movement[1]
                self.back_arms.image_offset[1] += frame_movement[1]

        # Use copies to avoid mutating the original offsets (which causes glitches)
        front_arms_true_offset = list(self.front_arms.image_offset)
        back_arms_true_offset = list(self.back_arms.image_offset)

        if self.anchor == "top_right":
            front_arms_true_offset[0] = self.front_arms.image_offset[0] * -1
            back_arms_true_offset[0] = self.back_arms.image_offset[0] * -1
        elif self.anchor == "bottom_left":
            front_arms_true_offset[1] = self.front_arms.image_offset[1] * -1
            back_arms_true_offset[1] = self.back_arms.image_offset[1] * -1
        elif self.anchor == "bottom_right":
            front_arms_true_offset[0] = self.front_arms.image_offset[0] * -1
            back_arms_true_offset[0] = self.back_arms.image_offset[0] * -1
            front_arms_true_offset[1] = self.front_arms.image_offset[1] * -1
            back_arms_true_offset[1] = self.back_arms.image_offset[1] * -1

        front_center = [
            self.front_arms.pos[0] + front_arms_true_offset[0] + self.front_arms.surface.get_width() // 2,
            self.front_arms.pos[1] + front_arms_true_offset[1] + self.front_arms.surface.get_height() // 2
        ]
        back_center = [
            self.back_arms.pos[0] + back_arms_true_offset[0] + self.back_arms.surface.get_width() // 2,
            self.back_arms.pos[1] + back_arms_true_offset[1] + self.back_arms.surface.get_height() // 2
        ]

        intersection_x = (front_center[0] + back_center[0]) // 2
        intersection_y = (front_center[1] + back_center[1]) // 2

        self.hitbox_rect.x = intersection_x - 7
        self.hitbox_rect.y = intersection_y - 6
         
        self.front_arms.update()
        self.back_arms.update()
    
    def update_pos(self, pos):

        self.front_arms.pos = [pos[0] + self.arm_stagger[0] + self.pos_offset[0], pos[1] + self.pos_offset[1] + self.arm_stagger[1]]
        self.back_arms.pos = [pos[0] + self.pos_offset[0], pos[1] + self.pos_offset[1]]
    
    def update_offset(self, target):
        self.pos_offset = self.DIRECTION_CONFIG[target][self.direction]["pos_offset"]
        self.front_arms.update()
        self.back_arms.update()
        

    

       
 
            
             
