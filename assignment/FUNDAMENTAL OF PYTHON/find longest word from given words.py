# find longest word from given words

def find_longest_word(words_list):
    word_len = []

    
    for n in words_list:                                        #for loop to traverse the list
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]

result = find_longest_word(["MOUNTAIN", "PEEK", "TRAILER"])

print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
