import nltk
f=open('input.txt','r')
fil=f.readlines()

g=open('finalWords','r')
voc=g.readlines()
vocabulary=[]
filewords=[]
bsport={}
total=0
probability={'sport':511,'business':510,'tech':401,'entertainment':386,'politics':417}
for i in probability.keys():
	total+=probability[i]

for i in voc:
	vocabulary.append(i.strip())
	bsport[i.strip()]=0

for i in fil:
	line=i.strip().decode("ascii","ignore").encode("ascii")
	words=nltk.word_tokenize(line)
	for word in words:
		if word not in filewords:
			filewords.append(word)
for j in filewords:
	if j in vocabulary:
		bsport[j]=1
def classify(name,num):
	h=open('./word_frequencies/b'+name,'r')
	txt=h.readlines()
	h.close()
	freq={}
	for i in txt:
		data=i.strip().split('*')
		freq[data[0]]=float(data[1])
	prob=(num*1.0)/total
	for i in bsport.keys():
		prob*= ((bsport[i]*freq[i])+((1-bsport[i])*(1-freq[i])))
	return prob

val=-1
cls=''
for i in probability.keys():
    no=classify(i,probability[i])
    if val<no:
		cls=i
		val=no
print cls
