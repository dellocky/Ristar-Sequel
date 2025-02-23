import pygame
from scripts.entities.sprite import sprite

class grab_arms():
    def __init__(self, pos, direction, groups):
        
        self.pos = [pos[0] - 24, pos[1] + 16]
        self.direction = direction
        front = groups[0]
        back = groups[1]

        arm_image_front = pygame.image.load("assets/pictures/projectiles/arms/front/right/0.png").convert_alpha()
        arm_image_back = pygame.image.load("assets/pictures/projectiles/arms/back/right/0.png").convert_alpha()

        self.front_arms =  sprite("Arms_Front", [self.pos[0] - 4, self.pos[1] + 6], [front], self.pos, [5, 5], arm_image_front)
        self.back_arms =  sprite("Arms_Back", [self.pos[0], self.pos[1]], [back], self.pos, [5, 5], arm_image_back)

        self.back_arms.create_occlusion_rect(0, 0, 42, 20)
        self.front_arms.create_occlusion_rect(0, 0, 42, 20)

        #self.front_arms.surface = pygame.transform.rotate(self.front_arms.surface, 180)
        #self.front_arms.surface_image = pygame.transform.rotate(self.front_arms.surface_image, 180)

        #self.front_arms.draw_hitbox_rect = True
        #self.back_arms.draw_hitbox_rect = True

        #self.draw_hitbox_rect = False
        #groups[0].append(self)


    
    def run(self, delta_time):

        pass
        #self.surface.fill((0, 0, 1))
        #self.surface.blit(self.front_arms.surface, (0, 0))
        #self.surface.blit(self.back_arms.surface, (0, 0))
        #self.surface.fill((200, 0, 1))
    
        