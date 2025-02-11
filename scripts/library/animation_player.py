
class animation_player:
    def __init__(self, folder_map, looping):
        
        self.folder_map = folder_map
        self.animation_time = 0
        self.folder_index = 0
        self.current_image = self.folder_map[self.folder_index][0]
        self.animation_change = False
        self.looping = looping

            
    
    def tic(self, delta_time):
        
        self.animation_time += delta_time
        if self.animation_time > self.folder_map[self.folder_index][1]:
            self.animation_time -= self.folder_map[self.folder_index][1]
            self.folder_index += 1
            if self.folder_index == len(self.folder_map):
                if self.looping == True:
                    self.folder_index = 0
                else: 
                    self.folder_index -= 1
                    return
            self.current_image = self.folder_map[self.folder_index][0]
            self.animation_change = True

    def reset(self):

        self.folder_index = 0
        self.animation_time = 0
        self.current_image = self.folder_map[self.folder_index][0]


    def get_image(self):
        
        self.current_image = self.folder_map[self.folder_index][0]
        return self.current_image
    
    def change_animation(self):
        self.animation_change = True