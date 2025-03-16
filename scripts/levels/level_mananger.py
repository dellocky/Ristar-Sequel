from scripts.levels.rundune.rundune_1 import rundune_1
from scripts.levels.rundune.rundune_2 import rundune_2

class level_manager: 
    def __init__(self, display):
        
        self.tile_size = 32
        self.levels = {
            'main_menu': 'soon.tm',
            'rundune_1':  rundune_1(display),
            'rundune_2':  rundune_2()  
        }

        self.current_level = self.levels['rundune_1'] 

    def run(self, event_list, delta_time, display):
        self.current_level.run(event_list, delta_time, display)
        
        
        
