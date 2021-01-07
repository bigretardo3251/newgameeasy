import pygame
from bin import controller 
def printNames():
    """prints our names
    args none 
    returns str our names"""
    print("Emanuel Francisco: Back End")
    print("Quentin Zayats: Front End")
    print("Mark Lanning: Software Lead")
    print("")
    print(":)")
def main():
    printNames()
    pygame.init()
    mainWindow = controller.Controller()
    mainWindow.mainLoop()
main()
