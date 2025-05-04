import pygame
import manager

class Game:
    # Constante de la grille de jeu (vide)
    GRILLE_CONST = [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."]]

    # Générer les valeurs par default d'une partie
    def __init__(self):
        self.isPlaying = False
        self.isBot = True
        self.grille = self.GRILLE_CONST
        self.player = "X" # X = Jaune & O = Rouge
        self.round = 0
        self.winner = None
    
    # Lancer une partie
    def start(self, gamemode = True):
        self.isPlaying = True
        self.isBot = gamemode
    
    def finish(self, screen):
        # Afficher l'ecran de fin
        gameover = pygame.image.load("images/gameover.png")
        gameover = pygame.transform.scale(gameover, (1080, 720))
        screen.blit(gameover, (0, 0))
        pygame.display.flip()

        #Gerer les events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                column = manager.get_column(pos)
                # Todo : Verifier si on click bien sur le jeu (pas en dehors)
                if self.round % 2 == 0:
                    # Tour du Joueur 1 car le nombre de tour est pair
                    self.player = "X"
                    manager.add_jeton(column)
                    self.play_animation_jeton()
                else:
                    # Tour du Joueur 2 OU Bot car le nombre de tour est pair
                    self.player = "O"
                    manager.add_jeton(column)
                    self.play_animation_jeton()
    
    # Mettre l'animation et le positionnement du jeton jouer
    def play_animation_jeton(self, screen):
        if self.player == "X":
            jeton = pygame.image.load("images/pion_jaune.png")
        else:
            jeton = pygame.image.load("images/pion_rouge.png")
        jeton = pygame.transform.scale(jeton, (50, 50))
        screen.blit(jeton, (0, 0)) # Calculer la bonne position

    # Terminer la partie
    def end(self):
        self.isPlaying = False
        self.isBot = True
        self.grille = self.GRILLE_CONST
        self.player = "X"
        self.round = 0
        self.winner = None
        
    # Actualiser toujours lorsque la partie est lancé
    def update(self, screen):
        # Afficher le plateau
        plateau = pygame.image.load("images/plateau.png")
        plateau = pygame.transform.scale(plateau, (1080, 720))
        screen.blit(plateau, (0, 0))
        pygame.display.flip()

        #Gerer les events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                column = manager.get_column(pos)
                if self.round % 2 == 0:
                    # Tour du Joueur 1 car le nombre de tour est pair
                    self.player = "X"
                    manager.add_jeton(column)
                elif self.isBot:
                    # Tour du Bot car le nombre de tour est pair
                    self.player = "O"
                    manager.bot_play()
                else:
                    # Tour du Joueur 2 OU Bot car le nombre de tour est pair
                    self.player = "O"
                    manager.add_jeton(column)




