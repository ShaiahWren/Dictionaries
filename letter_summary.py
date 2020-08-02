word = input("Enter a word: ")


def letter_histogram(word):
    dictionary = {}
    for i in word:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary

print(letter_histogram(word))