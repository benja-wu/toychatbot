#!/bin/pthon3

import sqlite3
import itertools

conn = sqlite3.connect("../data/database/QA.sqlite3")

c = conn.cursor()

qa = open("../data/all_content.txt", "r")
while True :
	q = qa.readline().replace("\n","")
	a = qa.readline().replace("\n","")

	if not q or not a : break 
	else :
		kv =[]
		kv.append(q)
		kv.append(a)

		c.execute("insert into QApair values(NULL,?,?)", kv)

conn.commit()
conn.close()
