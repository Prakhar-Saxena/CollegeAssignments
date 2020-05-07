#!/usr/bin/env python


import sys
sys.path.append('..')
import events
import eventtypes
import pygame

def test_func():
    print "Button clicked!"

class Button(events.EventEnabled):
    """
    
    """
    
    def __init__(self, font, text, position_on_screen, callback=None):
        """
        
        """
        events.EventEnabled.__init__(self)
        # data
        self._callback = callback
        self._text = text
        self._hit = False
        
        # dawing
        self.font = font
        size = font.size(text)
        self.position = position_on_screen
        self._col_rect = pygame.Rect(self.position, size).inflate(10,10)
        self._col_rect.topleft = self.position
        
        self.image = pygame.Surface(self._col_rect.size).convert()
        self.image.fill((100,100,100))
        textimg = font.render(text, 1, (255,255,255), (100,100,100))
        xpos = (self._col_rect.width - size[0]) / 2
        ypos = (self._col_rect.height - size[1]) / 2
        self.image.blit(textimg, (xpos, ypos))
        
        
        
        
        # register events
        self.reg_event_func(pygame.KEYDOWN, self.on_keydown)
        self.reg_event_func(pygame.MOUSEMOTION, self.on_mousemotion)
        self.reg_event_func(pygame.MOUSEBUTTONDOWN, self.on_mousedown)
        self.reg_event_func(pygame.MOUSEBUTTONUP, self.on_mouseup)
        
    def on_keydown(self, event):
        """
        Decides what do to with a keypress.
        special meanings have these keys: 
        enter, left, right, home, end, backspace, delete
        """
        if event.type != pygame.KEYDOWN:
            print "textentry got wrong event:", event
        else:
            self.render()
### debug
            if __name__=='__main__' and event.key == pygame.K_ESCAPE:
                events.RootEventSource().stop()
        
    def on_mousedown(self, event):
        """
        
        """
        pos = event.pos
        if self._col_rect.collidepoint(pos):
            self._hit = True

        
    def on_mouseup(self, event):
        """
        
        """
##        print "mouse button up", event.pos
##        print self._up_col_rect
##        print self._down_col_rect
        pos = event.pos
        if self._hit and self._col_rect.collidepoint(pos):
            if self._callback:
                self._callback()
        self._hit = False
        
    def on_mousemotion(self, event):
        """
        
        """
        pass
        
    def set_callback(self, callback):
        """
        
        """
        self._callback = callback
        
    def render(self):
        """
        
        """
        pass
        
    def update(self):
        """
        Actually not needed. (only need if this module is run as a script)
        """
        # only need if this module is run as a script
        if __name__ == '__main__':
##            print "_min_w:", self._min_w, "len items:", len(self._items)
            screen = pygame.display.get_surface()
            screen.fill( (100, 0, 0))
            screen.blit(self.image, self.position)
##            pygame.draw.rect(screen, (255,255,0), self._text_col_rect, 1)
##            pygame.draw.rect(screen, (255,255,0), self._up_col_rect, 1)
##            pygame.draw.rect(screen, (255,255,0), self._down_col_rect, 1)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.key.set_repeat(500, 30)
    pygame.display.set_mode((800,600))
    t = Button(pygame.font.Font(None, 30), "cancel", (100,100), test_func)
    
##    tt = Spinner(pygame.font.Font(None, 30), (300,100))
##    tt.add(Item("Human", 1))
##    tt.add(Item("passive AI", 2))
##    tt.add(Item("dumb AI", 3))
##    tt.add(Item("better AI", 4))
##    tt.add(Item("None", 5))
    
    events.RootEventSource().add_listener(t)
    print t.parent
    events.RootEventSource().set_blocking(True)
    events.RootEventSource().run(t.update)
    