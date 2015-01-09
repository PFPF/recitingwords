#! /usr/bin/env python

f = open("wordswithExplainations.txt", "r+") 
words = []
vocabulary = f.readlines()
print vocabulary
for i in range(5014):
	line = vocabulary[i]
	line = line.split()
	words.append(line[0])


w = open("words.txt", "w+") 
for i in range(5014):
	w.write(words[i])
	#w.write(" 0 0")
	w.write("\n")
