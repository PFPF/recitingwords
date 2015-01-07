#! /usr/bin/env python
# This is a word-reciting software. It is very succinct.
import wx
import random
#words = []
mean_word = {"2":"1+1", "4":"2+2", "6":"3+3", "8":"4+4", "10":"5+5", "12":"6+6", "14":"7+7", "16":"8+8", "18":"9+9", "20":"10+10", "22":"11+11", "24":"12+12", "26":"13+13", "28":"14+14", "30":"15+15", "32":"16+16", "34":"17+17", "36":"18+18", "38":"19+19", "40":"20+20", "42":"21+21", "44":"22+22", "46":"23+23", "48":"24+24", "50":"25+25", "52":"26+26", "54":"27+27", "56":"28+28", "58":"29+29", "60":"30+30", "62":"31+31", "64":"32+32", "66":"33+33", "68":"34+34", "70":"35+35", "72":"36+36", "74":"37+37", "76":"38+38", "78":"39+39", "80":"40+40", "82":"41+41", "84":"42+42", "86":"43+43", "88":"44+44", "90":"45+45", "92":"46+46", "94":"47+47", "96":"48+48", "98":"49+49"}
time_word = {"2":0, "4":0, "6":0, "8":0, "10":0, "12":0, "14":0, "16":0, "18":0, "20":0, "22":0, "24":0, "26":0, "28":0, "30":0, "32":0, "34":0, "36":0, "38":0, "40":0, "42":0, "44":0, "46":0, "48":0, "50":0, "52":0, "54":0, "56":0, "58":0, "60":0, "62":0, "64":0, "66":0, "68":0, "70":0, "72":0, "74":0, "76":0, "78":0, "80":0, "82":0, "84":0, "86":0, "88":0, "90":0, "92":0, "94":0, "96":0, "98":0}
lv_word = {"2":0, "4":0, "6":0, "8":0, "10":0, "12":0, "14":0, "16":0, "18":0, "20":0, "22":0, "24":0, "26":0, "28":0, "30":0, "32":0, "34":0, "36":0, "38":0, "40":0, "42":0, "44":0, "46":0, "48":0, "50":0, "52":0, "54":0, "56":0, "58":0, "60":0, "62":0, "64":0, "66":0, "68":0, "70":0, "72":0, "74":0, "76":0, "78":0, "80":0, "82":0, "84":0, "86":0, "88":0, "90":0, "92":0, "94":0, "96":0, "98":0}
time_lv = {0:-10,1:-30,2:-60}

def load_file():
	wordf = open("words.txt", "r")
	lvf = open("words.txt", "r")
	global mean, lv
	lines = wordf.readlines()
	for line in lines:
		w = line.split()
		w[0] 
	#Huang Kun Peng
	

#--------------------------------------------


class WordsRecitingFrame(wx.Frame):
	def __init__(self, parent = None):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race!!!", size=(600,600)) # initialize the frame
		global time_word, mean_word
		self.word_using = max(time_word, key=time_word.get)
		self.panel = wx.Panel(self) # create a panel
		self.know = wx.Button(self.panel, label="Know", pos=(0,200))
		self.dontknow = wx.Button(self.panel, label="Don't know", pos=(200,200))
		self.correct = wx.Button(self.panel, label="Correct", pos=(0,200))
		self.incorrect = wx.Button(self.panel, label="Incorrect", pos=(200,200))
		self.next = wx.Button(self.panel, label="Next", pos=(0,200))
		self.word = wx.StaticText(self.panel, label=self.word_using, pos=(0,0))
		self.mean = wx.StaticText(self.panel, label=mean_word[self.word_using], pos=(0,100))
		self.know.Bind(wx.EVT_BUTTON, self.OnKnow)
		self.dontknow.Bind(wx.EVT_BUTTON, self.OnDontKnow)
		self.correct.Bind(wx.EVT_BUTTON, self.OnCorrect)
		self.incorrect.Bind(wx.EVT_BUTTON, self.OnIncorrect)
		self.next.Bind(wx.EVT_BUTTON, self.OnIncorrect)
		#self.panel.Bind(wx.EVT_CHAR_HOOK, self.OnKey)
		self.mean.Show(False)
		self.correct.Show(False)
		self.incorrect.Show(False)
		self.next.Show(False)
	def OnKey(self, e):
		key = e.GetKeyCode()
		if(key == 'y' and self.correct.Show() == True): self.OnCorrect(e)
		if(key == 'n' and self.correct.Show() == True): self.OnIncorrect(e)
		if(key == 'y' and self.know.Show() == True): self.OnKnow(e)
		if(key == 'n' and self.know.Show() == True): self.OnDontKnow(e)
		if(self.next.Show() == True): self.OnIncorrect(e)
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
		print time_word
		self.next.Show(False)
		self.correct.Show(False)
		self.incorrect.Show(False)
		
		self.word_using = max(time_word, key=time_word.get)
		self.word.SetLabel(self.word_using)
		self.mean.SetLabel(mean_word[self.word_using])
		
		
		self.mean.Show(True)
		self.know.Show(True)
		self.dontknow.Show(True)
		
	def OnIncorrect(self, e):
		global time_word,mean_word,time_lv
		period = 3
		for word in time_word: 
			if(time_word[word] < 0): time_word[word] += period
		
		lv_word[self.word_using] = 0
		time_word[self.word_using] = time_lv[0]
		print time_word
		self.next.Show(False)
		self.correct.Show(False)
		self.incorrect.Show(False)
		
		
		self.word_using = max(time_word, key=time_word.get)
		self.word.SetLabel(self.word_using)
		self.mean.SetLabel(mean_word[self.word_using])
		
		self.mean.Show(True)
		self.know.Show(True)
		self.dontknow.Show(True)
		
	
	
	
# -------- Main Program Below ------------

app = wx.App(False)
frame = WordsRecitingFrame(None)
frame.Show()
app.MainLoop()