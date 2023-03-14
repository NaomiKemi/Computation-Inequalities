import urllib.request
import re
import os
from bs4 import BeautifulSoup
from search import search
from textanalysis import numWordAnalysis
from wordCountAnalysis import wordCountAnaylsis
from senitmentanalysis import sentimentAnalyzer

CLEANR = re.compile('<.*?>')
# SQUAREBRACKETCLEANER = re.compile('[.*?]')

outputfilename = "lyrics.csv"
artists = ["Digga D"]
#artists = ["Headie One", "Digga D", "Unknown T","K-Trap","Double LZ","Central Cee","Ivorian Doll","M24","Aitch","Stormzy"]

def get_lyrics(url):
    request = urllib.request.Request(url)
    request.add_header("Authorization", "Bearer " + "Yw43A-HguHNcgZfNyH6yo4llsUYDxkACUqlAKa4hz5_wkaMzpkxw34cOp6kZ5fRD")
    request.add_header("User-Agent",
                       "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")
    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page, "lxml")
    ##lyrics = soup.find("div", class_= "Lyrics__Container")

    lyrics = soup.findAll("div", {"class": lambda L: L and L.startswith('Lyrics__Container')})
    print(repr(lyrics[0]))
    return lyrics[0]

def getArtistData():
    for artist in artists:
        a = search(artist, outputfilename, "Yw43A-HguHNcgZfNyH6yo4llsUYDxkACUqlAKa4hz5_wkaMzpkxw34cOp6kZ5fRD")
        urls = map(lambda t: t[3], a)
        # print(urls[0])
        f = open('lyrics/' + artist, 'wb')
        for url in urls:
            #print (url)
            lyrics = get_lyrics(url)
            f.write(lyrics.encode("utf8"))
        f.close()

    for artist in artists:
        f = open('lyrics/' + artist, 'rb')
        all_words = ''
        for sentence in f.readlines():
            this_sentence = sentence.decode('utf-8')
            all_words += this_sentence
        f.close()

        all_words = all_words.replace("<br/>", "\n")

        all_words = re.sub(CLEANR, '', all_words)

        print(all_words)
        # all_words = re.sub(SQUAREBRACKETCLEANER, '', all_words)
        # all_words = re.sub(r"[\([{})\]]", "", all_words)
        all_words = re.sub(r'[\(\[].*?[\)\]]', '', all_words)
        print(all_words)
        # remove identifiers like chorus, verse, etc

        # remove empty lines
        # all_words = os.linesep.join([s for s in all_words.splitlines() if s])


        f = open('lyrics/' + artist + '-cleaned', 'wb')
        f.write(all_words.encode('utf-8'))
        f.close()

# getArtistData()
#numWordAnalysis(artists)
wordCountAnaylsis(artists)
# sentimentAnalyzer(artists)
