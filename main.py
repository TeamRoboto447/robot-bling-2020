#!/usr/bin/python3
import board, neopixel, time
import networkTables, states, settings, threading
from group import LEDSection, SectionGroup
from copy import deepcopy

sett = settings.getSettings()

NUM_LED = 60 * 5
NEO_PIN = board.D18

pixels = neopixel.NeoPixel(NEO_PIN, NUM_LED, auto_write = False, brightness = 0.25)
pixels.show()

tables = networkTables.tables()

frameLeft = LEDSection(pixels,0,46)
frameRight = LEDSection(pixels,46,92)
frameFront = LEDSection(pixels,92,134)
frameBack = LEDSection(pixels,134,176)

turretRight = LEDSection(pixels,176,194)
turretLeft = LEDSection(pixels,194,212)

groups = {
    "frameLeft": frameLeft,
    "frameRight": frameRight,
    "frameFront": frameFront,
    "frameBack": frameBack,
    "frame": SectionGroup(frameLeft, frameRight, frameFront, frameBack),
    "turretRight": turretRight,
    "turretLeft": turretLeft,
    "turret": SectionGroup(turretLeft,turretRight)
}

statesDict = {
    "init": states.init(groups, tables, pixels),
    "idle": states.idle(groups, tables, pixels),
    "grade": states.grade(groups, tables, pixels),
    "fight": states.fight(groups, tables, pixels),
    "off": states.off(groups,tables,pixels)
}

state = statesDict["init"]
state.start()
while not state.run():
    time.sleep(sett["LoopDelay"])
state.end()
t = None



def changeState(key, value, isNew):
    global state, statesDict, t
    if t != None and t.is_alive():
        t.join()
    if key == sett["NetworkTables"]["BlingSelect"]:
        state.end()
        state = statesDict[value]
        state.start()
    elif key == sett["NetworkTables"]["TeamColor"]:
        state.teamChange(value)

tables.EventListener(changeState)

try:
    while True:
        t = threading.Thread(target=state.run)
        t.start()
        t.join()
        time.sleep(sett["LoopDelay"])
finally:
    state.end()
