import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game) -> None:
        super().__init__()
        # Charger l'image du joueur ici dans le constructeur
        self.image = pygame.image.load("pixel_dog.png")  
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect() 
        self.rect.x =200
        self.rect.y =500
        self.gravity=0.01
        self.velocity_x = 3 
        self.velocity_y=3
        self.jump_strength=-13
        self.is_jumping=False
        self.start_time=0


    

    
    def mouv_left(self):
        self.rect.x -= self.velocity_x
    
    def mouv_right(self):
         self.rect.x += self.velocity_x 
    def jump(self):
        if not self.is_jumping:
            start_action=pygame.time.get_ticks()
            self.velocity_y+=self.jump_strength
            if start_action==500:
                self.velocity_y=0
                self.apply_gravity()
                self.is_jumping=True
    def apply_gravity(self):
        self.velocity_y+=self.gravity
        self.rect.y+=self.velocity_y
        if self.rect.y>=700:
            self.rect.y=700
            self.velocity_y=0
            self.is_jumping=False

    