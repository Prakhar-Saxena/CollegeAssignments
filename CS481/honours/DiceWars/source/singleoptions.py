#!/usr/bin/env python


import sys
sys.path.insert(0,'..')
import os
import random

import pygame

import events
import eventtypes
import gui
import game
import grids
import diceland
import networkreplacement
import player
import config
from player import Player
##from gamelogic import GameLogic
from mapgenerator import MapGenerator


class Singleoptions(events.EventEnabled):
    """
    
    """
    
    
    def __init__(self):
        """
        
        """
        events.EventEnabled.__init__(self)
        font = pygame.font.Font(None, 25)
        self.font = font
        # create gui elements
        self.buttons = []
        self.buttons.append(gui.Button(font, "randomize map", (50,350), self.rand_map))
        self.buttons.append(gui.Button(font, "randomize lands", (200,350), self.rand_lands))
        self.buttons.append(gui.Button(font, "exit", (500,350), self.quit))
        self.buttons.append(gui.Button(font, "start", (600,350), self.start_game))
        
        self.spinners = []
        self.texts = []
        # number of players
        xpos = 500
        ypos = 30
        self.texts.append(gui.Text("number of Players: ", font, (xpos, ypos)))
        spinner = gui.Spinner(font, (xpos + 180,ypos), False)
        for num in range(2, 9):
            spinner.add(gui.Item(str(num), num))
        spinner.register_observer(self)
        self.spinners.append(spinner)
        # player config
        self.items = []
        self.items.append(gui.Item("human", player.HUMAN))
        self.items.append(gui.Item("passive AI", player.AI_PASSIVE))
        self.items.append(gui.Item("expander AI", player.AI_DUMB))
        self.items.append(gui.Item("AI 1", player.AI_1))
        self.items.append(gui.Item("none", None))
        for num in range(2):
            ypos += 30
            spinner = gui.Spinner(font, (xpos + 100, ypos))
            if num==2:
                self.items.insert(0, self.items.pop(-1))
            for item in self.items:
                spinner.add(item)
##            spinner.register_observer(self)
            self.spinners.append(spinner)
            self.texts.append(gui.text.Text("Player "+str(num+1)+": ", font, \
                                                                (xpos, ypos)))
        self.texts.append(gui.text.Text( \
            "Quick instructions", font, (10, 460)))
        self.texts.append(gui.text.Text( \
            "right click to end turn, left click to select lands", font, \
                                                                    (10, 500)))
        self.texts.append(gui.text.Text( \
            "you have to first select a own land with more than 1 dice on it, then you can attack an", font, (10, 530)))
        self.texts.append(gui.text.Text( \
             "ajectant land of different color"        , font, (10, 560)))

        # data
        self._running = True
        self._preview = pygame.Surface((0,0))
        self._preview.fill((255,255,255))
        
        # events
        self.reg_event_func(pygame.KEYDOWN, self.on_keydown)
        self.reg_event_func(pygame.QUIT, self.quit)
        for spinner in self.spinners:
            events.RootEventSource().add_listener(spinner)
        for button in self.buttons:
            events.RootEventSource().add_listener(button)
        self.setup_map()
            
            
    def setup_map(self):
        # map
        # creade world
        oddlocator = pygame.image.load(os.path.join('data', 'images', 'oddLocator.PNG')).convert()
        evenlocator = pygame.image.load(os.path.join('data', 'images', 'evenLocator.PNG')).convert()
        grid = grids.HexagonGrid((30, 27), oddlocator, evenlocator,(50,10))
        config.world = MapGenerator()
        config.world.create(grid, diceland.DiceLandFactory(config.world), percent_grid_fill=0.8)
        # players
        config.players = []
        for num in range(self.spinners[0].get_current_value()):
            config.players.append(Player(num))
        self.rand_lands()
        self.gen_map_preview()

    
    def on_keydown(self, event):
        """
        
        """
        if event.key == pygame.K_ESCAPE:
            print "singleoptions quit: esc"
            self.quit()
    
    def quit(self, event=None):
        """
        
        """
        self._running = False
        
    def start_game(self):
        """
        
        """
        old = events.RootEventSource().remove_all_listeners()
        events.RootEventSource().clear()
        
        
        # revert players to player type
        for idx, player in enumerate(config.players):
            player.revert_to_type(self.spinners[idx+1].get_current_value())
        # 1 dice per land, minimum
        for land in config.world.get_lands():
            land.set_num_dice(1)
        # additional dices per player
        num_dice = len(config.world.get_lands())*2
        player_num_dice = num_dice / len(config.players) + 1
        
            
        print "starting game"
        chat = gui.ChatModul("your_nick")
        networkreplacement.NetworkReplacement()
        # new start the game
        g = game.Game(chat)
        eventtypes.post_start_game(g)
        g.run()
        
        events.RootEventSource().remove_all_listeners()
        events.RootEventSource().clear()
        
        self.rand_lands()
        self.setup_map()
        events.RootEventSource().set_all_listeners(old)
        
    def rand_map(self):
        """
        
        """
        print "randomizing"
        config.world.randomize()
        self.rand_lands()
        self.gen_map_preview()
        
    def rand_lands(self):
        """
        
        """
        print "randomizing lands"
        num_players = self.spinners[0].get_current_value()
        lands = list(config.world.get_lands())
        player_num_lands = len(lands) / num_players
        rest = len(lands) % num_players
        for player in config.players:
            for num in range(player_num_lands):
                land = random.choice(lands)
                land.set_player(player)
                lands.remove(land)
        for num in range(rest):
            player = random.choice(config.players)
            land = lands.pop()
            land.set_player(player)
        self.gen_map_preview()
            
        
    def gen_map_preview(self, zoom = 0.6):
        """
        returns an preview image with given size.
        """
        map_img = pygame.Surface(config.world.grid.get_size()).convert()
        map_img.fill((0x80, 0x00, 0x80)) # fill with color_key
        
        # color for each player (actually an index)
        idx = 0
        player_color = {}
        for player in config.players:
            player_color[player] = idx
            idx += 1

        # load tiles
        dir_path = os.path.join('data', 'images')
        tile_names = ['hexDGruen.PNG','hexGelb.PNG','hexHGruen.PNG', \
                      'hexOrange.PNG','hexRosa.PNG','hexRot.PNG', \
                      'hexTuerkis.PNG','hexViolette.PNG','hexSchwarz.PNG']
        tiles = []
        for name in tile_names:
            path = os.path.join(dir_path, name)
            img = pygame.image.load(path).convert()
            img.set_colorkey((0x80, 0x00, 0x80))
            tiles.append(img)
        screen_blit = map_img.blit
        grid_toabs = config.world.grid.grid_to_abs
        for land in config.world.get_lands():
            for cell in land.cells:
                if land.selected:
                    screen_blit(tiles[-1], grid_toabs(cell))
                else:
                    player = land.get_player()
                    idx = player_color[player]
                    blitx, blity = grid_toabs(cell)
                    blitx -= config.world.grid._offset_x
                    blity -= config.world.grid._offset_y
                    screen_blit(tiles[idx], (blitx, blity))
