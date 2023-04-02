# Count occurrence of each word in a given string

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word]= counts[word]+1
        else:
            counts[word] = 1

    return counts

print(word_count('the quick brown fox jumps over the lazy dog.'))
