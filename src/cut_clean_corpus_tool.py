#!/bin/python3

import jieba

f = open("../data/all_content.txt","r")
f1 = open("../data/all_content_cut_clean.txt" , "w+")

stopwords = {}.fromkeys([ line.rstrip() for line in open('../data/stop_words.txt') ])

for line in f.readlines():
	new_line = jieba.cut(line, cut_all=False)
	
	str = ' '.join(new_line).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
	.replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        .replace('’', '').replace('?','').replace('!','').replace('.','').replace(',','').replace('`','').replace(';','').replace('\'','').replace(':','').replace('"','').replace('-','')      

	final = ""
	
	segs = str.split(" ")	
	for seg in segs:
		if seg not in stopwords:
			final+=seg+" "

	f1.write(final)	


#cut_file ="./all_content_cut.txt"
#text = f.read()

#new_text = jieba.cut(text, cut_all=False)
	
#str_out = ' '.join(new_text).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
        #.replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        #.replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        #.replace('’', '').replace('?','').replace('!','').replace('.','').replace(',','').replace('`','').replace(';','')     

#fo = open(cut_file, 'w', encoding='utf-8')
#fo.write(str_out)
