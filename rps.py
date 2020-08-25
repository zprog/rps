from random import randint
from os import system

p1, p2 = "player", "computer"
score = {p1: 0, p2: 0}
weapons = ["r","p","s"]

class Player():
    def __init__(self, name, score=0, cpu=False):
        self.name = name
        self.score = score
        self.cpu = cpu

    def choose():
        c = input("R, P, S: ").lower()
        if c not in weapons:
            print(f"Incorrect choice: {c}" + "\n")
            self.choose()
        elif self.cpu:
            return weapons[randint(0,2)] #R=0, P=1, S=2
        system('clear')
        return c

def win(p):
    score[p] += 1
    scoreboard()

def scoreboard():
    print("Scoreboard:\nPlayer\tComputer\n" + f"{score['player']}" + "\t" + f"{score['computer']}" + "\n")

# Choose a weapon.
def choose():
    c = input("R, P, S: ")
    if c.lower() not in weapons:
        print(f"Incorrect choice: {c}" + "\n")
        choose()
    system("clear")
    return c

def cpu_choice():
    return weapons[randint(0,2)] #R=0, P=1, S=2

# rock, paper, scissors, SHOOT!
def shoot(p):
    if (p1_choice == weapons[0] and p2_choice == weapons[2] or
        p1_choice == weapons[1] and p2_choice == weapons[0] or
        p1_choice == weapons[2] and p2_choice == weapons[1]):
        return True

# Game loop
# Ctrl + C to quit
while True:
    p1_choice, p2_choice = choose(), cpu_choice()
    print(f"{p1} threw {p1_choice} & {p2} threw {p2_choice}" + "\n")
    #print(f"{p1} threw {p1_choice} & {p2} threw {p2_choice}." + "\n")
    if p1_choice == p2_choice:
        print("Tie!\n")
        scoreboard()
    elif (shoot(p1_choice)):
        win(p1)
    else:
        win(p2)
