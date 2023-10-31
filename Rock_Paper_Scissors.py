import random

score_me = 0
score_pc = 0
choices = ["Rock", "Paper", "Scissors"]

def judge(attack, opp):
    global score_me, score_pc
    if attack == opp:
        print("It's a Tie!")
    elif attack == "Rock" and opp in ("Paper", "Scissors"):
        score_me += 1
        print(f"{attack} beats {opp}")
    elif attack == "Paper" and opp in ("Rock", "Scissors"):
        score_pc += 1
        print(f"{opp} beats {attack}")
    elif attack == "Scissors" and opp in ("Rock", "Paper"):
        score_pc += 1
        print(f"{opp} beats {attack}")

while score_me < 3 and score_pc < 3:
    while True:
        attack = input("Choose your weapon: ").capitalize()
        if attack in choices:
            print(attack)
            break
        else:
            print("Invalid choice. Please choose from Rock, Paper, or Scissors.")

    opp = random.choice(choices)
    judge(attack, opp)
    print(f"Opponent: {score_pc} You: {score_me}")

if score_me > score_pc:
    print("You win!")
else:
    print("Computer wins!")
