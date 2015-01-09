#! /usr/bin/env python
# This is a word-reciting software. It is very succinct.
import wx
import random
#words = []
mean_word = {}
time_word = {}
lv_word = {}
words = []

time_lv = {0:-10, 1:-30, 2:-120, 3:-300, 4:-1800, 5:-3600, 6:-7200, 7:-100000, 8:-10000000}

def readF():
	f1 = open("wordswithExplainations.txt", "r")
	vocabulary = f1.readlines()

	f2 = open("wordswithLevelandTime.txt", "r")
	data = f2.readlines()
	#print vocabulary,"\n"*50, data
	# f3 = open("words.txt", "r+")
	# words = f3.readlines()
	
	global mean_word, time_word, lv_word, words
	
	for i in range(5013):
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
		#print "\n"*50,levelandTime
		
		level = levelandTime[1]
		time = levelandTime[2]
		#print "\n"*50,level,time
		
		time_word[str(word)] = float(time)
		lv_word[str(word)] = float(level)
	
		# ----------------------------------------------------

	
def writeF():
	
	f3 = open("wordswithLevelandTime.txt", "w")
	global lv_word,time_word,words
	
	for i in range(5013):
		f3.write(words[i])
		f3.write(" " + str(lv_word[words[i]]) + " " + str(time_word[words[i]]))
		f3.write("\n")
	

class WordsRecitingFrame(wx.Frame):
	def __init__(self, parent = None):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Cracking SAT vocabulary 5000+", size=(800,450)) # initialize the frame
		global time_word, mean_word
		self.word_using = max(time_word, key=time_word.get)
	
	
		self.begin = wx.Panel(self)
		self.panel = wx.Panel(self)
		self.panel.Show(False)
		
# --------------------------------------First Panel-----------------------------------------
		
		self.test = wx.StaticText(self.begin, label="lalala")

		self.background1 = wx.Image("Background1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.background1 = wx.StaticBitmap(self.begin, wx.ID_ANY, self.background1, pos=(100, 100))
		
		self.SATlogo = wx.Image("Background1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.SATlogoBit = wx.StaticBitmap(self.begin, wx.ID_ANY, self.SATlogo, pos=(100, 100))	

		
# --------------------------------------First Panel-----------------------------------------

		self.know = wx.Button(self.panel, label="Know", pos=(0,200))
		self.dontknow = wx.Button(self.panel, label="Don't know", pos=(200,200))
		self.correct = wx.Button(self.panel, label="Correct", pos=(0,200))
		self.incorrect = wx.Button(self.panel, label="Incorrect", pos=(200,200))
		self.close = wx.Button(self.panel, label="Close", pos=(300,0))
		self.next = wx.Button(self.panel, label="Next", pos=(0,200))
	
		self.word = wx.StaticText(self.panel, label=self.word_using, pos=(0,0))
		self.mean = wx.StaticText(self.panel, label=mean_word[self.word_using], pos=(0,100))
	
		self.know.Bind(wx.EVT_BUTTON, self.OnKnow)
		self.dontknow.Bind(wx.EVT_BUTTON, self.OnDontKnow)
		self.panel.Bind(wx.EVT_CHAR_HOOK, self.OnKey)
		self.correct.Bind(wx.EVT_BUTTON, self.OnCorrect)
		self.incorrect.Bind(wx.EVT_BUTTON, self.OnIncorrect)
		self.close.Bind(wx.EVT_BUTTON, self.OnClose)
		self.next.Bind(wx.EVT_BUTTON, self.OnIncorrect)
		#self.panel.Bind(wx.EVT_CHAR_HOOK, self.OnKey)
	
		self.mean.Show(False)
		self.correct.Show(False)
		self.incorrect.Show(False)
		self.next.Show(False)

	def OnKey(self, e):
		key = e.GetKeyCode()
		#print key,self.correct.IsShown(),self.know.IsShown(), self.next.IsShown()
		#wx.Sleep(0.5)
	
		if(key == 67 and self.correct.IsShown() == True): self.OnCorrect(e)
		if(key == 73 and self.correct.IsShown() == True): self.OnIncorrect(e)
		if(key == 75 and self.know.IsShown() == True): self.OnKnow(e)
		if(key == 68 and self.know.IsShown() == True): self.OnDontKnow(e)
		if(key != 68 and self.next.IsShown() == True): self.OnIncorrect(e)

	def OnClose(self,e):
		writeF()
		exit()

	def OnKnow(self, e):
		self.know.Show(False)
		self.dontknow.Show(False)
		self.mean.Show(True)
		self.correct.Show(True)
		self.incorrect.Show(True)
		
	def OnDontKnow(self, e):
		self.know.Show(False)
		self.dontknow.Show(False)
		self.mean.Show(True)
		self.next.Show(True)
		
	def OnCorrect(self,e):
		global time_word,mean_word,time_lv
		period = 3
		for word in time_word: 
			if(time_word[word] < 0): time_word[word] += period
		
		lv_word[self.word_using] += 1
		time_word[self.word_using] = time_lv[lv_word[self.word_using]]
		#print time_word
		self.next.Show(False)
		self.correct.Show(False)
		self.incorrect.Show(False)
		
		self.word_using = max(time_word, key=time_word.get)
		self.word.SetLabel(self.word_using)
		self.mean.SetLabel(mean_word[self.word_using])
		
		
		self.mean.Show(False)
		self.know.Show(True)
		self.dontknow.Show(True)
		
	def OnIncorrect(self, e):
		global time_word,mean_word,time_lv
		period = 3
		for word in time_word: 
			if(time_word[word] < 0): time_word[word] += period
		
		lv_word[self.word_using] = 0
		time_word[self.word_using] = time_lv[0]
		#print time_word
		self.next.Show(False)
		self.correct.Show(False)
		self.incorrect.Show(False)
		
		
		self.word_using = max(time_word, key=time_word.get)
		self.word.SetLabel(self.word_using)
		self.mean.SetLabel(mean_word[self.word_using])
		
		self.mean.Show(False)
		self.know.Show(True)
		self.dontknow.Show(True)
		
# -------- Main Program Below ------------
readF()
app = wx.App(False)
frame = WordsRecitingFrame(None)
frame.Show()
app.MainLoop()