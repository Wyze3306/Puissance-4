from main import game

# Recuperer la colonne avec la position d'un click (chauqe case fait 100 pixels dans notre grille sur l'image)
def get_column(position):
    x = position[0]
    # Modifier avec bonne position
    if 0 <= x < 800:
        return x // 100

# Obtenir le nom du joueur (après améliorer avec les pseudo custom)
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
    for ligne in reversed(range(len(game.grille))):
        if game.grille[ligne][colonne] == ".":
            game.grille[ligne][colonne] = game.player
            break

    win_check(colonne, ligne)

# Verifier si un joueur a gagné
def win_check(colonne, ligne):
    count = [1, 1, 1, 1]
    for i in range(1, 5):
        if ligne + i >= 6:
            continue
        if colonne + i >= 7:
            continue
        if game.grille[ligne + i][colonne] == game.player:
            count[0] += 1
        if game.grille[ligne][colonne + i] == game.player:
            count[1] += 1
        if game.grille[ligne + i][colonne + i] == game.player:
            count[2] += 1
        if game.grille[ligne - i][colonne - i] == game.player:
            count[3] += 1

    if (4 in count):
        game.winner = get_player()

# Fonction pour faire jouer intelligement le bot
def bot_play():
    # Todo
    add_jeton(1)