##                    if player.get_id() == self.current:
##                        screen_blit(tiles[idx], (512,650))
##                        draw_string2(self.screen, "Player:", (450, 650))

        
        # generate borders
        dir_path = os.path.join('data', 'images')
        # load borders images
        border_names = ['hexBorder0.PNG','hexBorder1.PNG','hexBorder2.PNG', \
                      'hexBorder3.PNG','hexBorder4.PNG','hexBorder5.PNG']
        borders = []
        for name in border_names:
            path = os.path.join(dir_path, name)
            img = pygame.image.load(path).convert()
            img.set_colorkey((0x80, 0x00, 0x80))
            borders.append(img)
        # draw borders
        num_cells = config.world.grid.get_num_cells()
        for posy in range(num_cells[1]):
            for posx in range(num_cells[0]):
                cell_land = config.world.cells[(posx, posy)]
                #get adj cells
                adj_cells = config.world.grid.get_adj_cells((posx, posy), True)
                # calculate position to blit
                blitx, blity = config.world.grid.grid_to_abs((posx, posy))
                # TODO: hack!!
                blitx -= config.world.grid._offset_x
                blity -= config.world.grid._offset_y
                # go through adj and check if they are from a different land
                for idx, adjcell in enumerate(adj_cells):
                    # check if cell is on map
                    if config.world.cells.has_key(adjcell):
                        if cell_land != config.world.cells[adjcell]:
                            map_img.blit(borders[idx], (blitx, blity))
                    else:
                        if cell_land:
                            map_img.blit(borders[idx], (blitx, blity))
        # return result
        map_img = pygame.transform.rotozoom(map_img, 0, zoom).convert()
        map_img.set_colorkey((0x80, 0x00, 0x80))
        self._preview = map_img

    def notify(self, subject):
        """
        
        """
##        print "notify from: ", subject, " value: ", subject.get_current_value()
        if subject == self.spinners[0]:
            if len(self.spinners)-1 > subject.get_current_value():
                spinner = self.spinners.pop()
                spinner.remove_observer(self)
                events.RootEventSource().remove_listener(spinner)
                self.texts.pop()
                config.players.pop()
                self.rand_lands()
            elif len(self.spinners)-1 < subject.get_current_value(): 
                # add new spinner for player
                xpos, ypos = self.spinners[-1].position
                spinner = gui.Spinner(self.font, (xpos, ypos+30))
                for item in self.items:
                    spinner.add(item)
                events.RootEventSource().add_listener(spinner)
                self.spinners.append(spinner)
                self.texts.append(gui.Text("Player "+str(len(self.spinners)-1)+\
                                    ": ", self.font, (xpos - 100, ypos + 30)))
                config.players.append(Player(len(self.spinners)-1))
                self.rand_lands()
        
    def run(self):
        """
        
        """
        screen = pygame.display.get_surface()
        screen.fill((0,0,0))
        while self._running:
            events.RootEventSource().update()
            for button in self.buttons:
                screen.blit(button.image, button.position)
            for spinner in self.spinners:
                screen.blit(spinner.image, spinner.position)
            for text in self.texts:
                screen.blit(text.image, text.position)
                
            screen.blit(self._preview, (20,20))
            pygame.display.flip()
            screen.fill((0,0,0))
            

def main():
    # simulate the state after Multivote or Singleoptions
    # init pygame and screen
    pygame.init()
    pygame.display.set_caption('Dice Wars')
    logo = pygame.image.load(os.path.join('data', 'images', 'logo32x32.png'))
    pygame.display.set_icon(logo)
    pygame.display.set_mode((800,600))#, pygame.FULLSCREEN)
##    # creade world
##    oddlocator = pygame.image.load(os.path.join('data', 'images', 'oddLocator.PNG')).convert()
##    evenlocator = pygame.image.load(os.path.join('data', 'images', 'evenLocator.PNG')).convert()
##    grid = grids.HexagonGrid((30, 27), oddlocator, evenlocator,(100,10))
##    config.world = MapGenerator()
##    config.world.create(grid, diceland.DiceLandFactory(config.world), percent_grid_fill=0.8)
    options = Singleoptions()
    events.RootEventSource().add_listener(options)
    events.RootEventSource().set_blocking(True)
    options.run()


if __name__=='__main__':
    main()