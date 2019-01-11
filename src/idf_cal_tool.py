#!/bin/python3

import math

def docs(w, D):
	c = 0 
	for d in D :
		if w in d:
			c +=1

	return c

raw_corpus = open("../data/all_content_cut_clean.txt","r").read()
corpus = raw_corpus.split('\n')
print("len of corpus is ",len(corpus))

W = set()
D = []
for i in range(len(corpus)):
	dt = [] 
	d = corpus[i].split(" ")
	for i in d :
		if len(i.strip() ) > 0: 
			print("i is",i)
			dt.append(i) 
	
	
	D.append(set(dt))
	W = W | set(dt)

idf_dict = {}

n = len(W)

for w in list(W):
	idf = math.log(n*1.0/docs(w,D))

	idf_dict[w]= idf

path = "../data/idf.txt"
f = open(path, "w")

for key in idf_dict.keys():
	f.write(str(key) + " "+ str(idf_dict[key]) +"\n")

f.close()
