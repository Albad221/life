# Définition de la classe pour le Jeu de la Vie de Conway
class GameOfLife:
    # Constructeur de la classe, initialisant les dimensions de la grille et la grille elle-même.
    def __init__(self, rows=60, cols=100):
        self.rows = rows  # Nombre de lignes dans la grille
        self.cols = cols  # Nombre de colonnes dans la grille
        # Création d'une grille de lignes x colonnes, remplie de zéros (cellules mortes).
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Méthode pour définir l'état d'une cellule (vivante ou morte).
    def set_cell(self, row, col, state):
        self.grid[row][col] = state  # Définir l'état de la cellule à la position spécifiée

    # Méthode pour compter les voisins vivants d'une cellule donnée.
    def count_neighbors(self, row, col):
        neighbors = 0  # Compteur pour les voisins vivants
        # Boucles pour vérifier les cellules autour d'une cellule donnée
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # Ignorer la cellule elle-même
                # Calcul de la position des voisins avec gestion des bords de la grille
                n_row = (row + i) % self.rows
                n_col = (col + j) % self.cols
                neighbors += self.grid[n_row][n_col]  # Ajouter l'état du voisin au compteur
        return neighbors  # Retourner le nombre de voisins vivants

    # Méthode pour passer à l'état suivant du jeu en suivant les règles de Conway.
    def next_state(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]  # Grille pour le prochain état
        # Parcourir chaque cellule de la grille pour mettre à jour son état
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = self.count_neighbors(row, col)  # Compter les voisins vivants
                # Appliquer les règles du jeu pour déterminer le prochain état de la cellule
                if self.grid[row][col] == 1 and live_neighbors in (2, 3):
                    new_grid[row][col] = 1  # La cellule reste vivante
                elif self.grid[row][col] == 0 and live_neighbors == 3:
                    new_grid[row][col] = 1  # Une nouvelle cellule naît
        self.grid = new_grid  # Mettre à jour la grille avec le nouvel état

    # Représentation textuelle de la grille pour affichage dans le terminal.
    def __str__(self):
        grid_str = ''
        for row in self.grid:
            grid_str += ''.join('█' if cell else ' ' for cell in row) + '\n'
        return grid_str  # Retourner la grille sous forme de chaîne de caractères

# Initialisation d'une instance du jeu avec une grille plus grande
game = GameOfLife()

# Définition d'un motif initial (exemple avec un planeur)
glider_pattern = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
for (row, col) in glider_pattern:
    game.set_cell(row, col, 1)  # Rendre les cellules du motif vivantes

# Définition du nombre d'itérations à exécuter
iterations = 5

# Exécution du jeu pour un nombre défini d'itérations et impression de chaque état
for _ in range(iterations):
    print(game)  # Afficher l'état actuel du jeu
    game.next_state()  # Passer à l'état suivant

# Importation de la bibliothèque tkinter pour la création de l'interface graphique utilisateur
import tkinter as tk

