import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        #initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.moveRight = True

        #used for jump method
        self.state = "standing"
        self.y_velocity = 0

    def jump(self):
        '''
        Makes the character jump. Checks to see if the state is "standing", if true then the state is set to "jumping" and the y_velocity is set to 100
        Args:
            none
        Returns:
            none
        '''
        if self.state == "standing" :
            #in the controller, each frame decrease y_velocity by some amount and when the sprite reaches ground level set y_velocity to 0 and self.maincharacter.state to "standing"
            self.y_velocity = -15

    def update(self):
        '''
        Moves the enemy around randomly, every 1 in 250 frames the enemy will randomly jump, every 1 in 250 frames the enemy will switch the direction its moving
        Args:
            none
        Returns:
            none
        '''
        if self.moveRight == True:
            self.rect.x += 1
        else:
            self.rect.x -= 1
            
        if random.randrange(1, 250) == 1:
            self.jump()
            self.moveRight = not self.moveRight

        self.rect.y += self.y_velocity

        
