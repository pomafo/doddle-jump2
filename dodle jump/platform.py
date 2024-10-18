import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image=pygame.image.load("Platform.png")
        self.image=pygame.transform.scale(self.image,(125,100))
        self.rect=self.image.get_rect()
        
        self.rect.y=600
        self.rect.x=250        