# Implémentation de l'interface graphique du jeu de la vie avec tkinter
class GameOfLifeGUI:
    # Constructeur de la classe de l'interface graphique, initialisant la fenêtre et ses composants
    def __init__(self, master, rows=60, cols=100, cell_size=10):
        self.master = master  # Fenêtre principale de l'application
        self.rows = rows  # Nombre de lignes de la grille dans l'interface graphique
        self.cols = cols  # Nombre de colonnes de la grille dans l'interface graphique
        self.cell_size = cell_size  # Taille d'une cellule dans l'interface graphique
        self.game = GameOfLife(rows, cols)  # Instance du jeu

        # Création du canvas pour dessiner le jeu
        self.canvas = tk.Canvas(self.master, width=self.cols*cell_size, height=self.rows*cell_size)
        self.canvas.pack()  # Ajout du canvas à la fenêtre

        # Ajout des boutons de contrôle du jeu
        self.start_button = tk.Button(self.master, text="Tambalii", command=self.start_game)
        self.start_button.pack(side='left')  # Bouton pour démarrer la simulation

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_game, state='disabled')
        self.pause_button.pack(side='left')  # Bouton pour mettre en pause la simulation

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_game)
        self.clear_button.pack(side='left')  # Bouton pour effacer la grille et réinitialiser le jeu

        self.running = False  # État de la simulation (en cours ou en pause)
        self.game_interval = 100  # Intervalle en millisecondes entre chaque génération
        self.canvas.bind("<Button-1>", self.canvas_click)  # Liaison du clic de souris au canvas

        # Dessin de la grille et mise à jour initiale de l'affichage
        self.draw_grid()
        self.update()

    # Méthode pour dessiner les lignes de la grille sur le canvas
    def draw_grid(self):
        # Dessiner les lignes verticales de la grille
        for i in range(0, self.cols*self.cell_size, self.cell_size):
            self.canvas.create_line([(i, 0), (i, self.rows*self.cell_size)], tag='grid_line')
        
        # Dessiner les lignes horizontales de la grille
        for i in range(0, self.rows*self.cell_size, self.cell_size):
            self.canvas.create_line([(0, i), (self.cols*self.cell_size, i)], tag='grid_line')

    # Méthode appelée lorsqu'une cellule du canvas est cliquée
    def canvas_click(self, event):
        col = event.x // self.cell_size  # Calcul de la colonne cliquée
        row = event.y // self.cell_size  # Calcul de la ligne cliquée
        # Changement de l'état de la cellule cliquée et mise à jour de l'affichage
        if self.game.grid[row][col]:
            self.game.set_cell(row, col, 0)
            self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size,
                                         (col+1)*self.cell_size, (row+1)*self.cell_size, fill="white")
        else:
            self.game.set_cell(row, col, 1)
            self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size,
                                         (col+1)*self.cell_size, (row+1)*self.cell_size, fill="black")

    # Méthode pour mettre à jour l'affichage du canvas avec l'état actuel du jeu
    def update(self):
        # Parcourir chaque cellule de la grille pour mettre à jour son affichage
        for row in range(self.rows):
            for col in range(self.cols):
                if self.game.grid[row][col]:
                    self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size,
                                                 (col+1)*self.cell_size, (row+1)*self.cell_size, fill="black")
                else:
                    self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size,
                                                 (col+1)*self.cell_size, (row+1)*self.cell_size, fill="white")

    # Méthode pour démarrer la simulation du jeu
    def start_game(self):
        self.running = True  # La simulation est en cours
        self.start_button.config(state='disabled')  # Désactivation du bouton de démarrage
        self.pause_button.config(state='normal')  # Activation du bouton de pause
        self.clear_button.config(state='disabled')  # Désactivation du bouton de réinitialisation
        self.run_game()  # Lancement de la simulation

    # Méthode pour mettre en pause la simulation du jeu
    def pause_game(self):
        self.running = False  # La simulation est en pause
        self.start_button.config(state='normal')  # Activation du bouton de démarrage
        self.pause_button.config(state='disabled')  # Désactivation du bouton de pause
        self.clear_button.config(state='normal')  # Activation du bouton de réinitialisation

    # Méthode pour effacer la grille et réinitialiser le jeu
    def clear_game(self):
        self.game = GameOfLife(self.rows, self.cols)  # Création d'une nouvelle instance du jeu
        self.update()  # Mise à jour de l'affichage
        self.canvas.delete('grid_item')  # Suppression des éléments de la grille sur le canvas

    # Méthode pour exécuter la simulation du jeu
    def run_game(self):
        self.game.next_state()  # Mise à jour de l'état du jeu
        self.update()  # Mise à jour de l'affichage
        # Planification de la prochaine mise à jour si la simulation est toujours en cours
        if self.running:
            self.master.after(self.game_interval, self.run_game)

# Initialisation et lancement de l'interface graphique
root = tk.Tk()
gui = GameOfLifeGUI(root)
root.mainloop()  # Boucle principale de l'interface graphique
