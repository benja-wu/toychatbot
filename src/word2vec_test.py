#!/bin/python3

from gensim.models import word2vec 
import jieba
import os
import numpy as np


stopwords = {}.fromkeys([ line.rstrip() for line in open('../data/stop_words.txt') ])
model = word2vec.Word2Vec.load("../model/chatbot.model")
index2word_set = set(model.wv.index2word)	

def sent2vec(s ,num_features ):
	new_line = jieba.cut(s, cut_all=False)
	
	str = ' '.join(new_line).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
	.replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        .replace('’', '').replace('?','').replace('!','').replace('.','').replace(',','').replace('`','').replace(';','')     
	M = []
	segs = str.split(" ")	
	print("segs is ",segs)

	s_vec = np.zeros((num_features, ), dtype='float32')

	n_words = 0 
	key_seg = [] 
	max_idf = 0 
	
	for seg in segs:
		if seg not in stopwords and seg in index2word_set:
		#if seg not in stopwords :
			M.append(model[seg])
			#cmd = "grep -w \""+seg+"\" ../data/idf_sort.txt | cut -d\" \" -f2 " 
			cmd = "awk -F' ' '{ if ($1==\"" +seg+ "\") print $2}' ../data/idf.txt"

			print("cmd is ",cmd)
			idf=os.popen(cmd).read()
			if len(idf) > 0 and float(idf) >= max_idf:
				max_idf = float(idf) 
				key_seg.append(seg)

			s_vec = np.add(s_vec, model[seg])
			n_words += 1

	
	print("key seg is ", key_seg, " idf is ", max_idf)
	M = np.array(M)
	v = M.sum(axis= 0 )

	M = v / np.sqrt((v ** 2).sum())
	if n_words>0 :
		s_vec  = np.divide(s_vec, n_words)

	#print("befor return, M is ",M, " s_vec is ",s_vec)
	return M, s_vec, key_seg


words= input('Enter your words:') 
print("input is :",words)
if len(words) > 1:
	wvec = sent2vec(words,50)

	print("m is ", wvec[0], " svec is ", wvec[1] ," key words", wvec[2])
else: 
	print("to short")

