from random import randint
from os import system


class Game():
    def __init__(self):
        self.isOn = True
        self.p1 = Player("Human")
        self.p2 = Player("Computer", isHuman=False)

    def shoot(self, c):
        if c == 0:
            print("\nTie\n")
        elif c in (-1, 2):
            self.win(self.p2)
        elif c in (1, -2):
            self.win(self.p1)
        return self.score()

    def win(self, player):
        player.score += 1
        print("\n{} wins!\n".format(player.name))

    def score(self):
        tally = (self.p1.score, self.p2.score)
        print("\nScore:\nPlayer\tComputer\n{}\t{}\n".format(*tally))

    def round(self):
        c = self.p1.choose() - self.p2.choose()
        print("{} & {}".format(self.p1.msg, self.p2.msg))
        self.shoot(c)

    def stop(self):
        self.isOn = False
        system("clear")
        self.score()
        print("Thanks for playing\n")
        return quit()


class Player():
    def __init__(self, name, isHuman=True):
        self.isHuman = isHuman
        self.name = name
        self.score = 0
        self.weapons = ['r', 'p', 's']
        self.equipped = 0  # store as number
        self.msg = ""

    def choose(self):
        if not self.isHuman:
            equipped = randint(0, 2)
        else:
            c = input("R, P, S, q: ").lower()
            system("clear")
            if c not in self.weapons:
                if c == "q":
                    return game.stop()
                else:
                    system("clear")
                    print("Incorrect choice: {}\n".format(c))
                    return self.choose()
            equipped = self.weapons.index(c)
        self.msg = "\n{} threw {}".format(self.name, self.weapons[equipped])
        return equipped


if __name__ == "__main__":
    game = Game()
    while game.isOn:
        game.round()
