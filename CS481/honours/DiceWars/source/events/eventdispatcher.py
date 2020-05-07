#!/usr/bin/env python


import pygame

class EventDispatcher(object):
    """
    A event dispatcher.
    """
    
    def __init__(self):
        object.__init__(self)
        self._eventdispatch = {} # {eventtype:[listeners]}, 
                                 # handle_event(event)->bool
        self.parent = None
    
    def get_eventtypes(self): # ->[eventtypes]
        """
        Returns the eventtypes this eventdispatcher need to listen.
        """
        return self._eventdispatch.keys()
    
    def handle_event(self, event):
        """
        Dispatches the event to all listeners.
        Returns True if the event has been processed else False.
        """
        evttype = event.type
        if evttype == pygame.USEREVENT:
            evttype = event.usertype
        resp = False
        if self._eventdispatch.has_key(evttype):
            resp = self.on_event(event)
            if not resp:
                for listener in self._eventdispatch[evttype]:
                    if listener.handle_event(event):
                        resp = True
            self.on_afterevent(event)
        return resp
    
    def on_event(self, event):
        """
        Is called befor the events are dispatched. You can override it. If
        you return True then the events are not dispatched to the listeners.
        """
        return False
    
    def on_afterevent(self, event):
        """
        This is called after the event has been dispatched to all listeners.
        """
        return False
    
    
    def add_listener(self, listener, eventtype=None, prio=None):
        """
        Adds the listener to the dispatch list for the given eventtypes.
        
        listener : reference to the object that listens for events
        eventtype: type of events it want to receive, can be a list of
                    eventtypes or a single eventtype or None (in that case
                    the listener's get_eventtypes() is called to get them).
        prio     : bool, if True then the listener will be inserted at first
                    position in the list
        """
        # remove old parent from listener
        if listener.parent and listener.parent != self:
            listener.parent.remove_listener(listener)
        listener.parent = self
        # check if it is a lits of eventtypes or not
        if eventtype:
            if not type(eventtype) == list or not type(eventtype) == tuple:
                eventtype = [eventtype]
        else:
            eventtype = listener.get_eventtypes()
        # add the different eventtypes
        for evttype in eventtype:
            # check if evnttype already exists, if not add empty list
            if not self._eventdispatch.has_key(evttype):
                self._eventdispatch[evttype] = []
                # register new eventtype at parent?
                if self.parent:
                    self.parent.add_listener(self, evttype, prio)
            # check if the listener is already listening for that eventtype, 
            # if not register the listener
            if listener not in self._eventdispatch[evttype]:
                if prio: # prio
                    self._eventdispatch[evttype].insert(0, listener)
                else:
                    self._eventdispatch[evttype].append(listener)
        
    def remove_listener(self, listener, eventtype=None):
        """
        removes a listener from the dispatch list.
        
        listener    : listener to remove
        eventtype   : eventype the listener wants to unregister
                      if it is None, the listener will not receive any event
        """
##        print "removing listener:", listener, eventtype
        # if eventtype is None then remove it from all types
        if eventtype is None:
            for evttype, listeners in self._eventdispatch.items():
                if listener in listeners:
                    listeners.remove(listener)
                    # if no listener is left for this eventtype, remove it
                    if len(listeners) == 0:
                        del self._eventdispatch[evttype]
                        # remove eventtype from parent
                        if self.parent:
                            self.parent.remove_listener(self, evttype)
        else:
            # check if eventtype is a list or not
            if not type(eventtype) == list or not type(eventtype) == tuple:
                eventtype = [eventtype]
            
            for evttype in eventtype:
                listeners = self._eventdispatch[evttype]
                if listener in listeners:
                    listeners.remove(listener)
                    # if no listener is left for this eventtype, remove it
                    if len(listeners) == 0:
                        del self._eventdispatch[evttype]
                        # remove eventtype from parent
                        if self.parent:
                            self.parent.remove_listener(self, evttype)
                    
##            for evttype in self._eventdispatch.keys():
##                evttype_listeners = self._eventdispatch[evttype]
##                if listener in evttype_listeners:
##                    if evttype in eventtype:
##                        evttype_listeners.remove(listener)
##                        # if no listener is left for this eventtype, remove it
##                        if len(evttype_listeners) == 0:
##                            del self._eventdispatch[evttype]
##                            # remove eventtype from parent
##                            if self.parent:
##                                self.parent.remove_listener(self, evttype)
                            
##        for eventtype in self._eventdispatch.keys():
##            for liste in self._eventdispatch[eventtype]:
##                if liste == listener:
##                    print ">>>>>>>>>>>>>>> still in dispatcher!!!!"

    def remove_all_listeners(self):
        """
        
        """
        old = self._eventdispatch
        self._eventdispatch = {}
        return old

    def set_all_listeners(self, new):
        """
        
        """
        old = self._eventdispatch
        self._eventdispatch = new
        return old
