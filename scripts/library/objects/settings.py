import json
from random import randint

with open('config/save_files/account_save_file.json', 'r') as file:
    account_save_file_data = json.load(file) 
    generate_window_name = bool(account_save_file_data['generate_window_name'])

print(generate_window_name)
class Settings:
    def __init__(self):
        self.TILE_SIZE = 32
        self.FPS = 80
        if generate_window_name:
            with open('config/misc/window_names.txt', 'r') as file:
                possible_window_names = file.readlines()
            index = randint(0, len(possible_window_names) - 1)
            self.WINDOW_NAME = possible_window_names[index].strip()
        else:
            self.WINDOW_NAME = "Ristar Sequel"
            account_save_file_data['generate_window_name'] = True
            with open('config/save_files/account_save_file.json', 'w') as file:
                json.dump(account_save_file_data, file, indent=4)

settings = Settings()





