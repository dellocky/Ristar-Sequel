from scripts.entities.player import player
from scripts.library.sprite_group import sprite_group
from scripts.library.camera import camera
from scripts.library.debug import debug, get_time
from scripts.entities.objects.sprite_object import sprite_object
import scripts.library.asset_import as asset_import
from scripts.library.settings import settings


class rundune_1:
    def __init__(self, display):

        self.entity_sprites = sprite_group()
        self.wall_sprites = sprite_group()

        self.tile_size = settings.TILE_SIZE
        self.tile_map = {}
        self.create_map()

        self.player = player([0, 0], [self.entity_sprites], self.tile_map)
        self.camera = camera(display, self.player)
        self.create_map()

    def create_map(self):

        layouts = {
            'Ground' : asset_import.csv_layout('map_layout/testmap.csv')
        }

        graphics= {
            'Ground' : asset_import.import_folder('assets/pictures/tiles')
        }
        
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    x = col_index
                    y = row_index 
                    if col != '-1':
                        if style == 'Ground':
                            #print([int(col)][1])
                            surf = graphics['Ground'][int(col)]
                            sprite = sprite_object(graphics['Ground'][int(col)],(x * self.tile_size ,y * self.tile_size),[self.wall_sprites], [self.tile_size, self.tile_size], surf)
                            self.tile_map[(x, y)] = sprite
        
        #tiles = sorted(self.tile_map.items(), key=operator.itemgetter(0))
        #for tile in tiles:
            #print(tile[1].pos)

        
    def draw(self, display):
        self.camera.draw(display, self.wall_sprites)
        self.camera.draw(display, self.entity_sprites)

    def run(self, event_list, delta_time, display):
        self.entity_sprites.run('run', event_list, delta_time)
        self.entity_sprites.run('fall', delta_time)
        self.draw(display)
        #print(self.player.pos)
