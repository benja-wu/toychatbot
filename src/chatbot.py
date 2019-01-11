#!/bin/python3

import sqlite3
from gensim.models import word2vec 
from scipy import spatial
import jieba
import os
import numpy as np


stopwords = {}.fromkeys([ line.rstrip() for line in open('../data/stop_words.txt') ])
model = word2vec.Word2Vec.load("../model/chatbot.model")
index2word_set = set(model.wv.index2word)	

def sent2vec(s  ):
	num_features = 50
	new_line = jieba.cut(s, cut_all=False)
	
	str = ' '.join(new_line).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
	.replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        .replace('’', '').replace('?','').replace('!','').replace('.','').replace(',','').replace('`','').replace(';','')     
	M = []
	segs = str.split(" ")	
	#print("segs is ",segs)

	s_vec = np.zeros((num_features, ), dtype='float32')

	n_words = 0 
	key_seg = [] 
	max_idf = 0 
	
	for seg in segs:
		if seg not in stopwords and seg in index2word_set:
		#if seg not in stopwords :
			M.append(model[seg])
			cmd = "awk -F' ' '{ if ($1==\"" +seg+ "\") print $2}' ../data/idf.txt"

			idf=os.popen(cmd).read()
			if len(idf) > 0 and float(idf) >= max_idf:
				max_idf = float(idf) 
				key_seg.append(seg)

			s_vec = np.add(s_vec, model[seg])
			n_words += 1

	
	if n_words>0 :
		s_vec  = np.divide(s_vec, n_words)
		M = np.array(M)
		v = M.sum(axis= 0 )

		M = v / np.sqrt((v ** 2).sum())

		return M, s_vec, key_seg , 0

	return [], [], [], 1	
		

conn = sqlite3.connect("../data/database/QA.sqlite3")

c = conn.cursor()

while 1 :
	words= input('your input is:')
	if len(words) > 1:
		wvec = sent2vec(words)
		
		if wvec[3] == 0 and len(wvec[2]) > 0 :
			min_sim = 100000
			answer = ""

			cursor = c.execute("select question, answer from QApair where question like '%"+wvec[2][0]+"%' limit 5")
			for row in cursor :
				print("--candidate is: ", row)
				can = sent2vec(row[0])	 			
				tmp_sim = 1-spatial.distance.cosine(wvec[0],can[0])
				if  tmp_sim < min_sim:
					min_sim = tmp_sim
					answer = row[1] 

			if len(answer ) == 0 :
				print("answer is :我找不到合适的答案")
			else:
				print("answer is :",answer)
		else:
			print("我不晓得你在说啥")
		
	else: 
		print("to short")

