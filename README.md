# 🪨 Stone Paper Scissor (Python)

A simple, interactive command-line implementation of the classic **Rock-Paper-Scissors** game built using Python. 

---

## 🎮 How to Play
The game pits you against the computer. You input your choice, the computer randomly selects its move, and the winner is determined based on standard rules.

### Rules:
* **Stone** beats **Scissor**
* **Paper** beats **Stone**
* **Scissor** beats **Paper**

---

## 🚀 Features
* **Quick Input:** Uses shorthand codes for faster gameplay (`st`, `p`, `sc`).
* **Randomized AI:** The computer's choice is generated using Python's `random` module.
* **Input Mapping:** Uses a dictionary-based system to map shorthand inputs to game logic.

---

## 🛠️ Installation & Usage

### Prerequisites
* Python 3.x installed on your machine.

### Running the Game
1. **Clone or Download** this repository.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the script.
4. Run the following command:
   ```bash
   python main.py
🕹️ ControlsWhen prompted, enter one of the following codes:InputRepresentsstStonepPaperscScissor📊 Logic OverviewThe game uses a numeric scoring system to evaluate winners:Stone: 0Paper: 1Scissor: -1The program compares the user's integer value against the computer's value using conditional if-elif statements to announce the result.
