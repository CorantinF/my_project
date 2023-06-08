def initialise(nr,nc):
    '''Renvoie une liste qui représente la grille de jeu du puissance 4 avec un nombre de colonnes et de lignes donnés
       :param nr:(int) le nombre de lignes de la grille
       :param nc:(int) le nombre de colonnes de la grille
       :return:(list) une liste de lignes représenté par une liste avec à l'interieur chaque éléments représente une colonne
       CU:nc<10
       Exemples:
       
       >>> initialise(6,7)
       [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
       
       >>> initialise(3,4)
       [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    '''
    l=[]
    for i in range(nr):
        l.append([0]*nc)
    return l
    
        
        
def nr(g):
    '''Renvoie le nombres de lignes de la grille g
       :param g:(list) une liste qui représente la grille
       :return:(int) le nombre de lignes trouvé dans cette grille
       CU:g une grille valide
       Exemples:
       
       >>> nr([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
       6
       >>> nr([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
       3
    '''
    return len(g)


def nc(g):
    '''Renvoie le nombres de colonnes de la grille g
       :param g:(list) une liste qui représente la grille
       :return:(int) le nombre de colonne trouvé dans cette grille
       CU:g une grille valide
       Exemples:
       
       >>> nc([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
       7
       >>> nc([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
       4
    '''
    return len(g[0])

def colonne_coup_valide(c,g):
    '''Renvoie True si la colonne c est un coup valide pour la grille g sinon False
       :param c:(int) la colonne testé si valide ou non de la grille
       :param g:(list) une liste qui représente la grille
       :return:(bool) True si on peut jouer dans la colonne c de la grille g sinon False
       CU:g une grille valide et non pleine
       Exemples:
       >>> colonne_coup_valide(1,[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
       True
       >>> colonne_coup_valide(3,[[2,0,0,0],[1,0,0,2],[1,0,2,1]])
       True
       >>> colonne_coup_valide(0,[[2,0,0,0],[1,0,0,2],[1,0,2,1]])
       False
    '''
    if c<=nc(g):
        for e in g:
            if e[c]==0:
                return True
        else:
            return False
    


def ligne_disque_joue(c,g):
    '''Renvoie la ligne où tombe le disque joué à la colonne c dans la grille g
       :param c:(int) le nombre de colonnes de la grille on le disque tombe
       :param g:(list) la grille de jeu représenté par une liste
       :return:(int) la ligne r ou le disque est tombé en partant du haut et la première ligne étant 0
       CU: g une grille valide et le coup est jouable dans la colonne c
       Exemples:
       
       >>> ligne_disque_joue(1,[[0, 0, 0, 0], [0, 0, 0, 0], [0,0,0,0]])
       2
       >>> ligne_disque_joue(2,[[2,0,0,0],[1,0,0,2],[1,0,2,1]])
       1
    '''
    x=0
    for i in range(len(g)):
        if g[i][c]==0:
            x=i
    return x
            
def modifie_grille(g,p,c):
    '''Modifie puis renvoie la grille avec le disque p qui a joué a la colonne c
       :param g:(list)la grille de jeu représenté par une liste
       :param p:(int) 1 ou 2 selon si le joueur 1 ou 2 joue
       :param c:(int) le nombre de colonnes de la grille on le disque tombe
       CU:g une grille valide
    '''
    assert colonne_coup_valide(c,g), "coup non valide plus de place dans la colonne"
    r=ligne_disque_joue(c,g)
    g[r][c]=p
    
def remplie(g):
    '''Renvoie True si une grille g est remplie sinon False
       :param g:(list) une liste qui représente la grille
       :return:(bool) True si la grille est remplie sinon False
       CU:g une grille valide
       Exemples:
       
       >>> remplie([[0, 0, 0, 0], [0, 0, 0, 0], [0,0,0,0]])
       False
       >>> remplie([[2,0,0,0],[1,0,0,2],[1,0,2,1]])
       False
       >>> remplie([[2,1,1,2],[1,2,1,2],[1,2,2,1]])
       True
    '''
    for e in g:
        for i in e:
            if i==0:
                return False
        else:
            return True


