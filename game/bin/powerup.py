import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        #initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #when the maincharacter sprite collides with the powerup set maincharacter.powerup = True in the controller
        #when the maincharacter reaches the ground after jumping set maincharacter.jumps = 2 if they have the powerup andmaincharacter.jumps = 1 if they dont

        
