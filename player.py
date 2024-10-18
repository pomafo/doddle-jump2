import pygame
from projectil import projectil

class player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game=game
        self.health=100
        self.max_health=100
        self.attack=20

        self.all_projectil=pygame.sprite.Group()
        self.velocity=1.5
        self.image=pygame.image.load("PygameAssets-main/player.png")
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=500


    def damage(self,amount):
        if self.health-amount>amount:
            self.health-=amount
        else:
            self.game.game_over()

    def launght_projectil(self):

        self.all_projectil.add(projectil(self))


    def update_health_bar(self,surface):

        pygame.draw.rect(surface, (60,63,60), [self.rect.x+50,self.rect.y+20,self.max_health,7])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+50,self.rect.y+20,self.health,7])


    def mouv_right(self):
        if not self.game.check_colision(self,self.game.all_monster):
            self.rect.x+=self.velocity

    def mouv_left(self):
        if not self.game.check_colision(self, self.game.all_monster):
            self.rect.x-=self.velocity
