from bin import enemy 
from bin import maincharacter 
from bin import platform
import pygame
import random
from bin import powerup
from bin import finishline
import sys
from bin import highscore
import json 

class Controller:
    def __init__(self,width=720,height=320):
        """controller that sets up all the sprite groups and screens
        args parameters of screen size 
        return all instance variables needed sets up platform and enemy positions sets the game state"""
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()
        self.platform = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.finishLine = pygame.sprite.Group()
        self.powerUp = pygame.sprite.Group()
        self.score = highscore.Highscore(0)
        load = open("highscore.json","r") 
        fileReading = load.read()
        self.highscore = json.loads(fileReading)
        load.close()
        
        #adds platforms
        for x in range(0,1500,50):
            self.platform.add(platform.Platform(x,316,'assets/platform.png'))
        for b in range(0,1500,300):
            self.platform.add(platform.Platform(b,200,'assets/platform.png'))
        for a in range(0,1500,600):
            self.platform.add(platform.Platform(a,100,'assets/platform.png'))
        ##adds enemies
        for x in range(100,1500,200):
            self.enemy.add(enemy.Enemy(x,286,'assets/enemy.png'))
        for b in range(0,1500,200):
            self.enemy.add(enemy.Enemy(b,170,'assets/enemy.png'))
        for a in range(0,1500,200):
            self.enemy.add(enemy.Enemy(a,70,'assets/enemy.png'))
        self.powerUp.add(powerup.PowerUp(475,260,'assets/powerup.png'))
        self.finishLine.add(finishline.FinishLine(1500,0,'assets/finishline.png'))
        self.finishLine.add(finishline.FinishLine(1500,180,'assets/finishline.png')) 
        self.finishLine.add(finishline.FinishLine(1500,150,'assets/finishline.png')) 
        self.hero = maincharacter.MainCharacter(0,290,'assets/standing.png')
        self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemy)+tuple(self.platform)+(self.powerUp,)+tuple(self.finishLine))
        self.state = "RUN"
        self.godMode = str(input("cheatcode"))
        if self.godMode == "Based":
            self.hero.lives = 1000
        self.backGround = pygame.image.load('assets/background.png')
        self.gameLost = pygame.image.load('assets/gameoverscreen.png')
        self.gameWonScreen = pygame.image.load('assets/winscreen.png')
        
    def mainLoop(self):
        """defines the state of the game
        args none 
        returns a different state and either continues or ends the game and chooses which ending to give"""
        while True: 
            if(self.state == "RUN"):
                self.gameLoop()
            elif(self.state == "END"):
                self.gameOver()
            elif(self.state == "WON"):
                self.gameWON()
    def gameLoop(self):
        """sets up all the events in the game from enemy,platform,hero,powerup, and finishline behavor as well as scrolls the screen, basically this is the whole game 
        args none
        returns a different event state of either continuing to run game loop or go to a different state of winning or losing the game"""
        pygame.key.set_repeat(1,50)
        halfFrame= True
        quarterFrame = True
        while self.state == "RUN":
            if self.hero.rect.x > self.width/2:
                self.hero.rect.x -= 3
                for e in (self.enemy):
                    e.rect.x -= 3
                for pu in (self.powerUp):
                    pu.rect.x -= 3
                for c in (self.finishLine):
                    c.rect.x -= 3
                for b in self.platform:
                    b.rect.x -= 3
            if self.hero.rect.x < self.width/2:
                self.hero.rect.x += 3
                for e in (self.enemy):
                    e.rect.x += 3
                for pu in (self.powerUp):
                    pu.rect.x += 3
                for c in (self.finishLine):
                    c.rect.x += 3
                for b in self.platform:
                    b.rect.x += 3
            
            self.screen.blit(self.backGround,(0,0)) 
            if halfFrame:
                if quarterFrame:
                    self.enemy.update()
                quarterFrame = not quarterFrame
            halfFrame = not halfFrame         
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_LEFT):
                        self.hero.moveLeft()
                    elif(event.key == pygame.K_UP):
                        self.hero.jump()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.moveRight()
                
            fight = pygame.sprite.spritecollide(self.hero, self.enemy, True)
            if (fight):
                for e in fight:
                    if (self.hero.rect.y + 10) < e.rect.y:
                        print(self.hero.rect.y+10)
                        print("enemy",e.rect.y) 
                        e.kill()
                        self.score.update()
                    else:
                        self.hero.lives -=1
            font = pygame.font.SysFont(None, 30, True)
            points = font.render('Points:'+ str(self.score.read()), False, (255,255,0))
            enemy_sur = font.render('Remaining Lives:'+ str(self.hero.lives), False, (250,0,0))
            self.screen.blit(enemy_sur, (10,50))
            self.screen.blit(points, (500,50))        
            self.all_sprites.draw(self.screen)
            pygame.display.flip() 

            #code for the main character's jump            
            self.hero.update()

            if pygame.sprite.spritecollideany(self.hero, self.platform):
                self.hero.state = "standing"
                self.hero.y_velocity = 0
                if self.hero.y_velocity >= 0:
                    self.hero.rect.bottom = pygame.sprite.spritecollideany(self.hero, self.platform).rect.top
                if self.hero.powerup == False:
                    self.hero.jumpcount = 1
                else:
                    self.hero.jumpcount = 2
            else:
                self.hero.state = "jumping"

            if self.hero.state == "jumping":
                self.hero.y_velocity += .5

            if pygame.sprite.spritecollide(self.hero, self.powerUp, True):
                self.hero.powerup = True

            #code for the enemy's jump
                
            for e in self.enemy:
                if pygame.sprite.spritecollideany(e, self.platform):
                    e.state = "standing"
                    e.y_velocity = 0
                    if e.y_velocity >= 0:
                        e.rect.bottom = pygame.sprite.spritecollideany(e, self.platform).rect.top
                else:
                    e.state = "jumping"

                if e.state == "jumping":
                    e.y_velocity += .5

            if(self.hero.lives == 0):
                self.state = "END"
            if pygame.sprite.spritecollide(self.hero, self.finishLine, True):
                self.state = "WON"
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
    def gameWON(self):
        """game won screen of the game if the hero reaches the end, displays gamewon screen
        args none 
        returns the game being done and your highscore"""
        self.hero.kill()
        self.screen.blit(self.gameWonScreen,(0,0))
        pygame.display.flip()
        print("Godmode cheatcode:Based")
        if self.score.read() > self.highscore["points"]:
            p = self.score
            something = open("highscore.json","w")
            json.dump(p.__dict__,something)
            something.close()
            print("new highscore:",self.score.read())                
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    def gameOver(self):
        """game over screen of the game if the hero dies, displays gameover screen
        args none 
        returns nothing but a screen of a sad frog looking at you and ends the game"""
        self.hero.kill()
        self.screen.blit(self.gameLost,(0,0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    

