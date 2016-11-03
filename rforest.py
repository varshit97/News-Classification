import nltk
import os
from randomforest import RandomForestClassifier
from sklearn import cross_validation
import numpy as np

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

#MultiVariate Bernoulli
def classify(name, num):
    h = open('./word_frequencies/b' + name, 'r')
    txt = h.readlines()
    h.close()
    freq = {}
    for i in txt:
	data = i.strip().split('*')
	freq[data[0]] = float(data[1])
    prob = (num * 1.0)/total
    for i in bsport.keys():
	prob *= ((bsport[i] * freq[i]) + ((1 - bsport[i]) * (1 - freq[i])))
    return prob

for i in voc:
    vocabulary.append(i.strip())

arr=['datasets','Input']
def creator(train):
    inp = []
    types = []
    for classes in probability.keys():
        inputFiles = os.listdir(arr[train] + '/' + classes)
        correct = 0
        for files in inputFiles:
            new = []
            filewords = []
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
            	        filewords.append(word)
            for j in filewords:
                if j in vocabulary:
                    bsport[j] = 1
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
        #print "Class:", classes, "Accuracy:", correct/50.0
    if train==0:
        X_train=np.array(inp)
        y_train=np.array(types)
        return X_train, y_train
    else:
        X_test=np.array(inp)
        y_test=np.array(types)
        return X_test, y_test

X_train, y_train = creator(0)
X_test, y_test = creator(1)
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(np.array(inp), np.array(types))
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

print 'Accuracy for each category'
for i in range(5):
    accuracy = getAccuracy(i)
    sumy = 0
    print accuracy
    for key in accuracy.keys():
        sumy += accuracy[key][1]
	#for key in accuracy.keys():
	#    print accuracy[i][0], ' --> ', accuracy[key][0], (100.0*accuracy[key][1])/sumy
		
