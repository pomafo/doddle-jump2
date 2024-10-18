import pygame
from player import Player 
from platform import Platform

import random
class Game():
    def __init__(self) :
        pass
        self.player=Player(self)
        self.all_platform=pygame.sprite.Group()
        self.pressed={}
        self.created_platform()
        
        game_over=True
        
    
    def update(self,screen):
        screen.blit(self.player.image,self.player.rect)
        self.player.apply_gravity()
    
        
    
            
    def created_platform(self):
        distance=-100
        initial_y=600
        for i in range(8):
            platform=Platform()
            
            if i ==0:
                platform.rect.x=250
                platform.rect.y=initial_y
            else:
                platform.rect.x=random.randint(0,400)
                platform.rect.y=initial_y+distance*i
            
            
            self.all_platform.add(platform)
    def bar(self):
        self.bar=pygame.Rect(0,800,500,1) 

    def check_colision(self,sprite,groupe):
        return pygame.sprite.spritecollide(sprite,groupe,False,pygame.sprite.collide_rect)
    
    def saut_platform(self):
        if self.check_colision(self,self.game.all_platform):
            self.player.jump()
        elif self.player.rect.y>=700:
            self.player.jump()

    
        
 