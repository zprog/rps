import argparse
from rps import *

def rps_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--weapon", help="Choose your weapon: r, p, or s.")
    args = parser.parse_args()
    w = ['r', 'p', 's']
    if args.weapon in w:
        cli_game(w.index(args.weapon))
    else:
        print("Please select: r, p, s")


if __name__ == "__main__":
    rps_args()
