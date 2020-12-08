import random
import math

class Tribe:
    name = ""

    def __init__(self):
        self.name = "nom_tribut"

    def hunt(self, sesChoix):
        return 0

class BetrayTribe(Tribe):

    def __init__(self):
        self.name = "betrayTribe"

    def hunt(self, sesChoix):
        return 1

class CoopTribe(Tribe):

    def __init__(self):
        self.name = "coopTribe"

    def hunt(self, sesChoix):

        return 0

class RndTribe(Tribe):

    def __init__(self):
        self.name = "rndTribe"

    def hunt(self, sesChoix):
        return random.randint(0,2)

class MyTribe(Tribe):

    def __init__(self):
        self.name = "Waimaka"

    def hunt(self, sesChoix):
        #Détecter le début de partie pour pouvoir commencer par de la coop
        print(sesChoix)
        if sesChoix[0] == -1:
            return 0

        #Chaque 10 tours, vérifier si la moyenne est supérieure à 1.5. Sinon, renoncer

        #Obtenir le numéro de manche actuelle
        roundActuel= 0
        nbDizaine = 0
        moy = 0
        for i in sesChoix:
            if sesChoix[i] != -1:
                roundActuel += 1
                moy += sesChoix[i]

                print("\nRound:", roundActuel)
                print("Valeur:", i)

                #Vérifier toutes les 10 manches la moyenne des 10 manches précédentes
                if roundActuel % 10 == 0:
                    nbDizaine += 1
                    moy /= 10
                    print("Moyenne:", moy)

                    #Si la moyenne est inférieure à 1.5, on renonce
                    if moy <= 1.5:
                        return 2


                    moy = 0




        return 0


def match(t1, t2, nbRounds):
    r1 = 0#récompenses tribu1
    r2 = 0#récompense tribu2

    #historique
    t1_choices = list()
    t2_choices = list()

    for i in range(nbRounds):
        t1_choices.append(-1)
        t2_choices.append(-1)

    #match
    for round in range(0, nbRounds):
        #faire les choix
        choice1 = t1.hunt(t2_choices)
        choice2 = t2.hunt(t1_choices)

        #maj historique
        t1_choices[round] = choice1
        t2_choices[round] = choice2

        #ajout recompense
        if choice1 == 2:
            if choice2 == 2:
                r1+=2
                r2+=2
            elif choice2 == 0:
                r1 += 2
                r2 += 1
            elif choice2 == 1:
                r1 += 2
                r2 += 1
        elif choice1 == 0:
            if choice2 == 2:
                r1+=1
                r2+=2
            elif choice2 == 0:
                r1 += 4
                r2 += 4
            elif choice2 == 1:
                r1 += 1
                r2 += 6
        elif choice1 == 1:
            if choice2 == 2:
                r1+=1
                r2+=2
            elif choice2 == 0:
                r1 += 6
                r2 += 1
            elif choice2 == 1:
                r1 += 1
                r2 += 1

    return (r1, r2)

def tournoi(tribes):
    nbRounds = 100
    points = list()
    wins = list()
    for i in range(0, len(tribes)):
        points.append(0)
        wins.append(0)

    for i in range(0, len(tribes)):
        tribe1 = tribes[i]
        for j in range(i, len(tribes)):
            tribe2 = tribes[j]
            if i < j:
                (score1, score2) = match(tribe1, tribe2, nbRounds)
                print(tribe1.name + " vs "+ tribe2.name)
                print(str(score1)+" - "+str(score2))
                points[i] += score1
                points[j] += score2
                if score1 > score2:
                    wins[i]+=1
                elif score1 < score2:
                    wins[j]+=1

    print("Final result")
    for i in range(0, len(tribes)):
        print(tribes[i].name+" "+str(points[i])+" "+str(wins[i]))


tribes = list()
tribes.append(CoopTribe())
tribes.append(BetrayTribe())
tribes.append(RndTribe())
tribes.append(MyTribe())

tournoi(tribes)