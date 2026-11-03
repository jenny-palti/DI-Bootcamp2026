# Mini-Project #2: Hangman - Week 1, Day 5

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference',
             'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

BODY_PARTS = ["head", "body", "left arm", "right arm", "left leg", "right leg"]


def show_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter == " " or letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display


def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please type one letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def play():
    guessed_letters = []
    mistakes = 0

    print("Welcome to Hangman!")

    while True:
        current = show_word(word, guessed_letters)
        print("\nWord:", current)
        print("Guessed so far:", ", ".join(guessed_letters))

        if "*" not in current:
            print("You solved it! The word was:", word)
            break

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print(f"No '{guess}' in the word. The gallows get a {BODY_PARTS[mistakes]}.")
            mistakes += 1
            print("Gallows:", ", ".join(BODY_PARTS[:mistakes]))

            if mistakes == len(BODY_PARTS):
                print("The whole body is on the gallows. You lost! The word was:", word)
                break


play()
