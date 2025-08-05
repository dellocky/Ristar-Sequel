import pygame
from scripts.library.objects.settings import settings
import os
import json

class video_menu:
    def __init__(self, display):
        self.finish = False
        self.display = display
        self.font = pygame.font.Font(None, 20)
        self.selected_rgb = (0, 255, 0)
        self.non_selected_rgb = (255, 255, 255)
        self.menu_items = ["Resolution"]
        self.selected_index = 0
        self.active_menu = False
        self.dropdown_open = None 
        self.dropdown_index = 0
        self.resolution_options = [
            (480, 270),
            (640, 360),
            (800, 450),
            (576, 1024),
            (1024, 576),
            (1280, 720),
            (1440, 810),
            (1680, 945),
            (1920, 1080),
            "Cancel"
        ]

    def run(self, event_list, delta_time, display):
        display.fill((0, 0, 20))
        menu_x = display.get_width() // 3
        menu_y = 40
        # Handle input
        if self.active_menu:
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if self.dropdown_open is None:
                        if event.key == pygame.K_UP:
                            self.selected_index = (self.selected_index - 1) % len(self.menu_items)
                        elif event.key == pygame.K_DOWN:
                            self.selected_index = (self.selected_index + 1) % len(self.menu_items)
                        if event.key == pygame.K_LEFT:
                            self.dropdown_open = None
                            self.active_menu = False
                        elif event.key == pygame.K_RETURN:
                            if self.menu_items[self.selected_index] == "Resolution":
                                self.dropdown_open = "resolution"
                                self.dropdown_index = 0
                            else:
                                print(f"Selected: {self.menu_items[self.selected_index]}")    
                    elif self.dropdown_open == "resolution":
                        if event.key == pygame.K_UP:
                            self.dropdown_index = (self.dropdown_index - 1) % len(self.resolution_options)
                        elif event.key == pygame.K_DOWN:
                            self.dropdown_index = (self.dropdown_index + 1) % len(self.resolution_options)
                        elif event.key == pygame.K_RETURN:
                            selected = self.resolution_options[self.dropdown_index]
                            if selected == "Cancel":
                                self.dropdown_open = None
                            else:
                                with open('config/settings/video_settings.json', 'r') as file:
                                    video_settings = json.load(file)
                                video_settings['resolution'] = tuple(selected)
                                with open('config/settings/video_settings.json', 'w') as file:
                                    json.dump(video_settings, file, indent=4)
                                settings.RESOLUTION = tuple(selected)
                                pygame.display.set_mode(settings.RESOLUTION)
                                self.dropdown_open = None

                        elif event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                            self.dropdown_open = None
                    
        # Render main menu
        for i, item in enumerate(self.menu_items):
            color = self.selected_rgb if i == self.selected_index and self.active_menu and self.dropdown_open is None else self.non_selected_rgb
            text_surface = self.font.render(item, True, color)
            y = menu_y + i * 40
            display.blit(text_surface, (menu_x - text_surface.get_width() // 2, y))

        # Render dropdown if open
        if self.dropdown_open == "resolution":
            dropdown_x = menu_x
            dropdown_y = menu_y + (self.selected_index + 1) * 20
            for j, option in enumerate(self.resolution_options):
                color = self.selected_rgb if j == self.dropdown_index else self.non_selected_rgb
                text = f"{option[0]}x{option[1]}" if isinstance(option, tuple) else str(option)
                text_surface = self.font.render(text, True, color)
                display.blit(text_surface, (dropdown_x - text_surface.get_width() // 2, dropdown_y + j * 12))