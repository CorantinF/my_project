from connect4 import *
from render_connect4 import *

def affiche_grille(g):
    '''Affiche une grille avec des caractères. On affiche un ’O’ pour un disque rouge, un ’X’ pour un disque jaune et un ’-’ pour une case vide.
       :param g:(list) la grille de jeu représenté par une liste
       CU: g une grille valide
       Exemples:
       
       >>> affiche_grille([[2,0,0,0],[1,0,0,2],[1,0,2,1]])
       X---
       O--X
       O-XO
       ====
       0123
       >>> affiche_grille([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
       -------
       -------
       -------
       -------
       -------
       -------
       =======
       0123456
    '''
    x=''
    for e in g:
        for i in e:
            if i == 0:
                x+='-'
            elif i==1:
                x+='O'
            else:
                x+='X'
        print(x)
        x=""
    print(nc(g)*'=')
    o =''
    for k in range(nc(g)):
        o+=str(k)
    print(o)
    
def saisir_colonne_valide(g):
    '''Demande et Renvoie la colonne ou le joueur veux jouer et vérifier si cela est possible
       :param g:(list) une liste qui représente la grille
       :return:(int) la colonne ou le joueur décide de jouer
       CU: g est une grille valide
    '''
    x=int(input("Saisissez une colonne: "))
    while colonne_coup_valide(x,g) == False:
        x=int(input("Colonne non valide, saisissez une autre colonne: "))
    return x

def play(g):
    '''Affiche la grille et Demande la colonne ou le joueur veux jouer,
       vérifier si cela est possible place 1 la ou le joueur veux jouer et 2 la ou le joueur 2 veux jouer,
       ensuite modifie la grille en fonction du coup joué et affiche de nouveau la grille jusque que la grille sois pleine
       :param g:(list) une liste qui représente la grille
       CU: g est une grille valide
    '''
    p=1
    affiche_grille(g)
    winn = False
    while remplie(g)==False and not winn:
        print('joueur',p)
        c=saisir_colonne_valide(g)
        r=ligne_disque_joue(c,g)
        modifie_grille(g,p,c)
        winn = is_win(g,r,c,p)
        p = 1 + p % 2
        affiche_grille(g)
        
    if remplie(g)==True:
        print('Match nul la grille est remplie')
    else:
        print('le joueur', p, 'a gagné bravo!')
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
                
    