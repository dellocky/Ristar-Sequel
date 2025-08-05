import pygame
from sys import exit

class main_menu:
    def __init__(self, display, return_to_index=None):
        self.finish = False
        self.display = display
        self.font = pygame.font.Font(None, 36)
        self.selected_rgb = (0, 255, 0)
        self.non_selected_rgb = (255, 255, 255)
        self.menu_items = ["Play", "Options", "Exit"]
        self.selected_index = return_to_index if return_to_index is not None else 0

    def run(self, event_list, delta_time, display):
        display.fill((0, 0, 0))  
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.menu_items)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:
                    if self.menu_items[self.selected_index] == "Play":
                        self.finish = True
                        self.new_level = 'rundune_1'  
                    elif self.menu_items[self.selected_index] == "Options":
                        self.finish = True
                        self.new_level = 'options_menu'
                    elif self.menu_items[self.selected_index] == "Exit":
                        pygame.quit()
                        exit()
                    else:
                        print(f"Selected: {self.menu_items[self.selected_index]}")  # Placeholder for actual game start logic

        # Render menu
        for i, item in enumerate(self.menu_items):
            color = self.selected_rgb if i == self.selected_index else self.non_selected_rgb
            text_surface = self.font.render(item, True, color)
            y = 50 + i * 60
            display.blit(text_surface, (display.get_width() // 2 - text_surface.get_width() // 2, y))