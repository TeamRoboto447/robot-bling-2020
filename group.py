from time import sleep
def grade(self,i,m,b):
	if self.inverted:
		return round(m * (self.max - i) + b)
	else:
		return round(m * (i - self.min) + b)

class LEDSection:
	def __init__(self, pixels, min, max, inverted = False):
		self.pixels = pixels
		self.min = min
		self.max = max
		self.range = list(range(min,max))
		self.setInverted(inverted)
		self.index = 0
		self.cont = True
	def setInverted(self, inverted):
		if inverted:
			self.currentRange = list(reversed(self.range))
		else:
			self.currentRange = self.range
		self.inverted = inverted
	def show(self,show):
		if show:
			self.pixels.show()
	def fill(self, color, show = False):
		for i in self.currentRange:
			self.pixels[i] = color
		self.show(show)
	def fillOverTime(self, color, numberPerLoop = 1):
		if not self.cont:
			return True
		for i in range(0,numberPerLoop):
			self.pixels[self.currentRange[self.index+i]] = color
		self.index += numberPerLoop
		self.pixels.show()
		if self.index >= len(self.currentRange) - 1:
			self.index == 0
			self.cont = False
			return True
		return False
	def invertedFillOverTime(self, color, numberPerLoop = 1):
		if not self.cont:
			return True
		for i in range(0,numberPerLoop):
			self.pixels[list(reversed(self.currentRange))[self.index+i]] = color
		self.index += numberPerLoop
		self.pixels.show()
		if self.index >= len(self.currentRange) - 1:
			self.index == 0
			self.cont = False
			return True
			self.cont = False
		return False
	def grade(self, colorStart, colorEnd, show = False):
		dX = self.max - self.min
		rM = (colorEnd[0] - colorStart[0]) / dX
		rB = colorStart[0]
		gM = (colorEnd[1] - colorStart[1]) / dX
		gB = colorStart[1]
		bM = (colorEnd[2] - colorStart[2]) / dX
		bB = colorStart[2] #Battleship
		for i in self.currentRange:
			self.pixels[i] = (grade(self,i,rM,rB),grade(self,i,gM,gB),grade(self,i,bM,bB))
		self.show(show)
	def reset(self):
		self.index = 0
		self.cont = True

class SectionGroup:
	def __init__(self, *items):
		self.items = items
	def fill(self, color, show = False):
		for item in self.items:
			item.fill(color, show)
	def fillOverTime(self, color, numberPerLoop = 1):
		for item in self.items:
			item.fillOverTime(color, numberPerLoop)
	def invertedFillOverTime(self, color, numberPerLoop = 1):
		for item in self.items:
			item.invertedFillOverTime(color, numberPerLoop)
	def grade(self, colorStart, colorEnd, show = False):
		for item in self.items:
			item.grade(colorStart, colorEnd, show)
