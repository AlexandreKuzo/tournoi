# Fichier comportant les classes du programme

import datetime  # Générer la date du tournoi


# On créé une classe Tournoi
class Tournoi:
    def __init__(self, nom, date, lieu):
        self.nom = nom
        self.date = datetime.datetime.now()
        self.lieu = lieu

    def creer_tournoi():
        nom = input("Nommez votre tournoi : ")
        date = datetime.datetime.now()
        lieu = input("Où va t-il se passer ?")
        print("OK c'est parti pour le tournoi {}".format(nom))
        print("Nous sommes le {}, on joue à {}".format(date, lieu))


# On crée une liste de joueurs (voir plus bas)
liste_joueurs = []


# On créé une classe joueur
class Joueur:
    def __init__(self, nom, prenom, nombre_points_joueur):
        self.nom = nom
        self.prenom = prenom
        self.nombre_points_joueur = nombre_points_joueur


Tour1 = []


class Match(Joueur):
    def __init__(self):
        # Cette classe hérite des paramètres des joueurs
        Joueur.__init__(self, nom, prenom, nombre_points_joueur)

    def creer_ronde():  # On crée les matchs
        match1 = [liste_joueurs[0], liste_joueurs[4]]
        Tour1.append(match1)  # Les matchs sont enregistrés dans la ronde
        match2 = [liste_joueurs[1], liste_joueurs[5]]
        Tour1.append(match2)
        match3 = [liste_joueurs[2], liste_joueurs[6]]
        Tour1.append(match3)
        match4 = [liste_joueurs[3], liste_joueurs[7]]
        Tour1.append(match4)
        for a, b in Tour1:
            print(a.prenom, "-", b.prenom)

    def creer_ronde_suivante():  # On créé de nouveaux matchs
        # On tient compte du classement mis à jour
        match1 = [liste_joueurs[0], liste_joueurs[1]]
        Tour1.append(match1)
        match2 = [liste_joueurs[2], liste_joueurs[3]]
        Tour1.append(match2)
        match3 = [liste_joueurs[4], liste_joueurs[5]]
        Tour1.append(match3)
        match4 = [liste_joueurs[6], liste_joueurs[7]]
        Tour1.append(match4)
        for a, b in Tour1:
            print(a.prenom, "-", b.prenom)

    def recuperer_scores():  # Fonction de récupération des scores
        a = Tour1[0]  # On affiche le match n°1 de la liste créée : "Tour 1"
        print("Match : {} - {}".format(a[0].prenom, a[1].prenom))
        a[0].score = input("Indiquez le score de {}:".format(a[0].prenom))
        a[1].score = input("Indiquez le score de {}:".format(a[1].prenom))
        if a[0].score > a[1].score:
            a[0].nombre_points_joueur += 1
            print("Vainqueur : ", a[0].prenom)
        elif a[0].score == a[1].score:
            a[0].nombre_points_joueur += 0.5
            a[1].nombre_points_joueur += 0.5
            print("Match nul!")
        elif a[0].score < a[1].score:
            a[1].nombre_points_joueur += 1
            print("Vainqueur : ", a[1].prenom)

        b = Tour1[1]  # Deuxième match
        print("Match : {} - {}".format(b[0].prenom, b[1].prenom))
        b[0].score = input("Indiquez le score de {}:".format(b[0].prenom))
        b[1].score = input("Indiquez le score de {}:".format(b[1].prenom))
        if b[0].score > b[1].score:
            b[0].nombre_points_joueur += 1
            print("Vainqueur : ", b[0].prenom)
        elif b[0].score == b[1].score:
            b[0].nombre_points_joueur += 0.5
            b[1].nombre_points_joueur += 0.5
            print("Match nul!")
        elif b[0].score < b[1].score:
            b[1].nombre_points_joueur += 1
            print("Vainqueur : ", b[1].prenom)

        c = Tour1[2]  # Troisième match
        print("Match : {} - {}".format(c[0].prenom, c[1].prenom))
        c[0].score = input("Indiquez le score de {}:".format(c[0].prenom))
        c[1].score = input("Indiquez le score de {}:".format(c[1].prenom))
        if c[0].score > c[1].score:
            c[0].nombre_points_joueur += 1
            print("Vainqueur : ", c[0].prenom)
        elif c[0].score == c[1].score:
            c[0].nombre_points_joueur += 0.5
            c[1].nombre_points_joueur += 0.5
            print("Match nul!")
        elif c[0].score < c[1].score:
            c[1].nombre_points_joueur += 1
            print("Vainqueur : ", c[1].prenom)

        d = Tour1[3]  # Quatrième match
        print("Match : {} - {}".format(d[0].prenom, d[1].prenom))
        d[0].score = input("Indiquez le score de {}:".format(d[0].prenom))
        d[1].score = input("Indiquez le score de {}:".format(d[1].prenom))
        if d[0].score > d[1].score:
            d[0].nombre_points_joueur += 1
            print("Vainqueur : ", d[0].prenom)
        elif d[0].score == d[1].score:
            d[0].nombre_points_joueur += 0.5
            d[1].nombre_points_joueur += 0.5
            print("Match nul!")
        elif d[0].score < d[1].score:
            d[1].nombre_points_joueur += 1
            print("Vainqueur : ", d[1].prenom)
        Tour1.clear()  # on "vide" la liste des matchs pour le tour suivant


# On créé les joueurs et les stocke dans une liste
player1 = Joueur("Guez", "Daniel", 0)
liste_joueurs.append(player1)
player2 = Joueur("Mek", "Yo", 0)
liste_joueurs.append(player2)
player3 = Joueur("Oukoi", "Bien", 0)
liste_joueurs.append(player3)
player4 = Joueur("Poto", "C'estcomment", 0)
liste_joueurs.append(player4)
player5 = Joueur("Frere", "Ondikoi", 0)
liste_joueurs.append(player5)
player6 = Joueur("Frero", "Wesh", 0)
liste_joueurs.append(player6)
player7 = Joueur("Le Gamin", "Oh", 0)
liste_joueurs.append(player7)
player8 = Joueur("Lafamille", "Sisi", 0)
liste_joueurs.append(player8)
