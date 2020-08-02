sentence = input("Enter a sentence: ")

def word_histogram(sentence):
    dictionary = {}
    split_sentence = sentence.split(" ")
    for i in split_sentence:
        if i not in dictionary:
            dictionary[i.lower()] = 1
        else:
            dictionary[i.lower()] += 1
    return dictionary


print(word_histogram(sentence))