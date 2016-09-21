from nltk import word_tokenize
from nltk.corpus import stopwords
import operator
from nltk.tokenize import RegexpTokenizer
import re

wordFreq = {}

stop = set(stopwords.words('english'))

def getWords(dataset, endValue):
    for i in range(1, endValue):
        fname = "{0:03}".format(i) + '.txt'
        f = open('./datasets/' + dataset + '/' + fname, 'r')
        data = f.readlines()
        newData = [a for a in data if a != '\n']
        f.close()
        for line in newData:
            newLine = re.sub('\'[a-zA-Z]+', '', line)
            tokenWords = word_tokenize(newLine.decode("ISO-8859-1"))
            #print "Initial ", tokenWords
            if tokenWords != []:
                sentence = ' '.join(tokenWords)
                words = [i for i in sentence.encode("ISO-8859-1").lower().split() if i not in stop]
                #print "Tokenization ", words
                newSentence = ' '.join(words)
                tokenizer = RegexpTokenizer(r'\w+')
                constructedSentence = tokenizer.tokenize(newSentence)
                #print "Punctuation ", constructedSentence
                for j in constructedSentence:
                    if j not in wordFreq.keys():
                        wordFreq[j] = 1
                    else:
                        wordFreq[j] += 1
        #break

getWords('sport', 512)
getWords('tech', 402)
getWords('politics', 418)
getWords('entertainment', 387)
getWords('business', 511)
newDict = reversed(sorted(wordFreq.items(), key=operator.itemgetter(1)))    

count = 0
for i in newDict:
    if count < 2000:
        print i[0]
    count += 1
