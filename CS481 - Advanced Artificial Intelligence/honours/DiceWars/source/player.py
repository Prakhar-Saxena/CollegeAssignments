#!/usr/bin/env python

import events
import pygame
import config
import eventtypes
import random

# TODO: rewrite it: Player should be a fassade, then divert to 
#       Human, Ai, Network

# ---define different types of players----##ffff00
HUMAN = 0
NETWORK = 1
AI_PASSIVE = 2
AI_DUMB = 3
AI_1 = 4


class Player(events.EventEnabled):
    """
    Player of the game. It will hold some information about the player like 
    which lands he posses.
    """

    def __init__(self, player_id):
        """
        id should be a unique id.
        """
        events.EventEnabled.__init__(self)
        self._lands = []
        self._player_id = player_id

        self.dead = False

        self._myturn = False

        self._implementation = None

        ##        self.revert_to_type(HUMAN)

        # register event functions
        # TODO: perhaps this should be done when entering 
        #       Multigame or Singlegame
        self.reg_event_func(eventtypes.NEWTURN, self.on_newturn)

        # register at a dispatcher, here source
        events.RootEventSource().add_listener(self)

    ##        print "player init", self.parent

    def get_id(self):
        """
        Returns the id of the player.
        """
        return self._player_id

    def add_land(self, land):
        """
        Add a land to this player and this player is set at the land too.
        """
        if land not in self._lands:
            self._lands.append(land)
            land.set_player(self)

    def get_lands(self):
        """
        Returns a list of all lands owned by this player.
        """
        return self._lands

    def remove_land(self, land):
        """
        Removes the land from this player.
        """
        if land in self._lands:
            self._lands.remove(land)
            land.set_player(None)

    def revert_to_type(self, type):
        # TODO: rename that to revert_to_type(self, type)
        """
        Reverts this player to an AI player of difficulty (0 easy, 0< harder)
        """
        ##        print "reverting to type", type
        if type == HUMAN:
            self._implementation = Human(self)
        elif type == NETWORK:
            self._implementation = Network(self)
        elif type == AI_PASSIVE:
            self._implementation = AiPassive(self)
        elif type == AI_DUMB:
            self._implementation = AiDumb(self)
        elif type == AI_1:
            self._implementation = Ai1(self)

    def unreg_all_events(self):
        """
        
        """
        self.unreg_event_func()

    def send_end_turn(self):
        """
        
        """
        self._myturn = False
        eventtypes.post_end_turn(self, self._player_id)

    def get_selectable_lands(self):
        """
        
        """
        lands = {}  # {aggresor:[defensors]}
        for land in self._lands:
            if land.num_dice > 1:
                for linked in land.get_linked_lands():
                    if linked.get_player() != self:
                        if lands.has_key(land):
                            lands[land].append(linked)
                        else:
                            lands[land] = [linked]
        return lands

    # ---forwarded methods---##ffff00--
    def update(self):
        """
        
        """
        if self._myturn:
            self._implementation.update()

    def on_mouse_motion(self, event):
        """
        
        """
        if self._myturn:
            return self._implementation.on_mouse_motion(event)

    def on_mouse_btn_down(self, event):
        """
        
        """
        if self._myturn:
            return self._implementation.on_mouse_btn_down(event)

    def on_mouse_btn_up(self, event):
        """
        
        """
        ##        print "Player mouse btn up"
        if self._myturn:
            ##            print "player mouse btn up my turn"
            self._implementation.on_mouse_btn_up(event)

    def on_attack_result(self, event):
        """
        
        """
        if self._myturn:
            self._implementation.on_attack_result(event)

    def on_select_result(self, event):
        """
        
        """
        if self._myturn:
            self._implementation.on_select_result(event)

    def on_newturn(self, event):
        """
        
        """
        if event.playerid == self._player_id:
            print "================================================palyer new turn", event.playerid
            if self._implementation is None:
                self.revert_to_type(HUMAN)
            self._myturn = True
            self._implementation.on_newturn(event)
        else:
            self._myturn = False

    def on_gamestate_update(self, event):
        """
        
        """
        if self._myturn:
            self._implementation.on_gamestate_update(event)


##    def on_event(self, event):
##        if self._myturn:
##            print "player:", self._player_id
##            print event
##            return False


class AbstractImplementation(object):
    """
    
    """

    def __init__(self, data):
        object.__init__(self)
        self.type = -1
        self._data = data
        self._player_id = data._player_id
        self._source = data
        self._data.unreg_all_events()
        data.reg_event_func(eventtypes.NEWTURN, data.on_newturn)

    def update(self):
        """
        
        """
        pass

    def on_mouse_motion(self, event):
        """
        
        """
        pass

    def on_mouse_btn_down(self, event):
        """
        
        """
        pass

    def on_mouse_btn_up(self, event):
        """
        
        """
        pass

    def on_attack_result(self, event):
        """
        
        """
        pass

    def on_select_result(self, event):
        """
        
        """
        pass

    def on_newturn(self, event):
        """
       
        """
        pass

    def on_gamestate_update(self, vent):
        """
        
        """
        pass


