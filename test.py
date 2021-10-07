import pygame
import random

pygame.init()

screen = pygame.display.set_mode((360,670))
pygame.display.set_caption("example")
icon = pygame.image.load("example.png")
pygame.display.set_icon(icon)

running = True
while running:


     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = false

