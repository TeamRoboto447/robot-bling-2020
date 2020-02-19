#!/usr/bin/python3
import board, neopixel, time
from time import sleep

NUM_LED = 60 * 5
NEO_PIN = board.D18

speed = 5

pixels = neopixel.NeoPixel(NEO_PIN, NUM_LED, auto_write = False, brightness = 0.25)
pixels.show()

def flow(color):
        for i in range(NUM_LED):
                pixels[i] = color
                if i % speed is 0:
                        pixels.show()

def reverseFlow(color):
        for i in range(NUM_LED):
                pixels[NUM_LED - 1 - i] = color
                if i % speed is 0:
                        pixels.show()

def main():
        while(True):
                flow((255, 0, 0))
                reverseFlow((0, 0, 255))


try:
        main()
except:
        pixels.fill(0)
        pixels.show()
