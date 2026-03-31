#STONE PAPER SCISSOR GAME
 
# 0 = STONE
# 1 = PAPER
# -1 = SCISSOR

import random
computer = random.choice([0,1,-1])
youchose = input("Enter your choice : ")
options = {"st":0,"p":1,"sc":-1}
c_choice ={0:"Stone",1:"Paper",-1:"Scissor"}

you = options[youchose]

print(f"Your choice is :  {c_choice[you]}")
print(f"Computer choose : {c_choice[computer]}")

if(computer == you):
    print("Its draw")
else:
    if (computer == 0 and you ==1):
        print("You won")
        print("Congratulations")
    if (computer == 1 and you ==-1):
        print("You won")
        print("Congratulations")
    if (computer == -1 and you ==0):
        print("You won")
        print("Congratulations")                    
# 0 = STONE
# 1 = PAPER
# -1 = SCISSOR
    elif(computer == 1 and you == 0):
        print("You lose!\nBetter Luck Next Time. ")
    elif(computer == -1 and you == 1):
        print("You lose!\nBetter Luck Next Time. ")
    elif(computer == 0 and you == -1):
        print("You lose!\nBetter Luck Next Time. ")
print("")
