# coding=utf-8

import os
import nltk

f = open('finalWords','r')
fil = f.readlines()
f.close()

vocabulary = []
for i in fil[:2000]:
    vocabulary.append(i.strip())

B = {}

def calcProb(name, total):
    for i in vocabulary:
        B[i] = 0
    filewords = []
    a = []
    a = os.listdir('./datasets/' + name)
    for i in a:
    	g = open('./datasets/' + name + '/' + i, 'r')
    	txt = g.readlines()
            g.close()
    	for line in txt:
    	    line = line.strip().decode("ascii","ignore").encode("ascii")
    	    words = nltk.word_tokenize(line)
    	    for word in words:
    	        if word not in filewords:
    		    filewords.append(word)
    	for j in filewords:
    	    if j in vocabulary:
    		B[j]+=1
    k = open('./word_frequencies/' + 'b' + name, 'w')
    for i in B.keys():
    	k.write(i.strip() + '*' + str(1.0*B[i]/total) + '\n')
    k.close()
    
calcProb('sport', 511)
calcProb('business', 401)
calcProb('politics', 417)
calcProb('tech', 386)
calcProb('entertainment', 510)
