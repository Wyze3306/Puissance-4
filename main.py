class Game:
    # Générer les valeurs par default d'une partie
    def __init__(self):
        self.isPlaying = False
        self.isBot = True
        self.grille = [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."]]
        self.player = "X" # X = Jaune & O = Rouge
        self.round = 0
        self.winner = None
        self.jetons = []

    # Lancer une partie
    def start(self, gamemode = True):
        self.isPlaying = True
        self.isBot = gamemode

    def finish(self, screen, null = False):
        self.isPlaying = False

        # Afficher l'ecran de fin
        gameover = pygame.image.load("images/background.png")
        gameover = pygame.transform.scale(gameover, (1080, 720))

        back_button = pygame.image.load("images/back_button.png")
        back_button = pygame.transform.scale(back_button, (350, 200))
        back_button_react = back_button.get_rect()
        back_button_react.x = math.ceil(screen.get_width() / 3.085714285714286)
        back_button_react.y = math.ceil(screen.get_height() / 2)

        if null == True :
            imgWinName = "win_null"
        elif game.winner == "Joueur 1":
            imgWinName = "win_player1"
        else:
            imgWinName = "win_player2"
        text_win = pygame.image.load("images/" + imgWinName + ".png")
        text_win = pygame.transform.scale(text_win, (350, 200))
        text_win_react = text_win.get_rect()
        text_win_react.x = math.ceil(screen.get_width() / 3.085714285714286)
        text_win_react.y = math.ceil(screen.get_height() / 3)

        screen.blit(gameover, (0, 0))
        screen.blit(text_win, text_win_react)
        screen.blit(back_button, back_button_react)
        pygame.display.flip()

        #Gerer les events
        for event in pygame.event.get():
            # Evenement de fermer la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()

            # Gerer le bouton retour
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if back_button_react.collidepoint(pos):
                    self.end()

    # Ajouter la position du jeton jouer (Todo: Faire l'animation de pose juste pour le derniere jeton jouer)
    """def play_animation_jeton(self, position):
        if self.player == "X":
            jeton = pygame.image.load("images/pion_jaune.png")
        else:
            jeton = pygame.image.load("images/pion_rouge.png")
        jeton = pygame.transform.scale(jeton, (70, 70))
        self.jetons.append([jeton, (position[0] - 35, position[1] - 35)])

        # Jouer un son de jeton qui tombe
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/play_jeton.mp3")
        pygame.mixer.music.play()"""
    def play_animation_jeton(self, posUiJeton, posJeton):
        if self.player == "X":
            jeton_image = pygame.image.load("images/pion_jaune.png")
        else:
            jeton_image = pygame.image.load("images/pion_rouge.png")
        jeton_image = pygame.transform.scale(jeton_image, (70, 70))

        # Son
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/play_jeton.mp3")
        pygame.mixer.music.play()

        # Animation pour faire descendre le jeton
        colonne = posJeton[1]
        maxLigne = posJeton[0] # Ligne de la position final du jeton
        if maxLigne != 0: # Si pas la ligne max (pas d'animation)
            ligne = 0

            while ligne < maxLigne:
                tempPos = get_position_jeton((ligne, colonne))

                screen.blit(jeton_image, (tempPos[0] - 35, tempPos[1] - 35))
                pygame.display.flip()
                pygame.time.delay(40)
                ligne += 1

        # Ajouter le jeton à la bonne position finale
        self.jetons.append([jeton_image, (posUiJeton[0] - 35, posUiJeton[1] - 35)])


    # Terminer la partie
    def end(self):
        self.isPlaying = False
        self.isBot = True
        self.grille = [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."]]
        self.player = "X"
        self.round = 0
        self.winner = None
        self.jetons = []

    # Actualiser toujours lorsque la partie est lancé
    def update(self, screen):
        # Verifier si un joueur a win
        if self.winner != None:
            if self.winner == False:
                self.finish(screen, False)
                return
            else:
                # Jouer un son de win
                pygame.mixer.init()
                pygame.mixer.music.load("sounds/win.mp3")
                pygame.mixer.music.play()
                # Afficher l'écran de fin
                self.finish(screen)
                return

        # Afficher le plateau
        plateau = pygame.image.load("images/plateau.png")
        plateau = pygame.transform.scale(plateau, (1080, 720))
        screen.blit(plateau, (0, 0))

        # affiché tout les autres jetons
        for jeton in self.jetons:
            screen.blit(jeton[0], jeton[1])

        pygame.display.flip()

        #Gerer les events
        for event in pygame.event.get():
            # Evenement de fermer la fenetre
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                column = get_column(pos)
                if column == None:
                    return
                posJeton = event.pos
                if self.round % 2 == 0:
                    # Tour du Joueur 1 car le nombre de tour est pair
                    self.player = "X"
                    posJeton = add_jeton(column)
                    if posJeton == None:
                        return
                    posUiJeton = get_position_jeton(posJeton)
                    self.play_animation_jeton(posUiJeton, posJeton)
                    self.round += 1
                    if self.isBot == True:
                        bot_play()
                elif self.isBot == False:
                    # Tour du Joueur 2 car le nombre de tour est pair
                    self.player = "O"
                    posJeton = add_jeton(column)
                    if posJeton == None:
                        return
                    posUiJeton = get_position_jeton(posJeton)
                    self.play_animation_jeton(posUiJeton, posJeton)
                    self.round += 1

import pygame
import math
import random
from time import time
pygame.init()

# Initialisé le jeu
running = True
game = Game()

# Recuperer la colonne avec la position d'un click (chauqe case fait 100 pixels dans notre grille sur l'image)
def get_column(position):
    x = position[0]
    # Modifier avec bonne position
    if 200 <= x < 900:
        return x // 100 - 2
    else:
        return None

# Fonction pour calculer la position (x, y) d’un jeton
def get_position_jeton(position):
    ligne = position[0]
    colonne = position[1]

    # Centre d'un trou (en bas à gauche)
    X0 = 257
    Y0 = 554
    # Espacements
    ESP_X = 94
    ESP_Y = 82

    # Inverser la ligne pour que ligne 0 soit en bas visuellement
    ligne_visuelle = 5 - ligne

    x = X0 + colonne * ESP_X
    y = Y0 - ligne_visuelle * ESP_Y

    return (int(x), int(y))

# Obtenir le nom du joueur (Todo: améliorer avec les pseudo custom)
def get_player():
    if game.player == "X":
        return "Joueur 1"
    else:
        if game.isBot:
            return "Bot"
        else:
            return "Joueur 2"

# Ajouter un jeton dans la grille
def add_jeton(colonne):
    search = False
    for ligne in reversed(range(len(game.grille))):
        if game.grille[ligne][colonne] == ".":
            search = True
            game.grille[ligne][colonne] = game.player
            break

    if search == True:
        win_check(colonne, ligne)
        return [ligne, colonne]
    else:
        if check_null() == False:
            game.winner = False
        else:
            return None
    
def check_null():
    for ligne in game.grille:
        if "." in ligne:
            return True
    return False

# Verifier si un joueur a gagné
def win_check(colonne, ligne):
    win = False
    maxL = 5
    maxC = 6
    min = 0
    # VERTICALE
    if colonne + 3 <= maxL:
        if game.grille[ligne][colonne+1] == game.player and game.grille[ligne][colonne+2] == game.player and game.grille[ligne][colonne+3] == game.player:
            win = True
    if colonne - 3 >= min:
        if game.grille[ligne][colonne-1] == game.player and game.grille[ligne][colonne-2] == game.player and game.grille[ligne][colonne-3] == game.player:
            win = True
    # HORIZONTALE
    if ligne + 3 < maxC:
        if game.grille[ligne+1][colonne] == game.player and game.grille[ligne+2][colonne] == game.player and game.grille[ligne+3][colonne] == game.player:
            win = True
    if ligne - 3 >= min:
        if game.grille[ligne-1][colonne] == game.player and game.grille[ligne-2][colonne] == game.player and game.grille[ligne-3][colonne] == game.player:
            win = True

    # DIAGONALE
    if colonne + 3 <= maxC and ligne + 3 <= maxL:
        if game.grille[ligne+1][colonne+1] == game.player and game.grille[ligne+2][colonne+2] == game.player and game.grille[ligne+3][colonne+3] == game.player:
            win = True
    if colonne - 3 >= min and ligne - 3 >= min:
        if game.grille[ligne-1][colonne-1] == game.player and game.grille[ligne-2][colonne-2] == game.player and game.grille[ligne-3][colonne-3] == game.player:
            win = True
    if colonne + 3 <= maxC and ligne - 3 >= min:
        if game.grille[ligne-1][colonne+1] == game.player and game.grille[ligne-2][colonne+2] == game.player and game.grille[ligne-3][colonne+3] == game.player:
            win = True
    if colonne - 3 >= min and ligne + 3 <= maxL:
        if game.grille[ligne+1][colonne-1] == game.player and game.grille[ligne+2][colonne-2] == game.player and game.grille[ligne+3][colonne-3] == game.player:
            win = True

    if win == True:
        game.winner = get_player()

# Fonction pour faire jouer intelligement le bot
def bot_play():
    game.player = "O"

    forWin = check_win_3(game.player) # Voir si le bot (joueur 2) peut gagner en jouant

    if forWin == None:
        # Regarder si on peut bloquer le joueur
        forBlock = check_win_3("X") # Voir si le joueur adverse peut gagner
        if forBlock == None:
            # Jouer aléatoirement
            column = random.randint(0, 6)
        else:
            # Bloquer le joueur
            column = forBlock
    else:
        # Joueur le jeton pour gagner
        column = forWin

    posJeton = add_jeton(column)
    posUiJeton = get_position_jeton(posJeton)
    game.play_animation_jeton(posUiJeton, posJeton)
    game.round += 1

def check_win_3(player):
    i = 0
    while i < 6:
        j = 0
        while j < 7:
            # VERTICALE
            if i >= 3 and game.grille[i][j] == player and game.grille[i-1][j] == player and game.grille[i-2][j] == player and game.grille[i-3][j] == ".":
                return j

            if game.grille[i][j] == player:
                # HORIZONTALE DROITE
                if j <= 3 and game.grille[i][j+1] == player and game.grille[i][j+2] == player and game.grille[i][j+3] == "." and (i == 5 or game.grille[i+1][j+3] != "."):
                    return j+3

                # HORIZONTALE GAUCHE
                if j >= 3 and game.grille[i][j-1] == player and game.grille[i][j-2] == player and game.grille[i][j-3] == "." and (i == 5 or game.grille[i+1][j-3] != "."):
                    return j-3

                # DIAGONALE INVERSE
                if i <= 2 and j <= 3 and game.grille[i+1][j+1] == player and game.grille[i+2][j+2] == player and game.grille[i+3][j+3] == "." and (i+3 == 5 or game.grille[i+4][j+3] != "."):
                    return j+3

                # DIAGONALE
                if i <= 2 and j >= 3 and game.grille[i+1][j-1] == player and game.grille[i+2][j-2] == player and game.grille[i+3][j-3] == "." and (i+3 == 5 or game.grille[i+4][j-3] != "."):
                    return j-3
            j += 1
        i += 1
    return None


# Differentes variables d'interfaces
size = (1080, 720)
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

        # Click sur la souris -> verification bouton
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if friend_button_react.collidepoint(pos):
                game.start(False)
            elif bot_button_react.collidepoint(pos):
                game.start(True)