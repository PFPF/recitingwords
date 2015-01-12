def clear_all():
	f2 = open("wordswithLevelandTime.txt", "r")
	data = f2.readlines()
	words = []
	for i in range(5014):
		mean = data[i]
		mean = mean.split()
	
		word = mean[0]
		words.append(word)

	f3 = open("wordswithLevelandTime.txt", "w")

	for i in range(5014):
		f3.write(words[i])
		f3.write(" 0 0")
		f3.write("\n")