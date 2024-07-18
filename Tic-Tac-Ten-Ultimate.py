import tkinter as tk
import random

# Function to change the dice image
def change_dice_image(name):
    img = tk.PhotoImage(file=name)
    dice.config(image=img)
    dice.image = img

# Function to roll the dice
def roll_dice():
    global dice_value, dice_image_path, dice_rolled
    randvalue = random.randint(1, 6)
    image_paths = {
        1: '/Users/omaewamoushindeiru/Desktop/1.png',
        2: '/Users/omaewamoushindeiru/Desktop/2.png',
        3: '/Users/omaewamoushindeiru/Desktop/3.png',
        4: '/Users/omaewamoushindeiru/Desktop/4.png',
        5: '/Users/omaewamoushindeiru/Desktop/5.png',
        6: '/Users/omaewamoushindeiru/Desktop/6.png'
    }
    image_path = image_paths[randvalue]
    change_dice_image(image_path)
    dice_value, dice_image_path = randvalue, image_path
    dice_rolled = True
    label.config(text=f"{curr_player} rolled a {dice_value}. Place it on the board.")

# Function to set a tile in the Tic Tac Ten game
def set_tile(row, column):
    global curr_player, turns, game_over, dice_rolled

    if game_over or not dice_rolled:
        return

    if board[row][column]["text"] != "":
        return

    # Set the tile with the dice value
    board[row][column]["text"] = str(dice_value)

    if curr_player == player1:
        curr_player = player2
    else:
        curr_player = player1

    label.config(text=curr_player + "'s turn")
    turns += 1
    dice_rolled = False
    check_winner()

# Function to check for a winner in the Tic Tac Ten game
def check_winner():
    global game_over

    # Helper function to check if a line sums to 10
    def check_line_sum(line):
        values = [int(board[r][c]["text"]) for r, c in line if board[r][c]["text"] != ""]
        return len(values) == 3 and sum(values) == 10

    lines = [
        # Horizontal lines
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Vertical lines
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonal lines
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]

    for line in lines:
        if check_line_sum(line):
            label.config(text="We have a winner!", foreground="yellow")
            for r, c in line:
                board[r][c].config(foreground="yellow", background=color_white)
            game_over = True
            return

    if turns == 9:
        game_over = True
        label.config(text="IT'S A TIE", foreground="yellow", background="black")

# Function to start a new game
def new_game():
    global curr_player, turns, game_over, dice_rolled

    curr_player = player1
    turns = 0
    game_over = False
    dice_rolled = False
    label.config(text=curr_player + "'s turn")
    for row in range(3):
        for column in range(3):
            board[row][column]["text"] = ""
            board[row][column].config(foreground="black", background=color_white)

# Initialize Tkinter
root = tk.Tk()
root.title("Dice Rolling and Tic Tac Ten")

# Constants
player1 = "Player 1"
player2 = "Player 2"
curr_player = player1
turns = 0
game_over = False
dice_rolled = False
dice_value = 0
dice_image_path = ""

color_white = "#ffffff"

# Create frames
dice_frame = tk.Frame(root)
game_frame = tk.Frame(root)

# Create and pack widgets for dice rolling simulator
btn_roll_dice = tk.Button(dice_frame, text="Roll Dice", font=('Arial', 20, "bold"), command=roll_dice)
dice = tk.Label(dice_frame, image=None)  # Placeholder for dice image
btn_roll_dice.pack(pady=10)
dice.pack()

# Create widgets for Tic Tac Ten game
label = tk.Label(game_frame, text=curr_player + "'s turn", font=("Calibri", 20), background="gray")
label.grid(row=0, column=0, columnspan=3, sticky="we")

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(game_frame, text="", font=("Arial", 60, "bold"), background=color_white, width=4, height=1,
                                         command=lambda row=row, column=column: set_tile(row, column))
        buttons[row][column].grid(row=row + 1, column=column, padx=5, pady=5)
        board[row][column] = buttons[row][column]

btn_new_game = tk.Button(game_frame, text="New Game", font=("Calibri", 20), background="gray", foreground="white", command=new_game)
btn_new_game.grid(row=4, column=0, columnspan=3, sticky="we", pady=10)

# Pack frames into root window
dice_frame.pack(side=tk.LEFT, padx=20, pady=20)
game_frame.pack(side=tk.RIGHT, padx=20, pady=20)

# Center the main window on the screen
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Start the main loop
root.mainloop()