def lc_lignes(g,r,c):
    '''Construit et renvoie la liste des coordonnées des cases avec la valeur de la case pour la ligne
       :param g:(list) une liste qui représente la grille
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :retrun:(list) la liste des coordonnées des cases
       CU: c une colonne de g et r une ligne de g
       Exemples:
       
       >>> lc_lignes([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],2,2)
       [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)]
       >>> lc_lignes([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],0,3)
       [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
       >>> lc_lignes([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],0,3)
       [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
    '''
    lc=[]
    for i in range(c-3,c+4):
        if i>=0 and i<nc(g):
            lc.append((r,i))
    return lc
            
def lc_colonnes(g,r,c):
    '''Construit et renvoie la liste des coordonnées des cases avec la valeur de la case pour la colonne
       :param g:(list) une liste qui représente la grille
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :retrun:(list) la liste des coordonnées des cases
       CU: c une colonne de g et r une ligne de g
       Exemples:
       >>> lc_colonnes(initialise(6,7),2,3)
       [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3)]
       >>> lc_colonnes(initialise(6,7),0,5)
       [(0, 5), (1, 5), (2, 5), (3, 5)]
       
    '''
    lc=[]
    for j in range(-3,4):
        i = r + j
        if i>=0 and i<nr(g):
            lc.append((i,c))
    return lc

def lc_diagonalesv1(g,r,c):
    '''Construit et renvoie la liste des coordonnées des cases avec la valeur de la case pour la première diagonale
       :param g:(list) une liste qui représente la grille
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :retrun:(list) la liste des coordonnées des cases
       CU: c une colonne de g et r une ligne de g
       >>> lc_diagonalesv1(initialise(6,7),0,5)
       [(0, 5), (1, 6)]
       >>> lc_diagonalesv1(initialise(6,7),3,3)
       [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    '''
    lc=[]
    for j in range (-3,4):
        x = r + j
        y = c + j
        if x>=0 and x<nr(g) and y >=0 and y<nc(g):
            lc.append((x,y))
    return lc


def lc_diagonalesv2(g,r,c):
    '''Construit et renvoie la liste des coordonnées des cases avec la valeur de la case pour la deuxiéme diagonale
       :param g:(list) une liste qui représente la grille
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :retrun:(list) la liste des coordonnées des cases
       CU: c une colonne de g et r une ligne de g
       >>> lc_diagonalesv2(initialise(6,7),3,3)
       [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
       >>> lc_diagonalesv2(initialise(6,7),0,5)
       [(0, 5), (1, 4), (2, 3), (3, 2)]
    '''
    lc=[]
    for j in range (-3,4):
        x = r + j
        y = c - j
        if x>=0 and x<nr(g) and y >=0 and y<nc(g):
            lc.append((x,y))
    return lc




def is_align4(g,lc,p):
    '''Indique, pour la grille g, s’il y a 4 cases consécutives de valeur p pour les cases dont
       les coordonnées sont données dans la liste lc.
       :param g: (list) une liste qui représente la grille
       :param lc: (list) une liste de coordonnées des cases
       :param p: (int) 1 ou 2 selon si le joueur 1 ou 2 joue
       :return: (bool) True s'il y a 4 cases consécutives de valeur p pour les cases dont
       les coordonnées sont données dans la liste lc et False sinon
       CU:lc une liste d'index corespondant a des indices de g et p vaut 1 ou 2
       >>> is_align4([[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],lc_lignes([[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],0,0),1)
       True
       >>> is_align4([[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],lc_colonnes([[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],0,0),1)
       True
    '''
    ALIGN=False
    for i in range(len(lc)-3):
        if all(g[x][y]==p for (x,y) in lc[i:i+4]):
            ALIGN=True
    return ALIGN

