import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#Lisame pildid
bg = pygame.image.load("bg.jpg")
screen.blit(bg,[0,0])

pygame.display.flip()