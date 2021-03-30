#!/usr/bin/env python


import config
import player
from player import Player
from gamelogic import GameLogic
from mapgenerator import MapGenerator
from graphics import Graphics
from gamestate import GameState
import events
import eventtypes
import pygame


# TODO: how to differ between singleplayer and multiplayer?
class Game(events.EventEnabled):
    """
    
    """
    # TODO: hack!!
    def __init__(self, chat):
        """
        
        """
        events.EventEnabled.__init__(self)
        self.gamestate = GameState()
        self.game_logic = GameLogic(self.gamestate)
        self.graphics = Graphics()
        self.event_source = events.RootEventSource()
        self.event_source.set_blocking(False)
        
        self.chat = chat
        self._running = True
        
        self.reg_event_func(pygame.QUIT, self.on_quit)
        self.reg_event_func(pygame.KEYDOWN, self.on_key)
        self.event_source.add_listener(self)
        
        self.clock = pygame.time.Clock()
        
    def run(self):
        """
        
        """
        # here comes the main loop of the game
        self._running = True
        while self._running:
            self.clock.tick(60)
            # update network
            # update events
            self.event_source.update()
            # update gamelogic
            # udpate gamestate
            self.gamestate.update()
            # update graphics (draw)
            self.graphics.update(self.chat)
        
        
    def on_quit(self, event):
        """
        
        """
        self._running = False
        
    def on_key(self, event):
        if event.key == pygame.K_F1:
            print self.clock.get_fps()
        elif event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        
#------testing---------#0000FF#FFFF00---------
if __name__=='__main__':
    
    # simulate the state after Multivote or Singleoptions
    import grids
    import os
    import diceland
    import random
    import gui
    import networkreplacement
    # init pygame and screen
    pygame.init()
    pygame.display.set_mode((1024,768))#, pygame.FULLSCREEN)
    # creade world
    oddlocator = pygame.image.load(os.path.join('data', 'images', 'oddLocator.PNG')).convert()
    evenlocator = pygame.image.load(os.path.join('data', 'images', 'evenLocator.PNG')).convert()
    grid = grids.HexagonGrid((30, 27), oddlocator, evenlocator,(100,10))
    config.world = MapGenerator()
    config.world.create(grid, diceland.DiceLandFactory(config.world), percent_grid_fill=0.8)
    # players
    for i in range(8):
        p = Player(i)
        p.revert_to_type(player.HUMAN)
        if i >= 2:
            p.revert_to_type(player.AI_DUMB)
        elif i>=6:
            p.revert_to_type(player.AI_1)
        config.players.append(p)
    # set player to lands
    num_land = len(config.world._lands)/len(config.players)
    print "num_region:", num_land
    #TODO: hack!!
    lands = list(config.world._lands)
    player = None
    for player in config.players:
        for num in range(num_land):
##        chosen = random.sample(lands, num_land)
            chosen = [random.choice(lands)]
            for land in chosen:
                land.set_player(player)
                dices = random.randint(2,8)
                print "adding dices:", dices
                land.set_num_dice(dices)
                lands.remove(land)
                random.shuffle(lands)
    # set dice per land
    if len(lands)>0:
        for land in lands:
            dices = random.randint(2,8)
            print "adding dices:", dices
            land.set_num_dice(dices)
            land.set_player(random.choice(config.players))
            
    # gui
    chat = gui.ChatModul("your_nick")
    networkreplacement.NetworkReplacement()
    # new start the game
    game = Game(chat)
    eventtypes.post_start_game(game)
##    eventtypes.post_new_turn(game, config.players[0].player_id)
    game.run()