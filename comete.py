import pygame
import random



class comet(pygame.sprite.Sprite):
    def __init__(self,comete_event):
        super().__init__()
        self.image=pygame.image.load("PygameAssets-main/comet.png")
        self.rect=self.image.get_rect()

        self.velocity=random.randint(1,3)
        self.rect.x=random.randint(20,800)
        self.rect.y=- random.randint(0,800)
        self.comete_event=comete_event

    def remove(self):
        self.comete_event.all_comet.remove(self)



    def fall(self):
        self.rect.y+=self.velocity

        if self.rect.y>=600:
            self.remove()
        if len(self.comete_event.all_comet)==0:
            self.comete_event.reset_percent()
            self.comete_event.fall_mode=False

            self.comete_event.game.spawn_monster()
            self.comete_event.game.spawn_monster()
        if self.comete_event.game.check_colision(self,self.comete_event.game.all_player):
            print("joueur")
            self.remove()
            self.comete_event.game.player.dam