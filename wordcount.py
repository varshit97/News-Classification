# coding=utf-8
import os
import nltk
f=open('finalWords','r')
fil=f.readlines()
vocabulary=[]
for i in fil[:2]:
	vocabulary.append(i.strip())

bsport={}

def func(name):
	for i in vocabulary:
		bsport[i]=0
	filewords=[]
	a=[]
	a=os.listdir('./datasets/'+name)
	for i in a:
		g=open('./datasets/'+name+'/'+i,'r')
		txt=g.readlines()
		for line in txt:
			line=line.strip().decode("ascii","ignore").encode("ascii")
			words=nltk.word_tokenize(line)
			for word in words:
				if word not in filewords:
					filewords.append(word)
		for j in filewords:
			if j in vocabulary:
				bsport[j]+=1
	k=open('./word_frequencies/'+'b'+name,'w')
	for i in bsport.keys():
		k.write(i.strip()+'*'+str(bsport[i])+'\n')
	
func('sport')
func('business')
func('politics')
func('tech')
func('entertainment')
