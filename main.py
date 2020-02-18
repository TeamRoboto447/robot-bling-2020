#!/usr/bin/python3
import board, neopixel, time
from group import LEDSection, SectionGroup, 

NUM_LED = 60 * 5
NEO_PIN = board.D18

pixels = neopixel.NeoPixel(NEO_PIN, NUM_LED, auto_write = False, brightness = 0.25)
pixels.show()



