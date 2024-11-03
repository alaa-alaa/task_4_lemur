import random
from colorama import Fore, Style

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

    def valid_input(self):
        while True:
            print(Fore.YELLOW)
            choice = input(" paper | rock | scissors: ").lower()
            print(Style.RESET_ALL)
            if (
                choice == "paper"
                or choice == "rock"
                or choice == "scissors"
                or choice == "quit"
            ):
                return choice


# class PlayerRock
class PlayerRock(Player):
    def move(self):
        """return every round rock move"""
        return "rock"


# class RandomPlayer
class RandomPlayer(Player):
    def move(self):
        """return random move of palyer"""
        return random.choice(moves)


# class HumanPlayer
class HumanPlayer(Player):
    def move(self):
        """return input move"""
        return self.valid_input()


# class ReflectPlayer
class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = random.choice(moves)  # initail value first round

    def learn(self, my_move, their_move):
        """store the moves of reflect player & human palyer"""
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        """return the move of opponent palyer(human player)"""
        return self.their_move


# class CyclePlayer
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.indexOfCurrent_move = 0  # initail value first round

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        """return series of  move"""
        self.my_move = moves[self.indexOfCurrent_move]
        self.indexOfCurrent_move = (self.indexOfCurrent_move + 1) % len(moves)
        return self.my_move
