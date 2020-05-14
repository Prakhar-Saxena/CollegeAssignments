#!/usr/bin/env python


import config
import eventtypes
import events

class GameState(events.EventEnabled):
    """
    
    """
    
    def __init__(self):
        """
        
        """
        events.EventEnabled.__init__(self)
        # data
        self.players = config.players
        self.world   = config.world
        self.current_player = None
        self.state   = 0  # 0=not started, 1=playing, 2=ended
        
        # events
        self.reg_event_func(eventtypes.ATTACKRESULT, self.on_attackresult)
##        self.reg_event_func(eventtypes.ENDTURN, self.on_endturn)
        self.reg_event_func(eventtypes.NEWTURN, self.on_newturn)
        self.reg_event_func(eventtypes.PLAYERDEAD, self.on_playerdead)
        self.reg_event_func(eventtypes.PLAYERWIN, self.on_playerwin)
        self.reg_event_func(eventtypes.STARTGAME, self.on_startgame)
        self.reg_event_func(eventtypes.ENDGAME, self.on_endgame)
        self.reg_event_func(eventtypes.DROPDICE, self.on_dropdice)
        self.reg_event_func(eventtypes.SELECTRESULT, self.on_selectresult)
        self.reg_event_func(eventtypes.CONNINTERRUPT, self.on_connectioninterrupt)
        self.reg_event_func(eventtypes.PLAYERRECONN, self.on_playerreconnect)
        print self.get_eventtypes()
        # register it directly to source
        events.RootEventSource().add_listener(self, prio=1)
        
#---eventfuncions----##FFff00
    def on_attackresult(self, event):
        """
        
        """
        aggr_pips, def_pips = event.results
        def_pips, def_sum   = def_pips
        aggr_pips, aggr_sum = aggr_pips
        aggr_land = self.get_land_by_id(event.aggressorid)
        def_land  = self.get_land_by_id(event.defensorid)
        
        if aggr_sum > def_sum: # aggressor wins
            # move num_dices-1 into conquered land
            def_land.set_num_dice(aggr_land.num_dice-1)
            # add conquered land to the winner player
            def_land.set_player(aggr_land.get_player())
        # only one dice remains in land
        aggr_land.set_num_dice()
        print "post gamestate update, aggr:", event.aggressorid, "def:", event.defensorid
        eventtypes.post_gamestate_update(self, event.aggressorid, event.defensorid)
        
##    def on_endturn(self, event):
##        """
##        
##        """
##        self.current_player = None
        
    def on_newturn(self, event):
        """
        
        """
        self.current_player = self.get_player_by_id(event.playerid)
        if self.current_player is None:
            # TODO: request stateupdate?
            print "WARNING: no player found using id:", event.playerid
        print "its player", event.playerid, "turn"
        
    def on_playerdead(self, event):
        """
        
        """
        player = self.get_player_by_id(event.playerid)
        player.dead = True
        print "gamestate: player", event.playerid, "is dead."
        
    def on_playerwin(self, event):
        """
        
        """
        #TODO: implement: what to do?
        print "gamestate: Player", event.playerid,"wins!"
        
    def on_startgame(self, event):
        """
        
        """
        self.state = 1
        print "Game started."
        
    def on_endgame(self, event):
        """
        
        """
        self.state = 2
        for land in self.world.get_lands():
            land.selected = False
        print "Game ended."
        
    def on_dropdice(self, event):
        """
        
        """
        for land_id, num_dice in event.data.items():
            land = self.get_land_by_id(land_id)
            if land:
                land.set_num_dice(num_dice)
##                print "gamestate dropdice, land", land.get_id(), "has", land.num_dice
            else:
                # TODO: ?
                print "WARNING: no region found to drop dice, region id:", land_id
        
    def on_selectresult(self, event):
        """
        
        """
        if event.result == 0:
            land = self.get_land_by_id(event.landid)
            if land:
                land.selected = True
        elif event.result == 1:
            land = self.get_land_by_id(event.landid)
            if land:
                land.selected = False
        
    def on_connectioninterrupt(self, event):
        """
        
        """
        pass
        
    def on_playerreconnect(self, event):
        """
        
        """
        pass
### DEBUG
##    def on_event(self, event):
##        if event.type == eventtypes.ENDGAME:
##            print "gamestate:event:", event.type, "ENDGAME"
##        return False
##    
##    def on_afterevent(self, event):
##        if event.type == eventtypes.ENDGAME:
##            print "gamestate: afterevent ENDGAME!"

##    def on_event(self, event):
##        print "gamestate:"
##        print event
##        return False
    
        
#---other methods  ##ffff00
    def get_player_by_id(self, player_id):
        """
        
        """
        for player in self.players:
            if player.get_id() == player_id:
                return player
        # TODO: perhaps better to request stateupdate?
        return None
    
    def get_land_by_id(self, land_id):
        """
        
        """
        land = self.world.get_land_by_id(land_id)
        if land is None:
            # TODO: ?
            print "WARNING: no land found using id:", land_id
        return land
    
    def get_alive_players(self):
        """
        
        """
        alive = []
        for player in self.players:
            if not player.dead:
                alive.append(player)
        return alive
    
    def update(self):
        """
        
        """
        for player in self.players:
            player.update()
