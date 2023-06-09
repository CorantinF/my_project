# L3G4-PROJET-COO_HELLE_FRANCOIS
HELLE Thitouane
FRANCOIS Corantin

## rapide introduction sur le sujet du projet
    Création d'une compétition sportive, composé de match entre des compétiteurs, avec plusieurs règles de fonctionnement, plusieurs type de compétitions et un système d'observer de match.
    
## howto
    - récupération du dépôt
        aller sur notre dépot et faire un pull

    - créer classes    
        javac -classpath test/test-1.7.jar *.java test/*.java -d classes

    - commande de génération de la doc
    	javadoc competitions_sportives -d \competitions_sportives\docs\ 

    - tests 
    	javac -classpath test4poo.jar test/*.java

    - commande de génération de l'archive
        dans classes :
            jar cvfm ../competitions_sportives.jar ../manifest-competitions_sportives competitions_sportives

    - commande d'exécution de l'archive générée
        java -jar competitions_sportives.jar

## Présentation d'élément de code v1
    Nous avons suivi le schéma du Poly, le seul changement a été la méthode abstraite play(competitors) dans Competition passée de protected a public pour pouvoir l'appeler de n'importe ou.

    Il y a 2 versions de notre projet, une en projet elcipse, une autre normal.

## Présentation d'élément de code v2
    Nous avons fait un système de stratégie avec les exemples du sujet

## Présentation d'élément de code v3 
    Nous avons implémenter un système d'observer

## Diagramme UML
    Dans le fichier :
    ->  competitions_sportives.pdf

## Problèmes rencontrés v1
    - Problème matériel JUnit.
    - Nous avons du apprendre eclipse à la dernière minute pour pouvoir tout compiler et éxecuter les test car tout les autres moyens ne fonctionnaient pas, de ce fait les packages de notre projet sont un peu fouilli.
    - Compréhension des classes abstraites /tests de classes abstraites.
    - Difficulté à tout publier sur GitLab en temps et en heure car je dois tout faire à la main sur ma machine (les commandes ne marchent pas).

## Problèmes rencontrés v2
    - Le confinnement
    - compréhension du sujet, nous n'avions pas réalisé un master avec des stratégies 4, nous avions fait un truc plus général mais plus complexe
    - nous sommes revenus sur notre ancien code grace aux conseils du prof ce qui nous a pris du temps.

## Problèmes rencontrés v3
    - La compréhension du design pattern observer et sont application à notre sujet.