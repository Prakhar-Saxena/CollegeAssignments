#!/usr/bin/env python

import pygame
import config
import events
import eventtypes
import random
from os.path import join as join_path



pygame.font.init()
FONT = pygame.font.Font(None, 35)

def draw_string(screen, text, where):
    i = FONT.render(text, 2, (80, 0, 200, 155))
    screen.blit(i, where)

FONT2 = pygame.font.Font(None, 30)

def draw_string2(screen, text, where):
    i = FONT2.render(text, 2, (0, 0, 0, 255))
    screen.blit(i, where)



class Graphics(events.EventEnabled):
    """
    
    """
    
    def __init__(self):
        """
        
        """
        events.EventEnabled.__init__(self)
        self.screen = pygame.display.get_surface()
        self.world = config.world
        self.player_color = {}
        # color for each player (actually an index)
        idx = 0
        print ">>>>>>>>>Graphics:", config.players
        for player in config.players:
            self.player_color[player] = idx
            idx += 1
        # load tiles
        dir_path = join_path('data', 'images')
        tile_names = ['hexDGruen.PNG','hexGelb.PNG','hexHGruen.PNG', \
                      'hexOrange.PNG','hexRosa.PNG','hexRot.PNG', \
                      'hexTuerkis.PNG','hexViolette.PNG','hexSchwarz.PNG']
        self.tiles = []
        for name in tile_names:
            path = join_path(dir_path, name)
            img = pygame.image.load(path).convert()
            img.set_colorkey((0x80, 0x00, 0x80))
            self.tiles.append(img)
        # generate map image with borders
        self.map_img = None
        self.generate_borders()
                        
        random.shuffle(self.tiles[:-1])
        if len(self.tiles) != len(self.player_color):
            print "num tiles:", len(self.tiles), "num player:", len(self.player_color)
        self.current = None
##        self.reg_event_func(eventtypes.ATTACKRESULT, self.on_attack_result)
        self.reg_event_func(eventtypes.NEWTURN, self.on_newturn)
        events.RootEventSource().add_listener(self)
        
    def generate_borders(self):
        """
        
        """
        dir_path = join_path('data', 'images')
        # load borders
        border_names = ['hexBorder0.PNG','hexBorder1.PNG','hexBorder2.PNG', \
                      'hexBorder3.PNG','hexBorder4.PNG','hexBorder5.PNG']
        borders = []
        for name in border_names:
            path = join_path(dir_path, name)
            img = pygame.image.load(path).convert()
            img.set_colorkey((0x80, 0x00, 0x80))
            borders.append(img)
        self.map_img = pygame.Surface(self.world.grid.get_size()).convert()
        self.map_img.fill((0x80, 0x00, 0x80)) # fill with color_key
        self.map_img.set_colorkey((0x80, 0x00, 0x80))
        # draw borders
        num_cells = self.world.grid.get_num_cells()
        for posy in range(num_cells[1]):
            for posx in range(num_cells[0]):
                cell_land = self.world.cells[(posx, posy)]
                #get adj cells
                adj_cells = self.world.grid.get_adj_cells((posx, posy), True)
                # calculate position to blit
                blitx, blity = self.world.grid.grid_to_abs((posx, posy))
                # TODO: hack!!
                blitx -= self.world.grid._offset_x
                blity -= self.world.grid._offset_y
                # go through adj and check if they are from a different land
                for idx, adjcell in enumerate(adj_cells):
                    # check if cell is on map
                    if self.world.cells.has_key(adjcell):
                        if cell_land != self.world.cells[adjcell]:
                            self.map_img.blit(borders[idx], (blitx, blity))
                    else:
                        if cell_land:
                            self.map_img.blit(borders[idx], (blitx, blity))
##DEBUG                        
##                pygame.display.get_surface().fill((255, 255, 255))
##                pygame.display.get_surface().blit(self.map_img, (0,0))
##                pygame.display.flip()
##                pygame.event.wait()
        
        
    def update(self, chat):
        """
        
        """
        # draw the whole thing!
        # draw tile ons screen
        self.screen.fill((255, )*3)
        screen_blit = self.screen.blit
        tiles = self.tiles
        grid_toabs = self.world.grid.grid_to_abs
        for land in self.world._lands:
            for cell in land.cells:
                if land.selected:
                    screen_blit(tiles[-1], grid_toabs(cell))
                else:
                    player = land.get_player()
                    idx = self.player_color[player]
                    screen_blit(tiles[idx], grid_toabs(cell))
                    if player.get_id() == self.current:
                        screen_blit(tiles[idx], (730,350))
                        draw_string2(self.screen, "Player's turn:", (650, 300))
##            draw_string2(self.screen, str(land.get_id()), grid_toabs(land.cells[0]))
            # draw number of dices
        screen_blit(self.map_img, grid_toabs((0,0)))
        for land in self.world._lands:
            draw_string(self.screen, str(land.num_dice), grid_toabs(land.get_center_cell()))#cells[0]))
        screen_blit(chat.image, (50, 450))
        pygame.display.flip()

    def on_attack_result(self, event):
        """
        
        """
        print "attack result animation!!"
        return False
    
    def on_newturn(self, event):
        self.current = event.playerid