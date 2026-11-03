# Daily Challenge: Text Analysis - Week 2, Day 4

import os
import re
import string


# Part I: Analyzing a simple string
class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"'{word}' is not in the text."
        return count

    def most_common_word(self):
        words = self.text.split()
        frequencies = {}
        for word in words:
            frequencies[word] = frequencies.get(word, 0) + 1
        return max(frequencies, key=frequencies.get)

    def unique_words(self):
        words = self.text.split()
        return list(set(words))

    # Part II: Analyzing text from a file
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return cls(content)


# Bonus: Text modification
STOP_WORDS = {"a", "an", "the", "is", "are", "and", "or", "on", "in", "of", "to", "it", "at"}


class TextModification(Text):
    def remove_punctuation(self):
        return self.text.translate(str.maketrans("", "", string.punctuation))

    def remove_stop_words(self):
        words = self.text.split()
        kept = [word for word in words if word.lower() not in STOP_WORDS]
        return " ".join(kept)

    def remove_special_characters(self):
        return re.sub(r"[^A-Za-z0-9\s]", "", self.text)


# Tests
t = Text("the cat and the dog and the bird")
print("Frequency of 'the':", t.word_frequency("the"))
print("Frequency of 'fish':", t.word_frequency("fish"))
print("Most common word:", t.most_common_word())
print("Unique words:", sorted(t.unique_words()))

file_path = os.path.join(os.path.dirname(__file__), "sample_text.txt")
from_file = Text.from_file(file_path)
print("Most common word in the file:", from_file.most_common_word())

m = TextModification("Hello, World! The #1 rule: it is fun & easy.")
print("No punctuation:", m.remove_punctuation())
print("No stop words:", m.remove_stop_words())
print("No special characters:", m.remove_special_characters())
