import numpy as np
from copy import deepcopy
from collections import deque
import datetime

def sumSquare(x,y):
	return x**2+y**2
def endColumn(x,y):
	return (y>=x-1)
def expectedStr(secs):
	secs = abs(int(secs))
	days, secs = divmod(secs, 86400)
	hours, secs = divmod(secs, 3600)
	minutes,secs = divmod(secs, 60)
	if days > 0:
		return '%d days %dh%dm%ds' % (days,hours,minutes,secs)
	elif hours >0:
		return '%dh%dm%ds' % (hours,minutes,secs)
	elif minutes > 0:
		return '%dm%ds' % (minutes,secs)
	else:
		return '%ds' % (secs)

class Iterator611():
	infSquare = 4
	nextSquare = 9
	notFinishedCol = deque()
	notFinishedColForNextCateg = deque()
	SetOfSquare = set()
	x = 2
	y = 1
	count = 0
	N = 0
	Max = 0
	finishingCateg = True
	startTime = datetime.datetime.now()

	def __init__(self,Max):
		self.stop = np.floor(np.sqrt(Max))
		self.Max = Max
	def __iter__(self):
		return self

	def __next__(self):
		if self.x >= self.stop+1:
			raise StopIteration

		# Count iteration
		self.N = self.N+1
		square = sumSquare(self.x,self.y)

		#Count the square.
		if(square <= self.Max):
			if square in self.SetOfSquare:
				self.SetOfSquare.remove(square); 
				self.count -= 1;
			else:
				self.SetOfSquare.add(square)
				self.count+=1;

		#Estimate the time
		if(np.floor(np.log10(self.N)) == np.log10(self.N)):
			cur_time = datetime.datetime.now()
			exection_time = (cur_time - self.startTime).total_seconds()
			expectedTime = expectedStr(exection_time/self.N *self.Max)
			print("Iteration : ", self.N, "Count : ", self.count, "Time : ", exection_time, " Expected total duration : ", expectedTime)

		#Advance by categories.
		if ((sumSquare(self.x,self.y+1) <= self.nextSquare) and not endColumn(self.x,self.y)):
			self.y+=1		
		else:
			if self.finishingCateg:
				#print(" End of category : ", self.infSquare, " - ", self.nextSquare, " Count : ", self.count)
				self.finishingCateg = False
				self.SetOfSquare = set()
				self.infSquare = self.nextSquare
				self.nextSquare = (self.x+2)**2
				if not endColumn(self.x,self.y):
					self.notFinishedColForNextCateg.append((self.x,self.y+1))
				self.notFinishedCol = deepcopy(self.notFinishedColForNextCateg)
				self.notFinishedColForNextCateg = deque()

				(self.x,self.y) = self.nextElem()
			else:
				if not endColumn(self.x,self.y):
					self.notFinishedColForNextCateg.append((self.x,self.y+1))

				(self.x,self.y) = self.nextElem()

		return (self.count)

	def nextElem(self):
		if self.notFinishedCol:
			return self.notFinishedCol.popleft()
		else:
			self.finishingCateg = True
			return (self.x+1, 1)



