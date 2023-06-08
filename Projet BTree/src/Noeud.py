import ArbreB
#Noeud
class Noeud:
    '''
    Classe de noeud qui a pour la particularité d'être un noeud de sous les contraintes de l'Arbre B
    '''
    def __init__(self, arbre, parent, L, U):
        '''
        Construction d'un Noeud lié à un arbre, un parent(None si le noeud en question est la racine),
        L nombre de noeud fils min et U nombre de noeud fils max.
        :param arbre: (ArbreB) Arbre B auquel le noeud appartient
        :param parent: (Noeud) parent du noeud construit, None si le noeud construit est la racine
        :param L: (int) nombre de noeud fils min
        :param U: (int) nombre de noeud fils max
        :return: (Noeud) un noeud de l'arbre arbre lié au parent parent avec un nombre de noeud fils compris entre L et U 
        :CU: 2*L-1 <= U
        '''
        self.cle = []
        self.enfant = []
        self.U = U
        self.L = L
        self.parent = parent
        self.arbre = arbre
        
    def insere_noeud (self, c):
        '''
        Fonction qui insère une clé au bonne endroit dans un noeud d'un arbre B
        :param c:(int) clé que l'on veut insérer dans le noeud
        :return: None
        :CU:
        '''
        if len(self.cle) < self.U -1:
            self.cle.append(c)
            self.cle.sort()
            #si on a un noeud qui n'a pas atteint une taille de U-1 alors on peut ajouté la clé et on tri de nouveau le noeud
        else:
            #sinon on l'ajoute en triant 
            self.cle.append(c)
            self.cle.sort()
            noeud = Noeud(self.arbre, None, self.L, self.U)
            med = self.separe_cle(noeud)
            #il faut déterminer la clé median du noeud
            self.separe_enfant(noeud)
            #on sépare le noeud enfant garce au nouveau noeud qui va pouvoir acceuillir une partie des clés enfants
            if self.parent == None:
                #dans le cas ou le noeud qu'on cherche à séparer n'a pas de père pour aceuillir la clé médian on doit créé un père donc une racine
                noeud_racine = Noeud(self.arbre,None,self.L,self.U)
                noeud_racine.ajoute_enfant(self)
                #on relie la racine aux enfants qui viennent d'etre donné grace a la séparation
                self.arbre.racine = noeud_racine
                #on dit à l'arbre que le noeud raine est bien la racine de son arbre
            self.parent.ajoute_enfant(noeud)
            #si le noeud avait un parent de base on a juste ajouté l'enfant noeud (le nouveau noeud qui à acceuilli les enfants supérieur de la médiane)
            self.parent.insere_noeud(med)
            #on insere dans le noeud pere la médiane, si la taille de la liste de clé du pére on peut simplement ajouté la clé sinon on recommence les étapes et on recommence le split sur le pere pour remonter la médiane dans le grand père d'ou l'appel récursif
            

    def ajoute_enfant(self,e):
        '''
        ajoute un enfant au bon endroit
        :param e:(Noeud) un noeud enfant
        :return: None
        :CU:
        '''
        e.parent=self
        self.enfant.append(e)
        # ajoute un enfant au noeud grace a une lambda fonction sur la premiere cle de chaque enfant tri les enfant et les gardent bien classé 
        self.enfant.sort(key = lambda enfant: enfant.cle[0])
            
        
    def compare_enfant(self,e):
        '''
        Compare la premiere clé de deux enfants
        :param e: (Noeud) un noeud enfant
        :return: -1 si la première cle du noeud enfant e est plus grande 1 sinon
        :CU:
        >>> n1=Noeud(None,None,2,3)
        >>> n2=Noeud(None,None,2,3)
        >>> n1.insere_noeud(1)
        >>> n2.insere_noeud(2)
        >>> n1.compare_enfant(n2)
        -1
        >>> n2.compare_enfant(n1)
        1
        '''
        if self.cle[0] < e.cle[0]:
            return -1
        else:
            return 1
         
    
    def separe_cle(self, n):
        '''
        retourne la clé médian du noeud n et ajoute la parti de droite du médian dans le noeud n
        :param n:(Noeud) noeud dans lequel on ajoute la deuxième moitié des clés du noeud
        :return:(int) clé médian du noeud
        :CU:
        >>> n1=Noeud(None,None,2,4)
        >>> n1.insere_noeud(1)
        >>> n1.insere_noeud(2)
        >>> n1.insere_noeud(3)
        >>> n1.afficher_noeud()
        '[1, 2, 3]'
        >>> n2=Noeud(None,None,2,4)
        >>> n1.separe_cle(n2)
        2
        >>> n1.afficher_noeud()
        '[1]'
        >>> n2.afficher_noeud()
        '[3]'
        '''
        #tant que le nombre de cle est superieur a la mediane on ajoute les valeur supérieur à la médiane à un autre noeud et les supprime du noeud originel afin d'avoir 2 noeud de même taille et avoir la medianne qui va pouvoir remonter dans le noeud père
        middle = len(self.cle) // 2
        med = self.cle.pop(middle)
        while len(self.cle) > middle:
            n.cle.append(self.cle.pop(middle))
        return med
        
        
    def separe_enfant(self, n):
        '''
        sépare un noeud enfant
        :param n:(Noeud)
        :return: None
        :CU:
        '''
        middle = len(self.enfant) // 2
        # sépare les enfant d'un noeud en ajoutant à un nouveau noeud fils en gardant les enfant trié, et on supprime ceux qu'on a ajouté pour ne pas avoir de doublon
        while middle < len(self.enfant):
            n.ajoute_enfant(self.enfant.pop(middle))
            
    
        
    def est_feuille(self):
        '''
        vérifie si le noeud est une feuille ou non
        :return:(bool) True si le noeud est une feuille sinon False
        :CU:
        >>> n=Noeud(None,None,2,3)
        >>> n.est_feuille()
        True
        '''
        return len(self.enfant) == 0
    
    def afficher_noeud(self):
        '''
        Affiche un noeud sous un format str dans une liste 
        :return:(str) affiche un noeud avec un format défini 
        :CU:
        >>> n=Noeud(None,None,2,4)
        >>> n.insere_noeud(1)
        >>> n.insere_noeud(2)
        >>> n.insere_noeud(3)
    
        >>> n.afficher_noeud()
        '[1, 2, 3]'
        '''
        s = ""
        if (self.est_feuille()):
            return str(self.cle)
        else:
            for i in self.enfant:
                s += str(self.cle) + " ---> " + i.afficher_noeud() + "\n"
            return s
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
