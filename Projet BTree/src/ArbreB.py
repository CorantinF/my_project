from Noeud import *

# Tree
class ArbreB:
    '''
    Classe de l'Arbre B, une structure de données en arbres équilibré.   
    '''
    def __init__(self, L, U):
        '''
        Construction d'un ArbreB avec pour racine un Noeud sans parent, et commme contrainte 2 * L - 1 <= U dans chaque noeud
        '''
        if 2 * L - 1 <= U:
            self.U = U
            self.L = L
            self.racine = Noeud(self, None, L, U)
        else:
            raise()
        
        
    def __recherche_cle(self, c ,noeud):
        '''
        recherche une clé dans un arbre débute la recherche dans le noeud passé en paramètre
        :param c:(int) clé que l'on recherche
        :param noeud:(Noeud) noeud dans lequel on démarre la recherche
        :return:(bool) True si la clé est dans l'arbre B avec pour racine le Noeud n
        :CU:
        '''
        i=0
        while i < len(noeud.cle) and c > noeud.cle[i]:
            # boucle qui parcours les clés d'un noeud et vérifie si la clé passé en parametre et plus grande que celle a l'indice
            i+=1
        if noeud.est_feuille():
            # si le noeud est un noeud feuille on renvoie True si la valeur est dans la feuille sinon False
            return i < len(noeud.cle) and c == noeud.cle[i]
        else:
            #si dans le noeud on trouve la clé à l'indice i donnée on renvoie true
            if i < len(noeud.cle) and c == noeud.cle[i]:
                return True
            else:
                # Sinon on descend dans l'enfant à l'indice i afin de regarder si la clé est dans le noeud fils entre la clé a l'indice i et i+1 donc entre les deux clé, ceci récursivement
                return self.__recherche_cle(c, noeud.enfant[i])
        
        
    def recherche_cle(self, c):
        '''
        recherche un clé dans un arbre en partant de la racine
        :param c:(int) clé que l'on recherche
        :return:(bool) True si la clé est dans l'arbre B, recherche qui démarre a la racine de l'arbre
        :CU:
        >>> B = ArbreB(2,3)
        >>> B.insertion(0)
        >>> B.recherche_cle(0)
        True
        >>> B.recherche_cle(1)
        False
        '''
        #démare la recherche dans à partir de la racine
        return self.__recherche_cle(c, self.racine)
        
        
    def insertion(self, c):
        '''
        insére une clé dans un arbre au bon endroit partant de la racine
        :param c:(int) clé que l'on veut insérer dans l'arbre
        :return:(bool) False si la clé est déjà presente dans l'arbre
        :CU:
        >>> B = ArbreB(2,3)
        >>> B.insertion(0)
        >>> B.recherche_cle(0)
        True
        >>> B.afficher_arbre()
        '[0]'
        '''
        # démarre l'insertion à partir de la racine
        return self.__insertion(self.racine, c)

    def __insertion(self, noeud, c):
        '''
        insère une clé dans un arbre au bon endroit en partant du noeud passé en paramètre
        :param noeud:(Noeud) noeud dans lequel on démarre pour chercher a insérer la clé au bon endroit
        :param c:(int) clé que l'on veut insérer dans l'arbre
        :return:(bool) False si la clé est déja presente dans l'arbre qui a pour racine le noeud noeud
        :CU:
        '''
        i=0
        #on verifie d'abord si la clé est déjà dans l'arbre si elle l'est pas besoin de l'ajouté
        if self.recherche_cle(c) == True:
            return False
        else:
            # on parcours la liste des clé du noeud pour savoir a quel endroit il faut l'insérer
            while i < len(noeud.cle) and c > noeud.cle[i]:
                i+=1
            if not noeud.est_feuille():
                # si le noeud n'est pas une feuille alors on regarde le fils à l'indice i récursivement jusqu'a atteindre une feuille, afin de l'inserer dans le noeud enfant de i
                self.__insertion(noeud.enfant[i],c)
            else:
                # si le noeud est une feuille on applique la fonction insere noeud pour inserer la clé correctement dans le noeud. fonction de la classe noeud qui appelle nombreuse fonction
                noeud.insere_noeud(c)
                    

    def afficher_arbre(self):
        '''
        affiche un arbre sous un format str défini ou on voit les noeud représentés par des listes et leurs fils relié par une flèche  
        :return:(str) affiche un arbre selon un format défini
        :CU:
        >>> B = ArbreB(2,3)
        >>> B.insertion(0)
        >>> B.insertion(1)
        >>> B.insertion(2)
        >>> B.insertion(3)
        >>> B.insertion(4)
        >>> B.insertion(5)
        >>> B.insertion(6)
        >>> B.insertion(7)
        >>> B.insertion(8)
        >>> B.insertion(9)
        >>> print(B.afficher_arbre())
        [3] ---> [1] ---> [0]
        [1] ---> [2]
        <BLANKLINE>
        [3] ---> [5, 7] ---> [4]
        [5, 7] ---> [6]
        [5, 7] ---> [8, 9]
        <BLANKLINE>
        <BLANKLINE>
        '''
        return self.racine.afficher_noeud()
                
    def affiche_en_liste(self):
        '''
        affiche la liste de toute les clés présente dans l'arbre en partant de la racine, permet aussi de vérifier si l'arbre est bien trié
        :return:(list) affiche les élements de l'arbre à partir de la racine dans une liste 
        :CU:
        '''
        #affiche la liste en partant de la racine
        return self.__affiche_en_liste(self.racine)
                
                
    def __affiche_en_liste(self,n):
        '''
        affiche la liste de toute les clés présente dans l'arbre en partant du paramètre n, permet aussi de vérifier si l'arbre est bien trié
        :param n:(Noeud) noeud à partir duquelon affiche les clé de l'arbre
        :return:(list) une liste des clé presente dans l'arbre avec pour racine n
        :CU:
        >>> B = ArbreB(2,3)
        >>> B.insertion(0)
        >>> B.insertion(1)
        >>> B.insertion(2)
        >>> B.insertion(3)
        >>> B.insertion(4)
        >>> B.insertion(5)
        >>> B.insertion(6)
        >>> B.insertion(7)
        >>> B.insertion(8)
        >>> B.insertion(9)
        >>> print(B.affiche_en_liste())
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        '''
        if n.est_feuille():
            #si le noeud n est une feuille alors on renvoie la liste de clé du noeud
            return n.cle
        else:
            #alors on parcours l'arbre en partant du noeud enfant de n le plus petit et on ajoute a la liste en remontant pour avoir la liste des clé de l'arbe afin de vérifié si l'arbre est bien trié
            values = []
            for i in range (0, len(n.enfant)):
                values.extend(self.__affiche_en_liste(n.enfant[i]))
                if i < len(n.cle):
                    values.append(n.cle[i])
            return values
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
