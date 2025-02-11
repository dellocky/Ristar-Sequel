import pygame, sys, scripts.library.debug as debug
from time import time
from scripts.levels.level_mananger import level_manager
from scripts.library.settings import settings


class game:
    def __init__(self):
        pygame.init()
        self.screen =  pygame.display.set_mode((1460, 810))
        self.display = pygame.Surface((480, 270))
        self.clock=pygame.time.Clock()
        self.previous_time = time()
        self.level_manager = level_manager(self.display)

    def run(self):
        while True:

            self.time = time()
            delta_time = self.time-self.previous_time
            self.previous_time = self.time
            event_list =  pygame.event.get()
            self.display.fill('white')
            self.level_manager.run(event_list, delta_time, self.display)

            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(settings.FPS)

if __name__ == '__main__':
    
    Game = game()
    Game.run()
    
    