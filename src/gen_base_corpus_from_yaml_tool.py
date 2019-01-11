#!/bin/python

import os
import yaml

path="/Users/ben/code/chatbot/chatterbot-corpus-master/chatterbot_corpus/data/chinese"

files = os.listdir(path)

s = []

target_file = open("./all_content.txt", "w+")

for file in files:	
	f = open(path+"/"+file)
	msg = yaml.load(f)
	#print(msg["conversations"])
	for chat_pair in msg["conversations"]:
		#print("pair is ", chat_pair)
		print("question is ", chat_pair[0])
		print("answeris ", chat_pair[1])
		target_file.write(chat_pair[0]+'\n')
		target_file.write(chat_pair[1]+'\n')
			
	f.close()

