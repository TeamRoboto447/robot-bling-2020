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
		self.range = range(min,max)
		self.setInverted(inverted)
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
	def invertedFill(self, color, show = False):
                for i in self.currentRange:
                        self.pixels[i] = color
                        self.show(show)
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
		print('')
		self.show(show)
                

class SectionGroup:
	def __init__(self, *items):
		self.items = items
	def fill(self, color, show = False):
		for item in self.items:
			item.fill(color, show)
	def invertedFill(self, color, show = False):
                for item in self.items:
                        item.invertedFill(color, show)
	def grade(self, colorStart, colorEnd, show = False):
		for item in self.items:
			item.grade(colorStart, colorEnd, show)
