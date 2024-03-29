# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:30:31 2019

@author: U197327
"""

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from background import Background

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # make a ship.
    ship = Ship(ai_settings, screen)
    # make a ship.
    background = Background(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make a group to store aliens in
    aliens = Group()
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    
    #Start the main loop for the game.
    while True: 
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, background, ship, aliens, bullets)
        
run_game() 
