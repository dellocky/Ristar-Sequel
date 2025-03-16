import scripts.library.asset_import as asset_import
from scripts.library.animation_player import animation_player

class animation_controller:
    def __init__(self):
        self.animations_dict = {}
        self.timer_dict = {}
    
    def create_actions(self, *args):
        for arg in args:
            self.animations_dict[arg] = {}


    def create_animation(self, animation_path, action_name, direction, animation_duration, looping = True):
        animation_frames = asset_import.import_folder_with_time(animation_path, duration=animation_duration)
        animation = animation_player(animation_frames, looping)
        self.animations_dict[action_name][direction] = animation
    
    def animate(self, animation, delta_time):
        animation.tic(delta_time)
        if  animation.animation_change == True:
            surface_image = animation.current_image
            animation.animation_change = False
        return surface_image

    def reset_animations(self):
        for animations in self.animations_dict.values():
            for animation in animations.values():
                animation.reset()
    


     




