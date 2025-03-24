import pygame
from timeit import default_timer

pygame.init()
font=pygame.font.Font(None, 25)

def debug(surface, info, x=10 ,y=10):
    display_surface = surface
    debug_surf = font.render(str(info), True, "red")
    debug_rect = debug_surf.get_rect(topleft=(x,y))
    display_surface.blit(debug_surf,debug_rect)


def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        output = func(*args, **kwargs)
        end_time = default_timer()-start_time
        print(f"Function Time = {end_time}")
        return output
    return wrapper
