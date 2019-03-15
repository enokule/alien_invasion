# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:54:49 2019

@author: U197327
"""

import pygame

class Background():
    def __init__(self, ai_settings, screen):
        """Initialize the background and set the starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/screen.bmp').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        
    def blitme(self):
        """Draw the background."""
        self.screen.blit(self.image, self.rect)