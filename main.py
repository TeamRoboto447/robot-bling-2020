#!/usr/bin/python3
import board, neopixel, time
import networkTables, settings, threading
from group import LEDSection, SectionGroup
from copy import deepcopy

import chassieStates

sett = settings.getSettings()

NUM_LED = 38 * 2
NEO_PIN = board.D18

pixels = neopixel.NeoPixel(NEO_PIN, NUM_LED, auto_write = False, brightness = 0.25)
pixels.show()

tables = networkTables.tables()

frameLeft = LEDSection(pixels,0,38)
frameRight = LEDSection(pixels,38,76,inverted=True)

groups = {
    "frameLeft": frameLeft,
    "frameRight": frameRight,
    "frame": SectionGroup(frameLeft, frameRight),
    "frameCircle": SectionGroup(deepcopy(frameLeft),deepcopy(frameRight).setInverted(False))
}
SectionStates = [
    chassieStates
]

for sectionState in SectionStates:
    sectionState.initALL()

def teamChanged(entry, key, value, param):
    for sectionState in SectionStates:
        sectionState.teamChange(value)

try:
    for sectionState in SectionStates:
        sectionState.run()
finally:
    for sectionState in SectionStates:
        sectionState.end()
