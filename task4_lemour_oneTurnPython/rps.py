import player
import time
from colorama import Fore, Style


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def beats(self, one, two):
        return (
            (one == "rock" and two == "scissors")
            or (one == "scissors" and two == "paper")
            or (one == "paper" and two == "rock")
        )

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        time.sleep(1)
        if move1 == "quit":
            print(
                Fore.MAGENTA,
                f"Score-> PlayerOne :{self.score1}   PlayerTwo :{self.score2}",
            )
            self.player_score()
            return False

        print(
            Fore.BLUE,
            f"Move -> PlayerOne:{move1}    PlayerTwo:{move2}",
            Style.RESET_ALL,
        )

        if move1 == move2:
            print(Fore.RED, "--TIE--", Style.RESET_ALL)
        else:
            if self.beats(move1, move2):
                self.score1 += 1
            else:
                self.score2 += 1
        time.sleep(1)
        print(
            Fore.MAGENTA,
            f"Score-> PlayerOne :{self.score1}      PlayerTwo :{self.score2}",
        )
        print(Style.RESET_ALL)

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        return True

    def player_score(self):
        """ "print score of the player"""
        if self.score1 > self.score2:
            print(Fore.CYAN, "******** Player One Win ******", Style.RESET_ALL)
        elif self.score1 < self.score2:
            print(Fore.CYAN, "******** Player Two Win ******", Style.RESET_ALL)
        else:
            print(Fore.RED, "******** TIE GAME ********", Style.RESET_ALL)

    def play_game(self):
        """start game"""
        print(" Game start!")

        for round in range(6):
            print(Fore.GREEN, f"Round {round}:", Style.RESET_ALL)
            if not self.play_round():
                break

            self.player_score()

        print(Style.DIM, "Game Over!", Style.RESET_ALL)


def valid_input_str(prompt, options):
    while True:
        option = input(prompt).lower()
        if len(option) == 1 and option in options:
            return option


def print_pause(str, delay=0):
    time.sleep(delay)
    print(str)


if __name__ == "__main__":
    while True:
        print(Fore.YELLOW)
        stratege = {
            "1": player.PlayerRock(),
            "2": player.RandomPlayer(),
            "3": player.CyclePlayer(),
            "4": player.ReflectPlayer(),
        }
        choice1 = valid_input_str(
            "select the player strategy : \n"
            "you want play against \n"
            "1- Rock Player \n"
            "2- Random Player \n"
            "3- Cycle Player \n"
            "4- ReflectPlayer \n",
            ["1", "2", "3", "4"],
        )
        print(Style.RESET_ALL)

        print_pause(f"Human Player vs strategy choice {choice1}", 1)
        game = Game(player.HumanPlayer(), stratege[choice1])
        game.play_game()

        choice2 = valid_input_str(" do you like play again?(y/n)", ["y", "n"])
        if choice2 == "n":
            break
