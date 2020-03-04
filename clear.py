#!/usr/bin/python3
import board, neopixel, time, sys
from time import sleep
NUM_LED = 38*2
NEO_PIN = board.D18

pixels = neopixel.NeoPixel(NEO_PIN, NUM_LED, auto_write = True, brightness = 0.25)
pixels.fill(0)
