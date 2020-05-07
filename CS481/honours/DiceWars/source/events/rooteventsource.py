#!/usr/bin/env python


import pygame
from eventdispatcher import EventDispatcher

# TODO: debug event? -> dipatcher must have name -> print self.name, event
# TODO: use own eventqueue, each time an event is posted, get the events from
#       pygame first, then add new event (order is correct)
#       (overwrite pygame.event.post() )
#       Own event class??

class _RootEventSource(EventDispatcher):
    """
    Is the root of the events. Depends on pygame.
    pygame must be initialized befor you can use this class.
    """
    
    def __init__(self, focus=None):
        """
        
        """
        #TODO: make it a singleton
        EventDispatcher.__init__(self)
        self._focus = focus
        self._blocking = 0
        self._running = True
        self.__events = []
        
    def set_blocking(self, value=True):
        """
        Enabled or disable blocking mode. In blocking mode the update() method
        will block until an event is posted. Default: not blocking.
        """
        if value:
            self._blocking += 1
        else:
            self._blocking -= 1
            if self._blocking < 0:
                self._blocking = 0
        
    def stop(self):
        """
        Stop the from looping, only used if you use run().
        """
        self._running = False
        
    # TODO: any number of argumenst?
    # TODO: if event not handeld, call warning func?
    def update(self):
        """
        This retrives all events and dispatches them.
        If blocking is true, this method will block until a new event is 
        posted.
        """
        # get all events and send them out
        if self._blocking > 0:
            self.handle_event( pygame.event.wait() )
        self.__events = list(pygame.event.get())
        while len(self.__events):
            event = self.__events.pop(0)
            if not self._focus or not self._focus.handle_event(event):
                self.handle_event(event)
            
    def clear(self):
        """
        
        """
        self.__events = []
        pygame.event.clear()
    
    def run(self, functions=None):
        """
        This will run an loop until stop() is called. In each iteration of 
        the loop the functions will be called (with no arguments).
        """
        if not type(functions)==list or not type(functions)==tuple:
            if functions:
                functions = [functions]
            else:
                functions = []
        
        self._running = True
        while self._running:
            self.update()
            for func in functions:
                func()
                

# singleton pattern using the module
_root_event_source = _RootEventSource()
def RootEventSource():
    """
    
    """
    return _root_event_source