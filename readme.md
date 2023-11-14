# Jeu de la Vie de Conway - TL221 Challenge

Le Jeu de la Vie, également connu sous le nom de "Game of Life", est un automate cellulaire conçu par le mathématicien britannique John Horton Conway en 1970. C'est un jeu à zéro joueur, ce qui signifie que son évolution est déterminée par son état initial, nécessitant aucune entrée supplémentaire. On interagit avec le Jeu de la Vie en créant une configuration initiale et en observant comment elle évolue.

## Comment le jeu fonctionne

Le tableau de jeu est une grille de cellules carrées, chaque cellule étant dans l'un des deux états possibles : vivante ou morte. Chaque cellule interagit avec ses huit voisins, qui sont les cellules adjacentes horizontalement, verticalement ou diagonalement.

À chaque étape, les transitions suivantes se produisent :
1. Toute cellule vivante avec moins de deux voisins vivants meurt, comme si elle était causée par une sous-population.
2. Toute cellule vivante avec deux ou trois voisins vivants vit pour la prochaine génération.
3. Toute cellule vivante avec plus de trois voisins vivants meurt, comme si elle était causée par une surpopulation.
4. Toute cellule morte avec exactement trois voisins vivants devient une cellule vivante, comme si elle était reproduite.

## Installation

Pour exécuter ce projet, vous aurez besoin de Python installé sur votre machine.

1. Clonez le dépôt sur votre machine locale en utilisant la commande suivante :
 # ```bash
git clone https://github.com/Albad221/life/

2. Naviguez dans le répertoire cloné :
bash
Copy code
cd chemin_vers_le_répertoire
(Optionnel) Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet :
bash
Copy code
python -m venv env
source env/bin/activate  # Sur Windows utilisez `env\Scripts\activate`
Exécutez le fichier golgui.py avec Python pour démarrer le jeu :
bash
Copy code
python golgui.py

## Utilisation
Une fois le jeu lancé, l'interface graphique devrait s'afficher. Voici comment vous pouvez interagir avec le jeu :

Cliquer sur une cellule : Change l'état de la cellule (vivante ou morte).
Bouton Tambalii : Commence la simulation du jeu.
Bouton Pause : Met en pause la simulation.
Bouton Clear : Efface la grille et réinitialise le jeu à son état initial.
Vous pouvez également modifier le motif initial dans le fichier golgui.py avant de démarrer le jeu pour observer différentes évolutions.

## Technologies utilisées
Python : Langage de programmation utilisé pour la logique du jeu.
Tkinter : Bibliothèque Python pour la création de l'interface graphique utilisateur.
Contributions
Les contributions à ce projet sont les bienvenues. Si vous avez des suggestions d'amélioration ou des corrections, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Contact
Pour toute question ou commentaire, veuillez ouvrir une issue dans le dépôt GitHub du projet.

Merci de vous intéresser au Jeu de la Vie de Conway - TL221 Challenge !
