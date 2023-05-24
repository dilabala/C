#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int nombreMystere, nombreJoueur, tentative = 0;
    srand(time(NULL));  // Initialisation du générateur de nombres aléatoires

    nombreMystere = rand() % 100 + 1;  // Génère un nombre aléatoire entre 1 et 100

    printf("Bienvenue dans le jeu de devinette !\n");

    do {
        printf("Veuillez entrer un nombre entre 1 et 100 : ");
        scanf("%d", &nombreJoueur);
        tentative++;

        if (nombreJoueur > nombreMystere) {
            printf("C'est moins !\n");
        } else if (nombreJoueur < nombreMystere) {
            printf("C'est plus !\n");
        } else {
            printf("Félicitations ! Vous avez trouvé le nombre mystère en %d tentatives.\n", tentative);
        }
    } while (nombreJoueur != nombreMystere);

    return 0;
}
