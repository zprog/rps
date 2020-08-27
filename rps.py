from random import randint
from os import system, name


class Game():
    """ A class to represent the game.

    Attributes
    ----------
    isOn : Boolean
        Is game on or off?
    p1 : Player() instance
        Player One
    p2 : Player() instance
        Player Two
    """

    def __init__(self):
        """ initialize game with default: Human vs. CPU. """

        self.isOn = True
        self.p1 = Player("Human")
        self.p2 = Player("Computer", isHuman=False)

    def shoot(self, c):
        """ awards a player based on the value of c.

        Positional argument:
        c -- difference between choices
        example: p1.choice() - p2.choice() = c

        c = 0 : print("Tie")

        Returns score()
        """

        if c == 0:
            print("\nTie\n")
        elif c in (-1, 2):
            self.win(self.p2)
        elif c in (1, -2):
            self.win(self.p1)
        return self.score()

    def win(self, player):
        """ increment player score"""

        player.score += 1
        print("\n{} wins!\n".format(player.name))

    def score(self):
        """ prints cumulative score """

        tally = (self.p1.score, self.p2.score)
        print("Score:\nPlayer\tComputer\n{}\t{}\n".format(*tally))

    def round(self):
        """ basis for rps game loop """

        c = self.p1.choose() - self.p2.choose()
        print("{} & {}".format(self.p1.msg(), self.p2.msg()))
        self.shoot(c)

    def stop(self):
        """ Stop game loop """

        self.isOn = False
        clear()
        self.score()
        print("Thanks for playing\n")
        return quit()


class Player():
    """
    A class to represent the player

    Attributes
    ----------
    isHuman : Boolean
        Human: True; Computer: False
    name : String
        Name of the Player
    weapons : List of chars
        r: rock, p: paper, s: scissors
    equipped : Int
        selected weapon expressed as an int.
        0: rock, 1: paper, 2: scissors
    """

    def __init__(self, name, isHuman=True):
        """initialize player with defaults"""

        self.isHuman = isHuman
        self.name = name
        self.score = 0
        self.weapons = ['r', 'p', 's']
        self.equipped = 0

    def choose(self):
        """ select r, p, or s. returns int

        r -- 0
        p -- 1
        s -- 2
        q -- game.stop()
        """

        if not self.isHuman:
            self.equipped = randint(0, 2)
        else:
            c = input("R, P, S, q: ").lower()
            clear()
            if c not in self.weapons:
                if c == "q":
                    return game.stop()
                else:
                    clear()
                    print("Incorrect choice: {}\n".format(c))
                    return self.choose()
            self.equipped = self.weapons.index(c)
        return self.equipped

    def msg(self):
        """ returns string of player and their choice """

        return "{} threw {}".format(self.name, self.weapons[self.equipped])


def clear():
    """ clears screen. platform agnostics """

    return system('cls' if name == 'nt' else 'clear')


if __name__ == "__main__":
    game = Game()
    while game.isOn:
        game.round()
