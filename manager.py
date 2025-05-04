# Recuperer la colonne avec la position d'un click (chauqe case fait 100 pixels dans notre grille sur l'image)
def get_column(position):
    x = position[0]
    if 0 <= x < 800:
        return x // 100

# Ajouter un jeton dans la grille
def add_jeton(grille, colonne, jeton):
    for ligne in reversed(range(len(grille))):
        if grille[ligne][colonne] == ".":
            grille[ligne][colonne] = jeton
            break

    win_check(grille, colonne, ligne, jeton)


# Verifier si un joueur a gagné
def win_check(grille, colonne, ligne, jeton):
    count = [1, 1, 1, 1]
    for i in range(1, 5):
        if ligne + i >= 6:
            continue
        if colonne + i >= 7:
            continue
        if grille[ligne + i][colonne] == jeton:
            count[0] += 1
        if grille[ligne][colonne + i] == jeton:
            count[1] += 1
        if grille[ligne + i][colonne + i] == jeton:
            count[2] += 1
        if grille[ligne - i][colonne - i] == jeton:
            count[3] += 1

    if (4 in count):
        global winner
        winner = player_with_jeton(jeton)


def player_with_jeton(jeton):
    if jeton == "X":
        return ""
    elif jeton == "O":
        return "player2"
    
def finish(winner):
    print("Le joueur ", winner, "a gagné !")
    reload = None
    while reload != "oui" or reload != 'non':
        reload = input("Voulez vous refaire une partie ? (oui/non)")
        if reload == "oui":
            grille = [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."]]
            player1 = input("Qu'elle le pseudo du première joueur ? ")
            player2 = input("Qu'elle le pseudo du deuxième joueur ? ")
            roundPlayer = 1
            winner = None
        elif reload == "non":
            exit()
