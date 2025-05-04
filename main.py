import pygame
import math
from game import Game
pygame.init()

# Initialisé le jeu
game = Game()
running = True

# Differentes variables d'interfaces
size = (1080, 720) # background.get_size()
pygame.display.set_caption("Puissance 4 by GRISOLLET Rémy & LESAUX Antonin")
screen = pygame.display.set_mode(size)

background = pygame.image.load("images/background.png")
background = pygame.transform.scale(background, size)

friend_button = pygame.image.load("images/friend_button.png")
friend_button = pygame.transform.scale(friend_button, (350, 200))
friend_button_react = friend_button.get_rect()
friend_button_react.x = math.ceil(screen.get_width() / 2)
friend_button_react.y = math.ceil(screen.get_height() / 2)

bot_button = pygame.image.load("images/bot_button.png")
bot_button = pygame.transform.scale(bot_button, (350, 200))
bot_button_react = bot_button.get_rect()
bot_button_react.x = math.ceil(screen.get_width() / 6)
bot_button_react.y = math.ceil(screen.get_height() / 2)


while running:
    # Voir si la partie est lancé (donc update la fenetre)
    if game.isPlaying:
        game.update(screen)
    elif game.winner != None:
        game.finish(screen)
    else:
        # Gérer le menu
        screen.blit(background, (0, 0))
        screen.blit(friend_button, friend_button_react)
        screen.blit(bot_button, bot_button_react)
        pygame.display.flip()
        
    
    #Gérer les events
    for event in pygame.event.get():
        # Evenement de fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        # Click sur la souris -> verification bouton
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if friend_button_react.collidepoint(pos):
                game.start(False)
            elif bot_button_react.collidepoint(pos):
                game.start(True)