import random

def devinette():
    mots = ["pomme", "banane", "orange", "fraise", "kiwi"]
    mot_choisi = random.choice(mots)
    nb_chances = 3
    
    print("Bienvenue dans le jeu de devinettes !")
    print("Je pense à un fruit. À toi de deviner lequel.")
    
    while nb_chances > 0:
        guess = input("Devine le fruit : ")
        
        if guess.lower() == mot_choisi:
            print("Bravo ! Tu as deviné le fruit.")
            break
        else:
            nb_chances -= 1
            if nb_chances > 0:
                print("Ce n'est pas le bon fruit. Il te reste", nb_chances, "chance(s).")
    
    if nb_chances == 0:
        print("Dommage ! Tu as épuisé toutes tes chances.")
        print("Le fruit que je pensais était", mot_choisi)
    
devinette()
