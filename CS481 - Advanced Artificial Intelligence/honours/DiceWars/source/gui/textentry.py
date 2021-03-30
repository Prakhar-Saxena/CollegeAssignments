#!/usr/bin/env python


import sys
sys.path.append('..')
import events
import eventtypes
import pygame


class TextEntry(events.EventEnabled):
    """
    Simple text entry component.
    """
    
    def __init__(self, nickname, font, width=600):
        """
        nickname: nickname, all messages will be prefixed with the nickname 
        font    : pygame.font.Font object
        width   : in pixel that this element can use (this restricts the number
                  of char you can enter
                
        events:
        in : pygame.KEYDOWN
        out: eventtypes.CHATMSG
        """
        events.EventEnabled.__init__(self)
        
        # data
        self.text = ""
        self.caretpos = 0
        self.max = 255
        self.nickname = nickname
                
        # drawing
        self.dirty = True
        self.font = font
        height = self.font.get_ascent() - self.font.get_descent()+1+4
        self.image = pygame.Surface( (width, height)).convert()
        self.size = (width, height)
        self.fill_color = (220, 220, 220)
        self.text_color = (1, 1, 1)
        self.image.fill(self.fill_color)
        self.text_field_rect = pygame.Rect(0,0, width-1, height-1)
        self.text_img = pygame.Surface((2,2))
        self.pixel_width = width-4
        self.render()
        
        
        # needed events
        self.reg_event_func(pygame.KEYDOWN, self.on_keydown)
    
    def on_keydown(self, event):
        """
        Decides what do to with a keypress.
        special meanings have these keys: 
        enter, left, right, home, end, backspace, delete
        """
        if event.type != pygame.KEYDOWN:
            print "textentry got wrong event:", event
        else:
            if event.key == pygame.K_RETURN:
                self.on_enter()
            elif event.key == pygame.K_RIGHT:
                self.move_caret()
            elif event.key == pygame.K_LEFT:
                self.move_caret(-1)
            elif event.key == pygame.K_HOME:
                self.move_caret('home')
            elif event.key == pygame.K_END:
                self.move_caret('end')
            elif event.key == pygame.K_BACKSPACE:
                self.backspace_char()
            elif event.key == pygame.K_DELETE:
                self.delete_char()
            else:
                if event.unicode != u'':
                    if len(self.text) < self.max:
                        self.text = self.text[:self.caretpos]+ event.unicode+ \
                                                    self.text[self.caretpos:]
                        self.caretpos += 1
            self.render()
### debug
            if __name__=='__main__' and event.key == pygame.K_ESCAPE:
                events.RootEventSource().stop()
        
    def on_enter(self, event=None):
        """
        When the enter key (return) is pressed then a chatmsg is send out.
        """
        if len(self.text):
            eventtypes.post_chatmsg(self, self.nickname+': '+self.text)
            self.text = ""
            self.caretpos = 0
        
    def move_caret(self, steps=1):
        """
        Moves the caret about steps. Positive numbers moves it right, negative
        numbers left.
        """
        if steps == 'home':
            self.caretpos = 0
        elif steps == 'end':
            self.caretpos = len(self.text)
        else:
            self.caretpos += steps
        if self.caretpos < 0:
            self.caretpos = 0
        if self.caretpos > len(self.text):
            self.caretpos = len(self.text)
        
    def backspace_char(self):
        """
        Deltes the char befor the caret position.
        """
        if self.caretpos>0:
            self.text = self.text[:self.caretpos-1]+self.text[self.caretpos:]
            self.caretpos -= 1
        
    def delete_char(self):
        """
        Deltes the char after the caret position.
        """
        self.text = self.text[:self.caretpos]+self.text[self.caretpos+1:]
        
    def render(self):
        """
        Renders the string to self.image.
        """
        self.dirty = True
        self.image.fill(self.fill_color)
        if len(self.text):
            while self.font.size(self.text)[0]> self.pixel_width:
                self.backspace_char()
            self.text_img = self.font.render(self.text, 1, self.text_color, \
                                                               self.fill_color)
            self.image.blit(self.text_img, (2,2))
            xpos = self.font.size(self.text[:self.caretpos])[0]+2
            pygame.draw.line(self.image, (255, 255, 255, 255), (xpos, 2), \
                                         (xpos, self.image.get_height()-2), 1)
        else:
            pygame.draw.line(self.image, (255, 255, 255), (3, 2), \
                                            (3, self.image.get_height()-2), 1)
        pygame.draw.rect(self.image, (100, 100, 100), self.text_field_rect , 2)
        
    def update(self):
        """
        Actually not needed. (only need if this module is run as a script)
        """
        # only need if this module is run as a script
        if __name__ == '__main__':
            print self.text, len(self.text), self.caretpos
            screen = pygame.display.get_surface()
            screen.fill( (0, 0, 0))
            screen.blit(self.image, (100,100))
            pygame.display.flip()
        
        
if __name__ == '__main__':
    pygame.init()
    pygame.key.set_repeat(500, 30)
    pygame.display.set_mode((800,600))
    t = TextEntry("supernick:", pygame.font.Font(None, 22))
    events.RootEventSource().add_listener(t)
    print t.parent
    events.RootEventSource().set_blocking(True)
    events.RootEventSource().run(t.update)
    