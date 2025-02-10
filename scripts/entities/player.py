import pygame
import scripts.library.asset_import as asset_import
#from scripts.library.animation_player import animation_player
from scripts.entities.physics_sprite import physics_sprite


class player(physics_sprite):
    def __init__(self, pos, groups, tile_map):

        time_walk =.092
   
        self.walk_speed = 90
        self.current_velocity = [0, 0]
        self.jumps_maximum = 1
        self.jumps_current = 1
     
        self.collide_ground = False

        self.tile_map = tile_map
        self.direction_movement = 'right'
        self.direction_animation = 'right'
        self.movement = 'idle'
        self.action = 'none'
        #down_idle_animation = asset_import.import_folder_with_time("assets/characters/main/idle/down", "main_idle_down")
        
                                                                      #assets/pictures/characters/player/walking/left/player_walking_left
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
        for I, animation in enumerate(left_idle_animation):
             animation[1] = time_walk 

        right_jumping_animation = asset_import.import_folder_with_time("assets/pictures/characters/player/jumping/right")
        for I, animation in enumerate(right_idle_animation):
             animation[1] = time_walk 

     

        self.animations_dict = {}

        self.walking_animations = {}
        self.idle_animations = {}

        self.animations_dict["walking"] = self.walking_animations
        self.animations_dict["idle"] = self.idle_animations

        self.create_animation(right_walking_animation, self.walking_animations, "right")
        self.create_animation(left_walking_animation, self.walking_animations, "left")
        
        self.create_animation(right_idle_animation, self.idle_animations, "right")
        self.create_animation(left_idle_animation, self.idle_animations, "left")

        self.surface_image = left_walking_animation[0][0]
        self.surface = pygame.surface.Surface((50, 50))
        self.surface.set_colorkey((0, 0, 1))
        super().__init__("Player", pos, [pos[0] - 16, pos[1] - 10], groups, [16, 30])

        print(self.hitbox_rect.topleft)
        print(self.hitbox_offset)
        print(self.pos)


    def input(self, event_loop):
        
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.current_velocity[0] = 0

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.current_velocity[0] = -self.walk_speed
            self.direction_movement = 'left'
            self.direction_animation = 'left'

  
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.current_velocity[0] = self.walk_speed
            self.direction_movement = 'right'
            self.direction_animation = 'right'

        else:
            self.current_velocity[0] = 0
       
        if self.movement == 'idle' and (self.current_velocity[0] > 0 or self.current_velocity[0] < 0):
            self.movement = 'walking'
            self.reset_animations()
        
        elif self.movement == 'walking' and self.action == 'none' and self.current_velocity[0] == 0:
            self.movement = 'idle'
            self.reset_animations
        
        if keys[pygame.K_SPACE] and self.jumps_current > 0: #save processing power unless input detected, eventloop needed to prevent hold down
            for event in event_loop:
                if event.type == pygame.KEYDOWN and event.key == 32:
                    print("jump")
                    self.current_velocity[1] = -215
                    #self.jumps_current -= 1
            
            
    def run(self, event_loop, delta_time):

        self.input(event_loop)
        self.move(self.current_velocity, delta_time)
        self.surface.fill((0, 0, 1))
        self.surface.blit(self.surface_image, (0, -(self.height_difference))) 
        try:
            if self.action == "none":
                self.animate(self.animations_dict[self.movement][self.direction_animation], delta_time)
            else:
                self.animate(self.animations_dict[self.action][self.direction_animation], delta_time)
        except:
            pass

        