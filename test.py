class Compteur:
    def __init__(self, valeur_initiale=0):
        self.valeur = valeur_initiale

    def incrementer(self):
        self.valeur += 1

    def decrementer(self):
        if self.valeur > 0:
            self.valeur -= 1

    def reinitialiser(self):
        self.valeur = 0

    def obtenir_valeur(self):
        return self.valeur


# Programme principal
mon_compteur = Compteur()  # Crée une instance du compteur avec valeur initiale 0

print("Valeur initiale du compteur :", mon_compteur.obtenir_valeur())

mon_compteur.incrementer()
mon_compteur.incrementer()
mon_compteur.incrementer()

print("Valeur après trois incréments :", mon_compteur.obtenir_valeur())

mon_compteur.decrementer()

print("Valeur après un décrément :", mon_compteur.obtenir_valeur())

mon_compteur.reinitialiser()

print("Valeur après réinitialisation :", mon_compteur.obtenir_valeur())
