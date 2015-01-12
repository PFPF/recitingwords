#! /usr/bin/env python
# This is a word-reciting software. It is very succinct.
'''
New Things:
split
join
global
max

'''
'''FRANK'''
import wx
import random
import CLEAR
import time

mean_word = {}
time_word = {}
lv_word = {}
words = []

time_lv = {0:-30, 1:-120, 2:-300, 3:-750, 4:-1800, 5:-3600, 6:-7200, 7:-14400, 8:-10000000, 9:-1e50}


def readF():
	f1 = open("wordswithExplainations.txt", "r")
	vocabulary = f1.readlines()

	f2 = open("wordswithLevelandTime.txt", "r")
	data = f2.readlines()
	
	global mean_word, time_word, lv_word, words
	
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
		
		time_word[str(word)] = float(time)
		lv_word[str(word)] = int(level)
	
		# ----------------------------------------------------


	
def writeF():
	
	f3 = open("wordswithLevelandTime.txt", "w")
	global lv_word,time_word,words
	

	for i in range(5014):

		f3.write(words[i])
		f3.write(" " + str(lv_word[words[i]]) + " " + str(time_word[words[i]]))
		f3.write("\n")
	

class WordsRecitingFrame(wx.Frame):
	def __init__(self, parent = None):
		
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Cracking SAT Vocabulary 5000+", size=(800,450)) # initialize the frame
		global time_word, mean_word
		self.word_using = max(time_word, key=time_word.get)
	
		self.begin = wx.Panel(self, size = (1280, 720))

		self.panel = wx.Panel(self, size = (1280, 720))
		self.final = wx.Panel(self, size = (1280, 720))

		self.panel.Show(False)
		self.final.Show(False)
		self.currentTime = time.time()
		
