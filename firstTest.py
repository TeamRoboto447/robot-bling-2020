#!/usr/bin/python3
import board, neopixel, time

NUM_LED = 60 * 5
NEO_PIN = board.D18

pixels = neopixel.NeoPixel(NEO_PIN, NUM_LED, auto_write = False)
pixels.show()

for i in range(NUM_LED):
	pixels[i] = (i * 5 % 255, (i + 85) * 5 % 255, (i + 170) * 5 % 255)
	pixels.show()
time.sleep(10)
pixels.fill([0,0,0])
