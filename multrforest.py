import nltk
import os
from sklearn.datasets import load_digits
from sklearn import cross_validation
import numpy as np
from randomforest import RandomForestClassifier

g = open('finalWords', 'r')
voc = g.readlines()
g.close()

vocabulary = []
filewords = []
bsport = {}
total = 0
probability = {
        'sport': 511,
        'business': 510,
        'tech': 401,
        'entertainment': 386,
        'politics': 417
        }

for i in probability.keys():
    total += probability[i]

def classify(name, num):
    h = open('./mult_word_frequencies/b' + name, 'r')
    txt = h.readlines()
    h.close()
    freq = {}
    for i in txt:
    	data = i.strip().split('*')
        freq[data[0]] = float(data[1])
        prob = (num * 1.0)/total
    for i in bsport.keys():
	    prob *= freq[i]**bsport[i]
    return prob

for i in voc:
    vocabulary.append(i.strip())

arr = ['datasets', 'Input']
def creator(train):
    inp = []
    types = []
    for classes in probability.keys():
        inputFiles = os.listdir(arr[train] + '/' + classes)
        correct = 0
        print classes
        for files in inputFiles:
            new = []
            filewords = {}
            f = open(arr[train] + '/' + classes + '/' + files, 'r')
            fil = f.readlines()
            f.close()
            for i in voc:
                bsport[i.strip()] = 0
            for i in fil:
                line = i.strip().decode("ascii", "ignore").encode("ascii")
                words = nltk.word_tokenize(line)
                for word in words:
                    if word not in filewords:
                        filewords[word] = 1
                    else:
                        filewords[word] += 1
            for j in filewords:
                if j in vocabulary:
                    bsport[j] += filewords[j]
            maxProb = -1
            finalclass = ''
            for i in probability.keys():
                presProb = classify(i, probability[i])
                if maxProb < presProb:
                    finalClass = i
                    maxProb = presProb 
            if classes == finalClass:
                correct += 1
            for i in bsport.keys():
                new.append(bsport[i])
            inp.append(new)
            if classes == 'business':
                types.append(0)
            if classes == 'sport':
                types.append(1)
            if classes == 'tech':
                types.append(2)
            if classes == 'politics':
                types.append(3)
            if classes == 'entertainment':
                types.append(4)
    if train == 0:
        X_train = np.array(inp)
        y_train = np.array(types)
        return X_train, y_train
    else:
        X_test = np.array(inp)
        y_test = np.array(types)
        return X_test, y_test

X_train, y_train = creator(0)
X_test, y_test = creator(1)
forest = RandomForestClassifier()
forest.fit(X_train, y_train)

accuracy = forest.score(X_test, y_test)
print 'The accuracy was', 100*accuracy, '% on the test data.'

classifications = forest.predict(X_test)

def getAccuracy(category):
    accuracy = {
            0:['business',0],
            1:['sport', 0],
            2:['tech', 0],
            3:['politics', 0],
            4:['entertainment', 0]
            }
    for i in range(len(classifications)):
        if y_test[i] == category:
            accuracy[classifications[i]][1] += 1
    return accuracy

for i in range(5):
    accuracy = getAccuracy(i)
    sumy = 0
    for key in accuracy.keys():
        sumy += accuracy[key][1]
    for key in accuracy.keys():
        print accuracy[i][0], ' --> ', accuracy[key][0], (100.0*accuracy[key][1])/sumy
