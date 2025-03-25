import pygame
from scripts.entities.physics_sprite import physics_sprite
from scripts.entities.projectiles.grab_arms import grab_arms
from scripts.library.classes.animation_controller import animation_controller


class player(physics_sprite):
    def __init__(self, pos, self_groups, grab_arms_groups, tile_map):
        self.tile_map = tile_map
        self.grab_arms = False
        self.grab_arms_groups = grab_arms_groups

        self.direction_action = 'right'
        self.direction_movement = 'right'
        self.movement = 'idle'
        self.action = False
        
        self.walk_speed = 130
        self.current_velocity = [0, 0]
        self.jumps_maximum = 1
        self.jumps_current = 1

        time_walk =.082
        time_jump = time_walk * 2.4
        
        self.reset_delay = time_walk * 4
        self.reset_delay_timer = 0

        self.falling_delay = time_walk 
        self.falling_delay_timer = 0
    
        self.idle_delay = .12
        self.idle_delay_timer = 0

        self.movement_options = {
            "move" : True,
            "grab" : True,
            "jump" : True
        }

        self.animation_controller = animation_controller()
        self.animation_controller.create_actions("walking", "idle", "jumping", "falling" , "grabbing_ground", "grabbing_air")
        self.animation_controller.create_animation("assets/pictures/characters/player/walking/left", "walking", "left", time_walk)
        self.animation_controller.create_animation("assets/pictures/characters/player/walking/right", "walking", "right", time_walk)    
        self.animation_controller.create_animation("assets/pictures/characters/player/idle/left", "idle", "left", time_walk)            
        self.animation_controller.create_animation("assets/pictures/characters/player/idle/right", "idle", "right", time_walk)
        self.animation_controller.create_animation("assets/pictures/characters/player/jumping/left", "jumping", "left", time_jump, looping = False)
        self.animation_controller.create_animation("assets/pictures/characters/player/jumping/right", "jumping", "right", time_jump, looping = False)
        self.animation_controller.create_animation("assets/pictures/characters/player/falling/left", "falling", "left", time_jump, looping = False)
        self.animation_controller.create_animation("assets/pictures/characters/player/falling/right", "falling", "right", time_jump, looping = False)

        self.animation_controller.create_animation("assets/pictures/characters/player/grabbing_ground/left", "grabbing_ground", "left", 0, auto_play=False)            
        self.animation_controller.create_animation("assets/pictures/characters/player/grabbing_ground/right", "grabbing_ground", "right", 0, auto_play=False)
        self.animation_controller.create_animation("assets/pictures/characters/player/grabbing_ground/upleft", "grabbing_ground", "upleft", 0, auto_play=False)
        self.animation_controller.create_animation("assets/pictures/characters/player/grabbing_ground/upright", "grabbing_ground", "upright", 0, auto_play=False)
        self.animation_controller.create_animation("assets/pictures/characters/player/grabbing_ground/upupleft", "grabbing_ground", "upupleft", 0, auto_play=False)
        self.animation_controller.create_animation("assets/pictures/characters/player/grabbing_ground/upupright", "grabbing_ground", "upupright", 0, auto_play=False)
        

        super().__init__("Player", pos, self_groups, [pos[0] - 16, pos[1] - 15], [16, 30], self.animation_controller["walking"]["left"].current_image, buffer = [0, 9])

        self.animate_movement()
        #self.draw_hitbox_rect = True

    def input(self, event_loop, delta_time):
        
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        #Movement
        if self.movement_options["move"]:
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                self.current_velocity[0] = 0

            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.current_velocity[0] = -self.walk_speed
                self.direction_action = 'left'
                self.direction_movement =  'left'
                self.reset_delay_timer = 0
                self.idle_delay_timer = 0
    
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.current_velocity[0] = self.walk_speed
                self.direction_action = 'right'
                self.direction_movement = 'right'
                self.reset_delay_timer = 0
                self.idle_delay_timer = 0

            else:
                self.current_velocity[0] = 0
        
        #From Idle to Walking Animation---> 
        if self.movement == 'idle' and (self.current_velocity[0] != 0):
            self.movement = 'walking'
            self.animate_movement()
            self.current_animation.change_animation()
            self.reset_delay_timer = 0
            self.idle_delay_timer = 0
            #self.animation_controller.reset_animations()

        #From Walking to Idle Animation---> 
        elif self.movement == 'walking' and self.current_velocity[0] == 0: #and self.action == False:
            self.reset_delay_timer += delta_time
            self.idle_delay_timer += delta_time
            if self.idle_delay_timer >= self.idle_delay:
                self.movement = 'idle'
                self.animate_movement()
                self.current_animation.change_animation()
            if self.reset_delay_timer >= self.reset_delay:
                self.animation_controller.reset_animations()

        #Touching the Ground
        elif self.collide_ground and (self.movement == "falling" or self.movement == "jumping"):
            self.falling_delay_timer = 0
            if not self.movement_options["grab"]:
                    self.movement_options["move"] = False
                    self.current_velocity[0] = 0

            elif self.current_velocity[0] != 0:
                self.movement = "walking"
                self.animate_movement()
                self.current_animation.change_animation()
                self.animation_controller.reset_animations()

            else:
                self.movement = "idle"
                self.animate_movement()
                self.current_animation.change_animation()
                self.animation_controller.reset_animations()
            
        #Entering falling state
        if not self.collide_ground and self.current_velocity[1] > 0 and self.movement != "falling":
            self.falling_delay_timer += delta_time
            if self.falling_delay_timer >= self.falling_delay:
                self.movement = 'falling'
                self.animate_movement()
                self.animation_controller.reset_animations()
                self.current_animation.change_animation()

                
        #Jumping
        if keys[pygame.K_SPACE] and self.jumps_current > 0: 
            for event in event_loop:
                if event.type == pygame.KEYDOWN and event.key == 32 and self.collide_ground and self.movement_options['jump']:
                    self.current_velocity[1] = -240
                    self.movement = "jumping"
                    self.animate_movement()
                    self.current_animation.change_animation()
                    break
                    #self.jumps_current -= 1

        #Grabbing
        if keys[pygame.K_e]:
            for event in event_loop:
                if event.type == pygame.KEYDOWN and event.key == 101 and self.movement_options['grab']:
                    grab_direction = self.get_direction(keys)
                    if grab_direction:
                        if self.collide_ground:
                            if grab_direction == "downright":
                                grab_direction = "right"
                            elif grab_direction == "downleft":
                                grab_direction = "left"
                            elif grab_direction == "down":
                                grab_direction = self.direction_action
                                
                        self.direction_action = grab_direction
                    

                    self.grab_arms = grab_arms(self.pos, self.direction_action, self.grab_arms_groups)
                    #animation handling for upward grab based off direction player is facing
                    if self.direction_action == "up":
                        if self.direction_movement =="left":
                            self.direction_action = "upupleft"
                        if self.direction_movement =="right":
                            self.direction_action = "upupright"
                    
                    self.action = "grabbing_ground"
                    self.animate_action()
                            
                    self.movement_options['grab'] = False
                    self.movement_options['jump'] = False
                    if self.collide_ground:
                        self.movement_options['move'] = False
                        self.current_velocity[0] = 0

                    if self.direction_action == "left" or self.direction_action == "upleft" or self.direction_action == "upupleft":
                        self.anchor = "bottom_right"
                    break
         
    def get_direction(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                return "upleft"
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                return "downleft"
            else:
                return "left"
            
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                return "upright"
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                return "downright"
            else:
                return "right"
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            return "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            return "down"
        
        else: return False

    def kill_grab_arms(self):
        for group in self.grab_arms_groups:
                if len(group) > 0:
                    group.pop(0)
                self.grab_arms = False
                self.movement = "idle"
                self.movement_options['grab'] = True
                self.movement_options['move'] = True
                self.movement_options['jump'] = True
                self.animation_controller.reset_animations()
                self.direction_action = self.direction_movement
                self.action = False
                self.anchor = "bottom_left"



    def run(self, event_loop, delta_time):

        self.input(event_loop, delta_time)
        self.move(self.current_velocity, delta_time)
        self.surface.fill((0, 0, 2))
        self.custom_blit()

        if self.grab_arms:
            self.grab_arms.update_pos(self.pos)
            self.grab_arms.run(delta_time)
            if self.grab_arms.destroy == True:
                for group in self.grab_arms_groups:
                    self.kill_grab_arms()
    
        #self.animate_movement()
        try:
            if self.action:
                self.animate_action()
            else:
                self.animate_movement()
            self.surface_image = self.animation_controller.animate(self.current_animation, delta_time)
            self.update_image_offset()
        except:
            pass
 

        