import pdb

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


def tally(dictionary):
    result = [("", 0), ("", 0), ("", 0)]    
    for key, value in dictionary.items():
        # pdb.set_trace()
        # result.append((key, value))
        if value > result[0][1]:
            pdb.set_trace()
            result = [(key, value)].append(result[0:2])
        elif value > result[1][1]:
            result = result[0] ++ [(key, value)] ++ result[1]
        elif value > result[2][1]:
            result = result[0:2] ++ [(key, value)]
    return result

dictionary = word_histogram(sentence)
print(tally(dictionary))