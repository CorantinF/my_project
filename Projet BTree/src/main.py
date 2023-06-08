from ArbreB import *

def main():
    '''
    Permet de réalisé le Test-1 et Test- du sujet du projet
    '''
#     B1 = ArbreB(2,3)
#     for i in range(0,38,2):
#         B1.insertion(i)
#     for i in range(7,15,2):
#         B1.insertion(i)
#     print(B1.afficher_arbre())
#     print(B1.affiche_en_liste())
#     
#     B2 = ArbreB(6,11)
#     for i in range(10,5001,10):
#         B2.insertion(i)
#     for i in range(5,4996,10):
#         B2.insertion(i)
#     print(B2.afficher_arbre())
#     print(B2.affiche_en_liste())
    
    B3 = ArbreB(2,3)
    for i in range(10,0,-1):
        B3.insertion(i)
    print(B3.afficher_arbre())
    print(B3.affiche_en_liste())
    print(B3.recherche_cle(12))
#    B = ArbreB(2,3)
#
#    for i in range(9):
#        print(B.afficher_arbre())
#        B.insertion(i)
#
#    B.afficher_arbre()
#    for i in range(9):
#        print(B.recherche_cle(i))
#    B.insertion(2)
#    print(B.afficher_arbre())
#    print(B.affiche_en_liste())

if __name__ == '__main__':
    main()
