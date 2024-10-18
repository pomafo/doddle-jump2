import pygame
from player import player
from monster import monster
from comete_event import *

class game():
    def __init__(self):
        self.is_playing=False
        self.player=player(self)
        self.all_player=pygame.sprite.Group()
        self.all_player.add(self.player)
        self.comete_event=CometFallEvent(self)
        self.all_monster=pygame.sprite.Group()

        self.pressed={}



    def start(self):
        self.is_playing=True
        self.spawn_monster()
        self.spawn_monster()
    def game_over(self):
        self.all_monster=pygame.sprite.Group()
        self.player.health=self.player.max_health
        self.is_playing=False
    def update (self,screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar((screen))
        self.comete_event.update_bar(screen)

        for projectil in self.player.all_projectil:
            projectil.mouv()

        self.player.all_projectil.draw(screen)
        self.all_monster.draw(screen)
        self.comete_event.all_comet.draw(screen)

        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        for comete in self.comete_event.all_comet:
            comete.fall()

        if self.pressed.get(pygame.K_d) and self.player.rect.x < 900:
            self.player.mouv_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.mouv_left()
    def spawn_monster (self):
        Monster=monster(self)
        self.all_monster.add(Monster)

    def check_colision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)


