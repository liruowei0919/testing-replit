#!/usr/bin/python
# -*- encoding: utf-8 -*-

# IDEA
# Import and Initialization
import pygame
from classes.Game import Game
from classes.Screen import Screen
print("the game starts!")
pygame.init()
#write here

#



# Display configuration
screen = Screen('Hit the Mole!', 800, 600)
# Entities
game = Game(screen)
# Run Game
game.start()

print("this has just been updated")
# if __name__ == '__main__':
#     game.start()
