from scripts.entities.sprite import sprite
from scripts.library.settings import settings
import scripts.library.logic as logic



class physics_sprite(sprite):
    def __init__(self, name, pos, hitbox_rect_size, groups, hitbox_rect_pos, buffer = 0) -> None:
        super().__init__(name, pos, hitbox_rect_size, groups, hitbox_rect_pos, buffer)
        self.count = 0

    def fall(self, delta_time):
        if self.current_velocity[1] < 1600:
            self.current_velocity[1] += 800 * delta_time

    def collision_detection_x(self):
        current_tiles = []
        coordinates = (int(self.hitbox_rect.left//settings.TILE_SIZE),int(self.hitbox_rect.top//settings.TILE_SIZE))
        for coordinate in logic.get_neighbors(coordinates):
            if coordinate in self.tile_map.keys():
                    self.collide_x(self.tile_map[coordinate])

    def collision_detection_y(self):
        current_tiles = []
        coordinates = (int(self.hitbox_rect.centerx//settings.TILE_SIZE),int(self.hitbox_rect.bottom//settings.TILE_SIZE))
        for coordinate in logic.get_neighbors(coordinates):
            if coordinate in self.tile_map.keys():
                    self.collide_y(self.tile_map[coordinate])
    
    def normalize_rects(self):
        self.hitbox_rect.center = ((self.pos[0]+(self.hitbox_rect.width/2)) - self.hitbox_offset[0], (self.pos[1]+(self.hitbox_rect.height/2) - self.hitbox_offset[1]))
    
    def normalize_pos(self):
        self.pos = ([self.hitbox_rect.topleft[0] + self.hitbox_offset[0], self.hitbox_rect.topleft[1] + self.hitbox_offset[1]])

    def move(self, current_velocity, delta_time):


                self.pos[0] = self.pos[0]+current_velocity[0]*delta_time
                self.normalize_rects()
                self.collision_detection_x()

                self.pos[1] = self.pos[1]+current_velocity[1]*delta_time
                self.normalize_rects()
                self.collide_ground = False
                self.collision_detection_y()
                
            
        #self.hitbox_rect.center = (self.pos[0]+(self.hitbox_rect.width/2),self.pos[1]+(self.hitbox_rect.height/2))
        
        #if self.image_rect:
            #self.image_rect.bottomleft = (self.pos[0]+(self.image_rect.width/2),self.pos[1]+(self.image_rect.height/2))

    
    def collide_x(self, entity):
        for rect in entity.hitbox_rects:
            if self.hitbox_rect.colliderect(rect):

                if self.current_velocity[0] > 0:
                    self.pos[0] = entity.hitbox_rect.left - self.hitbox_rect.width + self.hitbox_offset[0]
                    self.normalize_rects()
                    self.current_velocity[0] = 0
                
                if self.current_velocity[0] < 0:
                    self.pos[0] = entity.hitbox_rect.right + self.hitbox_offset[0]
                    self.normalize_rects()
                    self.current_velocity[0] = 0    
    
    def collide_y(self, entity):
        for rect in entity.hitbox_rects:
            if self.current_velocity[1] > 0:
                if entity.hitbox_rect.bottom > self.hitbox_rect.top:
                    if  entity.hitbox_rect.top <= self.hitbox_rect.bottom and entity.hitbox_rect.right > self.hitbox_rect.left and entity.hitbox_rect.left < self.hitbox_rect.right:
                        self.pos[1] = entity.hitbox_rect.top - self.hitbox_rect.height + self.hitbox_offset[1]
                        self.pos[1] = round(self.pos[1])
                        self.normalize_rects()
                        self.collide_ground = True
                        self.current_velocity[1] = 0

            if self.hitbox_rect.colliderect(rect):
                if self.current_velocity[1] < 0:
                    self.pos[1] = entity.hitbox_rect.bottom + self.hitbox_offset[1]
                    self.normalize_rects()
                    self.current_velocity[1] = 0    
                
                    

            


                

                        
                

                
            

    