class Human(AbstractImplementation):
    """
    
    """

    def __init__(self, data):
        """
        
        """
        AbstractImplementation.__init__(self, data)
        self.type = HUMAN
        data.reg_event_func(pygame.MOUSEBUTTONDOWN, data.on_mouse_btn_down)
        data.reg_event_func(pygame.MOUSEBUTTONUP, data.on_mouse_btn_up)
        data.reg_event_func(pygame.MOUSEMOTION, data.on_mouse_motion)

    ##        print "Human __init__"

    def on_mouse_btn_up(self, event):
        """
        
        """
        ##        print "Human player mouse btn up"
        if self._data._myturn:
            if event.button == 1:
                pos = event.pos
                # TODO: hack!! need it really ref to world?
                land = config.world.get_land_from_abs(pos)
                if land:
                    eventtypes.post_select_land(self._source, self._player_id, land.get_id())
            else:
                # TODO: hack, not good, should be the "next turn" button!!
                self._data.send_end_turn()


##                eventtypes.post_end_turn(self._source, self._player_id)
##                self._data._myturn = False


class Network(AbstractImplementation):
    """
    
    """

    def __init__(self, data):
        """
        
        """
        AbstractImplementation.__init__(self, data)
        self.type = NETWORK


class AiPassive(AbstractImplementation):
    """
    
    """

    def __init__(self, data):
        """
        
        """
        AbstractImplementation.__init__(self, data)
        self.type = AI_PASSIVE
        self._data.reg_event_func(eventtypes.ATTACKRESULT, data.on_attack_result)
        self._data.reg_event_func(eventtypes.SELECTRESULT, data.on_select_result)
        self._data.reg_event_func(eventtypes.GSUPDATE, data.on_gamestate_update)

    def on_newturn(self, event):
        """
        
        """
        self._data.send_end_turn()


# TODO: correct implementation using selectresult!!
class AiDumb(AiPassive):
    """
    
    """

    def __init__(self, data):
        """
        
        """
        AiPassive.__init__(self, data)
        self.type = AI_DUMB
        self.last_aggr = None

    def on_newturn(self, event):
        """
        
        """
        event = pygame.event.Event(eventtypes.GSUPDATE, {"aggressorid": self.last_aggr})
        self.on_gamestate_update(event)

    def on_gamestate_update(self, event):
        """
        
        """
        if self.last_aggr == event.aggressorid:
            lands = self._data.get_selectable_lands()
            print "=====================dumb ai:"
            for land, linked in lands.items(): print land.get_id(), [i.get_id() for i in linked]
            print "---------------"
            if len(lands):
                count = 0
                land = random.choice(lands.keys())
                while land.num_dice < 2 and count < len(lands) and land.get_id() != self.selection:
                    land = random.choice(lands.keys())
                    count += 1

                print "dumb ai, chosen land:", land.get_id()
                if land.num_dice < 2:
                    print "dumb ai: to less dices"
                    self._data.send_end_turn()
                defensor = random.choice(lands[land])
                print "defensor:", defensor.get_id()
                self.last_aggr = land.get_id()
                eventtypes.post_select_land(self._source, self._player_id, land.get_id())
                eventtypes.post_select_land(self._source, self._player_id, defensor.get_id())
            else:
                self._data.send_end_turn()


class Ai1(AiPassive):
    """
    
    """

    def __init__(self, data):
        """
        
        """
        AiPassive.__init__(self, data)
        self.type = AI_1
        self.num_conquer = 0

    def on_newturn(self, event):
        """

        """
        self.on_gamestate_update(event)

    def on_gamestate_update(self, event):
        """

        """

        lands = self._data.get_selectable_lands()
        if len(lands):
            get_num_dice = len(lands)
            num_dice = 0
            for land in lands:
                num_dice += land.num_dice
            max_dice = len(lands) * 8
            full = (max_dice <= num_dice)
            print "full:", full, "<<<<<<<<<<<<<<<<<<<"
            if self.num_conquer < 1:
                if full:
                    self.num_conquer = get_num_dice / 8
                    land = random.choice(lands.keys())
                    defensor = random.choice(lands[land])
                    eventtypes.post_select_land(self._source, self._player_id, land.get_id())
                    eventtypes.post_select_land(self._source, self._player_id, defensor.get_id())

                else:
                    self.num_conquer = 0
                    self._data.send_end_turn()
            else:
                print "num_conquer", self.num_conquer
                print "max_dice", max_dice
                ##            print "num_lands", num_lands
                print "num_dice", num_dice
                self.num_conquer -= 1
                land = random.choice(lands.keys())
                defensor = random.choice(lands[land])
                eventtypes.post_select_land(self._source, self._player_id, land.get_id())
                eventtypes.post_select_land(self._source, self._player_id, defensor.get_id())
        else:
            self.num_conquer = 0
            self._data.send_end_turn()
