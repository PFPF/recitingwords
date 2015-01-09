#! /usr/bin/env python


def readandWrite():
	f1 = open("wordswithExplainations.txt", "r+")
	vocabulary = f1.readlines()

	f2 = open("wordswithLevelandTime.txt", "r+")
	data = f2.readlines()

	# f3 = open("words.txt", "r+")
	# words = f3.readlines()
	words = []
	global mean_word, time_word, lv_word
	
	for i in range(5014):
		mean = vocabulary[i]
		mean = mean.split()
		
		word = mean[0]
		mean.remove(mean[0])
		
		seq = " "
		explanation = seq.join(mean)
		
		mean_word[str(word)] = str(explanation)
		words.append(word)
		# -----------------------------------------------
		
		levelandTime = data[i]
		levelandTime = levelandTime.split()
		
		level = levelandTime[1]
		time = levelandTime[2]
		
		time_word[str(word)] = time
		lv_word[str(word)] = level
	
		# ----------------------------------------------------

	f2.truncate()

	for i in range(5014):
		f2.write(words[i])
		f2.write(" " + lv_word[words[i]] + " " + time_word[words[i]])
		f2.write("\n")
	
