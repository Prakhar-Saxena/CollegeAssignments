#!/usr/bin/env python



import pygame

class Text(object):
    """
    
    """
    
    def __init__(self, text, font, position):
        """
        
        """
        
        self.text = text
        self.position = position
        
        size = font.size(text)
        rect = pygame.Rect((0,0),size)
        self.image = pygame.Surface(rect.size).convert()
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        
        txtimg = font.render(text, 1, (255, 255, 255), (0, 0, 0))
        xpos = (rect.width-size[0])/2
        ypos = (rect.height-size[1])/2
        self.image.blit(txtimg, (xpos, ypos))