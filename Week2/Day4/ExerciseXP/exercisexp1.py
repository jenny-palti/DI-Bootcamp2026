# Exercise 1: Random Sentence Generator - Week 2, Day 4
# Needs words.txt in this same folder (from the course's word list download)

import os
import random

WORDS_FILE = os.path.join(os.path.dirname(__file__), "words.txt")


def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content.split()


def get_random_sentence(length):
    words = get_words_from_file(WORDS_FILE)
    chosen = []
    for _ in range(length):
        chosen.append(random.choice(words))
    sentence = " ".join(chosen)
    return sentence.lower()


def main():
    print("This program makes a random sentence from a list of words.")
    answer = input("How many words should the sentence have? (2-20): ")

    try:
        length = int(answer)
    except ValueError:
        print("Error: please enter a whole number.")
        return

    if length < 2 or length > 20:
        print("Error: the number must be between 2 and 20.")
        return

    print(get_random_sentence(length))


main()
