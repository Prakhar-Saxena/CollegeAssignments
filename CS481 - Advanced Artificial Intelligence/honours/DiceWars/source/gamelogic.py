#!/usr/bin/env python


import events
from eventtypes import *
import config
import random

# TODO: remove all print

class GameLogic(events.EventEnabled):
    """
    
    """
    
    def __init__(self, gamestate):
        """
        
        """
        events.EventEnabled.__init__(self)
        self.state = gamestate
        self.selection = None
        self.reg_event_func(ENDTURN, self.on_endturn)
        self.reg_event_func(SELECT, self.on_select)
        self.reg_event_func(STARTGAME, self.on_startgame)
        self.reg_event_func(CONNINTERRUPT, self.on_connectioninterrupt)
        self.reg_event_func(DROPDICE, self.on_drop_dice)
        events.RootEventSource().add_listener(self)
        
        
#---eventmethods---##ffff00
    def on_endturn(self, event):
        """
        
        """
        if self.state.state != 1:
            print "Game is not in playing."
            return
        # deliver dices
        lands = list(self.state.current_player.get_lands())
        num_dices = len(lands)
        
##        print "<====================================>"
##        for l in lands: print l.get_id(), l.num_dice

        # remove all full lands
        for land in list(lands):
            if land.num_dice == 8:
                lands.remove(land)
                
##        print "--------------after remove-------------"
##        for l in lands: print l.get_id(), l.num_dice
##        print "____________________________"
        
        after_lands = {} # save modified lands
        # add dices to remaining lands
        for num in range(num_dices):
            # do it only if a land remains on the list
            if len(lands):
                # chose a land
                
##                print "------------------------------------"
##                for land in lands:
##                    print land.get_id(), land.num_dice

                land = random.choice(lands)
                # get the number of dices of that land, if modified look it up
                if after_lands.has_key(land.get_id()):
                    num_dices_land = after_lands[land.get_id()]
                else:
                    num_dices_land = land.num_dice
                # add one dice
                num_dices_land += 1
                # save for look up and send
                after_lands[land.get_id()] = num_dices_land
                
##                print "land", land.get_id(), "has now", num_dices_land, "dices", after_lands

                # remove land if number of dices is 8
                if num_dices_land == 8:
                    lands.remove(land)
                    
        # only send if anything changed
##        if len(after_lands): 
        post_drop_dice(self, after_lands)
        
        #remove selection
        if self.selection:
            self.selection.selected = False
            self.selection = None
        
    def on_drop_dice(self, event):
        """
        
        """
        # turn rotation
        players = self.state.get_alive_players()
        idx = players.index(self.state.current_player)
        idx += 1
        if idx >= len(players):
            idx = 0
        post_new_turn(self, players[idx].get_id())
        
    def on_select(self, event):
        """
        
        """
        if self.state.get_player_by_id(event.playerid) != self.state.current_player:
            return 
        land = self.state.get_land_by_id(event.landid)
        # first select?
        if self.selection is None:
            # is it cur_palyer land?
            if land.get_player() != self.state.current_player:
                print "land does not belong to current player."
                post_select_result(self, land.get_id(), 2) # not possible
                return False
            # has it more than 1 dice
            if land.num_dice < 2:
                print "land has only 1 dice!."
                post_select_result(self, land.get_id(), 2) # not possible
                return False
            # has it adj lands to attack?
            pot_defensors = []
            for lnk in land.get_linked_lands():
                if lnk.get_player() != self.state.current_player:
                    pot_defensors.append(lnk)
            if len(pot_defensors) == 0:
                print "land has no adj land to attack."
                post_select_result(self, land.get_id(), 2) # not possible
                return False
            # -> SELECTRESULT
            self.selection = land
            post_select_result(self, event.landid, 0) #ok
        
        else:
        # second select
            # belongs it to same player?
            if land.get_player() == self.state.current_player:
                # same as selection? -> deselect -> SELECTRESULT
                if self.selection == land:
                    self.selection = None
                    post_select_result(self, event.landid, 1) #deselect
                    return False
                else:
                    print "Cant select two land of same player, selection:",self.selection.get_id(),"land:", land.get_id()
                    post_select_result(self, land.get_id(), 2) # not possible
                    return False
            # is it adj to first selection?
            if land not in self.selection.get_linked_lands():
                print "land is not adj to the selection, selection:",self.selection.get_id(), "not adj", land.get_id()
                post_select_result(self, land.get_id(), 2) # not possible
                return False
            # perform attack
            self.attack(self.selection, land)
            # -> SELECTRESULT
            # deselct all
            post_select_result(self, event.landid, 1)
            post_select_result(self, self.selection.get_id(), 1)
            self.selection = None
        
    def on_startgame(self, event):
        """
        
        """
        for player in self.state.players:
            player.dead = False
        post_new_turn(self, self.state.players[0].get_id())
        
    def on_connectioninterrupt(self, event):
        """
        
        """
        pass
        
##    def on_event(self, event):
##        print "gamelogic:"
##        print event
##        return False
    
#---methods---##ffff00
    def attack(self, aggressor, defensor):
        """
        
        """
        # roll dice
        aggr_pips , aggr_sum = aggressor.roll_dice()
        def_pips, def_sum = defensor.roll_dice()
        
        # -> RESULT
        post_attack_result(self, aggressor.get_id(), defensor.get_id(), \
                                ((aggr_pips, aggr_sum),(def_pips, def_sum)))
                                
        print aggressor.get_id(), "attacked", defensor.get_id()," result:", aggr_sum,":", def_sum, "    ", aggr_pips,":", def_pips
        
        if aggr_sum > def_sum:
            # aggressor wins
            # check if player dead
            if len(defensor.get_player().get_lands()) == 1:
                print "gamelogic: player", defensor.get_player().get_id(),"is dead"
                post_player_dead(self, defensor.get_player().get_id())
            
                # check if player wins
                if len(self.state.get_alive_players()) == 2:
                    print "gamelogic: player", aggressor.get_player().get_id(), "wins"
                    post_player_win(self, aggressor.get_player().get_id())
                    print "gamelogic: post end game!"
                    post_end_game(self)
