#!/usr/bin/python3
import board, neopixel, time
from group import LEDSection, SectionGroup

NUM_LED = 60 * 5
NEO_PIN = board.D18

pixels = neopixel.NeoPixel(NEO_PIN, NUM_LED, auto_write = False, brightness = 0.25)
pixels.show()

sectionAll = LEDSection(pixels, 0, 300)
section1 = LEDSection(pixels, 0, 150)
section2 = LEDSection(pixels, 150, 300)

group = SectionGroup(section1,section2)

try:
	#sectionAll.grade((0, 0, 0), (255, 255, 255))
	#section1.grade((0,255,0),(255/2,255/2,0))
	#section2.grade((255/2, 255/2, 0), (255, 0, 0))
	group.grade((255, 0, 0), (0, 0, 255))
	pixels.show()
	while True:
		time.sleep(1)
finally:
	#section1.fill((0,0,0))
	#section2.fill((0,0,0))
	pixels.show()


