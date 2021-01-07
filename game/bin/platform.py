import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        #initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (100,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
