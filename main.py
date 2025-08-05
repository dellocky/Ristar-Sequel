import pygame, sys, scripts.library.functions.debug as debug
from time import time
from scripts.levels.level_mananger import level_manager
from scripts.library.objects.settings import settings
from os import environ
environ['SDL_VIDEO_CENTERED'] = '1'

class game:
    def __init__(self):
        pygame.init()
        self.screen =  pygame.display.set_mode(settings.RESOLUTION)
        pygame.display.set_caption(settings.WINDOW_NAME)
        pygame.display.set_icon(pygame.image.load('assets/icon.ico'))
        self.display = pygame.Surface((400, 225))
        self.clock=pygame.time.Clock()
        self.previous_time = time()
        self.level_manager = level_manager(self.display)

    def run(self):
        while True: 
            
            self.time = time()
            delta_time = self.time-self.previous_time
            self.previous_time = self.time
            event_list =  pygame.event.get()
            self.display.fill((255, 255, 255)) 
            self.level_manager.run(event_list, delta_time, self.display)

            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            #debug.debug(self.screen, self.clock.get_fps())# display fps with this
            pygame.display.update()
            self.clock.tick(settings.FPS)
   

if __name__ == '__main__':
    
    Game = game()
    Game.run()
    
    