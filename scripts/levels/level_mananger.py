from scripts.levels.rundune.rundune_1 import rundune_1
from scripts.levels.rundune.rundune_2 import rundune_2
from scripts.levels.menus.main_menu import main_menu
from scripts.levels.menus.options_menu import options_menu

class level_manager: 
    def __init__(self, display):
        self.level_classes = {
            'main_menu':  main_menu,
            'options_menu': options_menu,
            'rundune_1':  rundune_1,
            'rundune_2':  rundune_2
        }
        self.display = display
        self.current_level_name = 'main_menu'
        self.current_level = self.create_level('main_menu')

    def create_level(self, level_name, **kwargs):
        instance = self.level_classes[level_name](self.display, **kwargs)
        return instance

    def run(self, event_list, delta_time, display):
        self.current_level.run(event_list, delta_time, display)
        if getattr(self.current_level, 'finish', False) == True:
            next_level_name = getattr(self.current_level, 'new_level', None)
            extra_kwargs = {}
            if self.current_level_name == 'options_menu' and next_level_name == 'main_menu':
                extra_kwargs = {'return_to_index': 1}
            self.current_level = self.create_level(next_level_name, **extra_kwargs)
            self.current_level_name = next_level_name

        
        
        
