#!/usr/bin/env python


import sys
sys.path.append('..')
import textentry
import scrolltext
import events
import eventtypes
import pygame


class ChatModul(events.EventDispatcher):
    """
    
    """
    
    def __init__(self, nickname, lines=5, width=600):
        """
        
        """
        self.dirty = True
        events.EventDispatcher.__init__(self)
        font = pygame.font.Font(None, 22)
        self.text_entry = textentry.TextEntry(nickname, font, width)
        self.scroll_text = scrolltext.ScrollText(font, lines, width)
        
        self.image = pygame.Surface((width+10, self.text_entry.size[1]+\
                                        self.scroll_text.size[1]+15)).convert()
        self.image.fill((255,255,255))
        
        self.on_afterevent(1)
        
        # event stuff
        self.add_listener(self.text_entry)
        self.add_listener(self.scroll_text)
        events.RootEventSource().add_listener(self)
        
    def on_afterevent(self, event):
        """
        
        """
        self.dirty = True
        self.image.blit(self.scroll_text.image, (5,5))
        self.image.blit(self.text_entry.image, (5, self.scroll_text.size[1]+5+5))
        
        
if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    chat = ChatModul("nickname", 10)
    pygame.key.set_repeat(500, 30)
    while 1:
        events.RootEventSource().update()
        if chat.dirty:
            screen.fill((0,0,0))
            chat.dirty = False
            r = screen.blit(chat.image,(0, 0))
            pygame.display.update(r)
        