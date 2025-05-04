# Afficher la grille completement
def print_grille(grille, playerName):
    ligneTxt = None
    print("Puissance 4 - C'est au tour de", playerName, "\n")
    print("    1   2   3   4   5   6   7  ")
    print("-------------------------------")
    for ligne in range(len(grille)):
        for colonne in range(len(grille[ligne])):
            if ligneTxt == None:
                ligneTxt = "|" + str(ligne + 1) + "| "
            ligneTxt += grille[ligne][colonne] + " | "
        print(ligneTxt)
        ligneTxt = None


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
        return player1
    elif jeton == "O":
        return player2

global winner, player1, player2
grille = [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."]]
player1 = input("Qu'elle le pseudo du première joueur ? ")
player2 = input("Qu'elle le pseudo du deuxième joueur ? ")
roundPlayer = 1
winner = None

while True:
    if winner != None:
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

    # C'est le tour du joueur 1
    if roundPlayer == 1:
        print_grille(grille, player1)
        colonne = 999
        while colonne > len(grille)+1 or colonne <= 0:
            colonne = int(input(player2 + ": Dans qu'elle colonne voulez vous mettre un jeton ? (1-7)"))

        add_jeton(grille, colonne - 1, "X")
        roundPlayer = 2
    # C'est le tour du joueur 2
    elif roundPlayer == 2:
        print_grille(grille, player2)
        colonne = 999
        while colonne > len(grille)+1 or colonne <= 0:
            colonne = int(input(player2 + ": Dans qu'elle colonne voulez vous mettre un jeton ? (1-7)"))

        add_jeton(grille, colonne - 1, "O")
        roundPlayer = 1
