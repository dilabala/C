class Compteur:
    def __init__(self):
        self.valeur = 0

    def incrementer(self):
        self.valeur += 1

    def decrementer(self):
        if self.valeur > 0:
            self.valeur -= 1

    def obtenir_valeur(self):
        return self.valeur


# Programme de test
mon_compteur = Compteur()

print(mon_compteur.obtenir_valeur())  # Affiche 0

for _ in range(10):
    mon_compteur.incrementer()

print(mon_compteur.obtenir_valeur())  # Affiche 10

for _ in range(20):
    mon_compteur.decrementer()

print(mon_compteur.obtenir_valeur())  # Affiche 0
