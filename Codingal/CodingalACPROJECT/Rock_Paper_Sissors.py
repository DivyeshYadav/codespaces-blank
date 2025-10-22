import tkinter as tk
import random

# --- Global Score Variables ---
player_score = 0
computer_score = 0

# --- Functions ---
def play(user_choice):
    global player_score, computer_score # Declare as global to modify them
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""
    winner = None # To determine who gets the point

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        winner = "player"
    else:
        result = "You Lose!"
        winner = "computer"

    # Update scores
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1

    # Update labels
    player_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    
    # Update score display
    score_label.config(text=f"Score: Player {player_score} - {computer_score} Computer")

def reset_score():
    """Resets the scores and updates the score label."""
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text=f"Score: Player {player_score} - {computer_score} Computer")
    # Clear result and choice labels for a fresh start
    player_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="Score has been reset!")

# --- GUI setup ---
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500") # Increased height for new labels/button
root.config(bg="#222")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#222", fg="white")
title_label.pack(pady=20)

# --- New Score Label ---
score_label = tk.Label(root, text=f"Score: Player {player_score} - {computer_score} Computer", 
                       font=("Arial", 16), bg="#222", fg="yellow")
score_label.pack(pady=10)
# ------------------------

# Buttons for player choices
button_frame = tk.Frame(root, bg="#222")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="🪨 Rock", width=10, font=("Arial", 14), command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="📜 Paper", width=10, font=("Arial", 14), command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="✂️ Scissors", width=10, font=("Arial", 14), command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Labels for displaying choices and result
player_choice_label = tk.Label(root, text="", font=("Arial", 14), bg="#222", fg="lightgreen")
player_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="", font=("Arial", 14), bg="#222", fg="lightblue")
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#222", fg="yellow")
result_label.pack(pady=20)


reset_button = tk.Button(root, text="Reset Score", font=("Arial", 12), bg="orange", fg="white", command=reset_score)
reset_button.pack(pady=5)
# ------------------------
# Quit button
quit_button = tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="red", fg="white", command=root.destroy)
quit_button.pack(pady=10)

root.mainloop()