import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x550")
root.configure(bg="#2b2d42")  # Gradient-inspired dark background

# Variables for player names and turns
player1_name = tk.StringVar()
player2_name = tk.StringVar()
current_player = tk.StringVar(value="X")

# Game state variables
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 board

# Function to check for a winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

# Function to handle cell clicks
def cell_click(event):
    row = event.y // 100
    col = event.x // 100

    if board[row][col] == "":
        # Draw X or O with vibrant colors
        color = "#e63946" if current_player.get() == "X" else "#457b9d"
        canvas.create_text(
            col * 100 + 50, row * 100 + 50, text=current_player.get(), font=("Poppins", 36, "bold"), fill=color
        )
        board[row][col] = current_player.get()
        winner = check_winner()

        if winner:
            winner_name = (
                player1_name.get() if winner == "X" else player2_name.get()
            )
            messagebox.showinfo("Game Over", f"🎉 {winner_name} Wins! 🎉")
            reset_game()
        elif all(all(cell != "" for cell in row) for row in board):
            messagebox.showinfo("Game Over", "🤝 It's a Tie! 🤝")
            reset_game()
        else:
            # Switch players and update the turn display
            if current_player.get() == "X":
                current_player.set("O")
                player_turn_label.config(
                    text=f"{player2_name.get()}'s Turn (O)", fg="#457b9d"
                )
            else:
                current_player.set("X")
                player_turn_label.config(
                    text=f"{player1_name.get()}'s Turn (X)", fg="#e63946"
                )

# Function to reset the game
def reset_game():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    canvas.delete("all")
    draw_grid()
    current_player.set("X")
    player_turn_label.config(text=f"{player1_name.get()}'s Turn (X)", fg="#e63946")

# Function to draw the grid
def draw_grid():
    for i in range(1, 3):
        canvas.create_line(0, i * 100, 300, i * 100, width=3, fill="#a8dadc")
        canvas.create_line(i * 100, 0, i * 100, 300, width=3, fill="#a8dadc")

# Function to start the game
def start_game():
    if not player1_name.get() or not player2_name.get():
        messagebox.showwarning("Input Error", "Please enter both player names!")
        return

    start_frame.pack_forget()
    game_frame.pack()
    player_turn_label.config(text=f"{player1_name.get()}'s Turn (X)", fg="#e63946")

# GUI Layout
# Start screen for entering player names
start_frame = tk.Frame(root, bg="#2b2d42")
tk.Label(start_frame, text="Player 1 (X):", bg="#2b2d42", fg="#f1faee", font=("Poppins", 12)).grid(row=0, column=0, padx=10, pady=10)
tk.Entry(start_frame, textvariable=player1_name, font=("Poppins", 12), bg="#3a3d4d", fg="#f1faee", insertbackground="#f1faee").grid(row=0, column=1, padx=10, pady=10)

tk.Label(start_frame, text="Player 2 (O):", bg="#2b2d42", fg="#f1faee", font=("Poppins", 12)).grid(row=1, column=0, padx=10, pady=10)
tk.Entry(start_frame, textvariable=player2_name, font=("Poppins", 12), bg="#3a3d4d", fg="#f1faee", insertbackground="#f1faee").grid(row=1, column=1, padx=10, pady=10)

tk.Button(start_frame, text="Start Game", command=start_game, bg="#4caf50", fg="#ffffff", font=("Poppins", 12, "bold"), activebackground="#81c784").grid(
    row=2, column=0, columnspan=2, pady=20
)
start_frame.pack()

# Game screen with the board and turn display
game_frame = tk.Frame(root, bg="#2b2d42")

# Turn label
player_turn_label = tk.Label(game_frame, text="", bg="#2b2d42", font=("Poppins", 16, "bold"))
player_turn_label.grid(row=0, column=0, pady=10)

# Canvas for the game board
canvas = tk.Canvas(game_frame, width=300, height=300, bg="#3a3d4d", highlightthickness=0)
canvas.grid(row=1, column=0, pady=10)
canvas.bind("<Button-1>", cell_click)

# Reset button
tk.Button(game_frame, text="Reset Game", command=reset_game, bg="#e63946", fg="#ffffff", font=("Poppins", 12, "bold"), activebackground="#f76c6c").grid(
    row=2, column=0, pady=10
)

# Draw the initial grid
draw_grid()

# Run the Tkinter event loop
root.mainloop()
