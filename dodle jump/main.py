import pygame
from game import Game

pygame.init()
screen = pygame.display.set_mode((500,800))  
pygame.display.set_caption("Doodle Jump") 
background = pygame.image.load("background.png") 
game = Game()  
running = True

while running:
    screen.blit(background, (0, 0))
    game.all_platform.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True 
              
        elif game.pressed.get(pygame.K_p):
             pygame.QUIT()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False  
    
    if game.pressed.get(pygame.K_q):  
                game.player.mouv_left()
                if game.player.rect.x<=0:
                    game.player.rect.x=500
    elif game.pressed.get(pygame.K_d)and game.player.rect.x<=800:  
                game.player.mouv_right()
                if game.player.rect.x>=500:
                    game.player.rect.x=0
    game.update(screen) 
    
    pygame.display.flip()  
pygame.quit()  
