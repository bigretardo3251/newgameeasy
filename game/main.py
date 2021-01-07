import pygame
from bin import controller 
def main():
    pygame.init()
    mainWindow = controller.Controller()
    mainWindow.mainLoop()
main()
