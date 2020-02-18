def grade(min,i,m,b):
	return round(m * (i - min) + b)

class LEDSection:
	def __init__(self, pixels, min, max):
		self.pixels = pixels
		self.min = min
		self.max = max
	def show(self,show):
		if show:
			self.pixels.show()
	def fill(self, color, show = False):
		for i in range(self.min, self.max):
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
		for i in range(self.min,self.max):
			self.pixels[i] = (grade(self.min,i,rM,rB),grade(self.min,i,gM,gB),grade(self.min,i,bM,bB))
		self.show(show)

class SectionGroup:
	def __init__(self, *items):
		self.items = items
	def fill(self, color, show = False):
		for item in self.items:
			item.fill(color, show)
	def grade(self, colorStart, colorEnd, show = False):
		for item in self.items:
			print(item)
			item.grade(colorStart,colorEnd,show)
