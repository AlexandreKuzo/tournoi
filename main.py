from grandtournoi import *


def main():

    print("Bonjour et bienvenue ! Crééz le tournoi ! ")
    Tournoi.creer_tournoi()


    # On affiche les joueurs engagés dans le tournoi
    print("Liste des joueurs engagés : ")
    for liste_joueur in liste_joueurs:
        print(liste_joueur.prenom, liste_joueur.nom)


    # on créé une fonction classement pour compter les points
    def classement():
        liste_joueurs.sort(key=lambda x: x.nombre_points_joueur, reverse=True)
        for a in liste_joueurs:
            print(a.prenom, a.nombre_points_joueur)


    # On appelle les fonctions des classes pour afficher le classement...
    # ... les matchs, entrer, récupérer les scores, et mettre à jour...
    # ... le classement et afficher le vainqueur.
    classement()
    print("Jouons le premier match! Les affiches :")
    Match.creer_ronde()
    Match.recuperer_scores()
    print("Classement après le match n°1 :")
    classement()
    print("OK jouons le deuxième match ! Les affiches : ")
    Match.creer_ronde_suivante()
    Match.recuperer_scores()
    print("Classement après le match n°2 : ")
    classement()
    print("OK jouons le troisième match ! Les affiches : ")
    Match.creer_ronde_suivante()
    Match.recuperer_scores()
    print("Classement après le match n°3 : ")
    classement()
    print("OK jouons le quatrième match ! Les affiches : ")
    Match.creer_ronde_suivante()
    Match.recuperer_scores()
    print("Classement après le match n°4 : ")
    classement()
    # On annonce le vainqueur
    print("Vainqueur du tournoi : ", liste_joueurs[0].prenom)

if __name__ == '__main__':
    main()
