import random

shoot = ["rock", "paper", "scissors"]
comp = random.choice(shoot)
user = input("What are you choosing... rock, paper, or scissors?")
comp_score = 0
user_score = 0

while comp_score or user_score <= 9:
    if comp_score or user_score <= 9:
        if comp == user:
            print("Woah we picked the same thing")
        elif comp != user:
            if comp == "rock" and user == "paper":
                print("Ai picked", comp)
                print("user won this round")
                user_score += 1
            elif comp == "rock" and user == "scissors":
                print("Ai picked", comp)
                print("Ai won this round")
                comp_score += 1
            elif comp == "paper" and user == "scissors":
                print("Ai picked", comp)
                print("user won this round")
                user_score += 1
            elif comp == "paper" and user == "rock":
                print("Ai picked", comp)
                print("Ai won this round")
                comp_score += 1
            elif comp == "scissors" and user == "paper":
                print("Ai picked", comp)
                print("Ai won this round")
                comp_score += 1
            elif comp == "scissors" and user == "rock":
                print("Ai picked", comp)
                print("user won this round")
                user_score += 1
            else:
                print("Ai picked", comp, " and you picked ", user)
                print("something went wrong...")
        print("your score is", user_score, "Ai score is", comp_score)
        comp = random.choice(shoot)
        user = input("What are you choosing... rock, paper, or scissors?")
        print(comp)
    elif comp_score > 9:
        print("congrats Ai you won!")
    elif user_score > 9:
        print("congrats User you won!")
    else:
        print("The game broke")

