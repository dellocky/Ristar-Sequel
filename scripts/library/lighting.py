import library.custom_surfaces as custom_surfaces
import pygame
class lighting():

    def __init__(self, radius, brightness, pos, size, player_light_sprites) -> None:

        self.light_strength = brightness
        self.current_strength = self.light_strength
        self.color_multiplier = 1.5
        self.light_color = (self.current_strength*self.color_multiplier, self.current_strength, self.current_strength*self.color_multiplier)
        self.radius = radius
        self.size = size
        self.pos = pos
        self.lights = player_light_sprites
        self.display = pygame.display.get_surface()
        #self.pos = pos

        self.create_lights()
    
    def create_lights(self):

        self.lights.clear()
        self.light_number = round(self.radius/8)
        for I in range(self.light_number):
            
            occlusion = [None] * 2
            occlusion[0] = custom_surfaces.circle_surface(round(self.radius - (self.radius/self.light_number * (I + 1))), self.light_color)
            occlusion[0].hitbox_rect.x = self.pos[0] - occlusion[0].radius + (self.size/2)
            occlusion[0].hitbox_rect.y = self.pos[1] - occlusion[0].radius + (self.size/2)
            occlusion[1] = "sub"
            self.lights.append(occlusion)
  

            self.current_strength += self.light_strength
            self.light_color = (self.current_strength*self.color_multiplier, self.current_strength, self.current_strength*self.color_multiplier)

            light = [None] * 2
            light[0] = custom_surfaces.circle_surface(round(self.radius - (self.radius/self.light_number * I)), self.light_color)
            light[0].hitbox_rect.x = self.pos[0] - light[0].radius + (self.size/2)
            light[0].hitbox_rect.y = self.pos[1] - light[0].radius + (self.size/2)
            light[1] = "add"
            self.lights.append(light)
            
    

        self.current_strength = self.light_strength
        self.light_color = (self.current_strength*self.color_multiplier, self.current_strength, self.current_strength*self.color_multiplier)

    #def prepare_draw(self, pos):
        #for light in self.lights:
            #self.display.blit(light.surface, (pos[0] - light.radius + (self.size/2), pos[1] - light.radius + (self.size/2)), special_flags=pygame.BLEND_RGB_ADD)
            
        

        