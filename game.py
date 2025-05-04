import pygame

class Game:
    # Constante de la grille de jeu (vide)
    GRILLE_CONST = [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."]]

    # Generer les valeurs par default d'une partie
    def __init__(self):
        self.isPlaying = False
        self.isBot = True
        self.grille = self.GRILLE_CONST
    
    # Lancer une partie
    def start(self, gamemode = True):
        self.isPlaying = True
        self.isBot = gamemode
    
    # Terminé la partie
    def end(self):
        self.isPlaying = False
        self.isBot = True
        self.grille = self.GRILLE_CONST
    
    # Actualiser toujours lorsque la partie est lancé
    def update(self, screen):
        # Afficher le plateau
        plateau = pygame.image.load("images/plateau.png")
        screen.blit(plateau, (0, 100))
        pygame.display.flip()

        #Gerer les events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #position
                pos = event.pos
                #column = manager.getColumn(pos)
                print("down souris", pos)