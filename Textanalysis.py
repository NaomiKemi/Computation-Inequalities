import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
plt.rcParams['figure.figsize'] = (8,6)
def numWordAnalysis(artists):
    df = pd.DataFrame(columns=('artist', 'words'))
    i=0
    for artist in artists:
        f = open('lyrics/' + artist + '-cleaned', 'rb')
        num_words = 0
        all_text = ''
        for sentence in f.readlines():
            this_sentence = sentence.decode('utf-8')
            num_words_this = len(this_sentence.split(" "))
            num_words += num_words_this

        df.loc[i] = (artist, num_words)
        i+=1

    df.plot.bar(x='artist', y='words', title='Number of Words for each Artist');
    plt.show()
