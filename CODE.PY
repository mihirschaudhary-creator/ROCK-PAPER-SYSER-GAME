import random

# --- Section 1: Name Registration ---
print("==================================")
print("    STONE PAPER SCISSOR GAME      ")
print("==================================")

player_name = input("Enter your name to register: ").strip()

# Default name if the user leaves it blank
if not player_name:
    player_name = "Player 1"

print(f"Welcome, {player_name}! Let's see if you can beat the computer.\n")

# --- Section 2: Game Configuration ---
# 0 = STONE | 1 = PAPER | -1 = SCISSOR
options = {"st": 0, "p": 1, "sc": -1}
c_choice = {0: "Stone", 1: "Paper", -1: "Scissor"}

# Computer makes a random choice
computer = random.choice([0, 1, -1])

# --- Section 3: User Input ---
print("Controls: [st] Stone | [p] Paper | [sc] Scissor")
user_input = input("Enter your choice: ").lower().strip()

# --- Section 4: Game Logic & Results ---
if user_input in options:
    you = options[user_input]

    print(f"\n{player_name} chose: {c_choice[you]}")
    print(f"Computer chose: {c_choice[computer]}")
    print("-" * 34)

    if computer == you:
        print("RESULT: It's a DRAW! 🤝")
    
    # Winning conditions for the Player
    elif (computer == 0 and you == 1) or \
         (computer == 1 and you == -1) or \
         (computer == -1 and you == 0):
        print(f"RESULT: Congratulations {player_name}, YOU WON! 🎉")
    
    # All other non-draw conditions mean the Player lost
    else:
        print(f"RESULT: Sorry {player_name}, YOU LOSE! ❌")
        print("Better luck next time!")

else:
    print("\n[ERROR] Invalid input! Please restart and type 'st', 'p', or 'sc'.")

print("==================================")
