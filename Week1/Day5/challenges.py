# Daily Challenge: Challenges - Week 1, Day 5


# Challenge 1: Sorting
def sort_words():
    text = input("Enter words separated by commas: ")
    words = text.split(",")
    words.sort()
    result = ",".join(words)
    print(result)


# Challenge 2: Longest Word
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


sort_words()

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
