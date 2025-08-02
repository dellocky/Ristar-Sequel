from scripts.levels.rundune.rundune_1 import rundune_1
from scripts.levels.rundune.rundune_2 import rundune_2
from scripts.levels.menus.main_menu import main_menu

class level_manager: 
    def __init__(self, display):
        
        self.tile_size = 32
        self.levels = {
            'main_menu':  main_menu(display),
            'rundune_1':  rundune_1(display),
            'rundune_2':  rundune_2()  
        }

        self.current_level = self.levels['main_menu'] 

    def run(self, event_list, delta_time, display):
        self.current_level.run(event_list, delta_time, display)
        if self.current_level.finish == True:
            old_level = self.current_level
            self.current_level = self.levels[self.current_level.new_level] 
            old_level.finish = False
        
        
        
