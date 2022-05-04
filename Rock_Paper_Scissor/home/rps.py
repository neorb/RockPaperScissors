#!/usr/bin/env python3
import random
import time
import sys


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


# Parent class <-------------
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Players(Player):
    pass


# Random move <---------------
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Validate input User <------------------
def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print(f"Sorry, {response} input. Please answer:")
    return response


# Validate choice User <-----------------
def valid_choice(prompt, option1, option2, option3, option4):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        elif option4 in response:
            break
        else:
            print(f"Sorry, {response} is invalid. Try agian!.")
    return response


# Reflect moves <-----------------
class ReflectPlayer(Player):
    def __init__(self):
        self.nextMove = random.choice(moves)

    def move(self):
        return self.nextMove

    def learn(self, my_move, their_move):
        self.nextMove = their_move


# CyclePlayer <------------
class CyclePlayer(Player):
    def __init__(self):
        self.nextMove = random.choice(moves)

    def move(self):
        return self.nextMove

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.nextMove = 'paper'
        elif my_move == 'paper':
            self.nextMove = 'scissors'
        elif my_move == 'scissors':
            self.nextMove = 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def blink(self):
    for x in range(5):
        print(" *** YOU ARE THE WINNER! ***", end='\r')
        time.sleep(0.5)
        sys.stdout.write('\033[2K\r')
        time.sleep(0.5)


def print_pause(message, delay=0):
    time.sleep(delay)
    print(message)


# subclass for human player <-------------
class HumanPlayer(Player):
    def move(self):
        choice = valid_choice("Rock, Paper or Scissors? -> ",
                              "rock", "paper", "scissors", "quit")
        if "rock" == choice:
            return "rock"
        elif "paper" == choice:
            return "paper"
        elif "scissors" == choice:
            return "scissors"
        elif "quit" == choice:
            exit(0)
        else:
            print(f"{choice} is not valit, please try to concetrate!.")
        return self.move()


class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        # initialize the scores <--------------
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move_p1 = self.player_1.move()
        move_p2 = self.player_2.move()
        print_pause(f" - You played: {move_p1}", 1)
        print_pause(f" - Pc played: {move_p2}", 1)
        # Result of player score <-------------
        if beats(move_p1, move_p2):
            self.score_p1 += 1
            print_pause(" ** YOU WINS **\n", 1)
        elif beats(move_p2, move_p1):
            self.score_p2 += 1
            print_pause("** PC WINS **\n", 1)
        else:
            print("Draw!\n")
        print_pause(f"Your score: {self.score_p1}", 2)
        print_pause(f"Pc score: {self.score_p2}\n", 2)
        self.player_1.learn(move_p1, move_p2)
        self.player_2.learn(move_p2, move_p1)

    def play_game(self):
        print_pause(" *** Game start! ***\n", 1)
        for round in range(3):
            print_pause(f"Round {round} --", 2)
            self.play_round()
        if self.score_p1 == self.score_p2:
            print_pause(" ** It is a Draw! **", 1)
        elif self.score_p1 > self.score_p2:
            blink(self)
        else:
            print_pause(" ** PC is the Winner! ** ")
        print("** GAME OVER ** ")
        self.play_again()

    # Aks player to play agin <--------------
    def play_again(self):
        choice = valid_input("Play again? [y|n]\n",
                             'y', 'n')
        if choice == 'n':
            print_pause('Thanks for playing! Goodbye!', 0.5)
            exit(0)
        elif choice == 'y':
            self.play_game()
        else:
            print_pause(f"{choice} is not valid input,"
                        "please try to concentrate", 0.5)
            return self.play_again()


# Name Main Do <-----------------
if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
           [Players(), RandomPlayer(), ReflectPlayer(),
            CyclePlayer()]))
    game.play_game()
