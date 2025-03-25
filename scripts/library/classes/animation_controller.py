import scripts.library.functions.asset_import as asset_import
from scripts.library.classes.animation_player import animation_player
from os import walk

class animation_controller(dict):
    def __init__(self, path):
        super().__init__()
        path

    
    def create_actions(self, *args):
        for arg in args:
            self[arg] = {}


    def create_animation(self, animation_path, action_name, direction, animation_duration, looping = True, auto_play = True):
        animation_frames = asset_import.import_folder_with_time(animation_path, duration=animation_duration)
        animation = animation_player(animation_frames, looping, auto_play)
        self[action_name][direction] = animation
    
    def animate(self, animation, delta_time):
        if animation.auto_play == True:
            animation.tic(delta_time)
            if  animation.animation_change == True:
                surface_image = animation.current_image
                animation.animation_change = False
            return surface_image

    def reset_animations(self):
        for animations in self.values():
            for animation in animations.values():
                animation.reset()
    


     




