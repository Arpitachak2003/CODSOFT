import random

print("~~Welcome to RPS~~")

u_score=0
c_score=0
ties=0

name=input("Enter your name : ")
while True:
    print("""
winning rules:
1.rock vs scissors --> rock
2.scissors vs paper -->scissors
3.paper vs rock --> paper\n""")

    choice= int(input("1 --> Paper\n2 --> Rock\n3 --> Scissors\nEnter your choice : "))
    print()
    while choice > 3 or choice < 1:
        choice=int(input("enter valid choice : "))

    if choice == 1:
        u_choice="paper"
    elif choice == 2:
        u_choice="rock"
    else:
        u_choice="scissors"
    print("user's choice :",u_choice)

    computer = random.randint(1,3)

    if computer == 1:
        c_choice = "rock"
    elif computer == 2:
        c_choice = "scissors"
    else:
        c_choice = "paper"
        

    print("computer's choice :",c_choice)

    if ((u_choice == "scissors" and c_choice == "rock") or (u_choice == "rock" and c_choice == "scissors")):
        print("rock wins")
        result="rock"
    elif ((u_choice == "paper" and c_choice == "scissors") or (u_choice == "scissors" and c_choice == "paper")):
        print("scissors wins")
        result="scissors"
    elif (u_choice == c_choice):
        print("it's a tie")
        result="tie"
    else:
        print("paper wins")
        result="paper"

    if result == "tie":
        ties+=1
    elif result == u_choice:
        print("user wins")
        u_score+=1
    else:
        print("computer wins")
        c_score+=1

    print("scores are")
    print(name,"score =",u_score)
    print("computer's score =", c_score)
    print("ties =",ties)

    repeat = input("do u want to repeat the game?")
    if repeat == "NO" or repeat == "no":
        break

print("GAME OVER!!!!!")
print("THANKS FOR PLAYING THE RPS GAME!!!")
