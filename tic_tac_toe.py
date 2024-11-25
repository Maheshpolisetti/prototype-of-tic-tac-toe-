import tkinter as tk
from tkinter import messagebox
# Multi-line ASCII art for the title
title = """
  _______  _        _______           _______         
 |__   __|(_)      |__   __|         |__   __|        
    | |    _  ___     | | __ _  ___     | | ___   ___ 
    | |   | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\
    | |   | | (__     | | (_| | (__     | | (_) |  __/
    |_|   |_|\___|    |_|\__,_|\___|    |_|\___/ \\___|
"""



# Check for empty cells
def check(grid):
    for row in grid:
        if " " in row:
            return True
    return False

# Check game conditions
def conditions(grid):
    for x in range(3):
        # Check rows and columns
        if grid[x][0] == grid[x][1] == grid[x][2] and grid[x][0] != " ":
            return f"{grid[x][0]} wins"
        if grid[0][x] == grid[1][x] == grid[2][x] and grid[0][x] != " ":
            return f"{grid[0][x]} wins"
    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
        return f"{grid[0][0]} wins"
    if grid[2][0] == grid[1][1] == grid[0][2] and grid[2][0] != " ":
        return f"{grid[2][0]} wins"
    # Check for draw
    if not check(grid):
        return "Draw"
    return None

def disable_all_buttons(buttons):
    for row in buttons:
        for button in row:
            button.config(state="disabled")

# Handle button clicks
t = 0
def handle_click(x, y, button, grid,buttons):
    global t
    if grid[x][y] == " ":
        grid[x][y] = "X" if t == 0 else "O"
        button.config(text=grid[x][y], state="disabled")
        t = 1 - t  # Toggle player
        result = conditions(grid)
        if result:
            messagebox.showinfo("Tic Tac Toe", result)
            disable_all_buttons(buttons)
            # state="disabled"


def create_game_board(root):
    grid = [[" " for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]  # Keep track of buttons
    for row in range(3):
        for col in range(3):
            button = tk.Button(
                root,
                text="",
                font=("Helvetica", 24),
                width=5,
                height=2,
                command=lambda r=row, c=col: handle_click(r, c, buttons[r][c], grid,buttons)
            )
            button.grid(row=row, column=col, padx=5, pady=5)
            buttons[row][col] = button  # Store button reference in the 2D list

# Create the main game window
def create():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    create_game_board(root)
    root.mainloop()

#### play with bot 

def minimax(board, depth, is_maximizing):
    winner = conditions(board)
    if winner == "X wins":  # Maximizing player wins
        return 10 - depth
    elif winner == "O wins":  # Minimizing player wins
        return depth - 10
    elif not check(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  # Maximizing player
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "  # Undo move
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  # Minimizing player
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "  # Undo move
                    best_score = min(best_score, score)
        return best_score


# Best Move Function
def find_best_move(board):
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board,0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def bot_click(x, y, button, grid, buttons):
    if grid[x][y] == " ":  # Player's move
        grid[x][y] = "O"
        button.config(text="O", state="disabled")
        result = conditions(grid)
        if result:  # Player wins or draw
            messagebox.showinfo("Tic Tac Toe", result)
            disable_all_buttons(buttons)
            return

        move = find_best_move(grid)  # Bot calculates the best move
        if move:
            grid[move[0]][move[1]] = "X"
            buttons[move[0]][move[1]].config(text="X", state="disabled")
            result = conditions(grid)
            if result:  # Bot wins or draw
                messagebox.showinfo("Tic Tac Toe", result)
                disable_all_buttons(buttons)


def create_bot_board(root):
    grid = [[" " for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]  # Keep track of buttons
    for row in range(3):
        for col in range(3):
            button = tk.Button(
                root,
                text="",
                font=("Helvetica", 24),
                width=5,
                height=2,
                command=lambda r=row, c=col: bot_click(r, c, buttons[r][c], grid, buttons)
            )
            button.grid(row=row, column=col, padx=5, pady=5)
            buttons[row][col] = button  # Store button reference in the 2D list

####

# Create the main game window
def create_bot():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    create_bot_board(root)
    root.mainloop()

####

# Create main menu interface
def create_tic_tac_toe_interface():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.geometry("600x400")
    root.configure(bg="black")

    title_label = tk.Label(
        root,
        text=title,
        font=("Courier", 14),
        fg="blue",
        bg="black",
        justify="center"
    )
    title_label.pack(pady=20)
    # prototype upcoming version
    # Load an image
    # image = PhotoImage(file=f"C:\Users\psvma\OneDrive\Pictures\Saved Pictures\logo.jpg")  
    # Ensure it's a supported format, like .png or .gif

    # # Add the image to a label
    # label = Label(root, image=image)
    # label.pack()


    play_button = tk.Button(
        root,
        text="Play with Friend",
        font=("Helvetica", 12),
        bg="green",
        fg="white",
        padx=20,
        pady=10,
        command=create
    )
    play_button.pack(pady=20)

    play_button2 = tk.Button(
        root,
        text="Play Computer (prototype)",
        font=("Helvetica", 12),
        bg="green",
        fg="white",
        padx=20,
        pady=10,
        command=create_bot
        # state="disabled"
    )
    play_button2.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_tic_tac_toe_interface()
