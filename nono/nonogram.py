#Groupe: Helle - Francois - Taleb-Ahmed
#Sujet: Nonogram
#Date: 21/03

from tk_nonogram import *

cat={
 "rows": "1,1;3;5;4;5",
 "cols": "3;3;5;4;3,1"
 }

foot={
    "rows":"3;5;3,1;2,1;3,3,4;2,2,7;6,1,1;4,2,2;1,1;3,1;6;2,7;6,3,1;1,2,2,1,1;4,1,1,3;4,2,2;3,3,1;3,3;3;2,1",
    "cols":"2;1,2;2,3;2,3;3,1,1;2,1,1;1,1,1,2,2;1,1,3,1,3;2,6,4;3,3,9,1;5,3,2;3,1,2,2;5,3,2;3,1,2,2;2,1,7;3,3,2;2,4;2,1,2;2,2,1;2,2;1;1"
    }

canard={
    "rows":"4;6;6,3;8;7;6;5;5;4;5;6;5;6;7,10;20,1;15,5;18,4;19,1,1;19,1;7,9,2,1;7,7,4,1;8,10,2;8,7,3;9,3;12,2",
    "cols":"1;1;1,7;3,10;5,13;6,15;2,21;25;24;9,5,5;5,6,4;8,3;9,2;9,2;10,1;10,1;10,1;2,7,1;2,4,2,1;2,3,3;3,2,3,1;3,3,2;3,2,2;2,1,3;4,4"
    }

def tableau(dico):
    """
        Fait un tableau à partir d'un dictionnaire
        :param dico: (dict)   le dictionnaire à mettre sous forme de tableau
        :return: (list)
        CU: Le dictionnaire doit être conforme à la norme que l on a établi
        Exemples :
        >>> tableau(cat)
        [[['1', '1'], ['3'], ['5'], ['4'], ['5']], [['3'], ['3'], ['5'], ['4'], ['3', '1']]]
        >>> tableau(foot)
        [[['3'], ['5'], ['3', '1'], ['2', '1'], ['3', '3', '4'], ['2', '2', '7'], ['6', '1', '1'], ['4', '2', '2'], ['1', '1'], ['3', '1'], ['6'], ['2', '7'], ['6', '3', '1'], ['1', '2', '2', '1', '1'], ['4', '1', '1', '3'], ['4', '2', '2'], ['3', '3', '1'], ['3', '3'], ['3'], ['2', '1']], [['2'], ['1', '2'], ['2', '3'], ['2', '3'], ['3', '1', '1'], ['2', '1', '1'], ['1', '1', '1', '2', '2'], ['1', '1', '3', '1', '3'], ['2', '6', '4'], ['3', '3', '9', '1'], ['5', '3', '2'], ['3', '1', '2', '2'], ['5', '3', '2'], ['3', '1', '2', '2'], ['2', '1', '7'], ['3', '3', '2'], ['2', '4'], ['2', '1', '2'], ['2', '2', '1'], ['2', '2'], ['1'], ['1']]]
        >>> tableau(canard)
        [[['4'], ['6'], ['6', '3'], ['8'], ['7'], ['6'], ['5'], ['5'], ['4'], ['5'], ['6'], ['5'], ['6'], ['7', '10'], ['20', '1'], ['15', '5'], ['18', '4'], ['19', '1', '1'], ['19', '1'], ['7', '9', '2', '1'], ['7', '7', '4', '1'], ['8', '10', '2'], ['8', '7', '3'], ['9', '3'], ['12', '2']], [['1'], ['1'], ['1', '7'], ['3', '10'], ['5', '13'], ['6', '15'], ['2', '21'], ['25'], ['24'], ['9', '5', '5'], ['5', '6', '4'], ['8', '3'], ['9', '2'], ['9', '2'], ['10', '1'], ['10', '1'], ['10', '1'], ['2', '7', '1'], ['2', '4', '2', '1'], ['2', '3', '3'], ['3', '2', '3', '1'], ['3', '3', '2'], ['3', '2', '2'], ['2', '1', '3'], ['4', '4']]]
    """
    l1=list()
    l2=list()
    d1=dico["rows"].split(';')
    
    l3=list()
    l4=list()
    d2=dico["cols"].split(';')
    
    for e in d1 :
        l1+=[e]
    for e in l1 :
        l2+=[e.split(',')]
        
    for e in d2 :
        l3+=[e]
    for e in l3 :
        l4+=[e.split(',')]
    return [l2, l4]

