#!/bin/python3

from gensim.models import word2vec 
from gensim.models.word2vec import LineSentence


model = word2vec.Word2Vec(LineSentence('../data/all_content_cut_clean.txt'),size=50,  window=5,min_count=1)


model.save('../model/chatbot.model')
model.wv.save_word2vec_format('./model/readable.txt',binary=False)

for e in model.most_similar(positive=['机器'],topn=10):
	print(e[0], e[1])
