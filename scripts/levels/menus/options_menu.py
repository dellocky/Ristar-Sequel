import pygame
from scripts.levels.menus.option_menus.video_menu import video_menu

class options_menu:
    def __init__(self, display):
        self.finish = False
        self.display = display
        self.font = pygame.font.Font(None, 36)
        self.selected_rgb = (0, 255, 0)
        self.non_selected_rgb = (255, 255, 255)
        self.menu_items = ["Video", "Audio","Hotkeys", "Back"]
        self.selected_index = 0
        self.sub_menus = {
            "Video": video_menu,
            "Audio": None,
            "Hotkeys": None,
            "Back": None
        }
        self.border_width = 5
        self.active_menu = True
        self.sub_menu_surface = pygame.Surface(((display.get_width()/2) - self.border_width, display.get_height() - (self.border_width*2)))
        self.current_sub_menu = self.sub_menus[self.menu_items[self.selected_index]](self.sub_menu_surface)
        self.skip_submenu_enter = False

    def run(self, event_list, delta_time, display):
        display.fill((0, 0, 0))  
        for event in event_list:
            if self.active_menu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.menu_items)
                        if self.sub_menus[self.menu_items[self.selected_index]] != None:
                            self.current_sub_menu = self.sub_menus[self.menu_items[self.selected_index]](self.sub_menu_surface)
                        else:
                            self.current_sub_menu = None
                            self.sub_menu_surface.fill((0,0,0))
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.menu_items)
                        if self.sub_menus[self.menu_items[self.selected_index]] != None:
                            self.current_sub_menu = self.sub_menus[self.menu_items[self.selected_index]](self.sub_menu_surface)
                        else:
                            self.current_sub_menu = None
                            self.sub_menu_surface.fill((0,0,0))
                    elif event.key == pygame.K_RIGHT:
                        if self.current_sub_menu != None:
                            self.current_sub_menu.active_menu = True
                            self.active_menu = False
                            self.skip_submenu_enter = False
                    elif event.key == pygame.K_RETURN:
                        if self.menu_items[self.selected_index] == "Back":
                            self.finish = True
                            self.new_level = 'main_menu'
                            self.return_to_index = 1
                        else:
                            if self.current_sub_menu != None:
                                self.active_menu = False
                                self.current_sub_menu.active_menu = True
                                self.skip_submenu_enter = True

        # Render menu
        for i, item in enumerate(self.menu_items):
            color = self.selected_rgb if i == self.selected_index and self.active_menu else self.non_selected_rgb
            text_surface = self.font.render(item, True, color)
            y = 40 + i * 40
            display.blit(text_surface, (display.get_width() // 4 - text_surface.get_width() // 2, y))
        if self.current_sub_menu != None:
            filtered_events = event_list
            if self.skip_submenu_enter:
                filtered_events = [e for e in event_list if not (e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN)]
                self.skip_submenu_enter = False
            self.current_sub_menu.run(filtered_events, delta_time, self.sub_menu_surface)
            display.blit(self.sub_menu_surface, (display.get_width() // 2 , self.border_width))
            if self.current_sub_menu.active_menu == False:
                self.active_menu = True
                
        