def is_win(g,r,c,p):
    '''Indique si la case (r,c) provoque la victoire du joueur p.
       :param g: (list) une liste qui représente la grille
       :param p: (int) 1 ou 2 selon si le joueur 1 ou 2 joue
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :return: (bool) True si la case (r,c) provoque la victoire du joueur p et False sinon
       CU:c une colonne de g et r une ligne de g et p vaut 1 et 2
       is_win([[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],0,0,1)
       True
       >>> is_win([[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],0,0,1)
       True
    '''
    gagne=False
    if is_align4(g,lc_colonnes(g,r,c),p)==True:
        gagne=True
    elif is_align4(g,lc_lignes(g,r,c),p)==True:
        gagne=True
    elif is_align4(g,lc_diagonalesv1(g,r,c),p)==True:
        gagne=True
    elif is_align4(g,lc_diagonalesv2(g,r,c),p)==True:
        gagne=True
    return gagne

from random import *
def ia_aleat(g):
    '''Renvoie aléatoirement une colonne c qui sera le coup d el'ordinateur.
       :param g: (list) une liste qui représente la grille
       :return: (int)  une colonne c qui sera le coup d el'ordinateur
       CU: il faut choisir aléatoirement parmi les coups valides uniquement, et non sur toutes les colonnes
    '''
    c= randint(0,6)
    if colonne_coup_valide(c,g)==False:
        c=randint(0,6)
    else:
        return c

def unmove(g,c):
    '''Annule le dernier coup c dans la grille.
       :param g: (list) une liste qui représente la grille
       :param c: (int) coordonnée de la colonne testé
       CU:c une colonne de g
       
    '''
    r=ligne_disque_joue(c,g)
    g[r][c]=0
    

def ia_win(g,p):
    '''Deteremine si un coup est gagnant, si oui il le joue sinon il joue aleatoirement
       :param g: (list) une liste qui représente la grille
       :param p: (int) 1 ou 2 selon si le joueur 1 ou 2 joue
       :return: (int) colonne joué par l'ordinateur.
       CU: p vaut un ou deux g grille valide
    '''
    c=0
    while c<nc(g):
        r=ligne_disque_joue(c,g)
        g[r][c]=p
        if is_win(g,r,c,p)==True:
            g[r][c]=0
            return c
        else:
            g[r][c]=0
            c+=1
    return ia_aleat(g)

def score4(l):
    '''Calcule le score d’un quadruplet.
       :param l:(list) une liste qui rerésente un quadruplet
       :return:(int) le score du quadruplet
       CU: l une liste de quatre int contenant soit des 1 ou 2 ou 0
       >>> score4((1,1,1,2))
       0
       >>> score4((1,1,1,0))
       1000
       >>> score4((0,0,2,2))
       -10
    '''
    score=0
    if l.count(0)==4:
        score+=0
    elif l.count(1)>0 and l.count(2)>0:
        score+=0
    elif l.count(1)==1 and l.count(0)==3:
        score+=1
    elif l.count(1)==2 and l.count(0)==2:
        score+=10
    elif l.count(1)==3 and l.count(0)==1:
        score+=1000
    elif l.count(1)==4:
        score+=100000
    elif l.count(2)==1 and l.count(0)==3:
        score-=1
    elif l.count(2)==2 and l.count(0)==2:
        score-=10
    elif l.count(2)==3 and l.count(0)==1:
        score-=500
    return score


def score_ligne(g):
    '''Renvoie le score de toute les lignes de la grille
       :param g:(list) une grille de jeu
       :return:(list) une liste des score des lignes
       CU: g une grille valide
       >>> score_ligne([[0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
       [1000, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       >>> score_ligne([[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
       [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    '''
    i=0
    n=[]
    for l in range(len(g)):
        i=0
        while i<len(g)-4:
            n.append(score4(g[l][i:i+4]))
            i+=1
    return n

def score_colonne(g):
    s=[]
    n=[]
    for i in range (len(g)):
        for l in range(4):
            s.append(g[i][l])
        n.append(score4(s))
        s=[]
    return n


def score_diav1(g):
    s=[]
    n=[]
    for r in range(3):
        for c in range(4):
            for j in range (-3,4):
                x = r + j
                y = c + j
                if x>=0 and x<nr(g) and y >=0 and y<nc(g):
                    s.append(g[x][y])
            n.append(score4(s))
            s=[]
    return n


