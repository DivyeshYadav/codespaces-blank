import tkinter as tk
from tkinter import messagebox

# --- Game setup ---
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x450")
root.config(bg="#222")

current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# --- Functions ---
def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            highlight_winner([(row, 0), (row, 1), (row, 2)])
            return buttons[row][0]["text"]

    # Check columns
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            highlight_winner([(0, col), (1, col), (2, col)])
            return buttons[0][col]["text"]

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        return buttons[0][2]["text"]

    # Check draw
    if all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
        return "Draw"

    return None


def highlight_winner(cells):
    for (r, c) in cells:
        buttons[r][c].config(bg="green", fg="white")


def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col].config(fg="#fff" if current_player == "X" else "orange")
        winner = check_winner()

        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} Wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"


def reset_game():
    global current_player
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", bg="#333")


# --- GUI layout ---
title = tk.Label(root, text="Tic Tac Toe", font=("Arial", 22, "bold"), fg="white", bg="#222")
title.pack(pady=20)

frame = tk.Frame(root, bg="#222")
frame.pack()

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(
            frame,
            text="",
            font=("Arial", 28, "bold"),
            width=4,
            height=1,
            bg="#333",
            fg="white",
            activebackground="#444",
            command=lambda r=r, c=c: button_click(r, c)
        )
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

reset_btn = tk.Button(root, text="Reset", font=("Arial", 14, "bold"), bg="red", fg="white", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
