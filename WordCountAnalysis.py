from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib
import string
plt.rcParams['figure.figsize'] = (8,6)

ignoreWords = ["the"]


def wordCountAnaylsis(artists):
    df = pd.DataFrame(columns=('artist', 'lexicalrichness'))
    i = 0
    for artist in artists:
        f = open('lyrics/' + artist + '-cleaned', 'rb')
        raw_text = ""
        for sentence in f.readlines():
            this_sentence = sentence.decode('utf-8')
            this_sentence = this_sentence.lower()
            raw_text += this_sentence
            print(sentence)

        raw_text_array = filter(lambda x: x in string.printable, raw_text)
        raw_text = ""
        for c in raw_text_array:
            raw_text += c

        raw_text = raw_text.replace("\n", " ")
        raw_text = raw_text.replace('\t', ' ')
        raw_text = raw_text.replace('"', ' ')
        raw_text = raw_text.replace(',', ' ')
        words = raw_text.split(" ")
        uniqueWords = {}

        for word in words:

            if len(word) < 2:
                continue

            if word in ignoreWords:
                continue

            result = uniqueWords.get(word)
            if result == None:
                uniqueWords[word] = 1
            else:
                uniqueWords[word] += 1


        uniqueWords = orderDictionary(uniqueWords)


        print(f"There are {len(uniqueWords)} unique words")

        for word in uniqueWords:
            print(f'{word}:{uniqueWords[word]}')



    #     filtered_words = [word for word in words if word not in stopwords.words('english') and len(word) > 1 and word not in ['na', 'la']]
    #     a = len(set(filtered_words))
    #     b = len(words)
    #     df.loc[i] = (artist, (a / float(b)) * 100)
    #     i += 1
    #


# df.plot.bar(x='artist', y='lexicalrichness', title='Lexical richness of each Artist');
# plt.show()

def orderDictionary(oldDict):
    newDict = {}
    while len(oldDict) > 0:
        largestKey = None
        largestAmount = -1
        for key in oldDict:
            if oldDict[key] > largestAmount:
                largestAmount = oldDict[key]
                largestKey = key
        newDict[largestKey] = largestAmount
        del oldDict[largestKey]
    return newDict
