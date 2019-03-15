# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:05:34 2019

@author: U197327
"""

class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
       
        
        #Ship settings
        self.ship_speed_factor = 1.5
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 255, 255, 0
        self.bullets_allowed = 3