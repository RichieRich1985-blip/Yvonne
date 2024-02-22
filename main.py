# Yvonne Anyanwu
# CIS 2131
# Project 3
# Hangman game
# 2/22/2024

import random
def hidden_word(blanks):  # user need to guess the hidden word one letter at a time
    int(input("welcome to the hangman game, can you guess the hidden letter but do not repeat the letter"))
def print_hidden_word():  # user is going to enter the hidden word
    print("guess the hidden word: ")

word_list = ["chair", "table", "bag", "dress", "house", "phone", "clock", "pot", "tree"]
print(word_list)
random_word = word_list[random.randint(0, len(word_list)) - 1]
print(random_word)
guess = input("enter the hidden letter: _ _ _ n _")
guessing = input("enter another letter: _ _ _ n_")
guessed = input("enter another letter: _ _ _ n _")
guesses = input("enter another letter: _ _ _ n_")
word = input("enter another letter: _ _ _ n_")
list = input("enter another letter: _ _ _n_")

print("user quit after 6 attempts")
def game_over():  # user game will end after 6 incorrect guesses
    print("sorry user you lost the game")
def print_gallows():  # user should draw the hangman after 6 incorrect guesses

    gallows(0)
    # - - - - - - - -
    # |                |
    # |
    # |              -
    # |
    # |
    # |
    # |
    # _ _ _ _ _ _ _ _ _ _ _

    gallow(6)
# - - - - - - - - - - -
# |                    |
# |                    0
 #|                  --| - -
# |                    |
# |                   /\
# |
# |
# _ _ _ _ _ _ _ _ _ _ _ _ _
