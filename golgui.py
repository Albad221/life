class GameOfLife:
    def __init__(self, rows=60, cols=100):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, row, col, state):
        self.grid[row][col] = state

    def count_neighbors(self, row, col):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                n_row = (row + i) % self.rows  # wrap around at the edges
                n_col = (col + j) % self.cols  # wrap around at the edges
                neighbors += self.grid[n_row][n_col]
        return neighbors

    def next_state(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = self.count_neighbors(row, col)
                if self.grid[row][col] == 1 and live_neighbors in (2, 3):
                    new_grid[row][col] = 1
                elif self.grid[row][col] == 0 and live_neighbors == 3:
                    new_grid[row][col] = 1
        self.grid = new_grid

    def __str__(self):
        grid_str = ''
        for row in self.grid:
            grid_str += ''.join('█' if cell else ' ' for cell in row) + '\n'
        return grid_str


# Initialize a larger game grid
game = GameOfLife()

# Set an initial pattern (e.g., a glider)
glider_pattern = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
for (row, col) in glider_pattern:
    game.set_cell(row, col, 1)

# Define the number of iterations to run
iterations = 5

# Run the game for a defined number of iterations and print each state
for _ in range(iterations):
    print(game)
    game.next_state()


import tkinter as tk

# Implementation of the Game of Life GUI using tkinter
class GameOfLifeGUI:
    def __init__(self, master, rows=60, cols=100, cell_size=10):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.game = GameOfLife(rows, cols)

        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]
        self.master.title("Conway's Game of Life")

        self.canvas = tk.Canvas(self.master, width=self.cols*cell_size, height=self.rows*cell_size)
        self.canvas.pack()

        self.start_button = tk.Button(self.master, text="Tambalii", command=self.start_game)
        self.start_button.pack(side='left')

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_game, state='disabled')
        self.pause_button.pack(side='left')

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_game)
        self.clear_button.pack(side='left')

        self.running = False
        self.game_interval = 100  # ms between generations
        self.canvas.bind("<Button-1>", self.canvas_click)

        self.draw_grid()
        self.update()

    def draw_grid(self):
        for i in range(0, self.cols*self.cell_size, self.cell_size):
            self.canvas.create_line([(i, 0), (i, self.rows*self.cell_size)], tag='grid_line')
        
        for i in range(0, self.rows*self.cell_size, self.cell_size):
            self.canvas.create_line([(0, i), (self.cols*self.cell_size, i)], tag='grid_line')

    def canvas_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if self.game.grid[row][col]:
            self.game.set_cell(row, col, 0)
            self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size,
                                         (col+1)*self.cell_size, (row+1)*self.cell_size, fill="white")
        else:
            self.game.set_cell(row, col, 1)
            self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size,
                                         (col+1)*self.cell_size, (row+1)*self.cell_size, fill="black")

    def update(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.game.grid[row][col]:
                    self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size,
                                                 (col+1)*self.cell_size, (row+1)*self.cell_size, fill="black")
                else:
                    self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size,
                                                 (col+1)*self.cell_size, (row+1)*self.cell_size, fill="white")

    def start_game(self):
        self.running = True
        self.start_button.config(state='disabled')
        self.pause_button.config(state='normal')
        self.clear_button.config(state='disabled')
        self.run_game()

    def pause_game(self):
        self.running = False
        self.start_button.config(state='normal')
        self.pause_button.config(state='disabled')
        self.clear_button.config(state='normal')

    def clear_game(self):
        self.game = GameOfLife(self.rows, self.cols)
        self.update()
        self.canvas.delete('grid_item')

    def run_game(self):
        self.game.next_state()
        self.update()
        if self.running:
            self.master.after(self.game_interval, self.run_game)

# Run the GUI
root = tk.Tk()
gui = GameOfLifeGUI(root)
root.mainloop()
