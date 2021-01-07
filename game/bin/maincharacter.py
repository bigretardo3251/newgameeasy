import pygame

class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        #initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.lives = 3
        #used for jumping method
        self.y_velocity = 0
        self.powerup = False
        self.jumpcount = 1
        self.state = "standing"
        
    def moveLeft(self):
        '''
        Moves the character left by 3 units each frame the key is pressed
        Args:
            none
        Returns:
            updates the characters x position
        '''
        self.rect.x -= 3

    def moveRight(self):
        '''
        Moves the character right by 3 units each frame the key is pressed
        Args:
            none
        Returns:
            updates the characters x position
        '''
        self.rect.x += 3

    def jump(self):
        '''
        Makes the character jump. If the player has a powerup the character can double jump.
        Args:
            none
        Returns:
            changes the characters y velocity
        '''
  
        if self.jumpcount == 1:
            if self.y_velocity > -10:
                self.y_velocity = -15
                self.jumpcount -= 1
        if self.jumpcount == 2:
            self.y_velocity = -15
            self.jumpcount -= 1
            
    def update(self):
        '''
        Uses the characters y velocity to make the jump method work and apply gravity
        Args: none
        Returns: updates the characters y position
        '''
        self.rect.y += self.y_velocity