# --------------------------------------First Panel-----------------------------------------
		


		self.background1 = wx.Image("Background1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.backgroundBitmap = wx.StaticBitmap(self.begin, wx.ID_ANY, self.background1, pos=(0, 0))
		
		self.SATlogo = wx.Image("SATlogo.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.SATlogoBitmap = wx.StaticBitmap(self.begin, wx.ID_ANY, self.SATlogo, pos=(20, 20))	
		
		self.start = wx.Button(self.begin, label = "Start (Any Key)", pos=(0,275), size=(790,100))
		self.start.Bind(wx.EVT_BUTTON, self.OnStart)
		self.begin.Bind(wx.EVT_CHAR_HOOK, self.OnStart)
		
		self.SATFond = wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
		self.numberFond = wx.Font(80, wx.DECORATIVE, wx.NORMAL, wx.BOLD)

		self.SAT = wx.StaticText(self.begin, label = "Cracking SAT Vocabulary", pos=(185,100))
		self.SAT.SetFont(self.SATFond)
		
		self.number = wx.StaticText(self.begin, label = "5000+", pos=(315,150))
		self.number.SetFont(self.numberFond)

		self.number.SetForegroundColour((255,0,0)) # set text color
		self.SAT.SetForegroundColour((255,165,0)) # set text color

# --------------------------------------Second Panel-----------------------------------------
		
		self.background2 = wx.Image("Background2.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.backgroundBitmap2 = wx.StaticBitmap(self.panel, wx.ID_ANY, self.background2, pos=(0, 0))

		self.know = wx.Button(self.panel, label = "Know (K)", pos = (275,250))
		self.dontknow = wx.Button(self.panel, label = "I'm NOOB (B)", pos = (425,250))
		self.correct = wx.Button(self.panel, label = "Correct (C)", pos = (275,250))
		self.incorrect = wx.Button(self.panel, label = "Incorrect (I)", pos = (425,250))
		self.contributorBTN = wx.Button(self.panel, label = "Contributors", pos = (700,0))
		self.next = wx.Button(self.panel, label = "Next (N)", pos = (275,250), size = (250,20))
	
		self.word = wx.StaticText(self.panel, label = self.word_using, pos = (350,80))
		self.mean = wx.StaticText(self.panel, label = mean_word[self.word_using], pos = (75,180))
			
		self.vocaFont = wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		self.word.SetFont(self.vocaFont)
		
		self.meanFont = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL)
		self.mean.SetFont(self.meanFont)
		self.reset1 = wx.CheckBox(self.panel, label="CLEAR this record when close", pos=(500,300))
		self.reset2 = wx.CheckBox(self.panel, label="CLEAR ALL the record when close", pos=(500,320))
		
		'''Frederic'''
		self.reset1.Bind(wx.EVT_CHECKBOX, self.OnReset)
		self.reset2.Bind(wx.EVT_CHECKBOX, self.OnReset)
		self.know.Bind(wx.EVT_BUTTON, self.OnKnow)
		self.dontknow.Bind(wx.EVT_BUTTON, self.OnDontKnow)
		self.panel.Bind(wx.EVT_CHAR_HOOK, self.OnKey)
		self.correct.Bind(wx.EVT_BUTTON, self.OnCorrect)
		self.incorrect.Bind(wx.EVT_BUTTON, self.OnIncorrect)
		self.contributorBTN.Bind(wx.EVT_BUTTON, self.OnContributor)
		self.next.Bind(wx.EVT_BUTTON, self.OnIncorrect)
		self.Bind(wx.EVT_CLOSE, self.OnClose)

		self.mean.Show(False)
		self.correct.Show(False)
		self.incorrect.Show(False)
		self.next.Show(False)

#-----------------------------------Final Panel---------------------------------------
		
		self.background1 = wx.Image("Background1.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.backgroundBitmap = wx.StaticBitmap(self.final, wx.ID_ANY, self.background1, pos=(0, 0))
		
		self.resume = wx.Button(self.final, label="Resume", pos=(700,0))
		self.resume.Bind(wx.EVT_BUTTON, self.OnResume)
		
		
		
		self.snapshot = wx.Image("snapshot.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.snapshot = wx.StaticBitmap(self.final, wx.ID_ANY, self.snapshot, pos=(0, 0))
		
		self.contributor = wx.StaticText(self.final, label = "Contributors:", pos=(675,100))
		self.Frederic = wx.StaticText(self.final, label = "Frederic Peng", pos=(675,125))
		self.Frank = wx.StaticText(self.final, label = "Frank Huang", pos=(675,150))
		
#----------------------------------- Function ---------------------------------------

		
	'''Frederic'''
	def OnStart(self, e):
		self.panel.Show(True)
		self.begin.Show(False)

	def OnKey(self, e):
		key = e.GetKeyCode()

		if(key == 67 and self.correct.IsShown() == True): self.OnCorrect(e)
		if(key == 73 and self.correct.IsShown() == True): self.OnIncorrect(e)
		if(key == 75 and self.know.IsShown() == True): self.OnKnow(e)
		if(key == 66 and self.know.IsShown() == True): self.OnDontKnow(e)
		if(key != 66 and self.next.IsShown() == True): self.OnIncorrect(e)

	def OnContributor(self,e):
		self.final.Show(True)
	def OnClose(self,e):
		self.resetAll = self.reset2.GetValue()
		self.resetThis = self.reset1.GetValue()
		if self.resetAll: 
			CLEAR.clear_all()
		if not self.resetThis: 
			writeF()
		exit()
		
		
	def OnResume(self,e):
		self.final.Show(False)
		
	def OnReset(self,e):
		self.resetAll = self.reset2.GetValue()
		if self.resetAll:
			self.reset1.Disable()
			self.reset1.SetValue(True)
		else:
			self.reset1.Enable()
		self.resetThis = self.reset1.GetValue()

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
		period = time.time() - self.currentTime
		self.currentTime = time.time()
		
		for word in time_word: 
			if(time_word[word] < 0): time_word[word] += period
		
		if(time_word[self.word_using] == 0 or lv_word[self.word_using] == 9): 
			lv_word[self.word_using] = 9
		else: 
			lv_word[self.word_using] += 1
		time_word[self.word_using] = time_lv[lv_word[self.word_using]]

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
		global time_word, mean_word, time_lv
		period = time.time() - self.currentTime
		self.currentTime = time.time()
		for word in time_word: 
			if(time_word[word] < 0): time_word[word] += period
		
		lv_word[self.word_using] = 0
		time_word[self.word_using] = time_lv[0]

		self.next.Show(False)
		self.correct.Show(False)
		self.incorrect.Show(False)
		
		self.word_using = max(time_word, key = time_word.get)
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