import pygame
import scripts.library.asset_import as asset_import
#from scripts.library.animation_player import animation_player
from scripts.entities.physics_sprite import physics_sprite



class player(physics_sprite):
    def __init__(self, pos, self_groups, grab_arms_groups, tile_map):

        self.tile_map = tile_map
        self.direction_movement = 'right'
        self.direction_animation = 'right'
        self.movement = 'idle'
        self.action = 'none'
        
        self.walk_speed = 130
        self.current_velocity = [0, 0]
        self.jumps_maximum = 1
        self.jumps_current = 1
        self.collide_ground = False

        time_walk =.082
        time_jump = time_walk * 2.4
        
        self.reset_delay = time_walk
        self.reset_delay_timer = 0

        self.falling_delay = time_walk
        self.falling_delay_timer = 0
    
        self.idle_delay = .05
        self.idle_delay_timer = 0

        self.can_grab = True
        left_walking_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/walking/left")
        for I, animation in enumerate(left_walking_animation):
            animation[1] = time_walk 

        right_walking_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/walking/right")
        for I, animation in enumerate(right_walking_animation):
             animation[1] = time_walk 

        
        left_idle_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/idle/left")
        for I, animation in enumerate(left_idle_animation):
             animation[1] = time_walk 

        right_idle_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/idle/right")
        for I, animation in enumerate(right_idle_animation):
             animation[1] = time_walk 

        left_jumping_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/jumping/left")
        for I, animation in enumerate(left_jumping_animation):
             animation[1] = time_jump 

        right_jumping_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/jumping/right")
        for I, animation in enumerate(right_jumping_animation):
             animation[1] = time_jump 

        left_falling_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/falling/left")
        for I, animation in enumerate(left_falling_animation):
             animation[1] = time_jump 

        right_falling_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/falling/right")
        for I, animation in enumerate(right_falling_animation):
             animation[1] = time_jump

        self.animations_dict = {}

        self.walking_animations = {}
        self.idle_animations = {}
        self.jumping_animations = {}
        self.falling_animations = {}

        self.animations_dict["walking"] = self.walking_animations
        self.animations_dict["idle"] = self.idle_animations
        self.animations_dict["jumping"] = self.jumping_animations
        self.animations_dict["falling"] = self.falling_animations

        self.create_animation(right_walking_animation, self.walking_animations, "right")
        self.create_animation(left_walking_animation, self.walking_animations, "left")
        
        self.create_animation(right_idle_animation, self.idle_animations, "right")
        self.create_animation(left_idle_animation, self.idle_animations, "left")

        self.create_animation(right_jumping_animation, self.jumping_animations,  "right", looping = False)
        self.create_animation(left_jumping_animation, self.jumping_animations, "left", looping = False)

        self.create_animation(right_falling_animation, self.falling_animations,  "right", looping = False)
        self.create_animation(left_falling_animation, self.falling_animations, "left", looping = False)

        super().__init__("Player", pos, self_groups, [pos[0] - 16, pos[1] - 15], [16, 30], left_walking_animation[0][0], buffer = 9)

        self.current_animation = self.animations_dict[self.movement][self.direction_animation]

    def input(self, event_loop, delta_time):
        
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.current_velocity[0] = 0

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            
            if self.movement == "falling" and self.current_velocity[0] >= 0:
                self.animations_dict[self.movement][self.direction_animation].animation_change = True
                 
            self.current_velocity[0] = -self.walk_speed
            self.direction_movement = 'left'
            self.direction_animation = 'left'
            self.idle_delay_timer = 0
   
            

  
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
           
            if self.movement == "falling" and self.current_velocity[0] <= 0:
                  self.animations_dict[self.movement][self.direction_animation].animation_change = True
                
            self.current_velocity[0] = self.walk_speed
            self.direction_movement = 'right'
            self.direction_animation = 'right'
            self.reset_delay_timer = 0
            self.idle_delay_timer = 0

        else:
            self.current_velocity[0] = 0
       
        if self.movement == 'idle' and (self.current_velocity[0] > 0 or self.current_velocity[0] < 0):
            self.movement = 'walking'
            self.current_animation = self.animations_dict[self.movement][self.direction_animation]
            self.current_animation.change_animation()
            self.reset_delay_timer = 0
            self.idle_delay_timer = 0
            #self.reset_animations()

        elif self.movement == 'walking' and self.current_velocity[0] == 0:
            self.reset_delay_timer += delta_time
            self.idle_delay_timer += delta_time
            if self.idle_delay_timer >= self.idle_delay:
                self.movement = 'idle'
                self.current_animation = self.animations_dict[self.movement][self.direction_animation]
                self.current_animation.change_animation()
            if self.reset_delay_timer >= self.reset_delay:
                self.reset_animations()
        
        if self.collide_ground == False and self.current_velocity[1] > 0 and self.movement != "falling":
            self.falling_delay_timer += delta_time
            if self.falling_delay_timer >= self.falling_delay:
                self.movement = 'falling'
                self.current_animation = self.animations_dict[self.movement][self.direction_animation]
                self.reset_animations()
                self.current_animation.change_animation()
            
        elif self.collide_ground == True and (self.movement == "falling" or self.movement == "jumping"):
            self.falling_delay_timer = 0
            if self.current_velocity[0] != 0:
                self.movement = "walking"
                self.current_animation = self.animations_dict[self.movement][self.direction_animation]
                self.current_animation.change_animation()
                self.reset_animations()
            else:
                self.movement = "idle"
                self.current_animation = self.animations_dict[self.movement][self.direction_animation]
                self.current_animation.change_animation()
                self.reset_animations()

                
        
        if keys[pygame.K_SPACE] and self.jumps_current > 0: #save processing power unless input detected, eventloop needed to prevent hold down
            for event in event_loop:
                if event.type == pygame.KEYDOWN and event.key == 32 and self.collide_ground == True:
                    self.current_velocity[1] = -240
                    self.movement = "jumping"
                    self.current_animation = self.animations_dict[self.movement][self.direction_animation]
                    self.current_animation.change_animation()
                    #self.jumps_current -= 1

        if keys[pygame.K_e]:
            for event in event_loop:
                if event.type == pygame.KEYDOWN and event.key == 101 and self.can_grab == True:
                    print("grab")
                    
            
            
    def run(self, event_loop, delta_time):

        self.input(event_loop, delta_time)
        self.move(self.current_velocity, delta_time)
        self.surface.fill((0, 0, 1))
        if self.draw_hitbox_rect == True:
            pygame.draw.rect(self.hitbox_surf, (0, 0, 255), self.hitbox_rect)
            self.surface.blit(self.hitbox_surf, (-self.hitbox_offset[0], -self.hitbox_offset[1]))
        self.surface.blit(self.surface_image, (0, -(self.height_difference)))
 
        #self.current_animation = self.animations_dict[self.movement][self.direction_animation]
        try:
            self.current_animation = self.animations_dict[self.movement][self.direction_animation]
            if self.action == "none":
                self.animate(self.current_animation, delta_time)
            else:
                self.animate(self.current_animation, delta_time)
        except:
            pass

        