def width (dico):
    """
        Renvoies le nombre de colonnes
        :param dico:  le dictionnaire à mettre sous forme de tableau
        :return: (int)
        CU: Le dictionnaire doit être conforme à la norme que l'on a établi
        Exemples :
        >>> width (cat)
        4
    """
    x=0
    for e in dico["cols"] :
        if e == ';' :
            x+=1
    return x

def height(dico):
    """
        Renvoies le nombre de rangées
        :param dico:  le dictionnaire à mettre sous forme de tableau
        :return: (int)
        CU: Le dictionnaire doit être conforme à la norme que l on a établi
        Exemples :
        >>> height (cat)
        4
    """
    y=0
    for i in dico["rows"] :
        if i == ';' :
            y+=1
    return y

def colsHeight(dico) :
    """
        renvoie la hauteur des colonnes
        :param dico:  le dictionnaire à mettre sous forme de tableau
        :return: (int)
        CU: Le dictionnaire doit être conforme à la norme que l on a établi
        Exemples :
        >>> colsHeight(cat)
        2
    """
    x=0
    list_dico=tableau(dico)
    for e in list_dico[0]:
        if len(e) > x :
            x = len(e)
    return x

def rowsWidth(dico) :
    """
        renvoie la largeur des rangées
        :param dico:  le dictionnaire à mettre sous forme de tableau
        :return: (int)
        CU: Le dictionnaire doit être conforme à la norme que l on a établi
        Exemples :
        >>> rowsWidth(cat)
        2
    """
    y=0
    list_dico=tableau(dico)
    for i in list_dico[1]:
        if len(i) > y :
            y = len(i)
    return y

def structure(dico) : 
	"""
		renvoie une structure de nonogram, juste le tableau
		:param dico:  le dictionnaire à mettre sous forme de tableau
        	CU: Le dictionnaire doit être conforme à la norme que l on a établi
	"""
	a = width(dico)
	b = height(dico)
	c = colsHeight(dico)
	d = rowsWidth(dico)
	nonogram=NonogramApplication(width= a, height= b, colsheight= c, rowswidth= d)
	return nonogram

def coordoTabl(dico) :
        """
                met en place les chiffres dans le nonogram
                :param dico:  le dictionnaire à mettre sous forme de tableau
                CU: Le dictionnaire doit être conforme à la norme que l on a établi
        """
        ##nono.setcols(x,y,value)     nono.setrows(x,y,value)
        nono=structure(dico)
        liste=tableau(dico)
        rows=liste[0]
        cols=liste[1]
        x=0
        y=0
        z=0
        t=0
        for e in rows:
            for i in e :
                if len(e) == 1 :
                    x+= 1
                    nono.setrows(x, y, e)
                else :
                    y+= 1
                    nono.setrows(x, y, i)
                
        for e in cols:
            for i in e :
                if len(e) == 1 :
                    z+= 1
                    nono.setcols(t, z, e)
                else :
                    t+= 1
                    nono.setcols(t, z, i)

def fonction_bouton1(x, y):
    """
        applique au clic gauche de la souris le fait de remplir une case
        :param dico:  le dictionnaire à mettre sous forme de tableau
        CU: Le dictionnaire doit être conforme à la norme que l on a établi
    """
    nono=structure(dico)
    nono.fillbox(x, y, 'black')
def fonction_bouton3(x, y):
    """
        applique au clique droit de la souris le fait de mettre une croix dans une case
        :param dico:  le dictionnaire à mettre sous forme de tableau
        CU: Le dictionnaire doit être conforme à la norme que l on a établi
    """
    nono=structure(dico)
    nono.checkbox(x, y)


def doNonogram(dico) :
    """
        fonction finale, elle renvoie le nonogram complet
        :param dico:  le dictionnaire à mettre sous forme de tableau
        CU: Le dictionnaire doit être conforme à la norme que l on a établi
    """
    nono=structure(dico)
    nono.master.title('- Nonograms -')
    coordoTabl(dico)
    nono.appele(1, fonction_bouton1)
    nono.appele(3, fonction_bouton3)    
    nono.mainloop()        

## 	nono.quitanddestroy()


if __name__ == "__main__":
     import doctest
     doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                             verbose=True)