def score_diav2(g):
    s=[]
    n=[]
    for r in range(3):
        for c in range(3,7):
            for j in range (-3,4):
                x = r + j
                y = c - j
                if x>=0 and x<nr(g) and y >=0 and y<nc(g):
                    s.append(g[x][y])
            n.append(score4(s))
            s=[]
    return n
 

def score_grille(g):
    l=score_diav1(g)+score_diav2(g)+score_colonne(g)+score_ligne(g)
    s=sorted(l)
    return s



###PUISSANCE 5

def lc_lignes_5(g,r,c):
    '''Construit et renvoie la liste des coordonnées des cases avec la valeur de la case pour la ligne
       :param g:(list) une liste qui représente la grille
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :retrun:(list) la liste des coordonnées des cases
       CU: c une colonne de g et r une ligne de g
       Exemples:
    '''
    lc=[]
    for i in range(c-4,c+5):
        if i>=0 and i<nc(g):
            lc.append((r,i))
    return lc
            
def lc_colonnes_5(g,r,c):
    '''Construit et renvoie la liste des coordonnées des cases avec la valeur de la case pour la colonne
       :param g:(list) une liste qui représente la grille
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :retrun:(list) la liste des coordonnées des cases
       CU: c une colonne de g et r une ligne de g
    '''
    lc=[]
    for j in range(-4,5):
        i = r + j
        if i>=0 and i<nr(g):
            lc.append((i,c))
    return lc

def lc_diagonalesv1_5(g,r,c):
    '''Construit et renvoie la liste des coordonnées des cases avec la valeur de la case pour la première diagonale
       :param g:(list) une liste qui représente la grille
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :retrun:(list) la liste des coordonnées des cases
       CU: c une colonne de g et r une ligne de g
    '''
    lc=[]
    for j in range (-4,5):
        x = r + j
        y = c + j
        if x>=0 and x<nr(g) and y >=0 and y<nc(g):
            lc.append((x,y))
    return lc


def lc_diagonalesv2_5(g,r,c):
    '''Construit et renvoie la liste des coordonnées des cases avec la valeur de la case pour la deuxiéme diagonale
       :param g:(list) une liste qui représente la grille
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :retrun:(list) la liste des coordonnées des cases
       CU: c une colonne de g et r une ligne de g
    '''
    lc=[]
    for j in range (-4,5):
        x = r + j
        y = c - j
        if x>=0 and x<nr(g) and y >=0 and y<nc(g):
            lc.append((x,y))
    return lc




def is_align5(g,lc,p):
    '''Indique, pour la grille g, s’il y a 4 cases consécutives de valeur p pour les cases dont
       les coordonnées sont données dans la liste lc.
       :param g: (list) une liste qui représente la grille
       :param lc: (list) une liste de coordonnées des cases
       :param p: (int) 1 ou 2 selon si le joueur 1 ou 2 joue
       :return: (bool) True s'il y a 4 cases consécutives de valeur p pour les cases dont
       les coordonnées sont données dans la liste lc et False sinon
       CU:
    '''
    ALIGN=False
    for i in range(len(lc)-4):
        if all(g[x][y]==p for (x,y) in lc[i:i+5]):
            ALIGN=True
    return ALIGN

def is_win5(g,r,c,p):
    '''Indique si la case (r,c) provoque la victoire du joueur p.
       :param g: (list) une liste qui représente la grille
       :param p: (int) 1 ou 2 selon si le joueur 1 ou 2 joue
       :param c:(int) coordonnée de la colonne testé
       :param r:(int) coordonnée de la ligne testé
       :return: (bool) True si la case (r,c) provoque la victoire du joueur p et False sinon
       CU:
    '''
    gagne=False
    if is_align5(g,lc_colonnes_5(g,r,c),p)==True:
        gagne=True
    elif is_align5(g,lc_lignes_5(g,r,c),p)==True:
        gagne=True
    elif is_align5(g,lc_diagonalesv1_5(g,r,c),p)==True:
        gagne=True
    elif is_align5(g,lc_diagonalesv2_5(g,r,c),p)==True:
        gagne=True
    return gagne


if __name__ == "__main__":
    import doctest
    doctest.testmod()
        


        
        
